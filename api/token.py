from project import db
import requests,json,hashlib,base64


"""
获取登录token
"""
class info:
    def __init__(self):
        self.dict = {}
        auth_token ={}
        login_token = {}

    def get_info(self):
        sql = "select * from 'api_info' order by id desc"  #倒叙排序,取最新一次存入的数据
        address = db.session.execute(sql)
        info= address.fetchone()
        self.dict['host'] = info[1]
        self.dict['agent_id'] = info[2]
        self.dict['agent_key'] = info[3]
        self.dict['user_name'] = info[4]
        self.dict['order_num'] = info[5]
        return self.dict

    def get_auth_token(self):
        dict = self.get_info()
        auth_token = {
            'method': 'post',
            'url': dict["host"] + '/api/platform/auth',
            #'agentname': 'test01',
            'kv': {
                'agentID': '{}'.format(dict["agent_id"]),
                'secret_key': '{}'.format(dict['agent_key'])}
        },
        return auth_token

    def get_login_token(self):
        dict = self.get_info()
        login_token = {
            'method': 'post',
            'url':  dict["host"] + '/api/platform/login',
            'kv': {
                'token': '',
                'username': '{}'.format(dict["user_name"])}
        }
        return login_token


    def post(self):
        auth_token = self.get_auth_token()[0]
        login_token = self.get_login_token()
        r = requests.post(url=auth_token['url'], data=auth_token['kv'], timeout=5)
        text = json.loads(r.text)

        token = text['data']['token']
        m = hashlib.md5()
        id = bytes(auth_token['kv']['agentID'], "utf-8")
        m.update(id)
        mk = m.hexdigest()
        m1 = hashlib.md5()
        key = bytes(auth_token['kv']['secret_key'], "utf-8")
        m1.update(key)
        m2 = m1.hexdigest()
        a_param = "{}|{}|{}".format(mk, token, m2)
        b_a_param = bytes(a_param, "utf-8")
        agenttoken = base64.b64encode(b_a_param)
        login_token['kv']['token'] = agenttoken
        r = requests.post(url=login_token['url'], data=login_token['kv'], timeout=5)
        logintoken = json.loads(r.text)['data']['token']
        return logintoken