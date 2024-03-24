import cv2
import random

# загрузка видео
video_path = '../платина.mp4'
capture = cv2.VideoCapture(video_path)

# информация о видео
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(capture.get(cv2.CAP_PROP_FPS))

# VideoWriter для сохранения обработанного видео
output_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# обрабатываем каждый кадр
while True:
    ret, frame = capture.read()
    if not ret:
        break

    # генерируем случайные координаты для размещения квадрата
    x = random.randint(0, frame_width - 50)
    y = random.randint(0, frame_height - 50)

    # рисуем белого квадрата
    cv2.rectangle(frame, (x, y), (x + 50, y + 50), (255, 255, 255), -1)

    # записываем обработанный кадр
    out.write(frame)

    # отображаем обработанный кадр
    cv2.imshow('Processed Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# освобождаем ресурсы
capture.release()
out.release()
cv2.destroyAllWindows()