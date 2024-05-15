class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result=[]
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in groups:
                groups[size] = []
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []
        return result