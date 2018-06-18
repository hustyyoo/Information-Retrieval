import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:

        r = requests.get(url, timeout=30, headers={
            'user-agent': ('Mozilla/5.0 '
                           '(Linux; Android 5.1; m1 metal Build/LMY47I; wv) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 '
                           'Chrome/53.0.2785.49 ')
        })
        r.raise_for_status()

        r.encoding = 'utf-8'

        return r.text
    except:
        return ""


def writeTxt(soup, i):
    for script in soup(["script", "style"]):
        script.decompose()
    fl = 0
    try:
        f = open('./News_C/News_'+str(i)+'.txt', 'w', encoding='UTF-8')
        f.write(soup.title.get_text())
        for it in soup.find_all('p'):
            f.write(it.get_text())

    except:
        print('write error!')


def getUrl(host, html, link):
    soup = BeautifulSoup(html, "lxml")
    #print(soup)
    for it in soup.find_all('a'):
        href = str(it.get('href'))
        if 'ShowNews' in href:
            if href in link:
                continue
            link.append(host+href)


def main():
    link = []
    host = 'http://news.swjtu.edu.cn/'
    for page in range(1, 20):
        url = host+'ShowList-94-0-'+str(page)+'.shtml'
        getUrl(host, getHTMLText(url), link)
    l = len(link)

    for i in range(0, l):
        writeTxt(BeautifulSoup(getHTMLText(link[i]), "lxml"), i+1)


if __name__ == '__main__':
    main()
