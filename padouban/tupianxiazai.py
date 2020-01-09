import requests
from padouban.settings import USER_AGENT
headers = {
    'Referer':'http://www.douban.com/',
    'User-Agent':USER_AGENT,
}
def download_img(src):
    filename = src.split('/')[-1]
    img = requests.get(src, headers=headers)
    img.encoding = "utf-8"
    # img是图片响应，不能字符串解析;
    # img.content是图片的字节内容
    with open('imgs/' + filename, 'wb') as file:
        file.write(img.content)
    print(src, filename)
