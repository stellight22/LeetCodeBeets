"""second easy leetcode Question
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:

        #list comprehension to turn x into an iterable object of string
        int_to_str = [str(a) for a in str(x)]
        str_len = len(int_to_str)
        
        switch = True
        #starting positions depending on odd/even length
        if str_len % 2 == 1: #length is odd, middle is easy to find
            start = int((str_len-1)/2) #so we don't have decimal for index
            #you have to compare for start/left number of times
            #put into for loop
            left = start
            right = start
            while switch:
                #now the comparison of integers moving left and right
                left -= 1
                right += 1

                if left < 0: #it will go out of bounds when the number is a palindrome because it will keep moving
                    switch = True
                    break

                if int_to_str[left] != int_to_str[right]:
                    switch = False
            
              
        elif str_len % 2 == 0:
            #for even length, starting positions are different
            l_start = int(str_len/2)-1
            r_start = int(str_len/2)

            #comparison part
            if int_to_str[l_start] != int_to_str[r_start]:
                    switch = False
            #outer for loop to continue for lower middle number of times
            while switch:

                l_start -= 1
                r_start += 1

                if l_start < 0: #it will go out of bounds when the number is a palindrome because it will keep moving
                    switch = True
                    break

                if int_to_str[l_start] != int_to_str[r_start]:
                    switch = False
                     
            
        return switch


                   

s = Solution()
print(s.isPalindrome(343))
print(s.isPalindrome(34543))
print(s.isPalindrome(34549))
print(s.isPalindrome(312213))
print(s.isPalindrome(-734567))
print(s.isPalindrome(10))
print(s.isPalindrome(11))
print(s.isPalindrome(1))



