def lengthOfLongestSubstring(s):
    max_len = 0
    for i in range(len(s)):
        storage = set()
        count = 0
        for j in range(i, len(s)):
            if not s[j] in storage:
                storage.append(s[j])
                count += 1
            else:
                break
        max_len = max(max_len, count)
    return max_len

print(lengthOfLongestSubstring('abcabcbb'))