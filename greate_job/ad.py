# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
import json
import urllib.request

zbx_url = "http://192.168.73.140/zabbix/api_jsonrpc.php"
zabbix_user = "Admin"
zabbix_pwd = "zabbix"


def get_token(zbx_url_par, zabbix_user_par, zabbix_pwd_par):  # 得到token值，这是一个令牌，用以获取其他API
    url = zbx_url_par
    header = {"Content-Type": "application/json"}
    data = '''{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "%s",
        "password": "%s"},
    "id": 0
        }''' % (zabbix_user_par, zabbix_pwd_par)
    request = urllib.request.Request(url, data.encode())
    for key in header:
        request.add_header(key, header[key])
    try:
        result = urllib.request.urlopen(request)
    except urllib.request.URLError as e:
        print('error!!', e)
    else:
        response = json.loads(result.read())
        result.close()
        # print('ads')
        return response['result']


def zbx_req(zbx_action_par, zbx_params_par):
# def zbx_req():
    header = {"Content-Type": "application/json"}
    url = zbx_url
    # print(zbx_action_par, zbx_params_par)
    zbx_token_par = get_token(zbx_url, zabbix_user, zabbix_pwd)
    data = '''{"jsonrpc": "2.0", "method": "%s", "params": %s,"auth": "%s","id": 1 }''' % (zbx_action_par, zbx_params_par, zbx_token_par)
    # data = '''{"jsonrpc": "2.0", "method": "host.get", "params": {"output":"extend","actionids":"3"},"auth": "%s","id": 1 }''' % zbx_token_par

    request = urllib.request.Request(url, data.encode())
    for key in header:
        request.add_header(key, header[key])
    try:
        result = urllib.request.urlopen(request)
    except urllib.request.URLError as e:
        print('error', e)
    else:
        response = json.loads(result.read())
        if 'error' in response:
            print(response['error'])
            return False
        elif not response['result']:
            print(response)
            return False
        else:
            # rst = response['result']
            # ss = {}
            # for i in range(len(rst)):
            #     for key, value in rst[i].items():
            #         ss[key] = value
            # return ss
            return response['result']
        result.close()


par = '{"output": "extend","actionids":"3"}'
action = "host.get"
# result = zbx_req(action, par)
# result = zbx_req()
# print(result)
# for i in result:
#     print(i)
#     for key, value in result[i].items():
#         print(key, value)



