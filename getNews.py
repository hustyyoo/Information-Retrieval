import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30, headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'},
                         verify=False) #防ban，不验证ssl
        r.raise_for_status()

        r.encoding = 'utf-8' #强制编码，便于后期处理

        return r.text
    except:
        return ""


def writeTxt(soup, i):
    for script in soup(["script", "style"]):
        script.decompose()
    fl = 0
    try:
        f = open('./News_E/News_'+str(i)+'.txt', 'w', encoding='UTF-8')
        f.write(soup.title.get_text())
        for it in soup.find_all('p'):
            f.write(it.get_text())

    except:
        print('write error! url is : '+url)


def getUrl(host, html, link):
    soup = BeautifulSoup(html, "lxml")
    #print(soup)
    for it in soup.find_all('a'):
        href = str(it.get('href'))
        if 'briefings-statements' in href:
            if href in link:
                continue
            link.append(href)
    print(len(link))

def main():

    link = []
    host = 'http://www.whitehouse.gov/'
    for page in range(1, 80):

        url = host+'news/page/'+str(page)+'/'

        getUrl(host, getHTMLText(url), link)

    for i in range(0, len(link)):
        writeTxt(BeautifulSoup(getHTMLText(link[i]), "lxml"), i+1)
    

if __name__ == '__main__':
    requests.urllib3.disable_warnings() #忽略白宫网站ssl验证
    main()
