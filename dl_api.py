# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:48:31 2022

@author: Admin
"""

from fastapi import FastAPI
from pydantic import BaseModel
import json
import numpy as np
 
# keras
from keras.models import load_model

app = FastAPI()

class model_input(BaseModel):
    
    src_bytes : int
    dst_bytes : int
    duration : int
    dst_host_srv_count : int
    count : int
    dst_host_count : int
    service : int
    flag : int
    dst_host_srv_serror_rate : float
    srv_serror_rate : float
    serror_rate : float
    dst_host_serror_rate : float
    logged_in : int
    num_root : int
    num_compromised : int
    dst_host_same_srv_rate : float
    same_srv_rate : float
    srv_rerror_rate : float
    rerror_rate : float
    dst_host_srv_rerror_rate : float
        
    
# Model saved with Keras model.save()
MODEL_PATH = 'model_cls.h5'

# Loading  our trained model
model = load_model(MODEL_PATH)
    
@app.post('/network_attack_prediction')
def attack_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    sb = input_dictionary['src_bytes']
    db = input_dictionary['dst_bytes']
    dur = input_dictionary['duration']
    dhsc = input_dictionary['dst_host_srv_count']
    cnt = input_dictionary['count']
    dhc = input_dictionary['dst_host_count']
    ser = input_dictionary['service']
    fg = input_dictionary['flag']
    dhssr = input_dictionary['dst_host_srv_serror_rate']
    ssr = input_dictionary['srv_serror_rate']
    sr = input_dictionary['serror_rate']
    dhsr = input_dictionary['dst_host_serror_rate']
    li = input_dictionary['logged_in']
    nr = input_dictionary['num_root']
    nc = input_dictionary['num_compromised']
    dhsasr = input_dictionary['dst_host_same_srv_rate']
    sasr = input_dictionary['same_srv_rate']
    srr = input_dictionary['srv_rerror_rate']
    rr = input_dictionary['rerror_rate']
    dhsrr = input_dictionary['dst_host_srv_rerror_rate']
    
    input_list = [sb, db, dur, dhsc, cnt, dhc, ser, fg, dhssr, ssr, sr, dhsr, li, nr, nc, dhsasr, sasr, srr, rr, dhsrr]
    
    pred = model.predict([input_list])
    
    prediction = np.where(pred > 0.5,1,0)
    

    if prediction[0] == 0:
        return "Normal"
    else:
        return "Malicious"
    
    
    
    
    
