# CrowJDPrice.py
import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    try:
        header = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        li_list = soup.find_all('li', 'gl-item')
        for li in li_list:
            price = li.strong.i.string
            title = re.findall(r"<em>(.*?)<font.*?font>(.*?)</em>", str(li))
            if title:
                title_str = title[0][0] + title[0][1]
            else:
                title_str = ""
            ilt.append([price, title_str])
    except Exception as e:
        print("error:{}".format(e))


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1][:24]))


def main():
    goods = '书包'
    depth = 2
    start_url = 'https://search.jd.com/Search?keyword=' + goods + '&enc=utf-8'
    infoList = []
    for i in range(1, depth):
        try:
            url = start_url + '&page=' + str(2 * i - 1)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
