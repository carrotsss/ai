import json
import requests
from jianhang import head_index4

def handle_request(url ,data):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Charset": "GBK,utf-8,ZHS16GBK;q=0.7,*;q=0.3",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Cookie": "lastLoginTime=; tranCCBIBS1=EURGZwHZ4RcUmukRWHGKqwDdCyXueXwkRs%2C9ZrQvhh%2CjaJg8qYv9o1xpachCmbQbRoCqanAIRAD7aUwzRQCZaoQHZtBuZUQhNnMUTuKIpIM6ZR; userType=; custName=; domain=.ccb.com; ticket=;  path=/;  domain=ccb.com; INFO=9j9m|Xa2m6; path=/; JSESSIONID=yNDuRbi-TCG-rTLbGAbbTXBy7A2xFVnDD5Reu9HohPdVk6EJ71Il!882025334; tranFAVOR=Mz484j83u5w9IlhPaa09ZlgPAaL9YlaPna69GlwPTan9GlUPTa69Te0dOdKNPOzd3q; cs_cid=; null=1210254090.20480.0000;  expires=Sat, 18-Apr-2020 14:39:03 CEST; WCCTC=363955751_1944723847_1764278243",
        "Host": "life.ccb.com",
        "Connection": "Keep-Alive",
    }

    # response = requests.post(url=url,headers=header,data=data);
    response = requests.get(url = url ,headers = header)
    return response

loginFileUpdate = open("省份.txt", "w", errors='ignore')  # 创建一个中间文件


def crawl():
    url = "http://life.ccb.com/cn/payment/include/phone.json"
    data = {}
    respose  = handle_request(url=url , data=data)
    print(respose.text[respose.text.find("{"):])
    # loginFileUpdate.write(respose.text if respose.text.find("bill_merchant_desc") else "")
    country = json.loads(respose.text[respose.text.find("{"):])
    provinceList = country['province']
    provinces = []
    citys = []
    # for i in range (5000,5020):

    dict = {
        # "01021" : "医保缴费",
        # "60005" : "社保医保",
        # "60002" : "医院挂号",
        # "03002" : "保险续费",
        # "60008" : "健康管家",
        # "60004" : "体检预约",
        # "60010" : "药品回溯",
        # "01020" : "医院预缴金业务",
        # "07001" : "代收保险",
        # "03001" : "买保险",
        # "05007" : "工商管理费",
        # "05009" : "国税地税",
        # "05012" : "法院案款",
        "70004" : "印花税",
        "08007" : "养老院服务费",
        "08009" : "财务咨询费",
        "08002"  :"快递查询",
        "80011" : "善款",
        "80019" : "押金",
        "80006" : "租金",
        "08008" : "民盟费"
    }



    for key ,value in dict.items():
        loginFileUpdate = open("所有2/"+ value +".txt", "w", errors='ignore' , encoding="utf-8")  # 创建一个中间文件
        for pr in provinceList:
            provinces.append({pr['provinceid']:pr['name']})
            print(pr['provinceid'])
            if(pr['cities']==[]):
                head_index4(pr,{},key,loginFileUpdate)
                # head_index4(pr,{})
            for ct in pr['cities']:
                citys.append(ct)
                print(ct['cityid'])
                head_index4(pr,ct,key,loginFileUpdate)
                # head_index4(pr, ct)
        print(provinces)
        print(citys)
    loginFileUpdate.write(respose.text)

crawl()