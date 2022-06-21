class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1

        while i < j:
            # print(i)
            # print(j)
            # print(s[i])
            # print(s[j])
            # print(s[i].lower())
            # print(s[j].lower())

            while i<j and s[i].isalnum() == False:
                i += 1
            while i<j and s[j].isalnum() == False:
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
