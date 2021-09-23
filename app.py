from flask import Flask,render_template,request,abort
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


app = Flask(__name__)
def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('index.html')



@app.route('/after',methods=['POST','GET'])
def weather():
    api_key = '48a90ac42caa09f90dcaeee4096b9e53'
    if request.method == 'POST':
        city = request.form['city']
    else:
        #for default name mathura
        city = 'mathura'

    # source contain json data from api
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+api_key).read()
    except:
        return "Check The City Name Given"
    # converting json data to dictionary

    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "temp_cel": tocelcius(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city),
    }
    return render_template('after.html',data=data)


@app.route('/back')
def back():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
