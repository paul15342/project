from models import  Info,db
from flask import render_template,request,redirect,url_for
from __init__ import create_app
from form import DataForm
from api.token import info
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
		info = Info(address=form.address.data,agent_id=form.agent_id.data,agent_key = form.agent_key.data,
					user_name=form.user_name.data,order_num =form.order_num.data)
		db.session.add(info)
		try:
			db.session.commit()
		except:
			db.session.rollback()
		return redirect(url_for("post"))
	return render_template("form.html", form=form)



@app.route("/loginToken/",methods=["GET","POST"])
def post():
	logintoken = info().post()
	return render_template("loginToken.html",token=logintoken,title=u"登录token")


if __name__ == "__main__":
	app.run()
