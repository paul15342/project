##Flask + requests 实现一个小的web界面功能
#####需求：通过接口生成用户token。 此产品是提供给第三方的业务，在测试时获取用户token需要3步，为了缩减操作步骤开发此功能。提交所需数据后,可直接返回token。

1. 使用python的web框架Flask。 前端传递过来的参数保存在数据库中,在api的请求中从数据库获取对应的数据。
2. requests包通过3步获取用户token,所需参数从数据库中获取。

