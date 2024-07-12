class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substrings(s, sub, score):
            stack = []
            local_score = 0
            for char in s:
                if stack and stack[-1] + char == sub:
                    stack.pop()
                    local_score += score
                else:
                    stack.append(char)
            return ''.join(stack), local_score
        if x > y:
            s, score_ab = remove_substrings(s, "ab", x)
            s, score_ba = remove_substrings(s, "ba", y)
        else:
            s, score_ba = remove_substrings(s, "ba", y)
            s, score_ab = remove_substrings(s, "ab", x)
        return score_ab + score_ba