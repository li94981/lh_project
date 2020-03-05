import random

class Code:
    def __init__(self):
        self.num=['1','2','3','4','5','6','7','8','9','0']

    def get_code(self):
        n=random.sample(self.num,6)
        return ''.join(n)





# if __name__ == '__main__':
    # code=Code()
    # print(code.get_code())












