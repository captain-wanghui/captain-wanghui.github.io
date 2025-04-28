import requests
import os
import random
from bs4 import BeautifulSoup

def download_images():
    # 使用picsum.photos作为图片源
    url = 'https://picsum.photos/v2/list?page=1&limit=20'
    os.makedirs('e:/000.Blog-files/devlopr-jekyll-master-1/assets/images', exist_ok=True)
    
    # 图片描述分类
    descriptions = ['nature', 'city', 'animal', 'food', 'travel', 'art', 'technology', 'people', 
                   'architecture', 'business', 'fashion', 'health', 'education', 'sports', 'music',
                   'transportation', 'weather', 'landscape', 'abstract', 'macro']
    
    try:
        response = requests.get(url)
        data = response.json()
        
        for i, item in enumerate(data[:20], 1):
            try:
                img_url = item['download_url']
                img_data = requests.get(img_url).content
                
                desc = random.choice(descriptions)
                with open(f'e:/000.Blog-files/devlopr-jekyll-master-1/assets/images/{i:05d}-{desc}.jpg', 'wb') as handler:
                    handler.write(img_data)
                print(f'Downloaded image {i:05d}-{desc}.jpg')
            except Exception as e:
                print(f'Error downloading image {i}: {e}')
    except Exception as e:
        print(f'Error fetching image list: {e}')

if __name__ == '__main__':
    download_images()