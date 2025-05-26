from collections import defaultdict


def groupAnagram(strs):
    res = defaultdict(list)  # Dictionary to hold groups of anagrams

    for s in strs:
        count = [0] * 26  # Count of each letter (a to z) in the string

        for c in s:
            count[ord(c) - ord("a")] += 1  # Map character to index (0-25) and increment

        res[tuple(count)].append(s)  # Use count as key to group anagrams

    return list(res.values())  # Return grouped anagrams as a list

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagram(strs))