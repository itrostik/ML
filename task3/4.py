import requests
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import time
import pytz

# Установка вашего API ключа от OpenWeatherMap
api_key = '7b5502dcc70b85c3143e41d6cc2ac1c6'


def get_weather_data(city):
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
  response = requests.get(url)
  data = response.json()
  return data


def extract_weather_info(data):
  timestamp = datetime.now()
  temperature = data['main']['temp']
  humidity = data['main']['humidity']
  pressure = data['main']['pressure']
  return timestamp, temperature, humidity, pressure


def plot_temperature_data(timestamps, temperatures):
  plt.figure(figsize=(10, 6))
  plt.plot(timestamps, temperatures, label='Temperature (°C)', marker='o', linestyle='-')
  plt.xlabel('Local Time (Kazan)')
  plt.ylabel('Temperature (°C)')
  plt.title('Temperature Forecast in Kazan')
  plt.grid(True)
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.legend()
  plt.show()


if __name__ == '__main__':
  city = 'Kazan'
  timestamps = []
  temperatures = []

  with open('weather_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Timestamp', 'Temperature (°C)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
      data = get_weather_data(city)
      timestamp, temperature, _, _ = extract_weather_info(data)
      writer.writerow({
        'Timestamp': timestamp,
        'Temperature (°C)': temperature,
      })
      print(f'Weather data saved for {timestamp}')

      kazan_timezone = pytz.timezone('Europe/Moscow')
      timestamp_kazan = timestamp.astimezone(kazan_timezone)

      # Добавляем данные в списки для построения графика
      timestamps.append(timestamp_kazan)
      temperatures.append(temperature)

      # Построение графика изменения температуры
      plot_temperature_data(timestamps, temperatures)

      time.sleep(3600)  # Ждем 1 час
