def word_break(s, word_dict):
    """
    :type s: str
    :type word_dict: Set[str]
    :rtype: bool
    """
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(0, i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]