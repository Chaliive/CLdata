from urllib import request
import json

access_token = "c3e9164af36224199a7c5f34f58453c615f094bd1368c96cfead3b1b4e6dff4f"  # 钉钉机器人


def send_msg(item_name):
    """
     钉钉机器人API接口地址:
     https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1
     :param itemName:
     :return:
    """
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + access_token

    data = {
        "msgtype": "text",
        "text": {
            "content": item_name
        },
         "at": {
             "atMobiles": [
                 ""
             ],
             "isAtAll": False
         }
    }
    # 设置编码格式
    json_data = json.dumps(data).encode(encoding='utf-8')
    header_encoding = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
    try:
        req = request.Request(url=url, data=json_data, headers=header_encoding)
        request.urlopen(req)
        return True
    except Exception as e:
        print(e)
        return False
