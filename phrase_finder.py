from itertools import combinations, permutations
import hashlib

ANAGRAM = "poultry outwit sants"
ANAGRAM_LENGTH = len(ANAGRAM)
SORTED_ANAGRAM = "".join(sorted(ANAGRAM)).replace(" ", "")

MD5_HASHES = [
    "e4820b45d2277f3844eac66c903e84be",
    "23170acc097c24edb98fc5488ab033fe",
    "665e5bcb0c20062fe8abaaf4628bb154",
]

ANAGRAM_CHARACTER_MAP = {}
for char in ANAGRAM.replace(" ", ""):
    if char not in ANAGRAM_CHARACTER_MAP:
        ANAGRAM_CHARACTER_MAP[char] = 1
    else:
        ANAGRAM_CHARACTER_MAP[char] += 1


def is_word_in_anagram(word):
    """
    Checks if each character of a word can be part of the anagram.
    The following words are discarded:
     - words containing characters not present in the anagram
     - words where character x exceeds the total count of character x in the anagram
    """
    for character in word:
        anagram_character_count = ANAGRAM_CHARACTER_MAP.get(character)
        if anagram_character_count \
                and word.count(character) <= anagram_character_count:
            continue
        else:
            return False
    return True


def construct_phrase_string(combination):
    """
    Returns a phrase string based on a tuple of words,
    e.g. (cosmic, helmet, perk) -> 'cosmichelmetperk'
    """
    phrase = ""
    for word in combination:
        phrase += word
    return phrase


def construct_phrase_with_spaces(permutation):
    """
    Returns a full sentence based on a tuple of words,
    e.g. (cosmic, helmet, perk) -> 'cosmic helmet perk'.
    """
    phrase = ""
    for word in permutation:
        phrase += word + " "
    return phrase.rstrip(" ")


def filter_combinations(combination):
    """
    Discard target phrases that cannot be the anagram.
    A phrase is a potential anagram candidate if all characters match.
    """
    phrase_string = construct_phrase_string(combination)
    sorted_phrase = "".join(sorted(phrase_string))
    if sorted_phrase == SORTED_ANAGRAM:
        return True
    return False


def hash_phrase(phrase):
    """
    Returns the MD5 hash of a phrase.
    """
    return hashlib.md5(phrase.encode()).hexdigest()


def find_secret_phrases(filtered_words):
    """
    Finds combinations of words, starting with 3 word combinations.
    Computes permutations for each combination.
    MD5 hash of permuted phrase is then compared with the hash of the secret phrase.
    """
    no_of_words = 3
    found_phrases = []

    while len(found_phrases) < 3:
        print("Creating {}-word combinations".format(no_of_words))
        word_combinations = combinations(filtered_words, no_of_words)

        print("Filtering combinations")
        filtered_combinations = filter(filter_combinations, word_combinations)

        print("Creating permutations for each word combination")
        for combination in filtered_combinations:
            permutations_per_combination = permutations(combination, no_of_words)
            for permutation in permutations_per_combination:
                phrase = construct_phrase_with_spaces(permutation)
                phrase_hash = hash_phrase(phrase)
                if phrase_hash in MD5_HASHES:
                    found_phrases.append(phrase)
                    print("Found secret phrase:", phrase)
                    if len(found_phrases) == 3:  # 3rd match has been found so no need to search further
                        break
                else:
                    continue
        no_of_words += 1
    return found_phrases


if __name__ == "__main__":
    print("Reading file")
    words = []
    with open("wordlist") as f:
        lines = f.readlines()
        for line in lines:
            words.append(line.rstrip("\n"))

    unique_words = sorted(set(words))

    print("Filtering words")
    filtered_words = list(filter(is_word_in_anagram, unique_words))

    secret_phrases = find_secret_phrases(filtered_words)

    print("Complete. Identified all secret phrases:", secret_phrases)
