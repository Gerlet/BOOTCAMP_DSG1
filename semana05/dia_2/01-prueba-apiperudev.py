import requests
from decouple import config
import os 

token = config('API_TOKEN')
url_dni = 'https://apiperu.dev/api/dni'

dni = input("ingrese dni :")

data_request = {
    "dni": dni 
}

headers_request = {
    "Authorization": "Bearer " + str(token),
    "Content-Type": "application/json"
}

response = requests.post(url_dni,json=data_request,headers=headers_request)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}")


token = config('API_TOKEN')
url_ruc = 'https://apiperu.dev/api/ruc'

ruc = input("ingrese ruc :")

data_request_ruc = {
    "ruc": ruc 
}

headers_request_ruc = {
    "Authorization": "Bearer " + str(token),
    "Content-Type": "application/json"
}

response = requests.post(url_ruc,json=data_request_ruc,headers=headers_request_ruc)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}")



token = config('API_TOKEN')
url_tipo = ' https://apiperu.dev/api/tipo_de_cambio'

tipo = input("tipo de cambio :")

data_request_tipo = {
    "tipo_de_cambio": tipo 
}

headers_request_tipo = {
    "Authorization": "Bearer " + str(token),
    "Content-Type": "application/json"
}

response = requests.post(url_tipo,json=data_request_tipo,headers=headers_request_tipo)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}")