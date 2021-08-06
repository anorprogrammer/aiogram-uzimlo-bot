from uzwords import words
from transliterate import to_latin, to_cyrillic
from difflib import get_close_matches

def checkWord(word, words=words):
    word = word.lower()
    if word.isascii():
        cyr_alph = to_cyrillic(word)
        matches = set(get_close_matches(cyr_alph, words, n=5))
        available = False  # bunday so'z mavjud emas

        if cyr_alph in matches:
            available = True  # mavjud
            matches = cyr_alph
        elif 'ҳ' in cyr_alph:
            cyr_alph = cyr_alph.replace('ҳ', 'х')
            matches.update(get_close_matches(cyr_alph, words, n=5))
        elif 'х' in cyr_alph:
            cyr_alph = cyr_alph.replace('х', 'ҳ')
            matches.update(get_close_matches(cyr_alph, words, n=5))
        matches=map(lambda w: to_latin(w),matches)
        return {'available': available, 'matches': matches}
    else:
        matches = set(get_close_matches(word, words, n=5))
        available = False  # bunday so'z mavjud emas

        if word in matches:
            available = True  # mavjud
            matches = word
        elif 'ҳ' in word:
            word = word.replace('ҳ', 'х')
            matches.update(get_close_matches(word, words, n=5))
        elif 'х' in word:
            word = word.replace('х', 'ҳ')
            matches.update(get_close_matches(word, words, n=5))

        return {'available': available, 'matches': matches}
