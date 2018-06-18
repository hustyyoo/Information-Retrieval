# -*- coding: utf-8 -*-
# 导入数学计算库
import math

# 两个词向量
word1 = [0.2,0.4,0.3] # 喜爱
word2 = [0.5,0.4,0.1] # 喜欢


# 计算余弦相似度
def cosine_similarity(word1,word2):
    # >>>> 请补全函数定义 <<<<
    res=0.0
    for i in range(0,len(word1)):
        res+=word1[i] * math.log(word1[i]/word2[i],2)
        print(math.log(word1[i]/word2[i],2))
    return res


def kl_distance(word1,word2):
    # >>>> 请补全函数定义 <<<<
    res=0.0
    for i in range(0,len(word1)):
        res+=word1[i] * math.log(word1[i],2)- word1[i]* math.log(word2[i],2)
        print(math.log(word1[i],2)- math.log(word2[i],2))
    return res

cos_sim = cosine_similarity(word2, word1)
kl_dis = kl_distance(word2, word1)

print(cos_sim)
print(kl_dis)

print('log2(0.1/0.3)= '+str(math.log(0.1/0.3,2)))
print('log2(0.1/0.3)= '+str(math.log(0.1,2)- math.log(0.3,2)))