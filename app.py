import random

syllables = [
    'cha',
    'chu',
    'cho'
    'ka',
    'ku',
    'ko',
    'ta',
    'te',
    'to',
    'ba',
    'bu',
    'be',
    'bo',
    'sha',
    'shu',
    'she',
    'sho',
    'fa',
    'fu',
    'fo',
]

verb_suffixes = ['kher', 'khur', 'khar']
noun_suffixes = ['khen', 'khun']
adjective_suffixes = ['khab', 'kheb']
adverb_suffixes = ['kho', 'khi']

prepositions = ['ach', 'osh', 'tat']
pronoun = 'luch'


def make_root(number_of_syllables=3):
    if number_of_syllables is None:
        number_of_syllables = random.randint(1, 3)
    generator = (random.choice(syllables) for _ in range(number_of_syllables))
    return ''.join(generator)


def choose_suffix(root, suffixes):
    s = sum(ord(c) for c in root)
    return suffixes[s % len(suffixes)]


def make_verb(number_of_syllables_in_root=None):
    root = make_root(number_of_syllables_in_root)
    return root + choose_suffix(root, verb_suffixes)


def make_noun(number_of_syllables_in_root=None):
    root = make_root(number_of_syllables_in_root)
    return root + choose_suffix(root, noun_suffixes)


def make_adjective(number_of_syllables_in_root=None):
    root = make_root(number_of_syllables_in_root)
    return root + choose_suffix(root, adjective_suffixes)


def make_adverb(number_of_syllables_in_root=None):
    root = make_root(number_of_syllables_in_root)
    return root + choose_suffix(root, adverb_suffixes)


def make_sentence_v1():
    sentence = ' '.join((make_adjective(random.randint(1, 3)),
                         make_noun(random.randint(1, 3)),
                         make_adverb(random.randint(1, 3)),
                         make_verb(random.randint(1, 3))))
    return sentence.capitalize() + '.'


if __name__ == '__main__':
    for _ in range(5):
        print(make_sentence_v1())
