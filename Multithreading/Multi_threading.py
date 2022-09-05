"""
单线程与多线程对比
"""
import blog_spider
import threading
import time


def single_thread():
    print("------------单线程-------------")
    for url in blog_spider.urls:
        blog_spider.func(url)


def multi_thread():
    print("------------多线程-------------")
    threads = []
    for url in blog_spider.urls:
        s = threading.Thread(target=blog_spider.func, args=(url,))
        threads.append(s)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start = time.time()
    single_thread()
    print("单线程耗时:", time.time() - start, "s")

    start1 = time.time()
    multi_thread()
    print("多线程耗时:", time.time() - start1, "s")
