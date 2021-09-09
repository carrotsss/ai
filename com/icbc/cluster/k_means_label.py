import pandas as pd
from sklearn.cluster import KMeans
# from pandas import dataframe as df

# 建立模型。n_clusters参数用来设置分类个数，即K值，这里表示将样本分为两类。
clf_KMeans = KMeans(n_clusters=3, max_iter=10)

# 模型训练。得到预测值。
print("clf_KMeans聚类中心\n", (clf_KMeans.cluster_centers_))
quantity = pd.Series(clf_KMeans.labels_).value_counts()
print ("cluster2聚类数量\n", (quantity))

#获取聚类之后每个聚类中心的数据
res0Series = pd.Series(clf_KMeans.labels_)
res0 = res0Series[res0Series.values == 1]
# print("类别为1的数据\n",(df.iloc[res0.index]))






###########################################################################################

# 项目一：电商用户质量RFM聚类分析


from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd

# 导入并清洗数据
data = pd.read_csv('RFM.csv')
data.user_id = data.user_id.astype('str')
print(data.info())
print(data.describe())
X = data.values[:,1:]


# 数据标准化(z_score)
Model = preprocessing.StandardScaler()
X = Model.fit_transform(X)


# 迭代，选择合适的K
ch_score = []
ss_score = []
inertia = []
for k in range(2,10):
    clf = KMeans(n_clusters=k,max_iter=1000)
    pred = clf.fit_predict(X)
    ch = metrics.calinski_harabaz_score(X,pred)
    ss = metrics.silhouette_score(X,pred)
    ch_score.append(ch)
    ss_score.append(ss)
    inertia.append(clf.inertia_)


# 做图对比
fig = plt.figure()
ax1 = fig.add_subplot(131)
plt.plot(list(range(2,10)),ch_score,label='ch',c='y')
plt.title('CH(calinski_harabaz_score)')
plt.legend()


ax2 = fig.add_subplot(132)
plt.plot(list(range(2,10)),ss_score,label='ss',c='b')
plt.title('轮廓系数')
plt.legend()


ax3 = fig.add_subplot(133)
plt.plot(list(range(2,10)),inertia,label='inertia',c='g')
plt.title('inertia')
plt.legend()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']  # 设置正常显示中文
plt.show()


# 根据最佳的K值，聚类得到结果
model = KMeans(n_clusters=3,max_iter=1000)
model.fit_predict(X)
labels = pd.Series(model.labels_)
centers = pd.DataFrame(model.cluster_centers_)
result1 = pd.concat([centers,labels.value_counts().sort_index(ascending=True)],axis=1) # 将聚类中心和聚类个数拼接在一起
result1.columns = list(data.columns[1:]) + ['counts']
print(result1)
result = pd.concat([data,labels],axis=1)   # 将原始数据和聚类结果拼接在一起
result.columns = list(data.columns)+['label']  # 修改列名
pd.options.display.max_columns = None  # 设定展示所有的列
print(result.groupby(['label']).agg('mean')) # 分组计算各指标的均值

# 对聚类结果做图

fig = plt.figure()
ax1= fig.add_subplot(131)
ax1.plot(list(range(1,4)),s.R_days,c='y',label='R')
plt.title('R指标')
plt.legend()
ax2= fig.add_subplot(132)
ax2.plot(list(range(1,4)),s.F_times,c='b',label='F')
plt.title('F指标')
plt.legend()
ax3= fig.add_subplot(133)
ax3.plot(list(range(1,4)),s.M_money,c='g',label='M')
plt.title('M指标')
plt.legend()
plt.show()

####################################################################################

# -*- coding: utf-8 -*-
#导入相应的包
import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import numpy as np
import matplotlib.pylab as plt


#待聚类的数据点,cancer.csv有653行数据,每行数据有11维:
dataset = np.loadtxt('cancer.csv', delimiter=",")
#np数据从0开始计算，第0维维序号排除，第10维为标签排除，所以为1到9
points = dataset[:,1:9]
cancer_label = dataset[:,10]
print("points:\n",points)
print("cancer_label:\n",cancer_label)
# k-means聚类
#将原始数据做归一化处理
data=whiten(points)
#使用kmeans函数进行聚类,输入第一维为数据,第二维为聚类个数k.
#有些时候我们可能不知道最终究竟聚成多少类,一个办法是用层次聚类的结果进行初始化.当然也可以直接输入某个数值.
#k-means最后输出的结果其实是两维的,第一维是聚类中心,第二维是损失distortion,我们在这里只取第一维,所以最后有个[0]
#centroid = kmeans(data,max(cluster))[0]
centroid = kmeans(data,2)[0]
print(centroid)
#使用vq函数根据聚类中心对所有数据进行分类,vq的输出也是两维的,[0]表示的是所有数据的label
label=vq(data,centroid)[0]
num = [0,0]
for i in label:
    if(i == 0):
        num[0] = num[0] + 1
    else:
        num[1] = num[1] + 1
print('num =',num)
#np.savetxt('file.csv',label)
print("Final clustering by k-means:\n",label)
result = np.subtract(label,cancer_label)
print("result:\n",result )


count = [0,0]
for i in result:
    if(i == 0):
        count[0] = count[0] + 1
    else:
        count[1] = count[1] + 1
print( count)
print (float(count[1])/(count[0]+count[1]))