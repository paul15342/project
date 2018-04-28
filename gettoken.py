from models import  Info,db
from flask import render_template,request,redirect,url_for
from __init__ import create_app
import requests,json,hashlib,base64
from form import DataForm
app = create_app()

@app.route("/",methods=['GET','POST'])
def home():
	form = DataForm()
	if request.method == "POST":

		#同过html获取表单数据
		# address = request.form.get("address")
		# agent_id = request.form.get("agent_id")
		# agent_key = request.form.get("agent_key")
		# user_name = request.form.get("user_name")
		# order_num = request.form.get("order_num")
		#info = Info(address=request.form.get("address"),agent_id=agent_id,agent_key=agent_key,user_name=user_name,
		#			order_num=order_num)
		info = Info(address=form.address.data,agent_id=form.address.data,agent_key = form.agent_key.data,
					user_name=form.user_name.data,order_num =form.order_num.data)
		db.session.add(info)
		db.session.commit()

			# db.session.rollback()
		return redirect(url_for("post"))
	return render_template("base.html",form = form)


dict = {}
auth_token ={}
login_token = {}

def get_info():
	sql = "select * from 'api_info' order by id desc"  #倒叙排序,取最新一次存入的数据
	address = db.session.execute(sql)
	info= address.fetchone()
	dict['host'] = info[1]
	dict['agent_id'] = info[2]
	dict['agent_key'] = info[3]
	dict['user_name'] = info[4]
	dict['order_num'] = info[5]
	print(dict["user_name"])
	return dict

def get_auth_token():
	dict = get_info()
	auth_token = {
		'method': 'post',
		'url': dict["host"] + '/api/platform/auth',
		#'agentname': 'test01',
		'kv': {
			'agentID': '{}'.format(dict["agent_id"]),
			'secret_key': '{}'.format(dict['agent_key'])}
	},
	return auth_token

def get_login_token():
	dict = get_info()
	login_token = {
		'method': 'post',
		'url':  dict["host"] + '/api/platform/login',
		'kv': {
			'token': '',
			'username': '{}'.format(dict["user_name"])}
	}
	return login_token

@app.route("/loginToken/",methods=["GET","POST"])
def post():
	get_info()
	# get_auth_token()
	# get_login_token()
	auth_token = get_auth_token()[0]
	login_token = get_login_token()

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
	return render_template("loginToken.html",token=logintoken)



if __name__ == "__main__":
	app.run()
