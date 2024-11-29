import requests

url = 'https://randomuser.me/api/'

response= requests.get(url)

if response.status_code==200:
    print("conexión exitosa")
    data=response.json()
    print(type(data))
    usuario=data['results'][0]
    dic_usuario= {
        'nombre' : usuario['name']['first']+' '+ usuario['name']['last'],
        'pais' : usuario['location'],
        'email' : usuario['email'],
        'foto' : usuario['picture']
    }
    print(f"nombre : {dic_usuario["nombre"]}")
    print(f"pais : {dic_usuario["pais"]}")
    print(f"email : {dic_usuario["email"]}")
    print(f"foto : {dic_usuario["foto"]}")
else:
    print(f"error al conectarse al api : {response.status.code}")