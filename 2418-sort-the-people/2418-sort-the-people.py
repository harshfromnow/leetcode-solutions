class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #tuple creation
        name_height_pairs = list(zip(names, heights))

        name_height_pairs.sort(key=lambda x: x[1], reverse=True)

        sorted_names = [name for name, height in name_height_pairs]

        return sorted_names