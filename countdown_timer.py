from tkinter import *
from tkinter import ttk
import datetime
import time

# Instance of tkinter and label the top
root = Tk()
root.title('Countdown to the start of the 2021-22 NBA Season!')
# Styling the label widget for the displayed clock
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')

# establish the times needed
season_start = "2021-10-19 18:30:00"
dt_format = "%Y-%m-%d %H:%M:%S"
season_start_dt = datetime.datetime.strptime(season_start, dt_format)

# This function is used to display time on the label
def countdown():
    current_time = datetime.datetime.now()

    time_to_season = season_start_dt - current_time

    time_to_season_days = time_to_season.days
    time_to_season_seconds = time_to_season.seconds
    time_to_season_hours = time_to_season_seconds // 3600
    time_to_season_minutes = (time_to_season_seconds % 3600) // 60
    time_to_season_seconds = time_to_season_seconds % 60

    countdown_formatted = f"{time_to_season_days} days {time_to_season_hours} hours {time_to_season_minutes} minutes {time_to_season_seconds} seconds"
    
    lbl.config(text = countdown_formatted)
    lbl.after(1000, countdown)

# Placing clock at the centre of the tkinter window
lbl.pack(anchor = 'center')
countdown() 

mainloop()