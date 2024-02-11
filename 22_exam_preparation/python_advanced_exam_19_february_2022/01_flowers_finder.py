from collections import deque

words = ["rose", "tulip", "lotus", "daffodil"]

vowels = deque(input().split())
consonants = input().split()

letters_found = []
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for word in words:
        if vowel in word:
            letters_found.append(vowel)
        if consonant in word:
            letters_found.append(consonant)

    for word in words:
        if {x for x in tuple(word)}.issubset(tuple(letters_found)):
            print(f"Word found: {word}")
            if vowels:
                print(f"Vowels left: {' '.join(x for x in vowels)}")
            if consonants:
                print(f"Consonants left: {' '.join(x for x in consonants)}")

            raise SystemExit

print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(x for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(x for x in consonants)}")
