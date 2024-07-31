class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-num for num in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            num1=heapq.heappop(heap)
            num2=heapq.heappop(heap)
            if num1!=num2:
                heapq.heappush(heap,num1-num2)
        if heap:
            return abs(heap[0])
        else:
            return 0
