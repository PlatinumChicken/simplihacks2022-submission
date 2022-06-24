from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
import os
import requests
from .forms import NameForm

# Create your views here.
def index(request):
    load_dotenv()
    api = os.getenv("API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api}&q=London&aqi=yes"
    
    city_weather = requests.get(url).json()
    print(city_weather)

    weather = {
        'city' : city_weather['location']['name'],
        'temperature' : city_weather['current']['temp_f'],
        'description' : city_weather['current']['condition']['text'],
        'icon' : city_weather['current']['condition']['icon'],
        'aqi' : city_weather['current']['air_quality']['us-epa-index']
    }

    form = None

    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            print("YAYAYAYAYAYAYYAYAYAY")

    else:
        form = NameForm()

    return render(request, "simplihacks/index.html", weather, {"form" : form})