class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = []
        used = []

        for i in range(len(strs)):

            if strs[i] in used:
                continue

            group = [strs[i]]
            used.append(strs[i])

            t = ''.join(sorted(strs[i]))

            for j in range(i + 1, len(strs)):
                s = ''.join(sorted(strs[j]))

                if t == s:
                    group.append(strs[j])
                    used.append(strs[j])

            arr.append(group)

        return(arr)