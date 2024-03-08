def longestPalindromeSubseq(s: str) -> int:
    """Finds the length of the longest palindromic subsequence in a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence in the string.
    """

    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the dp table in a bottom-up manner
    for length in range(2, n + 1):  # Iterate over possible subsequence lengths
        for i in range(n - length + 1):
            j = i + length - 1  # Calculate the ending index 'j' of the subsequence

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

# Example usage
s = "cbbabc"
print("Length of the longest palindromic subsequence:", longestPalindromeSubseq(s))
