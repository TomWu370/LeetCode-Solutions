class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort(reverse=True)
        answers = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                k = j+1
                l = len(nums)-1
   
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    #print(f'sum',sum,'k:',k,'l:',l)
                    # return [[0]]
                    if sum == target and [nums[i], nums[j], nums[k], nums[l]] not in answers:
                        quadruplet = [nums[i], nums[j], nums[k], nums[l]]
                        answers.append(quadruplet)
                        while k < l and nums[k] == quadruplet[2]:
                            k +=1
                        while k < l and nums[l] == quadruplet[3]:
                            l -= 1
                    elif sum > target:
                        k += 1
                    elif sum < target:
                        l -= 1
                    else:
                        break
              
        return answers





# on the basis of 3Sum add 1 more pointer