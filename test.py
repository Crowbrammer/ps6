import random

class myClassYay(object):
    def __init__(self):
        self.name = "Bob"
        print(self.getName())

    def getName(self):
        return self.name

myClassYay()

print(int(random.random() * 360))

test_dict = {"hello": "hi", "How are you?": "fine", "You doing well?":"yes."}
print(len(test_dict.values()))
print([x for x in test_dict.values()])
