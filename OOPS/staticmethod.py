class abc:
    def __init__(self):
        pass
    @staticmethod
    def sayhello(name):
        print("hello",name)
# abc.sayhello("john")
b1=abc()
print(b1.sayhello("kopal"))

