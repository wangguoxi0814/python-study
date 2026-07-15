# 同步下载图片
import requests
import time
import os
import asyncio
import aiohttp

img_list = [
    'https://k.sinaimg.cn/www/dy/slidenews/4_img/2015_46/704_1775750_489797.jpg/w640slw.jpg',
    'https://pic.rmb.bdstatic.com/bjh/bb963316367/250904/e55063e18ddf94aeffcf18b1d5922615.jpeg',
    'https://www.sinaimg.cn/qc/model_lib/photo/100/19/57/87126_src.jpg'
] * 20

img_dir = str(time.time())
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

def download_img():
    start = time.time()
    for img_url in img_list:
        print(f'准备下载{img_url}')
        response = requests.get(img_url)
        print(f'下载成功!')
        with open(f'{img_dir}/{img_url[-10:]}', 'wb') as f:
            f.write(response.content)
    end = time.time()
    print(f'总耗时{end - start}秒')

async def aio_download_task(img_url, session):
    print(f'准备下载{img_url}')
    response = await session.get(img_url)
    content = await response.read()
    print(f'下载成功!')
    with open(f'{img_dir}/{img_url[-10:]}', 'wb') as f:
        f.write(content)
    await response.release()

async def aio_download_img():
    start = time.time()
    session = aiohttp.ClientSession()
    await asyncio.gather(*(aio_download_task(img_url, session) for img_url in img_list))
    await session.close()
    end = time.time()
    print(f'总耗时{end - start}秒')

if __name__ == '__main__':
    # 传统图片下载 16s下载60张
    # download_img()
    # aio图片下载 1.5s下载60张
    asyncio.run(aio_download_img())