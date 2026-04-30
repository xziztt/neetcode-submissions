class Solution:
    def check_anagrams(self, str1: str, str2:str):
        str1_lower = str1.lower()
        str2_lower = str2.lower()

        sorted_str1 = sorted(str1_lower)
        sorted_str2 = sorted(str2_lower)
        return sorted_str1 == sorted_str2
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found_anagram = {}
        anagrams_final_list = []
        for i in range (0,len(strs)):
            if strs[i] in found_anagram.keys():
                continue
            anagrams_list = [strs[i]]
            found_anagram[strs[i]] = True
            for j in range(i+1,len(strs)):
                if self.check_anagrams(strs[i],strs[j]):
                    found_anagram[strs[j]] = True
                    anagrams_list.append(strs[j])
            anagrams_final_list.append(anagrams_list)
        
        return anagrams_final_list

