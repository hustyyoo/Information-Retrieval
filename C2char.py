import os

def getLine(txt):
    t=0
    try:
        f=open(txt,'r',encoding='UTF-8')
        for l in f.readlines():
            if l.rsplit()!=[]:
                t+=1
    except:
        return -1
    return t


def getListdir(os):
    fa=os.listdir(os.getcwd())
    fa.sort(key=lambda num:int(num[num.index('_')+1:num.index('.txt')]))
    return fa


def main():
    d='./News_C/'
    os.chdir(d)
    fa=getListdir(os)
    c=l=len(fa)
    i=0
    for j in range(0,l):
        print('j='+str(j)+', '+'i='+str(i))
        if i not in range(0,c):
            break
        if getLine(fa[i])<2:
            fn=fa[i]
            print(fn)
            os.remove(fn)

            fa=getListdir(os)
            c=len(fa)
            if i<c-1:
                os.rename(fa[i],fn)
                for k in range(i+1,c):
                    os.rename(fa[k],fa[k-1])
            i-=1
            fa=getListdir(os)
        i+=1


if __name__ == '__main__':
    main()