class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [sorted(cuboid) for cuboid in cuboids]
        cuboids.sort()
        heights = {tuple(box): box[2] for box in cuboids}
        for i in range(1, len(cuboids)):
            box = tuple(cuboids[i])
            S = [tuple(cuboids[j]) for j in range(i) if self.canbestacked(cuboids[j], cuboids[i])]
            heights[box] = cuboids[i][2] + max([heights[b] for b in S], default=0)
        return max(heights.values(), default=0)

    def canbestacked(self, top, bottom):
        return top[0] <= bottom[0] and top[1] <= bottom[1] and top[2] <= bottom[2]