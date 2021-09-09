from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def decision():
    """
    决策树对异常类型进行预测
    :return: None
    """
    # 获取数据
    # titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    titan = pd.read_excel("C:\\Users\\kfzx-bocw\\Desktop\\AIops\\log27.csv", error_bad_lines=False)

    # 处理数据，找出特征值和目标值
    # _index	_type	_id	_score	_source-busiMetric-amount	_source-busiMetric-appSeqNo	_source-busiMetric-branch	_source-busiMetric-callerApp	_source-busiMetric-callerIp	_source-busiMetric-input	_source-busiMetric-methodName		_source-busiMetric-organization	_source-busiMetric-output	_source-busiMetric-returnCode	_source-busiMetric-returnCodeType	_source-busiMetric-serviceName	_source-busiMetric-spanId	_source-busiMetric-traceId	_source-busiMetric-truthService	_source-busiMetric-zone	_source-logtime	_source-pubMetric-logType	_source-pubMetric-serviceType	_source-pubMetric-timeCosted	_source-techMetric-template	_source-techMetric-templateGroup	_source-hostIP	_source-hostName	_source-logType	_source-appName	_source-destination	_source-@log_name	_source-@timestamp
    x = titan['index', 'type', 'id', 'score', 'source-busiMetric-amount','source-busiMetric-appSeqNo' , 'source-busiMetric-branch' , 'source-busiMetric-callerApp' ,'source-busiMetric-callerIp' , 'source-busiMetric-input' ,'source-busiMetric-organization' ,'source-busiMetric-output' ,'source-busiMetric-returnCode' , 'source-busiMetric-returnCodeType' ,'source-busiMetric-serviceName' , 'source-busiMetric-spanId' , 'source-busiMetric-traceId' ,'source-busiMetric-truthService' ,'source-busiMetric-zone' ,'source-logtime' ,'source-pubMetric-logType' ,'source-pubMetric-serviceType' ,'source-pubMetric-timeCosted' ,'source-techMetric-template' ,'source-techMetric-templateGroup' ,'source-hostIP' ,'source-hostName' ,'source-logType' ,'source-appName' , 'source-destination' ,'source-@log_name' ,'source-@timestamp']

    y = titan['class']

    print("x:",x)
    print("y:",y)
    # 缺失值处理
    # x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据集到训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    print(x_train)
    print(len(x_train))
    print(y_train)
    print(len(y_train))

    # 进行处理（特征工程）特征-》类别-》one_hot编码
    # dict = DictVectorizer(sparse=False)
    dict = CountVectorizer()

    # x_train = dict.fit_transform(x_train.to_dict(orient="records"))
    x_train = dict.fit_transform(x_train)

    # print(dict.get_feature_names())

    # x_test = dict.transform(x_test.to_dict(orient="records"))
    x_test = dict.transform(x_test)

    print(x_train)
    print(len(x_train))
    print(y_train)
    print(len(y_train))

    # 用决策树进行预测
    dec = DecisionTreeClassifier()

    dec.fit(x_train, y_train)

    # 预测准确率
    print("预测的准确率：", dec.score(x_test, y_test))

    # # 导出决策树的结构
    export_graphviz(dec, out_file="./tree.dot", feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])

    # 随机森林进行预测 （超参数调优）
    rf = RandomForestClassifier(n_jobs=-1)

    param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

    # 网格搜索与交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    print("准确率：", gc.score(x_test, y_test))

    print("查看选择的参数模型：", gc.best_params_)

    return None


if __name__ == "__main__":
    decision()
