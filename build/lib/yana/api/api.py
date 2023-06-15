from fastapi import FastAPI
from yana.models import Model1_1, Model1_2
from yana.http_encoder import http_decoder

app = FastAPI()

model1_1 = Model1_1()
model1_2 = Model1_2()

@app.get('/query_2')
def predict(query):
    print(query)
    query = http_decoder(query)
    prediction = model1_2.advice(query)
    print(prediction)
    return {'text' : prediction}

@app.get('/query_1')
def predict(query):
    print(query)
    query = http_decoder(query)
    prediction = model1_1.search(query)
    print(prediction)
    return {'text' : prediction}

@app.get('/')
def root ():
    return {'test': 'HelloWorld'}
