import requests

def test_details():
    res = requests.get("http://localhost:5000/details")
    assert res.status_code == 200

