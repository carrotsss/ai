import requests
from lxml import etree
import re
from handle_mongo import handle_get_task

def handle_douyin_we_share(task_id):
    share_web_url = 'http://v.douyin.com/%s'%task_id['share_id']
    share_web_header = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    share_web_response = requests.get(share_web_url,share_web_header)
    handle_decode(share_web_response)

def handle_decode(input_data):
    search_douyin_str = re.compile("抖音：")
    # regex_list = [{}]
    # for i1 in regex_list:
    #     for i2 in i1['name']:
    #         input_data = re.sub(i2,str(i1['value']),input_data)


    share_web_html = etree.HTML(input_data)
    print(input_data)
    user_info = {}
    user_info['nickname'] = share_web_html.xpath("//p[@class='nickname']/text()")[0]
    douyin_id1 = share_web_html.xpath("//p[@class='shatid']/text()")[0].replace(" ","")
    douyin_id2 = "".join(share_web_html.xpath("//p[@class='shatid']/i/text()")[0])
    user_info['user_id'] = re.sub(search_douyin_str,"",douyin_id1 + douyin_id2)
    user_info['job'] = share_web_html.xpath("//span[@class='info']/text()")[0].replace(" ", "")
    user_info['location'] = share_web_html.xpath("//p[@class=extra-info']/span[1]/text()")[0]
    user_info['xingzuo'] = share_web_html.xpath("//p[@class=extra-info']/span[2]/text()")[0]
    danwei = share_web_html.xpath("//p[@class='follow-info']/span[2]/span[@class='num]/text()")[0]
    print(user_info)

while True:
    task = handle_get_task()
    handle_douyin_we_share(task)
