import datetime
import time

season_start = "2021-10-19 18:30:00"
dt_format = "%Y-%m-%d %H:%M:%S"
season_start_dt = datetime.datetime.strptime(season_start, dt_format)

while datetime.datetime.now() < season_start_dt:
    
    current_time = datetime.datetime.now()

    time_to_season = season_start_dt - current_time



    print(time_to_season)
    time.sleep(0.99999999999)