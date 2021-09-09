#导入聊天记录
import pandas as pd
df = pd.read_excel("C:\\Users\\kfzx-bocw\\Desktop\\Label2.xlsx" ,sep=',',header=0,encoding='gb18030',dtype='str')
#将不同人说的换成0 1 类别
def func(a):
    if a == 'Pluto':
        return 1;
    else:
        return 0
df['label'] = df.exception.map(func)


import jieba.finalseg
from numpy import  *
#准备数据集
dataSet = []
for i in df.index:
    dataSet.append(" ".join(jieba.cut(df.content[i])).split())
classVec = df.label.tolist()
#创建一个包含在所有文档中出现的不重复的词的列表
def createVocabList(dataSet):
    vocabSet = set()
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)
vocabList = createVocabList(dataSet)
#将一个文档转换为词向量 存在改词即为1 否则为0
def setOfwords2Vec(vocabList, inputSet): #词汇表 inputSet表示某个文档
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print('the world: %s is not in my vocabulary' % word)
    return returnVec
#训练矩阵
trainMat = []
for postinDoc in dataSet:
    trainMat.append(setOfwords2Vec(vocabList,postinDoc))
print(shape(trainMat))
#p0Vect是类别为0的条件下每个特征词向量的出现的概率；
#p1Vect是类别为1的条件下每个特征词向量的出现的概率；
#pAbusive是类别为1的概率  1-pAbusive是类别为0的概率
def trainNB1(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs) #p(辱骂的=1)的概率


    p0Num = ones(numWords);p1Num = ones(numWords) #n列
    p0Denom = 2.0; p1Denom = 2.0 #分母
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i] #n列同时计数
            p1Denom += sum(trainMatrix[i]) ##标量 分母是该类的总词条数目
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive


#训练
p0V,p1V,pAb = trainNB1(trainMat,classVec)
p0V


#预测
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 =sum(vec2Classify*p1Vec) + log(pClass1) #转为log后*全部为+
    p0 =sum(vec2Classify*p0Vec) + log(1 - pClass1)
    if p1>p0:
        return 1
    else:
        return 0


def prefunc(string):
    testWords = string
    testEntry = " ".join(jieba.cut(testWords)).split()
    thisDoc = array(setOfwords2Vec(vocabList,testEntry))
    predict = classifyNB(thisDoc,p0V,p1V,pAb)
    if predict==0:
        print ("这句话是答应不如常在说的")
    else:
        print("这句话是Pluto说的")
#最后在这里预测
string = "你大爷"
prefunc(string)




