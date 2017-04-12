from flask import jsonify
from flask import Flask
from suds.client import Client
from location import location
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>hello world</h1>'

@app.route('/FIT3077-A2')
def main():
    url = 'http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl'
    client = Client(url)
    print(client)
    loc_list = [] # this list will contain all the location objects.
    locations = client.service.getLocations()
    for loc in locations:
        date_time, temperature = client.service.getTemperature(loc)
        date, time = date_time.split(' ')
        curr_loc = location(loc, date, time, temperature, client.service.getRainfall(loc)[-1])
        loc_list.append(curr_loc)
    print("DONE!")

    for i in range(len(loc_list)):
        print(loc_list[i])
        print()
        loc_list[i] = json.dumps(loc_list[i].__dict__)



    return jsonify(loc_list)

if __name__ == "__main__":
    app.run(debug=True)