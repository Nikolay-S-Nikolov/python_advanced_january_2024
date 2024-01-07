def palindrome(word, idx):

    if word[idx] != word[-idx - 1]:
        return f"{word} is not a palindrome"

    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    return palindrome(word, idx + 1)


print(palindrome("abba", 0))
