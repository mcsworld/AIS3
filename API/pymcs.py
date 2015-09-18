#!/usr/bin/python
#encoding: utf-8

import time
import json
import requests
from requests.auth import HTTPBasicAuth

def get_user_token(app_key, app_secret, email, password):
	url = "https://mcs.mediatek.com/oauth/login/thirdpart"
	data = {"email": email,
		"password": password
	}

	r = requests.post(url, auth=(app_key, app_secret), data=data)
	response = json.loads(r.text)

	if response['code'] != 200:
		print "[!] Get user token failed! MCS response: %s" % response['message']
		return None

	return response

def refresh_user_token(app_key, app_secret, token):
	url = "https://mcs.mediatek.com/oauth/login/thirdpart/refresh"
	data = {"token": token}

	r = requests.post(url, auth=(app_key, app_secret), data=data)
	response = json.loads(r.text)

	if response['code'] != 200:
		print "[!] Refresh user token failed! MCS response: %s" % response['message']
		return None

	return response['results']

def send_data(access_token, deviceId, chn_id, value):
	url = "https://api.mediatek.com/mcs/v2/devices/%s/datapoints" % deviceId
	headers = {"Authorization": "Bearer " + access_token,
			   "Content-Type": "application/json"
	}
	data = {"datapoints": [{"dataChnId": chn_id,
	                        "values": {"value": value}}]
	}

	r = requests.post(url, headers=headers, data=json.dumps(data))
	response = json.loads(r.text)

	if response['code'] != 200:
		print "[!] Send GPIO failed! MCS response: %s" % response['message']
		return False
	return True

def send_data_from_device(access_token, deviceId, device_key, chn_id, value):  
	url = "https://api.mediatek.com/mcs/v2/devices/%s/datapoints" % deviceId
	headers = {"deviceKey": device_key,
			   "Content-Type": "application/json"
	}
	data = {"datapoints": [{"dataChnId": chn_id,
	                        "values": {"value": value}}]
	}

	r = requests.post(url, headers=headers, data=json.dumps(data))
	response = json.loads(r.text)

	if response['code'] != 200:
		print "[!] Send data from device failed! MCS response: %s" % response['message']
		return False
	return True

def send_gps_from_device(access_token, deviceId, device_key, chn_id, value):  
	url = "https://api.mediatek.com/mcs/v2/devices/%s/datapoints" % deviceId
	headers = {"deviceKey": device_key,
			   "Content-Type": "application/json"
	}
	data = {"datapoints": [{"dataChnId": chn_id,
	                        "values": value}]
	}

	r = requests.post(url, headers=headers, data=json.dumps(data))
	response = json.loads(r.text)

	if response['code'] != 200:
		print "[!] Send gps data from device failed! MCS response: %s" % response['message']
		return False
	return True

