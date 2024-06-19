import os

import dotenv
import uvicorn
from fastapi import FastAPI, Request
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.schema.document import Document
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

LANGCHAIN_TRACING_V2 = os.environ["LANGCHAIN_TRACING_V2"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
model_name = os.environ["MODEL_NAME"]

app = FastAPI()


@app.post("/summarize")
async def summarize(request: Request):
    # Receiving data and creating Langchain Document from it
    data = await request.json()
    document = Document(page_content=data.get("text", ""))

    # Define prompt
    prompt_template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""
    prompt = PromptTemplate.from_template(template=prompt_template)

    # Define LLM chain
    llm = ChatOpenAI(temperature=0, model_name=model_name)
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    result = stuff_chain.invoke([document])

    return {"summary": result["output_text"]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
