import sys
from PIL import Image

images = []
for arg in sys.argv[1:]:          # 命令行传入多张图
    images.append(Image.open(arg))

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images=images[1:],    # 追加后续帧
    duration=200,                 # 每帧 200ms
    loop=0,                       # 0 = 无限循环
)