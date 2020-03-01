

def search_for_vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    # 返回词组中的元音
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """
    return  a set of the 'letters' found in 'phrase'.
    :param phrase:
    :param letters:
    :return:
    """
    return set(letters).intersection(set(phrase))
