class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f'이름:{self.name}, 점수:{self.score}')