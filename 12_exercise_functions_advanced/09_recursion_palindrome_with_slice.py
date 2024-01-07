def is_palindrome(word):
    if len(word) <= 1:
        return True

    if word[0] != word[- 1]:
        return False

    return is_palindrome(word[1:-1])


def palindrome(word, idx):
    if is_palindrome(word):
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abracba", 0))
