# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:53:23 2022

@author: Admin
"""

import json
import requests


url = "http://127.0.0.1:8000/network_attack_prediction"


input_data_for_model = {
    
    'src_bytes' : 491,
    'dst_bytes' : 0,
    'duration' : 0,
    'dst_host_srv_count' : 25,
    'count' : 2,
    'dst_host_count' : 150,
    'service' : 20,
    'flag' : 9,
    'dst_host_srv_serror_rate' : 0.0,
    'srv_serror_rate' : 0.0,
    'serror_rate' : 0.0,
    'dst_host_serror_rate' : 0.0,
    'logged_in' : 0,
    'num_root' : 0,
    'num_compromised' : 0,
    'dst_host_same_srv_rate' : 0.17,
    'same_srv_rate' : 1.0,
    'srv_rerror_rate' : 0.0,
    'rerror_rate' : 0.0,
    'dst_host_srv_rerror_rate' : 0.0
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data = input_json)

print(response.text)






