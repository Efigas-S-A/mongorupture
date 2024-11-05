from pymongo import MongoClient



def getInstance():
    ## funcion para obtener una instancia directa en la base de mongo
    #### CREDENCIALES DE CONEXIÓN
    host = "localhost"
    port = 27017
    username = "root" ## DEBE ESTAR EN VARIABLES DE ENTORNO
    password = "root123" ## DEBO CAMBIAR LA CONTRASEÑA
    # creamos una instancia del cliente
    client =  MongoClient(host,port,username=username,password=password)
    return client


if __name__ == '__main__':
    print(getInstance())

