from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from pymongo import MongoClient
import subprocess
import random
import os
import json

app = Flask(__name__)
cors = CORS(app)

client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://heroku_9mwpmxbf:kbjivvmpq9m46gr32u4t05bs8u@ds211708.mlab.com:11708/heroku_9mwpmxbf?retryWrites=false'))

@app.route("/")
def home():
  return render_template('know-city.html')

@app.route("/choose-places", methods=["POST"])
def sendCateg():
  sp_points = [
    {'name': u'Funda\xe7\xe3o Bienal de S\xe3o Paulo', 'price': None, 'address': [u'Pavilh\xe3o Ciccillo Matarazzo, Parque do Ibirapuera, Port\xe3o 3', u'Avenida Pedro \xc1lvares Cabral - Ibirapuera', u'S\xe3o Paulo - SP, 04094-000, Brazil'], 'hours': None, 'phone': u'(11) 5576-7600', 'closed': False, 'gPlusPlaceId': '102415334017243710071', 'gps': [-23.586576, -46.65243]},
    {'name': u'MAC Museu de Arte Contempor\xe2nea', 'price': None, 'address': [u'Pra\xe7a do Rel\xf3gio Solar, 160 - Butant\xe3', u'S\xe3o Paulo - SP', u'05508-050, Brazil'], 'hours': [[u'Monday', [[u'Closed']]], [u'Tuesday', [[u'10:00 am--6:00 pm']], 1], [u'Wednesday', [[u'10:00 am--6:00 pm']]], [u'Thursday', [[u'10:00 am--6:00 pm']]], [u'Friday', [[u'10:00 am--6:00 pm']]], [u'Saturday', [[u'10:00 am--6:00 pm']]], [u'Sunday', [[u'10:00 am--6:00 pm']]]], 'phone': u'(11) 3091-3039', 'closed': False, 'gPlusPlaceId': '103592739850995885212', 'gps': [-23.560525, -46.722193]},
    {'name': u'Pinacoteca do Estado de S\xe3o Paulo', 'price': None, 'address': [u'Pra\xe7a da Luz, 2 - Luz', u'S\xe3o Paulo - SP', u'01120-010, Brazil'], 'hours': [[u'Monday', [[u'Closed']]], [u'Tuesday', [[u'10:00 am--5:30 pm']]], [u'Wednesday', [[u'10:00 am--5:30 pm']], 1], [u'Thursday', [[u'10:00 am--10:00 pm']]], [u'Friday', [[u'10:00 am--5:30 pm']]], [u'Saturday', [[u'10:00 am--5:30 pm']]], [u'Sunday', [[u'10:00 am--5:30 pm']]]], 'phone': u'(11) 3324-1000', 'closed': False, 'gPlusPlaceId': '111695161134528390618', 'gps': [-23.534267, -46.633925]},
    {'name': u'Catedral Metropolitana Ortodoxa', 'price': None, 'address': [u'Rua Vergueiro, 1515 - Para\xedso', u'S\xe3o Paulo - SP', u'04101-000, Brazil'], 'hours': [[u'Monday', [[u'9:00 am--6:00 pm']]], [u'Tuesday', [[u'9:00 am--6:00 pm']]], [u'Wednesday', [[u'9:00 am--6:00 pm']], 1], [u'Thursday', [[u'9:00 am--6:00 pm']]], [u'Friday', [[u'9:00 am--6:00 pm']]], [u'Saturday', [[u'10:00 am--1:00 pm']]], [u'Sunday', [[u'Closed']]]], 'phone': u'(11) 5579-0019', 'closed': False, 'gPlusPlaceId': '113657696025506990707', 'gps': [-23.575505, -46.64013]},
    {'name': u'Mercado Municipal', 'price': None, 'address': [u'S\xe3o Paulo', u'SP', u'Brazil'], 'hours': [[u'Monday', [[u'6:00 am--6:00 pm']]], [u'Tuesday', [[u'6:00 am--6:00 pm']], 1], [u'Wednesday', [[u'6:00 am--6:00 pm']]], [u'Thursday', [[u'6:00 am--6:00 pm']]], [u'Friday', [[u'6:00 am--6:00 pm']]], [u'Saturday', [[u'6:00 am--6:00 pm']]], [u'Sunday', [[u'6:00 am--4:00 pm']]]], 'phone': u'(11) 3313-3365', 'closed': False, 'gPlusPlaceId': '107763848755756000380', 'gps': [-23.541823, -46.629432]},
    {'name': u'Parque Zoologico de Sao Paulo', 'price': None, 'address': [u'Avenida Miguel Est\xe9fano, 4241, \xc1gua Funda', u'S\xe3o Paulo - SP', u'04301-905, Brazil'], 'hours': [[u'Monday', [[u'Closed']]], [u'Tuesday', [[u'9:00 am--5:00 pm']], 1], [u'Wednesday', [[u'9:00 am--5:00 pm']]], [u'Thursday', [[u'9:00 am--5:00 pm']]], [u'Friday', [[u'9:00 am--5:00 pm']]], [u'Saturday', [[u'9:00 am--5:00 pm']]], [u'Sunday', [[u'9:00 am--5:00 pm']]]], 'phone': u'(11) 5073-0811', 'closed': False, 'gPlusPlaceId': '111909766301598831754', 'gps': [-23.650848, -46.620372]},
    {'name': u'Parque Municipal M\xe1rio Pimenta Camargo', 'price': None, 'address': [u'S\xe3o Paulo', u'SP', u'Brazil'], 'hours': None, 'phone': None, 'closed': False, 'gPlusPlaceId': '114564055244879555337', 'gps': [-23.587998, -46.688749]},
    {'name': u'Parque do Piqueri', 'price': None, 'address': [u'S\xe3o Paulo', u'SP', u'Brazil'], 'hours': [[u'Monday', [[u'6:00 am--6:00 pm']]], [u'Tuesday', [[u'6:00 am--6:00 pm']]], [u'Wednesday', [[u'6:00 am--6:00 pm']], 1], [u'Thursday', [[u'6:00 am--6:00 pm']]], [u'Friday', [[u'6:00 am--6:00 pm']]], [u'Saturday', [[u'6:00 am--6:00 pm']]], [u'Sunday', [[u'6:00 am--6:00 pm']]]], 'phone': u'(11) 2097-2213', 'closed': False, 'gPlusPlaceId': '113913598183042244318', 'gps': [-23.527772, -46.573578]},
    {'name': u'Parque Ecol\xf3gico do Tiet\xea', 'price': None, 'address': [u'Rua Guira Acangatara, 70 - Engenheiro Goulart', u'S\xe3o Paulo - SP', u'03719-000, Brazil'], 'hours': None, 'phone': u'(11) 2958-1477', 'closed': False, 'gPlusPlaceId': '101038083639074453927', 'gps': [-23.480882, -46.505433]},
    {'name': u'Altino Arantes Building', 'price': None, 'address': [u'S\xe3o Paulo', u'SP', u'Brazil'], 'hours': None, 'phone': None, 'closed': False, 'gPlusPlaceId': '101536603638594793565', 'gps': [-23.55052, -46.633309]},
    {'name': u'Jardim Bot\xe2nico', 'price': None, 'address': [u'Avenida Miguel Est\xe9fano, 3031 - \xc1gua Funda', u'S\xe3o Paulo - SP', u'04301-012, Brazil'], 'hours': None, 'phone': u'(11) 5073-6300', 'closed': False, 'gPlusPlaceId': '111791769193755942474', 'gps': [-23.63931, -46.627272]},
    {'name': u'Villa Lobos Park', 'price': None, 'address': [u'Av. Prof. Fonseca Rodrigues, 2001 - Alto dos Pinheiros', u'S\xe3o Paulo - SP', u'05461-010, Brazil'], 'hours': [[u'Monday', [[u'5:30 am--7:00 pm']]], [u'Tuesday', [[u'5:30 am--7:00 pm']], 1], [u'Wednesday', [[u'5:30 am--7:00 pm']]], [u'Thursday', [[u'5:30 am--7:00 pm']]], [u'Friday', [[u'5:30 am--7:00 pm']]], [u'Saturday', [[u'5:30 am--7:00 pm']]], [u'Sunday', [[u'5:30 am--7:00 pm']]]], 'phone': u'(11) 2683-6302', 'closed': False, 'gPlusPlaceId': '116048175015213511581', 'gps': [-23.54778, -46.724909]},
    {'name': u'Pateo do Collegio', 'price': None, 'address': [u'Pra\xe7a Pateo do Collegio, 2, Centro', u'Sao Paulo - SP', u'01016-040, Brazil'], 'hours': None, 'phone': u'(11) 3105-6899', 'closed': False, 'gPlusPlaceId': '107296545639935625199', 'gps': [-23.548056, -46.633026]},
    {'name': u'Mosteiro S\xe3o Bento S\xe3o Paulo', 'price': None, 'address': [u'Largo S\xe3o Bento - Centro', u'SP', u'01029-010, Brazil'], 'hours': None, 'phone': u'(11) 3328-8799', 'closed': False, 'gPlusPlaceId': '106333430672562544884', 'gps': [-23.544317, -46.634002]},
    {'name': u'Monumento aos Bandeirantes', 'price': None, 'address': [u'S\xe3o Paulo', u'SP', u'Brazil'], 'hours': None, 'phone': u'(11) 2226-0620', 'closed': False, 'gPlusPlaceId': '111049949775252012235', 'gps': [-23.580271, -46.660782]},
    {'name': u'Casa das Rosas - Espa\xe7o Haroldo de Campos de Poesia e Literatura', 'price': None, 'address': [u'Sao Paulo - SP', u'Brazil'], 'hours': [[u'Monday', [[u'Closed']]], [u'Tuesday', [[u'10:00 am--10:00 pm']]], [u'Wednesday', [[u'10:00 am--10:00 pm']], 1], [u'Thursday', [[u'10:00 am--10:00 pm']]], [u'Friday', [[u'10:00 am--10:00 pm']]], [u'Saturday', [[u'10:00 am--6:00 pm']]], [u'Sunday', [[u'10:00 am--6:00 pm']]]], 'phone': u'(11) 3251-5271', 'closed': False, 'gPlusPlaceId': '103077975069184185554', 'gps': [-23.57088, -46.645185]},
    {'name': u"Pub O'Malley's Bar", 'price': None, 'address': [u'Alameda Itu, 1529 - Jardim Paulista', u'S\xe3o Paulo - SP', u'01421-001, Brazil'], 'hours': [[u'Monday', [[u'12:00 pm--4:00 am']]], [u'Tuesday', [[u'12:00 pm--4:00 am']]], [u'Wednesday', [[u'12:00 pm--4:00 am']], 1], [u'Thursday', [[u'12:00 pm--4:00 am']]], [u'Friday', [[u'12:00 pm--5:00 am']]], [u'Saturday', [[u'12:00 pm--5:00 am']]], [u'Sunday', [[u'12:00 pm--4:00 am']]]], 'phone': u'(11) 3086-0780', 'closed': False, 'gPlusPlaceId': '112444160593219911604', 'gps': [-23.558046, -46.66608]},
    {'name': u'Casa 92', 'price': None, 'address': [u'Rua Crist\xf3v\xe3o Gon\xe7alves, 92 - Largo da Batata', u'S\xe3o Paulo - SP', u'05426-050, Brazil'], 'hours': None, 'phone': u'(11) 3032-0371', 'closed': False, 'gPlusPlaceId': '102158095308577242794', 'gps': [-23.564266, -46.694342]},
    {'name': u'Morrison Rock Bar', 'price': None, 'address': [u'Rua In\xe1cio Pereira da Rocha, 362 - Pinheiros', u'S\xe3o Paulo - SP', u'05432-011, Brazil'], 'hours': [[u'Monday', [[u'9:00 am--6:00 pm']]], [u'Tuesday', [[u'9:00 am--6:00 pm']], 1], [u'Wednesday', [[u'9:00 am--6:00 pm']]], [u'Thursday', [[u'9:00 am--6:00 pm']]], [u'Friday', [[u'9:00 am--6:00 pm']]], [u'Saturday', [[u'9:00 am--6:00 pm']]], [u'Sunday', [[u'Closed']]]], 'phone': u'(11) 3814-1022', 'closed': False, 'gPlusPlaceId': '110001791929073026084', 'gps': [-23.560363, -46.690244]},
    {'name': u'Eu Tu Eles Bar', 'price': None, 'address': [u'Avenida Brigadeiro Faria Lima, 2902 - Jardim Paulistano', u'S\xe3o Paulo - SP', u'01451-000, Brazil'], 'hours': [[u'Monday', [[u'Closed']]], [u'Tuesday', [[u'6:00 pm--2:30 am']]], [u'Wednesday', [[u'6:00 pm--2:30 am']], 1], [u'Thursday', [[u'6:00 pm--2:30 am']]], [u'Friday', [[u'6:00 pm--2:30 am']]], [u'Saturday', [[u'4:00 pm--2:30 am']]], [u'Sunday', [[u'4:00 pm--2:30 am']]]], 'phone': u'(11) 3071-4535', 'closed': False, 'gPlusPlaceId': '105310591144354735138', 'gps': [-23.581924, -46.684596]},
    {'name': u'Santa Julia', 'price': None, 'address': [u'Rua Gomes de Carvalho, 1705 - Vila Ol\xedmpia', u'S\xe3o Paulo - SP', u'04547-006, Brazil'], 'hours': [[u'Monday', [[u'6:00 am--1:00 am']]], [u'Tuesday', [[u'6:00 am--1:00 am']]], [u'Wednesday', [[u'6:00 am--1:00 am']], 1], [u'Thursday', [[u'6:00 am--1:00 am']]], [u'Friday', [[u'6:00 am--1:00 am']]], [u'Saturday', [[u'7:00 am--1:00 am']]], [u'Sunday', [[u'4:00 pm--12:00 am']]]], 'phone': u'(11) 3846-1452', 'closed': False, 'gPlusPlaceId': '114763254411722000870', 'gps': [-23.595388, -46.689039]},
    {'name': u'Tatu Bola Bar e Grelha', 'price': None, 'address': [u'Rua Clodomiro Amazonas, 202 - Vila Nova Conceicao', u'S\xe3o Paulo - SP', u'04537-000, Brazil'], 'hours': [[u'Monday', [[u'6:00 pm--2:00 am']]], [u'Tuesday', [[u'6:00 pm--2:00 am']]], [u'Wednesday', [[u'6:00 pm--2:00 am']], 1], [u'Thursday', [[u'6:00 pm--2:00 am']]], [u'Friday', [[u'6:00 pm--2:00 am']]], [u'Saturday', [[u'2:00--3:00 pm']]], [u'Sunday', [[u'Closed']]]], 'phone': u'(11) 2539-9071', 'closed': False, 'gPlusPlaceId': '103570646068319961370', 'gps': [-23.586078, -46.679612]},
    {'name': u'Cervejaria Nacional', 'price': None, 'address': [u'Avenida Pedroso de Morais, 604 - Pinheiros', u'S\xe3o Paulo - SP', u'05420-001, Brazil'], 'hours': [[u'Monday', [[u'5:00--11:30 pm']]], [u'Tuesday', [[u'5:00--11:30 pm']]], [u'Wednesday', [[u'5:00--11:30 pm']]], [u'Thursday', [[u'5:00 pm--1:30 am']], 1], [u'Friday', [[u'12:00 pm--1:30 am']]], [u'Saturday', [[u'12:00 pm--1:30 am']]], [u'Sunday', [[u'Closed']]]], 'phone': u'(11) 3628-5000', 'closed': False, 'gPlusPlaceId': '117668896723988852393', 'gps': [-23.564888, -46.690634]},
    {'name': u'Casa 92', 'price': None, 'address': [u'Rua Crist\xf3v\xe3o Gon\xe7alves, 92 - Largo da Batata', u'S\xe3o Paulo - SP', u'05426-050, Brazil'], 'hours': None, 'phone': u'(11) 3032-0371', 'closed': False, 'gPlusPlaceId': '102158095308577242794', 'gps': [-23.564266, -46.694342]},
    {'name': u'Maria Farof\xe1', 'price': None, 'address': [u'Rua Maria C\xe2ndida, 641 - Vila Guilherme', u'S\xe3o Paulo - SP', u'02071-011, Brazil'], 'hours': [[u'Monday', [[u'12:00 am--5:00 pm']]], [u'Tuesday', [[u'12:00 am--5:00 pm']]], [u'Wednesday', [[u'12:00 am--5:00 pm']]], [u'Thursday', [[u'12:00 am--5:00 pm']]], [u'Friday', [[u'12:00 am--5:00 pm']], 1], [u'Saturday', [[u'12:00 am--5:00 pm']]], [u'Sunday', [[u'Closed']]]], 'phone': u'(11) 2218-0438', 'closed': False, 'gPlusPlaceId': '106715211618200229201', 'gps': [-23.503676, -46.608529]},
    {'name': u'D.O.M. Restaurante', 'price': u'', 'address': [u'Rua Bar\xe3o de Capanema, 549 - Cerqueira C\xe9sar', u'S\xe3o Paulo - SP', u'01411-011, Brazil'], 'hours': [[u'Monday', [[u'12:00--3:00 pm'], [u'7:00 pm--12:00 am']], 1], [u'Tuesday', [[u'12:00--3:00 pm'], [u'7:00 pm--12:00 am']]], [u'Wednesday', [[u'12:00--3:00 pm'], [u'7:00 pm--12:00 am']]], [u'Thursday', [[u'12:00--3:00 pm'], [u'7:00 pm--12:00 am']]], [u'Friday', [[u'12:00--3:00 pm'], [u'7:00 pm--12:00 am']]], [u'Saturday', [[u'7:00 pm--12:00 am']]], [u'Sunday', [[u'Closed']]]], 'phone': u'(11) 3088-0761', 'closed': False, 'gPlusPlaceId': '114707756704043831424', 'gps': [-23.56594, -46.667565]},
    {'name': u'Sal Gastronomia', 'price': None, 'address': [u'Rua Minas Gerais, 350', u'SP', u'08391-599, Brazil'], 'hours': None, 'phone': u'(11) 3151-3085', 'closed': False, 'gPlusPlaceId': '107755385452865889968', 'gps': [-23.555248, -46.664672]},
    {'name': u'Terra\xe7o It\xe1lia', 'price': None, 'address': [u'Avenida Ipiranga, 344', u'Centro, S\xe3o Paulo - SP', u'01046-010, Brazil'], 'hours': [[u'Monday', [[u'9:00 am--6:00 pm']], 1], [u'Tuesday', [[u'9:00 am--6:00 pm']]], [u'Wednesday', [[u'9:00 am--6:00 pm']]], [u'Thursday', [[u'9:00 am--6:00 pm']]], [u'Friday', [[u'9:00 am--6:00 pm']]], [u'Saturday', [[u'9:00 am--6:00 pm']]], [u'Sunday', [[u'9:00 am--6:00 pm']]]], 'phone': u'(11) 2189-2929', 'closed': False, 'gPlusPlaceId': '100824233727493129740', 'gps': [-23.54547, -46.643794]},
    {'name': u'Pizza & Pasta Famiglia Mancini', 'price': None, 'address': [u'Rua Avanhandava, 25 - Bela Vista', u'S\xe3o Paulo - SP', u'01306-000, Brazil'], 'hours': [[u'Monday', [[u'11:30 am--12:00 am']]], [u'Tuesday', [[u'11:30 am--12:00 am']], 1], [u'Wednesday', [[u'11:30 am--12:00 am']]], [u'Thursday', [[u'11:00 am--1:00 am']]], [u'Friday', [[u'Closed']]], [u'Saturday', [[u'11:30 am--2:30 am']]], [u'Sunday', [[u'11:30 am--12:00 am']]]], 'phone': u'(11) 3231-0033', 'closed': False, 'gPlusPlaceId': '112308407643683173461', 'gps': [-23.54976, -46.645173]},
    {'name': u'Instituto Tomie Ohtake', 'price': None, 'address': [u'Rua Corop\xe9, 88 - Pinheiros', u'S\xe3o Paulo - SP', u'05426-010, Brazil'], 'hours': [[u'Monday', [[u'Closed']]], [u'Tuesday', [[u'11:00 am--8:00 pm']]], [u'Wednesday', [[u'11:00 am--8:00 pm']], 1], [u'Thursday', [[u'11:00 am--8:00 pm']]], [u'Friday', [[u'11:00 am--8:00 pm']]], [u'Saturday', [[u'11:00 am--8:00 pm']]], [u'Sunday', [[u'11:00 am--8:00 pm']]]], 'phone': u'(11) 2245-1900', 'closed': False, 'gPlusPlaceId': '101289912626126851910', 'gps': [-23.561214, -46.694309]},
    {'name': u'Espa\xe7o Cultural Sesc Pompeia', 'price': None, 'address': [u'Rua Cl\xe9lia, 93 - Vila Pomp\xe9ia', u'S\xe3o Paulo - SP', u'05042-000, Brazil'], 'hours': [[u'Monday', [[u'Closed']]], [u'Tuesday', [[u'8:00 am--10:00 pm']]], [u'Wednesday', [[u'8:00 am--10:00 pm']], 1], [u'Thursday', [[u'8:00 am--10:00 pm']]], [u'Friday', [[u'8:00 am--10:00 pm']]], [u'Saturday', [[u'8:00 am--10:00 pm']]], [u'Sunday', [[u'8:00 am--6:00 pm']]]], 'phone': u'(11) 3871-7700', 'closed': False, 'gPlusPlaceId': '109353417656975026246', 'gps': [-23.525194, -46.683598]},
    {'name': u'Bella Paulista Casa dos P\xe3es', 'price': None, 'address': [u'Rua Haddock Lobo, 354 - Consola\xe7\xe3o', u'S\xe3o Paulo - SP', u'01414-000, Brazil'], 'hours': [[u'Monday', [[u'Open 24 hours']]], [u'Tuesday', [[u'Open 24 hours']], 1], [u'Wednesday', [[u'Open 24 hours']]], [u'Thursday', [[u'Open 24 hours']]], [u'Friday', [[u'Open 24 hours']]], [u'Saturday', [[u'Open 24 hours']]], [u'Sunday', [[u'Open 24 hours']]]], 'phone': u'(11) 3214-3347', 'closed': False, 'gPlusPlaceId': '112292053009561912801', 'gps': [-23.556193, -46.659988]}
  ]
  user_name = request.form.get('user_name')
  user_email = request.form.get('user_email')
  knowCity = request.form.get('options')
  
  return render_template('choose_points.html', knowCity=knowCity, sp_points=sp_points, user_name=user_name, user_email=user_email)
  # return render_template('wait.html')
  
@app.route("/send_result", methods=['POST'])
def sendResult():
  
  req_data = request.get_json()
  gPlusUserId = random.random()*10000000000000000
  user_to_add = {'name': req_data['user']['name'], 'gPlusUserId': gPlusUserId, 'email': req_data['user']['email'], 'recommedCity': req_data['user']['recommedCity']}

  db=client.heroku_9mwpmxbf
  db.users.insert_one(user_to_add)
  
  for cat in req_data['categories']:
    db.user_categories.insert_one(cat)
  
  return 'ok'

@app.route("/get-routes")
def getRoutes():
  suggestion_id=request.args.get("suggestion-id")
  
  db=client.heroku_9mwpmxbf
  suggestion_to_find = db.suggestions.find_one({'suggestionId': int(suggestion_id)})
  suggestion_to_return = {'routes': suggestion_to_find['routes'], 'user': suggestion_to_find['user'], 'suggestionId': suggestion_to_find['suggestionId'] }
  
  return jsonify(suggestion_to_return)
  
@app.route("/get-user")
def getUser():
  user_id=request.args.get("user-id")
  
  db=client.heroku_9mwpmxbf
  user_to_find = db.users.find_one({'gPlusUserId': int(user_id)})
  user_to_return = {'email': user_to_find['email'], 'gPlusUserId': user_to_find['gPlusUserId'], 'recommedCity': user_to_find['recommedCity']}
  
  return jsonify(user_to_return)

@app.route("/send-evaluation", methods=['POST'])
def sendEvaluation():
  
  req_data = request.get_json()

  db=client.heroku_9mwpmxbf
  db.evaluation.insert_one(req_data)
  
  return 'ok'
    
if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT', 5000), host='0.0.0.0')
