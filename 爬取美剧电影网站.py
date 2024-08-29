import requests
#美剧网址

#抓取思路
#1 先看当前网站是什么类型的视频网站
#2 查看当前网站的视频是怎么样加载的(一次性加载的,还是分了多个视频段进行加载的)
#3 如果是多个片段的文件 需要找到当前包含多个片段文件的地址
headers={
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
session=requests.Session()
session.get("https://www.mjwo.net/",headers=headers)
url='https://www.mjwo.net/play/19487-1-1/'
first_m3u8_url="https://two.svipplay.com/lzm3u8/cc6e7ea8c9b0059ac1be5a38d27e5b42.m3u8?token=jVRWE96NhUK_qMtsIHk0DQ&expires=1724941325"

resp=session.get(first_m3u8_url,headers=headers)
with open('finall.txt', 'wb') as f:
  f.write(resp.content)
