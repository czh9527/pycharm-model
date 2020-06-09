import requests
import json
def get_comments(url):
    name_id = url.split('=')[1]
    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
    'Safari/537.36 Edg/83.0.478.37','referer'
    :'https://music.163.com/#/song?id=516728102'}
    params ='ckcm5NvDLWeL4UJp+NOKktccZLVMMvTSTCxA3FQjOD2xebXo2gYvefT91/MCduhVj6J0lPgbNSJVts7nI6Q6ke6gf5mP6kmQnrLBPRrQehK1FKrzvwp8q1OhMx7eVsI5c/kk6KlXudrn9VKq3AnRDYZfEnnzHWlBe4QzM0N3YwP7pVH6RT4tt8MU/HmOJxe2'
    encSecKey= 'c4c1dc23cee25ba52f9bc05d0ccf999ac4e20f2d7da797ec429d538bb1bf030d3dd82d624bd06ad51dad72ab81211c901fd26ab8890af3a342501f96aef50beea4e194272604a2c83efff869cf01ea196f08fe21326b8759d5ff37d04c0b38f5845d094ec2b63e70ca567e6c9a2888d902b148a349179d0106afd7b5f86c9f0a'
    data = {
        "params":params,
        "encSecKey":encSecKey
    }
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    res = requests.post(target_url,headers = headers,data= data)
    return res

def  get_hot_comments(res):
    comment_json = json.loads(res.text)
    hot_comments = comment_json['hotComments']
    with open("res.txt",'w',encoding="utf-8") as f:
        for each in hot_comments:
            f.write(each['user']['nickname']+':\n\n')
            f.write(each['content']+'\n')
            f.write('-------------------------------------\n')
def main():
    url = input("请输入链接地址")
    res = get_comments(url)
    get_hot_comments(res)

if __name__ == "__main__":
    main()