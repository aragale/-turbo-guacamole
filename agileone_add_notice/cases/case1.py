from agileone_add_notice.cases.base_function import BaseFunc

b = BaseFunc()
b.login()
b.add_notice("this is a test", "this is a test of adding notice")
b.check_msg()