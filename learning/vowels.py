def count_vowels(word):
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiouаеёиоуыэюя':
            total_vowels += 1
    return total_vowels