import os
import json
from C2char import getListdir
from aip import AipNlp

def App():
    APP_ID = '11169559'
    API_KEY = '7fPVe5wjK6E3yBCLRB0wYgFZ'
    SECRET_KEY = 'uIcvCi5YyaYG6tg5pu7IvgObCC2vSD7b'

    return AipNlp(APP_ID, API_KEY, SECRET_KEY)


def getText(txt):
    f=open(txt,'r',encoding='UTF-8')
    return f.read().encode('GBK','ignore').decode('GBK')


def getStopwords(txt):
    stopwords=[]
    with open(txt,'r',encoding='UTF-8') as f:
        for word in f.read().splitlines():
            stopwords.append(word)
    return stopwords


def writeJSON(text, i):
    with open('../News_ws_C/News_'+str(i)+'.json', 'w',encoding='UTF-8') as f:
        json.dump(text,f,ensure_ascii=False)


def delStopword(items,stopwords):
    newitems=[]
    for item in items:
        if item['item'] in stopwords:
            continue
        newitems.append(item)
    return newitems


def main():
    stopwords=getStopwords('./stop_words_zh.txt')
    d='./News_C/'
    os.chdir(d)
    fa=getListdir(os)
    client = App()
    e=[]
    for i in range(0,len(fa)):
        text = str(getText(fa[i]))
        r=client.lexer(text)
        if 'error_code' in r.keys():
            e.append(fa[i])
            continue
        print(fa[i])
        items={'items':delStopword(r['items'],stopwords)}
        writeJSON(items,i+1)
    print('error: ',end=' ')
    print(e)

if __name__=='__main__':
    main()
