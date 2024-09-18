city_temperatures = [32.6, 35.5, 30.4, 25.7, 40.4, 30.6, 30.9]
for day, temperature in enumerate(city_temperatures):
     if day == 0:
          day = "monday"
     elif day == 1:
          day = "tuesday"
     elif day == 2:
          day = "Wednesday"
     elif day == 3:
          day = "thursday"
     elif day == 4:
          day = "friday"
     elif day == 5:
          day = "saturday"
     elif day == 6:
          day = "sunday"
     print(f"on {day}, temperature was {temperature} ")
          
     
# or