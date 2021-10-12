#TwoSum

#Approach
'''
This is a brute force method to go through the entire list of integers from 
beginning to the end 
x starts at the beginning and y is the number that is one after
the inner loop y will run for every value in first iteration
y is always after x, so there is no need to go back to a value once x moves
-because we have already compared every possible combination with the value
'''
#Time complexity
''' n^2 because of nested for loop
10 % faster than other solutions
'''
#space complexity
'''
'''
#Mistakes Made
'''
'''
#code

from typing import List

class Solution:

    def twoSum(self,nums: List[int], target: int) -> List[int]:
        n_list = []
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] + nums[y] == target:
                    n_list.append(x)
                    n_list.append(y)
                    return n_list

listy = Solution()
print(listy.twoSum([0,1,2], 3))
