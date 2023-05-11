import requests


def get():

    api_url = "http://192.168.1.115:5001/incomes"
    response = requests.get(api_url)
    j = response.json()
    print(j)
    print(response.status_code)
    print(response.headers["Content-Type"])


def post():
    api_url = "http://192.168.1.115:5001/incomes"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=todo)

    print(response)
    print(response.status_code)
    print(response.headers["Content-Type"])


def put():

    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.get(api_url)
    response.json()
    todo = {"userId": 1, "title": "Wash car", "completed": True}
    response = requests.put(api_url, json=todo)
    response.json()
    response.status_code


def patch():
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    todo = {"title": "Mow lawn"}
    response = requests.patch(api_url, json=todo)
    response.json()

    response.status_code


def delete():
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.delete(api_url)
    response.json()


def getTime():
    api_url = "http://192.168.1.115:5001/time"
    response = requests.get(api_url)
    j = response.json()
    print(j)
    print(response.status_code)
    print(response.headers["Content-Type"])


def myS():
    with requests.Session() as session:
        username = "lily"
        password = "123"
        session.auth = (username, password)
        first_response = session.get("http://127.0.0.1:5000/time")

        print(first_response)
        #j = first_response.json()
        # print(j)
    return

    api_url = "http://192.168.1.115:5000/time"
    response = requests.get(api_url)
    j = response.json()
    print(j)
    print(response.status_code)
    print(response.headers["Content-Type"])


def kk():
    payload = {"username": "lily", "password": "123"}
    se = requests.Session()
    ret = se.post('http://127.0.0.1:5000/login', payload)
    print(ret.text)
    ret = se.get("http://127.0.0.1:5000/time")
    print(ret.text)


kk()
