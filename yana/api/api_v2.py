from fastapi import FastAPI
from yana.models import Model1_1
app = FastAPI()

model1_1 = Model1_1()
@app.get('/query_1')
def predict(query):
    prediction = model1_1.search(query)
    return {'text' : prediction}

@app.get('/')
def root ():
    return {'test': 'HelloWorld'}
