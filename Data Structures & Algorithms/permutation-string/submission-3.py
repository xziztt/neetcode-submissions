class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = 0
        left = 0

        matches = 0
        count1Map = {}
        count2Map = {}

        for i in s1:
            count1Map[i] = count1Map.get(i,0) + 1

        while left <= right and right < len(s2):

            count2Map[s2[right]] = count2Map.get(s2[right],0) + 1
            
            if s2[right] in count1Map.keys():
                if count2Map[s2[right]] == count1Map[s2[right]]:
                    matches +=1
                elif count2Map[s2[right]] == count1Map[s2[right]] + 1:
                    matches -= 1

            while right - left + 1 > len(s1):
                if s2[left] in count1Map.keys():
                    if count1Map[s2[left]] == count2Map[s2[left]]:
                        matches -= 1
                    elif count1Map[s2[left]] + 1 == count2Map[s2[left]]:
                        matches += 1

                count2Map[s2[left]] -= 1
                left += 1
            
            if len(count1Map) == matches:
                return True

            right += 1
        
        return False

