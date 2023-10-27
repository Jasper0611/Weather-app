from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd

app=Flask(__name__)

@app.route('/')
def webpage():
    return render_template("index.html")

@app.route('/weather_app',methods=['post'])

def weather():
    url="https://api.openweathermap.org/data/2.5/weather"
    api_key='c491a2e13de72b0ad836d2288bf4ba2a'
    city= request.form["city"]
    units=request.form["units"]

    params={'q':city,
            'units':units,
            'appid':api_key }

    response= requests.get(url, params=params)
    data=response.json()
    result=[]
    for i in data:
        result.append ({'name': i,'value' : data[i]})
    final_res=pd.DataFrame(result)
    final_res.index = final_res.index + 1
    return render_template('table.html', data=final_res.to_html())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
