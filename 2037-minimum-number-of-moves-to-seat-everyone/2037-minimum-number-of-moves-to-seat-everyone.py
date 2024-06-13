class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        s=0
        for k in range(len(seats)):
            s+=abs(seats[k]-students[k])
        return s