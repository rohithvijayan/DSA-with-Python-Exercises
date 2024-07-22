class Hashmap:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX

    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    def __settitem__(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value
ht=Hashmap()


ht["day5"]=105