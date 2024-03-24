import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import io
from urllib.request import urlopen

# Загрузка аудиофайла
audio_path = 'https://dagshub.com/kinkusuma/esc50-dataset/raw/master/dataset/1-100032-A-0.wav'
data, sample_rate = sf.read(io.BytesIO(urlopen(audio_path).read()))

# Визуализация амплитуды звуковой волны
plt.figure(figsize=(12, 4))
plt.plot(np.arange(len(data)) / sample_rate, data)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.show()

# Поиск участка с звуком лая (примерно с 2 до 4 секунд)
start_time = 2  # начальное время в секундах
end_time = 4  # конечное время в секундах
start_sample = int(start_time * sample_rate)
end_sample = int(end_time * sample_rate)
y_bark = data[start_sample:end_sample]

# Построение спектрограммы для найденного участка
plt.figure(figsize=(12, 4))
D = np.abs(np.fft.fft(y_bark))
freqs = np.fft.fftfreq(len(y_bark), 1/sample_rate)
plt.plot(freqs[:len(freqs)//2], 20 * np.log10(D[:len(D)//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Spectrogram')
plt.show()

# Находим индексы, где амплитуда больше порога (звук)
sound_threshold = 0.01
sound_indices = np.where(np.abs(data) > sound_threshold)[0]

# Если в аудиофайле нет звука, сохраняем пустой файл
if len(sound_indices) == 0:
    print("Аудиофайл не содержит звука.")
    exit()

# Находим первый и последний индексы не тишины
start_index = sound_indices[0]
end_index = sound_indices[-1]

# Определяем длительность участка без тишины
duration_without_silence = (end_index - start_index) / sample_rate

# Если длительность участка без тишины больше 0.5 секунды, обрезаем его
if duration_without_silence > 0.5:
    start_index = int(start_index + (duration_without_silence - 0.5) * sample_rate / 2)
    end_index = start_index + int(0.5 * sample_rate)

# Выбираем участок без тишины и с длительностью не более 0.5 секунды
data_without_silence = data[start_index:end_index]

# Сохраняем обработанный аудиофайл без тишины
output_path = 'output_without_silence.wav'
sf.write(output_path, data_without_silence, sample_rate)
print(f"Аудиофайл без тишины и длительностью 0.5 секунды сохранен по пути: {output_path}")



