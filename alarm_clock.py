from datetime import datetime
from playsound import playsound

def SetAlarm(): 
    alarm_time = input("Set the alarm in format HH:MM:SS: \n") 
    alarm_period = SetPeriod()
    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    print(f"Alarm has been set for {alarm_time} {alarm_period}")

    while True:
        current_datetime = datetime.now()
        current_hour = current_datetime.strftime("%I")
        current_min = current_datetime.strftime("%M")
        current_sec = current_datetime.strftime("%S")
        current_period = current_datetime.strftime("%p")
        
        if(alarm_period == current_period):
            if(alarm_hour == current_hour):
                if(alarm_min == current_min):
                    if(alarm_sec == current_sec):
                        print("Wake Up!")
                        playsound(r'./Projects/alarmsound.wav')
                        break

def SetPeriod():
    alarm_period = str(input("Set the period in format AM or PM: ").upper())  
    while alarm_period != "AM" and alarm_period != "PM":
        alarm_period = input("Invalid format, set the period in format AM or PM: ").upper()  
        
    return(alarm_period)
                
SetAlarm()