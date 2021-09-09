from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
# import mysql_conn
import numpy as np
import pandas as pd



def naviebayes():
    """
    朴素贝叶斯进行文本分类
    :return: None
    """
    # news = fetch_20newsgroups(subset='all')

    # # data = mysql_conn.getData()
    # # target = range(0,1704)
    # data = np.mat(np.arange(10).reshape((5,2)).tolist())
    # # data = np.arange(10).reshape((5,2))
    # target = range(5)

    titan = pd.read_excel("C:\\Users\\kfzx-bocw\\Desktop\\Label2.xlsx", error_bad_lines=False)

    # 处理数据，找出特征值和目标值
    x = titan['exception']

    y = titan['class']

    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    print("x_train:", x_train)
    print("x_test:", x_test)
    print("y_train:", y_train)
    print("y_test:", y_test)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()
    # tf = CountVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)

    print(tf.get_feature_names())

    x_test2 = tf.transform(x_test)

    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)

    print(x_train.toarray())

    mlt.fit(x_train, y_train)

    y_predict = mlt.predict(x_test2)

    print("预测的文章类别为：", y_predict)

    x_test = pd.DataFrame(x_test)
    predict = pd.DataFrame(y_predict)

    print("y_predict lenght : ", len(y_predict))
    result = pd.concat([x_test, predict], axis=1)
    # result = pd.merge(x_test,predict)
    result = x_test.append(predict)
    # result = pd.DataFrame([x_test, predict],columns=["exception","class"])
    print(result)

    print(len(x_test))
    print(len(predict))

    # writer1 = pd.ExcelWriter("x.xlsx", engine='openpyxl')
    # x.to_excel(writer1, sheet_name='predict1', startcol=0, index=False)
    # writer1.save()
    # writer2 = pd.ExcelWriter('y_predict.xlsx',engine='openyxl')
    # predict.to_excel(writer2, sheet_name='predict2', startcol=0, index=False)
    # writer2.save()
    writer = pd.ExcelWriter('predict.xlsx', engine='openpyxl')
    result.to_excel(writer, sheet_name='predict', startcol=0, index=False)
    writer.save()


    # 得出准确率
    print("准确率为：", mlt.score(x_test2, y_test))

    print("每个类别的精确率和召回率：\n", classification_report(y_test, y_predict))
    # print("每个类别的精确率和召回率：", classification_report(y_test, y_predict, target_names=data.target_names))

    return None



if __name__ == "__main__":
    naviebayes()


