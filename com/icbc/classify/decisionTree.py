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
    titan = pd.read_excel("C:\\Users\\kfzx-bocw\\Desktop\\Label2.xlsx", error_bad_lines=False)

    # 处理数据，找出特征值和目标值
    x = titan['exception']

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
