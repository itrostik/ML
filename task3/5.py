import requests
from datetime import datetime

token = '52'

ID = 'mashinnoe_obuchenie_ai_big_data'

def get_wall_posts(group_id, access_token, count, offset=0):
    response = requests.get(f'https://api.vk.com/method/wall.get?domain={group_id}&count={count}&offset={offset}&v=5.103&access_token={access_token}')
    data = response.json()
    if 'error' in data:
        print(f"Error: {data['error']['error_msg']}")
        return None
    else:
        return data['response']['items']

def save_posts_to_file(posts, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for post in posts:
            date = datetime.fromtimestamp(post['date']).strftime('%Y-%m-%d %H:%M:%S')
            text = post.get('text', '').replace('\n', ' ')
            if text:
                file.write(f"{date}\n{text}\n\n")

# Получаем сообщения со стены группы
wall_posts = []
offset = 0
while len(wall_posts) < 2000:
    posts = get_wall_posts(ID, token, count=100, offset=offset)
    if not posts:
        break
    wall_posts.extend(posts)
    offset += 100

# Сохраняем сообщения в файл
if wall_posts:
    save_posts_to_file(wall_posts, 'vk_wall_posts.txt')
    print("Сообщения сохранены в файл 'vk_wall_posts.txt'")
else:
    print("Не удалось получить достаточное количество сообщений со стены группы.")

