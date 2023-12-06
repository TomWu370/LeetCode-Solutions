class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        negInf = -math.inf
        first = negInf
        second = negInf
        third = negInf

        for i in nums:
            if i == first or i == second or i == third:
                continue
            elif i > first:
                third = second
                second = first
                first = i
            elif i > second:
                third = second
                second = i
            elif i > third:
                third = i
        return third if third > negInf else first
        