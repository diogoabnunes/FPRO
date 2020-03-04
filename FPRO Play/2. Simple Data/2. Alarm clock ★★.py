# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:52:50 2018

@author: diogo
"""
def alarm(hour,minutes):
    result_hour = (hour + 6 + (minutes + 51)//60) % 24
    result_minute = (minutes + 51) % 60
    
    result = str(result_hour).zfill(2) + ":" + str(result_minute).zfill(2)
    return result

print(alarm(5,10))