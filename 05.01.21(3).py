nums=[]
i=int(input())
res=0
while i!=0:
    nums.append(i)
    i=int(input())
for i in range(len(nums)):
    if nums[i]>nums[i-1]:
        res+=1
print(res)