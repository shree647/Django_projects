from django.shortcuts import render


import json

import urllib.request


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='+city+',&appid=c444f36a04bfae7c52cca54207f538fb').read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']), }

        print(data)
    else:
        data = {}
    return render(request, "main.html", data)


