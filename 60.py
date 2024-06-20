def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    # Table to store results of subproblems
    dp = [[False for x in range(n)] for y in range(n)]

    # All substrings of length 1 are palindromes
    start = 0
    max_length = 1
    for i in range(n):
        dp[i][i] = True

    # Check for sub-string of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length

    return s[start:start + max_length]

# Example usage
input_string = "babad"
print("Longest Palindromic Substring is:", longest_palindromic_substring(input_string))
