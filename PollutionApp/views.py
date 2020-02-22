from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from PollutionApp.models import Place
# import socket
# hostname = socket.gethostname()
# IP = socket.gethostbyname(hostname)
import requests
# C8A53746561311EA927A67FC0DE33DE2
print(dir(GeoIP2))

# g = GeoIP2()
# # print(g.city(IP))
# g = GeoIP()
# ip = request.META.get('REMOTE_ADDR', None)
# if ip:
#     city = g.city(ip)['city']
# else:
#     city = 'Rome'

'''
            { 'city': 'Lucknow',
              'country': 'India',
              'id': '1144',
              'last_update': '22-02-2020 05:00:00',
              'pollutant_avg': '61',
              'pollutant_id': 'PM2.5',
              'pollutant_max': '212',
              'pollutant_min': '33',
              'pollutant_unit': 'NA',
              'state': 'Uttar_Pradesh',
              'station': 'Gomti Nagar, Lucknow - UPPCB'}
'''
def get_data():
    response = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd00000164efdef19f3846087f87ad722eee8f82&format=json&limit=1')
    data = eval(response.text)
    total_count = eval(response.text)['total']
    new_response = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd00000164efdef19f3846087f87ad722eee8f82&format=json&limit=%s'%total_count)
    new_data = eval(new_response.text)
    return new_data

# Create your views here.
def home(request):
    data = get_data()
    g = GeoIP2()
    # print(g.city(IP))
    ip = request.META.get('REMOTE_ADDR', None)
    print('ip is'+ip)
    if ip:
        try:
            city = g.city(ip)['city']
        except:
            city = 'Bhopal'
    else:
        city = 'Bhopal'
    print ('city is : '+city)
    return render(request,'PollutionApp/home.html',{'records':data['records'],'current_city':city})
