"""
Challenge 64: `FastAPI` for Building a Web API

Problem Statement:
Use the `FastAPI` framework to create a simple web API with a single endpoint that returns a JSON message.

Requirements:
- You must first install the necessary libraries:
  `pip install "fastapi[all]"` (this includes `uvicorn`, the server)
- Create a Python file named `main_api.py`.
- In this file, import `FastAPI`.
- Create an instance of the `FastAPI` application.
- Create a "path operation decorator" for the root URL (`/`) that responds to GET requests.
- The function associated with this endpoint should return a simple Python dictionary. FastAPI will automatically convert it to a JSON response.

How to Run:
1. Save the code below as `main_api.py`.
2. Open your terminal in the same directory.
3. Run the server using this command: `uvicorn main_api:app --reload`
4. Open your web browser and navigate to `http://127.0.0.1:8000`. You should see the JSON response.

Solution (to be saved in `main_api.py`):
"""

from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a path operation decorator for the root endpoint ('/')
# This tells FastAPI that the function below is responsible for handling
# GET requests to the root URL.
@app.get("/")
def read_root():
    """
    This function handles requests to the root URL.
    It returns a dictionary that FastAPI converts to JSON.
    """
    return {"message": "Hello, World!", "status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    """
    An endpoint with a path parameter and an optional query parameter.
    """
    return {"item_id": item_id, "query_param": query_param}


"""
Expected Output in Browser (at http://127.0.0.1:8000):

{
  "message": "Hello, World!",
  "status": "ok"
}

Expected Output in Browser (at http://127.0.0.1:8000/items/5?query_param=test):

{
  "item_id": 5,
  "query_param": "test"
}
""" 