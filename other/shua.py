import requests
import threading
from nonebot import logger


# 定义一个函数来执行请求
def make_request():
    url = "http://yht.111tc.top/startnum.php?user=319597664"
    
    global cishu
    cishu = 0 
    while True:
        try:
            response = requests.get(url)
            cishu = cishu + 1
            logger.info(f"请求成功，共请求了{cishu}次！\n\n\n\n\n\n\n{response.text}")
        except Exception as e:
            logger.error(f"请求失败，共请求了{cishu}次，原因{str(e)}\n\n\n\n\n\n\nError")

# 创建多个线程来执行请求
threads = []
for _ in range(100):  # 创建10个线程
    thread = threading.Thread(target=make_request)
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()
