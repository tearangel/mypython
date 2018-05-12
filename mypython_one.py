class A():
    def __init__(self , name):
        self._name = name

    def  __gt__(self, other):
        print("{0}比{1}大吗？".format(self._name,other._name))
        return self._name  > other._name
a = A("one")
b = A("two")
print(a > b)
print(a<b)