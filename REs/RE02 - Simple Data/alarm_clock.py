#write a program that determines what is the actual time
#(using now of class datetime from module datetime) and prints it in the form
# hh:mm (hours and minutes).
#Given that an alarm is set up for 8 hours and 30 minutes later,
# the program prints the time on display at the time of the alarm, in the same format.
#Then, run the program, and copy the result followed by your program 
#(the content of the file alarm_clock.py) here:

import datetime
now = (datetime.datetime.now())
print("Now: " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2))
alarmhour = (now.hour + 8 + (now.minute + 30)//60) % 24
alarmminute = (now.minute + 30) % 60
print("Alarm: " + str(alarmhour).zfill(2) + ":" + str(alarmminute).zfill(2))

#Now: 11:36
#Alarm: 02:06

#import datetime
#now = (datetime.datetime.now())
#print("Now: " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2))
#alarmhour = (now.hour + 8 + (now.minute + 30)//60) % 24
#alarmminute = (now.minute + 30) % 60
#print("Alarm: " + str(alarmhour).zfill(2) + ":" + str(alarmminute).zfill(2))