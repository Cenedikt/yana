from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Define a GET endpoint at the root ("/") of the API
@app.get("/")
def read_root():
    # This function will be called when a GET request is made to "/"
    # Returns a simple JSON response
    return {"Welcome to": "YANA"}

# Define a GET endpoint at "/predict"
# @app.get("/predict")
# def predict(
#     query: str,
#     ):
#     # This function will be called when a GET request is made to "/predict"
#     # The 'query' parameter is automatically populated from the query parameters of the request
#     # For now, it simply returns the input as output
#     return {
#         "query": query,
#     }


# Define a GET endpoint at "/predict"
@app.get("/docker_test")
def docker_test():

    # This function will be called when a GET request is made to "/predict"
    # The 'query' parameter is automatically populated from the query parameters of the request
    # For now, it simply returns the input as output
    return {
        "This is": "docker",
        }
