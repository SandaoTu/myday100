

def search_for_vowels(phrase: str) ->set:
    """
    Return any vowels found in a supplied phrase.
    this is test
    """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search_for_letters(phrase: str,letters: str='aeiou') ->set:
    """
    return a set of the 'letters' found in 'phrase'.
    """
    return set(phrase).intersection(set(letters))
