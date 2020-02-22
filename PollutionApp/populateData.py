import requests
import pprint

def get_data():
	response = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd00000164efdef19f3846087f87ad722eee8f82&format=json&limit=1')

	data = eval(response.text)
	total_count = eval(response.text)['total']
	new_response = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd00000164efdef19f3846087f87ad722eee8f82&format=json&limit=%s'%total_count)

	new_data = eval(new_response.text)
	pprint.pprint(new_data)


if __name__ == '__main__':
    get_data()
