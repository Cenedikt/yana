from yana.api import api

#testing requests

def test_read_root():
    output = api.read_root()
    assert output == {"Welcome to": "YANA"}

# def test_predict():
#     query = "adfiusaedfjhn"
#     query_int = 42
#     output = api.predict(query)
#     assert output == dict(query=query)

#     output_int = api.predict(query_int)
#     assert output_int == dict(query=query_int)
