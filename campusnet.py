# coding=gb18030
import requests
import os


def CampusNetLogin():
    try:
        url = "http://172.30.16.34/include/auth_action.php"
        FormData = {"action": "login", "username": "313170", "password": "{B}ZmNzMTMxNDUyMA==", "ac_id": "88",
                    "user_ip": "10.128.174.47", "nas_ip": "", "user_mac": "00:42:38:aa:fa:78", "save_me": "1",
                    "ajax": "1"}
        dic = {'user-agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post(url, data=FormData, headers=dic)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        res = r.text[:8]
        #         print(res)
        if res == "login_ok":
            print("��¼�ɹ�")
            os.system("pause")
        else:
            print("���ڲ�ȷ�����أ����������д˳���")
            os.system("pause")
    except:
        print("��½ʧ��")
        os.system("pause")


CampusNetLogin()
