import numpy as np

# Генерация случайных данных
x = 365
y = 100
z = 3

weather_data = np.zeros((x, y, z))

# Генерация случайных температур, влажности и давления
weather_data[:, :, 0] = np.random.uniform(-20, 40, size=(x, y))  # температура
weather_data[:, :, 1] = np.random.uniform(20, 90, size=(x, y))  # влажность
weather_data[:, :, 2] = np.random.uniform(950, 1050, size=(x, y))  # давление


mean_temperature = np.mean(weather_data[:, :, 0], axis=(0, 1))
mean_humidity = np.mean(weather_data[:, :, 1], axis=(0, 1))
mean_pressure = np.mean(weather_data[:, :, 2], axis=(0, 1))

max_temperature = np.max(weather_data[:, :, 0])
min_temperature = np.min(weather_data[:, :, 0])

temperature_range = (max_temperature, min_temperature)

mean_pressure_per_station = np.mean(weather_data[:, :, 2], axis=0)
station_index = np.argmax(mean_pressure_per_station)


threshold_humidity = 40
mean_humidity_per_day = np.mean(weather_data[:, :, 1], axis=1)
low_humidity_days = np.where(mean_humidity_per_day < threshold_humidity)[0]
