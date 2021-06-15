def longest_substring_with_k_distinct_characters(s, k):
    current_longest_substring = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) > k:
                break
            if len(substring) > len(current_longest_substring):
                current_longest_substring = substring
    return len(current_longest_substring)

s = "aabbccdef"
k = 2

print(longest_substring_with_k_distinct_characters(s, k))