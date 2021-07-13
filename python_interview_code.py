
def is_anagram(word1, word2):
    sorted_word1 = "".join(sorted(word1))
    sorted_word2 = "".join(sorted(word2))
    return sorted_word1 == sorted_word2

assert is_anagram("adam", "peter")  == False
assert is_anagram("sport", "ports")  == True
assert is_anagram("taco", "octa")  == True
assert is_anagram("tacotaco", "taco")  == False
assert is_anagram("tacoslide", "taco")  == False
assert is_anagram("taco", "tacotaco") == False

def vowels(words):
    final_vowels = ""
    vowels = "aeiou"

    word = "".join(words)
    final_vowels = [char for char in word if char in vowels]

    return "".join(final_vowels)

assert vowels(["dog", "cat ", "car"]) == "oaa"
assert vowels(["foo", "bar"]) == "ooa"
assert vowels(["percy", "maria"]) == "eaia"


def add(*args):
    if len(args) >= 2:
        return sum(args)
    
    return lambda x: x + args[0]

assert add(1, 2) == 3
assert add(1)(2) == 3