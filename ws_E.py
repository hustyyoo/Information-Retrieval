import os
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from C2char import getListdir

def getText(txt):
    f=open(txt,'r',encoding='UTF-8')
    return f.read()

def writeTxt(text, i):
    f = open('../News_ws_E/News_'+str(i)+'.txt', 'a',encoding='UTF-8')
    for w in text:
        f.write(w+' ')


def main():    
    d='./News_E/'
    os.chdir(d)
    fa=getListdir(os)
    porter=nltk.PorterStemmer()
    e=[]
    
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    for i in range(0,len(fa)):
        #words=[]
        text = str(getText(fa[i]))
        lwords=nltk.word_tokenize(text)
        words=[w for w in lwords if w not in english_punctuations]
        fword = [w for w in words if w not in stopwords.words('english')]
        pword=[porter.stem(w) for w in fword]
        writeTxt(fword,i+1)
        
    print(e)


if __name__=='__main__':
    main()