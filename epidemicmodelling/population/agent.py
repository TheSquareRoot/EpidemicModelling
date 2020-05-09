class Agent:
    def __init__(self,age,sex,position,state):
        self.age = age
        self.sex = sex
        self.prevposition = position
        self.position = position
        self.state = state

    def display(self):
        print(f"age = {self.age}")
        print(f"sex = {self.sex}")
        print(f"previous position = {self.prevposition}")
        print(f"current position = {self.position}")
        print(f"state = {self.state}")
        print("-----------------------------------------")
