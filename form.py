from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class DataForm(Form):
    address = StringField("接口地址",validators=[Required()])
    agent_id = StringField("方案商ID",validators=[Required()])
    agent_key = StringField("方案商秘钥",validators=[Required()])
    user_name = StringField("测试账号",validators=[Required()])
    order_num = StringField("外部6-30位数字充值订单号",validators=[Required()])
    submit = SubmitField("submit")