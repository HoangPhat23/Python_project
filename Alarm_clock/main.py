from tkinter import *
import datetime
import time
import winsound
from threading import Thread

root = Tk()
root.title("Alarm Clock")
root.geometry("400x300")

alarm_running = False

def start_alarm():
    global alarm_running
    if not alarm_running:
        alarm_running = True
        Thread(target=alarm).start()


root.mainloop()

