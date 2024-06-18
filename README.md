# ai_pickles_test_task
This is simple web application that integrates an AI-powered text summarization service using FastAPI and LangChain.
It has only one endpoint `/summarize` to interact with.

## Installing / Getting started

A quick introduction of the minimal setup you need to get the application up &
running.

### Prerequisites

- Python 3.10 or higher
- Git

### Installation

```shell
# Clone the repository
git clone https://github.com/arturiermolenko/ai_pickles_task

# Navigate to the project directory
cd ai_pickles_task

# Create a virtual environment
python3 -m venv venv 

# Activate the virtual environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the dependencies
pip install -r requirements.txt

# Create the .env file
touch .env  # On Windows, use `echo > .env`
```
Fill the .env file according to the .env_sample file.

### Running the Application
To run the application, use the following command:

```shell
uvicorn main:app --reload
```

## Usage
To use the application, send a POST request to http://127.0.0.1:8000/summarize with JSON format data like:

```json
{
    "text": "text you want to summarize"
}
```
You will receive a summarized text as a response.

Have fun! 🙂
