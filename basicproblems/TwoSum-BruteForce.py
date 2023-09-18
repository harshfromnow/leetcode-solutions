def twoSum(nums, target):
    l=[]
    for k in range(len(nums)):
        for j in range(len(nums)):
            if k!=j and nums[k]+nums[j]==target:
              l.append(k)
              l.append(j)
              return l
