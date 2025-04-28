import os
from PIL import Image

def compress_images(folder_path, quality=85):
    """
    压缩指定文件夹中的所有图片
    :param folder_path: 图片文件夹路径
    :param quality: 压缩质量(1-100)，默认为85
    """
    supported_formats = ('.jpg', '.jpeg', '.png', '.webp')
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_formats):
            try:
                file_path = os.path.join(folder_path, filename)
                with Image.open(file_path) as img:
                    # 保存为JPEG格式，设置压缩质量
                    img.save(file_path, quality=quality, optimize=True)
                    print(f'成功压缩图片: {filename}')
            except Exception as e:
                print(f'压缩图片 {filename} 时出错: {e}')

if __name__ == '__main__':
    # 压缩指定目录下的图片
    image_folder = 'e:\\000.Blog-files\\devlopr-jekyll-master\\captain-wanghui.github.io-main\\assets\\images'
    compress_images(image_folder)