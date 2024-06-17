import requests as r

def create():
    data = {"id":0, "name":"standart", "customer":"standart", "price":1}
    response = r.post(url="http://localhost:8000/create", json=data)
    return response.status_code

def get_from_id():
    response = r.get(url="http://localhost:8000/get?Id=0")
    return response.status_code

def get_404():
    response = r.get(url="http://localhost:8000/get?Id=7")
    return response.status_code

def get_from_params():
    response = r.get(url="http://localhost:8000/?name='standart'&?customer='standart'")
    return response.status_code

def update():
    data = {"id":0, "name":"standart", "customer":"default", "price":1}
    response = r.post(url="http://localhost:8000/update", json=data)
    return response.status_code

def update_404():
    data = {"id":7, "name":"standart", "customer":"default", "price":1}
    response = r.post(url="http://localhost:8000/update", json=data)
    return response.status_code

def dlt():
    data = {"id":0}
    response = r.post(url="http://localhost:8000/delete", json=data)
    return response.status_code

def dlt_404():
    data = {"id":7}
    response = r.post(url="http://localhost:8000/delete", json=data)
    return response.status_code

def test_the_app():
    assert create() == 201
    assert get_from_id() == 200
    assert get_from_params() == 200
    assert get_404() == 404
    assert update() == 200
    assert dlt() == 200
    assert dlt_404() == 404
    assert update_404() == 404