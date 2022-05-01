Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> import requests
>>> page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Xo3fdVNKhKg")
>>> soup = BeautifulSoup(page.content, 'html.parser')
>>> seven_day = soup.find(id="seven-day-forecast")
>>> forecast_items = seven_day.find_all(class_="tombstone-container")
>>> tonight = forecast_items[0]
>>> print(tonight.prettify())
<div class="tombstone-container">
 <p class="period-name">
  Today
  <br/>
  <br/>
 </p>
 <p>
  <img alt="Today: Mostly sunny, with a high near 63. Calm wind becoming west southwest 5 to 9 mph in the afternoon. " class="forecast-icon" src="newimages/medium/sct.png" title="Today: Mostly sunny, with a high near 63. Calm wind becoming west southwest 5 to 9 mph in the afternoon. "/>
 </p>
 <p class="short-desc">
  Mostly Sunny
 </p>
 <p class="temp temp-high">
  High: 63 °F
 </p>
</div>
>>> period = tonight.find(class_="period-name").get_text()
>>> short_desc = tonight.find(class_="temp").get_text()
>>> print(period)
Today
>>> print(short_desc)
High: 63 °F
>>> temp = tonight.find(class_="short-desc").get_text()
>>> temp= tonight.find(class_="temp").get_text()
>>> print(period) print(short_desc) print(temp)
SyntaxError: invalid syntax
>>> print(period)
Today
>>> print(short_desc)
High: 63 °F
>>> print(temp)
High: 63 °F
>>> img = tonight.find('img')
>>> desc = img['title']
>>> print(desc)]
SyntaxError: unmatched ']'
>>> print(desc)
Today: Mostly sunny, with a high near 63. Calm wind becoming west southwest 5 to 9 mph in the afternoon. 
>>> period_tags = seven_day.select(".tombstone-container .period-name")
>>> periods = [pt.get_text() for pt in period_tags]
>>> periods
['Today', 'Tonight', 'Thursday', 'ThursdayNight', 'Friday', 'FridayNight', 'Saturday', 'SaturdayNight', 'Sunday']
>>> import pandas as pd
