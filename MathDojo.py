class MathDojoListsTuples(object):
    def __init__(self):
        self.num = 0
    def add(self, *addnum):
        for i in addnum:
            if type(i) == list or type(i) == tuple:
                self.num += sum(i)
            else:
                self.num += i
        return self
    def subtract(self, *subnum):
        for i in subnum:
            if type(i) == list or type(i) == tuple:
                self.num -= sum(i)
            else:
                self.num -= i
        return self
    '''def result(self):
        print self.num
        return self.num'''
md3 = MathDojoListsTuples()
print md3.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract((2,3,4), [2,3], [1.1, 2.3]).num

# class MathDojo(object):
#     def __init__(self):
#         self.result = 0
#     def add(self,*args):
#         #self += everything in parameters together
#         # if type(arg1) == int or type(arg1) == float:
#         #     self.result += arg1
#         # elif type[arg1]
#         self.result += sum(args)
#         return self
#     def subtract(self,*args):
#         #self -= everything in paras
#         self.result -= sum(args)
#         return self
#     def sumEverything(self, *test):
#         print type(test)
#         while type(test) is tuple or type(test) is list:
#             if type(test[0]) is tuple or type(test[0]) is list:
#                 test = list(map(sum,test))
#             else:
#                 for i in test:
#                     self.result += i
#                 test = self.result
#         # print test
#         # self.result += test
#         return self

# print MathDojo().add(2).add(2, 5).subtract(3, 2).result

# print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
# print MathDojo().sumEverything([(1, 2), (1, 3), (2, 3)]).result