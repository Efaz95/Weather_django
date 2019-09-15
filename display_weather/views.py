import requests
import os
from django.shortcuts import render

api_key = os.environ.get('OPEN_WEATHER_API')


# Create your views here.
def display(request):
	if request.method == 'POST':
		city = request.POST['city']

		url = f"http://api.openweathermap.org/data/2.5/weather/?q={city}&APPID={api_key}&units=imperial"
		response = requests.get(url)
		temp = response.json()['main']['temp']
		temp_max = response.json()['main']['temp_max']
		temp_min = response.json()['main']['temp_min']
		humidity = response.json()['main']['humidity']
		weather_description = response.json()['weather'][0]['description']
		return render(request, "display_weather/display.html", {'city':city, 'temp':temp, 'temp_max':temp_max, 'temp_min':temp_min, 
																'weather_description':weather_description, 'humidity':humidity})

	else:	
		return render(request, "display_weather/display.html")