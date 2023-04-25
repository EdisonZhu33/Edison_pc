from PIL import Image
import os

# 输入emf文件所在文件夹地址
emf_dir = "C:\\Users\zhucheng\Desktop\华中科技修改\图片_emf"
# 设置目标tif文件的保存地址
tif_dir = "C:\\Users\zhucheng\Desktop\华中科技修改\图片_tif"

# 遍历emf文件并转换为tif文件
for file_name in os.listdir(emf_dir):
    if file_name.endswith('.emf'):
        emf_path = os.path.join(emf_dir, file_name)
        tif_path = os.path.join(tif_dir, file_name.replace('.emf', '.tif'))
        with Image.open(emf_path) as im:
            im.save(tif_path)