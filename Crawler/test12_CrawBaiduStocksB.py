# CrawBaiduStocksB.py
import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            # 这一段是东方财富http://quote.eastmoney.com/stocklist.html的处理代码，现在已经变成了动态页面，获取不到了
            # href = i.attrs['href']
            # lst.append(re.findall(r"[s][hz]\d{6}", href)[0])

            # 这一段是'http://www.gupiaozhidao.com/quote/allstock.shtml'的处理代码
            stockinfo = i.string
            lst.append(re.findall(r"\((.*?)\)", stockinfo)[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    count = 0
    stock_num = 50
    for stock in lst[:stock_num]:
        url = stockURL + "sh" + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count * 100 / len(lst[:stock_num])), end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(lst[:stock_num])), end="")
            continue


def main():
    # stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_list_url = 'http://www.gupiaozhidao.com/quote/allstock.shtml'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = './BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


main()
