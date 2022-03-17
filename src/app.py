# importar flask
import pymysql
from multiprocessing  import connection
from flask import Flask,  make_response, jsonify


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host= '127.0.0.1',
            user= 'root',
            password= '1234',
            db = 'a2censo',
            port = 4550
        )

        self.cursor = self.connection.cursor()

    def select_user(self):
        sql = "SELECT idcampaign, name, amount, requestedAmount FROM campaign"

        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        
            info = []
            for compaing in data:
                valor = {
                    "idcampaign": compaing[0],
                    "name": compaing[1],
                    "amount": compaing[2],
                    "requestedAmount": compaing[3],
                } 
                info.append(valor)
               
            return info
            
        except Exception as e:
            raise


app = Flask(__name__)


@app.route('/')
def Index():
    return 'Bienvenido'


@app.route('/json', methods=['GET'])
def getData():
    database = Database()
    data = database.select_user()
    print(data)
         
    try:
        res = make_response(jsonify({
        "meta": {
            "status": 200
        }
    },
        {
        "data": data
    }))
        return res
    except Exception as ex:
        return 'Error'
    


def pag_not_found(error):
    return  '<h1> La página que intentas buscar no existe</h1>'


# comprobar que el archivo ejecutado es el principal
if __name__ == '__main__':
    # app.config.from_object(config['development'])
    app.register_error_handler(404,pag_not_found)
    # Establecer el puerto y para actualizar cambios
    app.run(debug=True)