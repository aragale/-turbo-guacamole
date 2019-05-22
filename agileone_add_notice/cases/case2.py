from agileone_add_notice.cases.base_function import BaseFunc

c = BaseFunc()
c.login()
c.add_notice(" ", "this is a test of adding notice")
c.check_msg()