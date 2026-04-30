class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1Map = {}

        for i in s1:
            count1Map[i] = count1Map.get(i,0) + 1
        
        count2Map = {}
        
        left = 0
        right = 0

        matches = 0

        while left <= right and right < len(s2):
            element = s2[right]
            count2Map[element] = count2Map.get(element,0) + 1
            if element in count1Map.keys():
                if count1Map[element] == count2Map[element]:
                    matches+=1
                elif count1Map[element] + 1 == count2Map[element]:
                    matches -= 1
            

            while right - left + 1 > len(s1):
                if s2[left] in count1Map.keys():
                    if count1Map[s2[left]] == count2Map[s2[left]]:
                        matches -= 1
                    elif count1Map[s2[left]] + 1 == count2Map[s2[left]]:
                        matches +=1

                count2Map[s2[left]] -= 1
                
                left += 1

            if matches == len(count1Map):
                return True
            
            right += 1
    
        return False