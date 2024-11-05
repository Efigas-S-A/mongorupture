##############################
### LIBRERIAS DEL SERVIDOR ###
##############################

from flask import Flask, request,jsonify,send_file
from flask_cors import CORS
import os
import io
##############################
### FUNCIONES MONGODB ########
##############################

from functions.users import createUser,deleteUser,updateUser,getUsers,loginUserV2
from functions.events import createEvent,deleteEvent,updateEvent,getEvents,getSpecificEvent
import pandas as pd
import bcrypt

### DEFINIMOS EL SERVIDOR
app = Flask(__name__)
CORS(app)


####################################
############# USERS ################
####################################
def hash_password(password):
    # Genera un salt y hashea la contraseña
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password



@app.route('/rupture/getUsers', methods=['GET'])

def GetUsers():
    response = getUsers()
    data = list(response)
    lista_items = []
    # Convert each ObjectId to string within dictionaries
    for item in data:
        item['_id'] = str(item['_id'])  # Assuming '_id' is the key for object IDs
        result = {key: value for key, value in item.items() if key != 'password'}
        lista_items.append(result)
    return jsonify(lista_items)

@app.route('/rupture/createUser', methods=['POST'])

def CreateUser():

    data = request.json
    data['password'] = hash_password(data['password'])
    response = createUser(data)

    return response ,201



@app.route('/rupture/deleteUser', methods=['POST'])

def DeleteUser():

    data = request.json
    response = deleteUser(data)
    if response.deleted_count == 1 :
        response = {"success": True, "message": "Elemento eliminado exitosamente"}
        status_code = 200
    else:
        response = {"error": "Error al eliminar el elemento"}
        status_code = 400
    return jsonify(response), status_code


@app.route('/rupture/updateUser',methods= ['POST'])

def UpdateUser():
    data = request.json
    result =  updateUser(data)
    if result.matched_count == 1:
        response = {"success": True, "message": "Elemento actualizado exitosamente"}
        status_code = 200
    else:
        response = {"error": "Error al actualizar el elemento"}
        status_code = 400
    return jsonify(response), status_code



##loginUser

@app.route('/rupture/login',methods = ['POST'])

def LoginV2():
    data =  request.json
    result  = loginUserV2(data)
    if(result['status'] == 'Registro éxitoso'):
        result['_id'] = str(result['_id'])
        result = {key: value for key, value in result.items() if key != 'password'}
        return result
    else:
        return result



##########################
####### EVENTOS ##########
##########################

@app.route('/rupture/getEvents', methods=['GET'])

def GetEvents():
    response = getEvents()
    data = list(response)
    lista_items = []
    # Convert each ObjectId to string within dictionaries
    for item in data:
        item['_id'] = str(item['_id'])  # Assuming '_id' is the key for object IDs
        lista_items.append(item)
    return jsonify(lista_items)

@app.route('/rupture/getSpecificEvent',methods=['POST'])
def GetSpecificEvent():
    json_ = request.json
    response = getSpecificEvent(json_)
    data = list(response)
    if(len(data) == 0):
        return {'status':'No hay elementos'}
    else:
        lista_items = []
        # Convert each ObjectId to string within dictionaries
        for item in data:
            item['_id'] = str(item['_id'])  # Assuming '_id' is the key for object IDs
            lista_items.append(item)
        return {'status':'Si hay elemento','info':lista_items[0]}



@app.route('/rupture/createEvent', methods=['POST'])

def CreateEvent():

    data = request.json
    response = createEvent(data)

    return response ,201



@app.route('/rupture/deleteEvent', methods=['POST'])

def DeleteEvent():

    data = request.json
    response = deleteEvent(data)
    if response.deleted_count == 1 :
        response = {"success": True, "message": "Elemento eliminado exitosamente"}
        status_code = 200
    else:
        response = {"error": "Error al eliminar el elemento"}
        status_code = 400
    return jsonify(response), status_code


@app.route('/rupture/updateEvent',methods= ['POST'])

def UpdateEvent():
    data = request.json
    result =  updateEvent(data)
    if result.matched_count == 1:
        response = {"success": True, "message": "Elemento actualizado exitosamente"}
        status_code = 200
    else:
        response = {"success": False, "message": "No fue posible actualizar el elemento"}
        status_code = 200
    return jsonify(response), status_code




if __name__=='__main__':
    app.run(host='0.0.0.0', port=4500)
