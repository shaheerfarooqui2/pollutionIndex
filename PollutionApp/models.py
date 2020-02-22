from django.db import models


'''
{'city': 'Lucknow',
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
# Create your models here.
class Place(models.Model):
    city = models.CharField(max_length=264)
    state = models.CharField(max_length=264)
    station = models.CharField(max_length=264)
    last_update = models.DateTimeField(auto_now=False,auto_now_add=False)
    city_id = models.IntegerField()
    pollutant_id = models.CharField(max_length=264)
    pollutant_avg = models.IntegerField()
    pollutant_max = models.IntegerField()
    pollutant_min = models.IntegerField()
    pollutant_unit = models.CharField(max_length=264)
