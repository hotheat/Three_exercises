"""
爬取豆瓣爱情电影海报
"""

import os
import requests


def make_dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def download_pic(url):
    response = requests.get(url).json()
    srcs = [i['cover'] for i in response['data']]
    titles = [i['title'] for i in response['data']]

    for t, s in zip(titles, srcs):
        download_image('img', t, s)


def download_image(folder, filename, url):
    path = os.path.join(folder, filename) + '.png'
    if os.path.exists(path):
        return

    make_dir(folder)
    headers = {
        'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
    }
    r = requests.get(url, headers)
    with open(path, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    url = 'https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start={}&genres=%E7%88%B1%E6%83%85'
    for i in range(0, 201, 20):
        u = url.format(i)
        print(u)
        download_pic(u)
