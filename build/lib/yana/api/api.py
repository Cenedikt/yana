
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Dict, List
import torch
from typing import Dict, List, Union
from scripts.models import Model1_1
from scripts.models import Model1_2

app = FastAPI()

class Query(BaseModel):
    """Data model for user queries."""
    text: str = Field(..., max_length=1000)

class Response(BaseModel):
    """Data model for the responses."""
    text: List[str]

model = Model1_1()

# results_dict: Dict[str, List[str]] = {}

def predict(user_query: str):
    """Function to predict using the model."""
    # Generate a prediction
    prediction = model.search(user_query, results=3)

    # Assuming the prediction is a list of 3 sentences
    # results_dict[user_query] = prediction
    return prediction

# Predict for Model1_1
@app.post("/query_1/", response_model=Response)
async def create_query(query: Query):
    """
    Processes the user's query and generates a prediction for it.
    """
    user_query = query.text
    prediction = predict(user_query)
    return {"text": prediction}

############################# MODEL1_2 #################################

class Response_2(BaseModel):
    """Data model for the responses."""
    posts: List[Dict[str, Union[str, int]]]


model_2 = Model1_2()

def predict_2(user_query: str):
    """Function to predict using the model_2."""
    # Generate a prediction
    prediction = model_2.advice(user_query)
    # The prediction should be a list of dictionaries, where each dictionary represents a post
    # And each dictionary should have the keys: "username", "title", "subreddit", "upvotes", and "text"
    # For example: prediction = [{"username": "user1", "title": "post1", "subreddit": "sub1", "upvotes": 100, "text": "This is a post"}, {...}, {...}]
    return prediction

# Predict for Model1_2
@app.post("/query_2/", response_model=Response_2)
async def create_query_2(query: Query):
    """
    Processes the user's query and generates a prediction for it.
    """
    user_query = query.text
    prediction = predict_2(user_query)
    # The "posts" key should be used in the returned dictionary to match the Response_2 model
    return {"posts": prediction}








#####################################################################################

# @app.get("/result/{query_text}", response_model=Response)
# async def get_result(query_text: str):
#     """
#     Retrieves the results for the given query from the dictionary and returns them.
#     """
#     if query_text not in results_dict:
#         raise HTTPException(status_code=404, detail="Results not found")

#     # Retrieve the results from the dictionary
#     prediction = results_dict[query_text]

#     return {"Users with similar worries wrote:": prediction}
