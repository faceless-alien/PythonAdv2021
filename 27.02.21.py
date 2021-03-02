class BigInt():
    def __init__(self,init):
        self.init=init
    def sum(self,target):
        first_int=[int(i) for i in self.init]
        second_int=[int(i) for i in target.init]
        first_int.reverse()
        second_int.reverse()
        res=[0]*len(second_int)
        for i in range(len(first_int)):
            if first_int[i]+second_int[i]<10:
                res[i]+=first_int[i]+second_int[i]
            else:
                res[i]+=(first_int[i]+second_int[i])%10
                try:
                    res[i+1]+=(first_int[i]+second_int[i])//10
                except IndexError:
                    res.append((first_int[i]+second_int[i])//10)
        res.reverse()
        str_res=''
        for i in res: str_res+=str(i)
        return str_res
    def tax(self):
        first_int=[i for i in self.init]
        b=len(first_int)
        if first_int[b-2:b]==['0', '0']:
            res=''
            for i in first_int[:b-2]: res+=i
            return res
        else: 
            res=''
            for i in first_int[:b-3]:res+=i
            res+=first_int[-2]
            return res
i=BigInt(input())
print(i.tax())