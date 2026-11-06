# 1 masala   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def majoritiy_el(lst:list):
    return max(set(lst), key=lst.count)


n = int(input("Nechta son kiritasiz? "))
nums=[]
for i in range(n):
    nums.append(int(input()))

print(majoritiy_el(nums))