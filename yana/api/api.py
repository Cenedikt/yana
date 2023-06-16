from fastapi import FastAPI
from yana.ml_logic.models import Model1_1, Model1_2

app = FastAPI()

@app.get('/query_2')
def predict(query: str) -> dict:
    '''
    makes a prediction with the second Model
    params: a querry
    return a dict
    '''
    model1_2 = Model1_2()
    prediction = model1_2.advice(query)

    return {'text' : prediction}

@app.get('/query_1')
def predict(query: str):
    '''
    makes a prediction withe fist Model
    params: a querry
    return a dict
    '''
    model1_1 = Model1_1()
    prediction = model1_1.search(query)

    return {'text' : prediction}

@app.get('/')
def root ():
    '''
    default rout to see if api works
    '''
    return {'test': 'HelloWorld'}
