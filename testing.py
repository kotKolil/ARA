import requests as r

def create():
    data = {"id":0, "name":"standart", "customer":"standart", "price":1}
    response = r.post(url="http://127.0.0.1/create", json=data)
    return response.status_code

def get_from_id():
    response = r.get(url="http://127.0.0.1/get?id=0")
    return response.json()

def get_from_params():
    response = r.get(url="http://127.0.0.1/get?id=0&?name='standart'&?customer='standart'")
    return response.json()

def update():
    data = {"id":0, "name":"standart", "customer":"default", "price":1}
    response = r.post(url="http://127.0.0.1/update", json=data)
    return response.status_code

def dlt():
    data = {"id":0}
    response = r.delete(url="http://127.0.0.1/update", json=data)
    return response.status_code

def app_test():
    assert create() == 201
    assert get_from_id() == {"id":0, "name":"standart", "customer":"standart", "price":1}
    assert get_from_params() == {"id":0, "name":"standart", "customer":"standart", "price":1}
    assert update() == 200
    assert dlt() == 200