import pymysql
import numpy as np

conn = pymysql.connect(host='122.66.157.54', user = "admin", passwd="admin123!", db="autotestplatform", port=3306, charset="utf8")
cur = conn.cursor()

def getData():
    print("start")
    #sql语句
    sql = "SELECT convert(exception_stack using utf8) from datacase_excute_info c where excute_id='a297132961fe491d8de9cc7bebc023a0'"
    # sql = "SELECT convert(exception_stack using utf8) FROM datacase_excute_info WHERE excute_id IN (SELECT excute_id FROM autocase_excute_info WHERE app_id = '104362' )"
    # sql = "SELECT convert(exception_stack using utf8) FROM datacase_excute_info WHERE excute_id IN (SELECT excute_id FROM autocase_excute_info WHERE app_id = '103622' )"

    list = cur.execute(sql)
    print(list)
    # type(list)

    result = cur.fetchall()
    array = np.array(result)
    list = array.tolist()
    print(type(array))

    list2 = [x for x in list if x != ['']]

    # for data in list2:
    #     print(data)
    #     data = ''.join(data)
    #     print(data)
    #     type1 = type(data)
    #     print(type1)

    for i in range(len(list2)):
        list2[i] = ''.join(str(list2[i]).strip())

    # while ['']  in list:
    #     print("清洗")
    #     list.remove([''])
    #     # list.remove("['']")

    for data in list2:
        print(data)


    return list2


    #数据
    # for i in range(len(person)):
    #     param = tuple(person[i])
    #     #执行sql语句
    #     count = cur.execute(sql, param)
    #     #判断是否成功
    #     if count > 0:
    #         print("添加数据成功！\n")
    #         #提交事务
    #         conn.commit()
    #         #查询数据
    #         cur.execute("select * from tb_user")
    #         #获取数据
    #         users = cur.fetchall();
    #         for i in range(len(users)):
    #             print(users[i])


def close():
    #关闭资源连接
    cur.close()
    conn.close()
    print("数据库断开连接！");



# getData()
# close()