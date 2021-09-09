import jieba.finalseg
from numpy import  *
import pickle
p0V = pickle.load(open('p0V','rb'))
p1V = pickle.load(open('p1V','rb'))
pAb = pickle.load(open('pAb','rb'))
vocabList = pickle.load(open('vocabList','rb'))
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 =sum(vec2Classify*p1Vec) + log(pClass1) #转为log后*全部为+
    p0 =sum(vec2Classify*p0Vec) + log(1 - pClass1)
    if p1>p0:
        return 1
    else:
        return 0


#将一个文档转换为词向量 存在改词即为1 否则为0
def setOfwords2Vec(vocabList, inputSet): #词汇表 inputSet表示某个文档
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print('the world: %s is not in my vocabulary' % word)
    return returnVec


def prefunc():
    testWords = var.get() #得到文本框输入的值
    testEntry = " ".join(jieba.cut(testWords)).split()
    thisDoc = array(setOfwords2Vec(vocabList,testEntry))
    predict = classifyNB(thisDoc,p0V,p1V,pAb)
    t.delete(0.0, END)
    if predict==0:
        t.insert('1.0',"这句话是答应不如常在说的\n")
    else:
        t.insert('1.0',"这句话是Pluto说的\n")


###################
from tkinter import *
root = Tk() #初始化tk（）
root.title("句子预测") #窗口名字
root.geometry('1000x500') #窗口大小
root.resizable(width=True,height=True) #宽高可变


label = Label(root,text="句子预测",font=('Arial',18),width=10,height=4)




frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L,text="请输入句子：",font=('Arial',14)).pack(side=TOP)
#Label(frm_L,text="预测说这句话的人是：",font=('Arial',14)).pack(side=TOP)
frm_L.pack(side=LEFT)
#right
frm_R = Frame(frm)
var = StringVar() #绑定的变量
e = Entry(frm_R,textvariable=var,width=80) #单行文本框
var.set("hello xiaojin")
e.pack()
frm_R.pack(side=RIGHT)


label.pack(side = TOP) #RIGHT  TOP BOTTOM
frm.pack()


#def printHello():
#    t.insert('1.0',var.get())
#    t.insert('1.0','\n')
t = Text(height=2, width=50)
t.pack()
Button(root,text="确定",font = ('Arial',18),command = prefunc).pack()


root.mainloop() #进入消息循环
