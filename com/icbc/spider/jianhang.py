import json
from multiprocessing import Queue
import requests
import threading


def handle_request(url ,data):

    # header = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2",
    #     "Cookie": "lastLoginTime=; tranCCBIBS1=Or2nDsIrhmeFeAqpQ3ah8aWhWzZU3BVcpTYknBndXjnp5nbgm175tqRqhTeU0FrdkzR0oDwcwjGkMIxckzagKCTcOjbYwPiKte; userType=; custName=; domain=.ccb.com; ticket=;  path=/;  domain=ccb.com; INFO=9j9g|XYnb8; path=/; JSESSIONID=w3higyFI4xeSSUWHgWe9cAuqmH4SM7EYV_SN-LluoRo-BjrOe00w!-973059345; tranFAVOR=RGf0PS4a%2CgmJQybL%2C2m7QWbb%2ClmzQfbq%2CYm1Qzbv%2C0mkQMbn%2CUf0ezeI4TN9Jw; cs_cid=; null=1428292362.20480.0000;  expires=Sun, 22-Mar-2020 10:03:44 CET; WCCTC=831506086_2062764081_1476892237",
    # }

    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2",
        "Cookie": "lastLoginTime=; tranCCBIBS1=QKyMjCv3GkfToVK7W1mjNonv9BTi9PmqZhxyRPnr3x17TO94M0SvqEF7%2ChDiYT2rGRmiNWZquhyuBOlrXhaeKRcsWhh2qdRGMu; userType=; custName=; domain=.ccb.com; ticket=;  path=/;  domain=ccb.com; INFO=8j9a|Xa/Ti; path=/; JSESSIONID=PBz20ktBVjSpj9j20r52L-7ouQwdonsQmm99UOhsSJUyGEkV3GNj!1012091373; tranFAVOR=GFRzqLOhjHLf1zAIj3Li17AJjpLL1mA2jYLp1oADjbLE1OArjUErDIDCmUC2IK; cs_cid=; null=1143145226.20480.0000;  expires=Mon, 20-Apr-2020 06:14:00 CEST; WCCTC=723219717_1912196058_449970558",
        "Host" :"life.ccb.com",
        "Connection": "Keep - Alive"
    }

    # response = requests.post(url=url,headers=header,data=data);

    response = requests.get(url = url ,headers = header)
    return response


def head_index1():

    loginFileUpdate = open("汽车服务/境外wifi.txt", "w", errors='ignore')  # 创建一个中间文件

    for i in range(100000,900000,1000):
        for j in range (i, i + 1000,100):
            url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01002&OPUN_COD=" + str(j) + \
                  "&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+str(i)+"&APPVERSION=4.2.1.002&APPFLAG=01"

            # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01002&OPUN_COD=610000&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD=610000&APPVERSION=4.2.1.002&APPFLAG=01";

            #     "client": "4",
            #     # "_session": "1568730680462863807031595576",
            #     # "keyword": "%E5%9C%9F%E8%B1%86",
            #     "_vs": "2305",
            #     # "cursor": "%7B%22data%22%3A%5B%22notes%22%2C%22recispe%22%2C%22courses%22%2C%22products%22%5D%2C%22type%22%3A2%7D",
            data = {}
            respose  = handle_request(url=url , data=data)
            print(respose.text)
            # try:
            print(type(respose.text))
            # print(respose.text).replace('\r','').replace("\n",'').replace(' ','').replace('\t','')
            # print(respose.text.lstrip('['))
            # jsonResponse = json.loads(respose.text.strip('[]'))
            # r = respose.json()
            # r=json.dump(respose.text)
            # print(r)
            # for item in r:
            #     var = item['bill_merchant_desc']
            #     print(var)
            # except Exception:
            #     print()
            flag = respose.text.find("bill_item")
            if flag!=-1:
                loginFileUpdate.write(respose.text )
            else:
                loginFileUpdate.write(str(j))
                # loginFile.close()
                # loginFileUpdate.close()
                # # 将中间文件的内容回写到原配置文件
                # loginFile = open("login.txt", "w")
                # loginFileUpdate = open("loginUpdate.txt", "r")
                # for line in loginFileUpdate:
                #     loginFile.write(line)
                # loginFile.close()
                # loginFileUpdate.close()

                # index_response_dict = json.loads(respose.text)
                # for index_item in index_response_dict['data']['webp_image_detail']:
                #     for index_item_1 in index_item['url_list']:
                #         # for item in index_item_1['url']:
                #             data_2 = {
                #                 "url" : index_item['url'],
                #             }
                #             print(data_2)
                #             queue_list.put(data_2)

                # index_response_dict = json.loads(respose.text)
                # for index_item in index_response_dict['result']['cs']:
                #     for index_item_1 in index_item['cs']:
                #         for item in index_item_1['cs']:
                #             data_2 = {
                #                 "client": "4",
                #                 "_session": "1568730680462863807031595576",
                #                 "keyword": item['name'],
                #                 "_vs": "400",
                #                 "cursor": "{\"data\":[\"notes\",\"recipe\",\"courses\",\"products\"],\"type\":2}",
                #             }
                #             queue_list.put(data_2)


 loginFileUpdate = open("保险医疗/代缴养老金.txt", "w", errors='ignore')  # 创建一个中间文件

def head_index4(pr, ct, key , loginFileUpdate):

    # if ct == "" or ct is None or ct == {} or ct['cityid'] is None or len(ct) == 0 or ct:
    if ct == {} or pr['provinceid'] == '110000' or pr['provinceid'] =='120000' or pr['provinceid'] == '500000' or pr['provinceid'] == '310000' :
        ct['cityid'] = pr['provinceid']
        ct['cityname'] = pr['name']

    #电费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01002&OPUN_COD=" + ct['cityid'] + \
    #       "&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 手机
    #url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01009&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #固话
    #url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01011&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #水费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01001&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #燃气费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01003&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 宽带费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01012&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #暖气费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01004&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #物业费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01005&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #彩票店
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=02003&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #房租
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01025&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 全国话费充值
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=10033&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 有线电视
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01008&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 联合收费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01015&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #联名卡充值
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01013&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #学杂费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05003&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #考试报名费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05001&OPUN_COD="+ ct['ciyid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 餐费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=50006&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 代办费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=50008&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #高考志愿咨询
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=50003&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 教材费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05016&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 培训费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05002&OPUN_COD="+ ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 外语培训
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=50005&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 校园卡充值
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05013&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 幼儿园缴费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05015&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #智慧校园
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=50007&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 证件照随拍
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=50009&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 停车费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=02018&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 交通罚款
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01006&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 餐卡充值
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=40008&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 学生平安险
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=60007&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 国税地税
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05009&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 非税缴费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05008&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 资金归集
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=06003&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 党费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05004&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 工会费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05006&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 公益捐款
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=06002&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 会员服务费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=80017&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 家政服务
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=80004&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 团费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=05005&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 我要付款
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=04004&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 洗护服务
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=80027&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 养老院服务费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=08007&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 租金
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=80006&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 租车
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01016&OPUN_COD=" + ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 智慧加油
    # url =  "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=20001&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 智慧停车
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=20002&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 无感交付
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=20015&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 车辆年检
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=20015&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 停车费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=20008&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 汽车养护
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=20007&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 车辆管理费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=20014&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 境外wifi
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=30009&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 旅游年卡
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=02016&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD=440000&APPVERSION=4.2.1.002&APPFLAG=01"
    # 旅游年票
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=30011&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 旅游团费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 配送费
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=04006&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 签到有礼
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=40007&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 体育赛事
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=40002&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 健康体检
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=60004&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    # 社保
    # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=60003&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    #代缴养老金
    url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=" + key + "&OPUN_COD=" +ct['cityid'] +"&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD="+ pr['provinceid'] +"&APPVERSION=4.2.1.002&APPFLAG=01"
    data = {}

    respose  = handle_request(url=url , data=data)
    print(respose.text)
    print(type(respose.text))
    # loginFileUpdate.write(respose.text if respose.text.find("bill_merchant_desc") else "")
    flag = respose.text.find("bill_item")
    if flag!=-1:
        # .join(["{\"all\":", "}"])
        print(respose.text[respose.text.find("["):][0:-7].join(["{\"all\":", "\n]\n}"]))
        j_result = json.loads(respose.text[respose.text.find("["):][0:-7].join(["{\"all\":", "\n]\n}"]))
        for company in j_result['all']:
            loginFileUpdate.writelines(pr['name'] + " " + ct['cityname'] + " " + company['bill_merchant_desc'] + "\n")
    else:
        # url = "http://life.ccb.com/tran/WCCMainPlatV5?SERVLET_NAME=WCCMainPlatV5&APPPLATFORM=01&BILL_ITEM=01025&OPUN_COD=" + \
        #       ct['cityid'] + "&CCB_IBSVersion=V5&isAjaxRequest=true&TXCODE=JF1105&BANK_COD=" + pr['provinceid'] + "&APPVERSION=4.2.1.002&APPFLAG=01"
        loginFileUpdate.write("")
        # loginFileUpdate.close()

def main():
    myThread1 = threading.Thread(target=head_index1())
    myThread4 = threading.Thread(target=head_index4())
    myThread1.start()
    myThread4.start()

# if __name__ == "__main__":
#     main()
#     loginFileUpdate.close()

# head_index()
# print(queue_list.qsize())