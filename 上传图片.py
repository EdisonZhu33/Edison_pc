import requests
from requests.exceptions import HTTPError
from PIL import Image
import io
import json


# 使用Imgur API上传图片并获取链接
def upload_image(image_path):
    client_id = 'Edison'
    url = "https://api.imgur.com/3/image"

    with open(image_path, "rb") as f:
        image_data = f.read()

    headers = {"Authorization": f"Client-ID {client_id}"}

    try:
        response = requests.post(url, headers=headers, data=image_data)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

    response_data = json.loads(response.text)["data"]
    return response_data["link"]


# 读取本地图片并上传
image_path = "C:\\Users\\zhucheng\\Desktop\\大论文\\图\\第四章图\\第四章图1.png"
image_link = upload_image(image_path)
print(image_link)
