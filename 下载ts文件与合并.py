import os.path
import requests
from concurrent.futures import ThreadPoolExecutor,wait
headers={
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
def download_one_video(url,i,path):
  """
  下载单个视频的函数
  """
  print(url,i,'开始下载')
  resp=requests.get(url,headers=headers)

  if not os.path.exists(path):
    os.makedirs(path)

  with open(os.path.join(path,f'{i}.tst'),'wb') as f:
    f.write(resp.content)
  print(url,i,'完成下载')

def download_all_videos(path):
  """

  """

  # 读取m3u8的文件内容
  with open('finall.txt') as f:
    data=f.readlines()
  #实例化 创建线程池
  pool=ThreadPoolExecutor(50)  #开50个线程
  tasks=[] #装所有线程任务
  i=0
  for line in data:
    #提取ts的url
    if line.startswith('#'):
      continue
    print(line.strip())
    #使用strip取出url结尾的换行符
    ts_url=line.strip()
    #0.ts 1.ts 2.ts 3.ts....
    tasks.append(pool.submit(download_one_video,ts_url,i,path)) # pool.submit将任务添加到线程池里
    i+=1
#集体等待我们线程对象执行完毕
  wait(tasks)
if __name__ == '__main__':
  path='ts'  #存储ts文件的目录
  download_all_videos(path)
