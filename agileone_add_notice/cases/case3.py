from agileone_add_notice.cases.base_function import BaseFunc

d = BaseFunc()
d.login()
d.add_notice("this is a test", " ")
d.check_msg()
