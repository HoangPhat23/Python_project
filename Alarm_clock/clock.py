
from tkinter import *
import time
import datetime
from threading import *
import winsound

root = Tk()
root.title("Alarm Clock")
root.geometry("300x300")

def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{sencond.get()}"
    curent_alarm_time = datetime.datetime.now().strftime("%H:%M:%S")
    if curent_alarm_time == set_alarm_time:
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
root.mainloop()