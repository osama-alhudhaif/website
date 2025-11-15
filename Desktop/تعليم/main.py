class test:

    def __init__(self):
        
        # self.name = "osama"
        # self.age = 24
        # self.job = "programmer"

        test = "ali", 25, "teacher" # type: ignore

    def print_info(self):
        # print(self.name)
        # print(self.age)
        # print(self.job)

        print(test)

obj = test()
obj.print_info()

