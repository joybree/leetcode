class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        substring = []
        substring_tmp = []
        last_len  = 0
        for i in range(len(s)): 
            if s[i] not in substring:
                substring.append(s[i])
                #print(s[i])
                #print(substring)
                
            else:
                if len(substring) > last_len:
                    last_len = len(substring)
                #print(substring.index(s[i]))
                idx = substring.index(s[i])
                #substring_tmp.extend(substring[idx+1:]) 
                substring_tmp = substring[idx+1:]              
                del substring 
                substring.extend(substring_tmp)
                if i != len(s)-1:
                    substring.append(s[i])
                substring_tmp = []
                #print(s[i])
                #print(substring)
       
        return max(len(substring),last_len)

   

if __name__ == "__main__":
    s1 = Solution()
    print(s1.lengthOfLongestSubstring("pwwkew"))
    print(s1.lengthOfLongestSubstring('ohvhjdml'))

    
  