from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Define a Pydantic model, which is used for request validation and serialization
class Item(BaseModel):
    text: str

# Define a GET endpoint at the root ("/") of the API
@app.get("/")
def read_root():
    # This function will be called when a GET request is made to "/"
    # Returns a simple JSON response
    return {"Welcome to": "YANA"}

# Define a POST endpoint at "/text"
@app.post("/text")
def process_text(item: Item):
    # This function will be called when a POST request is made to "/text"
    # The 'item' parameter is automatically populated from the JSON body of the request
    # For now, it simply returns the input as output
    result = item.text
    return {"result": result}

# Define a GET endpoint at "/predict"
@app.get("/predict")
def predict(
    query: str,
    ):
    # This function will be called when a GET request is made to "/predict"
    # The 'query' parameter is automatically populated from the query parameters of the request
    # For now, it simply returns the input as output
    return {
        "query": query,
    }
