import random 


accuracy=10
nums=set()

while round(sum(nums)*accuracy)!=accuracy or len(nums)!=100:
    rnd=random.uniform(-10,10)
    if(rnd not in nums):
        nums.add(rnd) 
        if(len(nums)==101):
            nums.pop()
    print("sum: {}, len: {}".format(sum(nums),len(nums)))

print("\n\nnumbers:",nums)