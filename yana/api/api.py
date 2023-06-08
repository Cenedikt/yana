from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List
import torch
from scripts.models import Model1_1


app = FastAPI()

class Query(BaseModel):
    """Data model for user queries."""
    text: str = Field(..., max_length=1000)

class Response(BaseModel):
    """Data model for the responses."""
    text: List[str]

# Instantiate the Model1_1 class with embedding
# embedding = torch.load('../data/embedding.pt')

model = Model1_1()


# Dictionary to store the results
results_dict: Dict[str, List[str]] = {}

@app.post("/query/")
async def create_query(query: Query):
    """
    Processes the user's query and generates a prediction for it.
    The query and the prediction are stored.
    """
    user_query = query.text

    # Generate a prediction
    prediction = model.search(user_query, results=3)

    # Assuming the prediction is a list of 3 sentences
    results_dict[user_query] = prediction

    return {"message": "Your query has been received and is being processed. Please use the '/result' endpoint with your query text to get the results."}


@app.get("/result/{query_text}", response_model=Response)
async def get_result(query_text: str):
    """
    Retrieves the results for the given query from the dictionary and returns them.
    """
    if query_text not in results_dict:
        raise HTTPException(status_code=404, detail="Results not found")

    # Retrieve the results from the dictionary
    prediction = results_dict[query_text]

    return {"Users with similar worries wrote:": prediction}
