from agileone_add_meeting.common.add_one_recode import InsertRecord


class Cases:
    def case1(self):
        InsertRecord("tom", "school", "module test", "class49", "this is a test")

    def case2(self):
        InsertRecord("jerry", "school", "", "class49", "this is a test")

    def case3(self):
        InsertRecord("tom", "school", "module test", "", "this is a test")

    def start_test(self):
        self.case1()
        self.case2()
        self.case3()


if __name__ == "__main__":
    Cases().start_test()
