#import statements
import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime
from geopy.geocoders import Nominatim
from suntime import Sun

def sun():
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")

        #get city from textbox entry
        ladd1 = str(ent.get())
        locat1 = geolocator.geocode(ladd1)

        #latitude and longitude from location
        latitude = locat1.latitude
        longitude = locat1.longitude

        sun = Sun(latitude, longitude)

        #gets correct time
        time_zone = datetime.datetime.now()

        #get rise and set times
        sunR = sun.get_local_sunrise_time(time_zone)
        sunS = sun.get_local_sunset_time(time_zone)

        #sets rise and set times
        res_rise = sunR.strftime('%H:%M')
        res_set = sunS.strftime('%I:%M %p')

        #results 1 & 2 are set to the rise and set times
        result1.set(res_rise)
        result2.set(res_set)

    except:
        #error messages if nothing is entered
        result1.set("Oops!")
        result2.set("Enter a city and try again.")

#instance of tk class
win = tk.Tk()
win.title("Sunrise/Sunset") #window title

result1 = StringVar() #gets rise time and sets as string
result2 = StringVar() #gets set time and sets as string

#add a label for textbox
ttk.Label(win, text="Enter a city:").grid(column=0, row=0)

#adding a textbox entry widget
ent = Entry(win, width=50)
ent.grid(column=2, row=0, padx=8, pady=5, sticky=W)

#label for sunrise and sunset
ttk.Label(win, text="Sunrise: ").grid(column=0, row=3, sticky=W, pady=10)
ttk.Label(win, text="Sunset: ").grid(column=0, row=4, sticky=W)

# Creating label for class variable
ttk.Label(win, text="", textvariable=result1).grid(row=3,column=2, sticky=W)
ttk.Label(win, text="", textvariable=result2).grid(row=4,column=2, sticky=W)

#add a button
ttk.Button(win, text="Check", command=sun).grid(column=3, row=0)

#add icon to window
win.iconphoto(False, tk.PhotoImage(file='sun.png'))
win.mainloop()
