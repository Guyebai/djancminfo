import urllib.parse
import urllib.request


"""
import coreapi
client = coreapi.Client()
action = ["api", "idcinfos > create"]
schema = client.get("http://127.0.0.1:8000/docs/")
params = {
    "idc_address": "北京互联国际",
    "idc_tag": "BJHL",
    "idc_leader": '王国荣',
    "idc_leader_phone": '18393323476',
    "idc_desc": '北京互联国际',
}
result = client.action(schema, action, params=params)
"""
tokenkey='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTM1NTYzNzA5LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.b1lMEBg1pGXNJFvpkwjaGXBPsaLzVM9DEwFi-gFeQjk'
def getHtml(url,values):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {'Authorization':"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTM1NTYzNzA5LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.b1lMEBg1pGXNJFvpkwjaGXBPsaLzVM9DEwFi-gFeQjk" }
    data = urllib.parse.urlencode(values)
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('utf-8')
    return html
def requestCnblogs(index):
    print('请求数据')
    url = 'http://localhost:8000/api/troubles/'
    """
    value= {
        "trouble_name": "主板故障",
        "trouble_influence": 1,
    }
    """
    result = getHtml(url,value)
    return result
url = 'http://localhost:8000/api/troubles/'
getHtml(url,"")
requestCnblogs()