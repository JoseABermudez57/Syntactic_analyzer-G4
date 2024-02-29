
grammar_v4 = {
    ('S', 'automata'): ['A', 'B', 'V'],
    ('A', 'automata'): ['automata'],
    ('V', 'fin'): ['fin'],
    ('B', 'alfabeto'): ['AL', 'F'],
    ('AL', 'alfabeto'): ['G', ':', 'SM', 'RA', ';'],
    ('G', 'alfabeto'): ['alfabeto'],
    ('G', ':'): ['ε'],
    ('SM', 'alpha'): ['alpha'],
    ('SM', 'digit'): ['digit'],
    ('RA', ','): [',', 'SM', 'RA'],
    ('RA', ';'): ['ε'],
    ('F', 'aceptacion'): ['C', ':', 'D', ';'],
    ('C', 'aceptacion'): ['aceptacion'],
    ('D', 'digit'): ['digit']
}

terminals = set([key[1] for key in grammar_v4.keys()])
reserved_words = ['automata', 'alfabeto', 'aceptacion', 'fin']


def organizer(words):
    symbols = []
    for word in words:
        if word in reserved_words:
            symbols.append(word)
        else:
            for letter in word:
                if letter.isalpha():
                    symbols.append('alpha')
                elif letter.isdigit():
                    symbols.append('digit')
                else:
                    symbols.append(letter)
    return symbols


def syntax_analyzer(input_text):
    stack = ['$', 'S']
    text = str(stack) + '\n'
    input_text = input_text.strip() + ' $'
    words = input_text.split(' ')
    symbols = organizer(words)
    index = 0
    while True:
        x = stack.pop()
        a = symbols[index]
        if x in terminals:  # <- Terminals
            if x == a:
                index += 1
                text += str(stack) + '\n'
            else:
                return text + '\nEntrada invalida!', False
        else:  # <- Non-terminals
            if x == '$':
                return text + '\nEntrada valida!', True
            if (x, a) in grammar_v4:
                productions = grammar_v4[(x, a)]
                if productions != ['ε']:
                    for production in reversed(productions):
                        stack.append(production)
                text += str(stack) + '\n'
            else:
                return text + '\nEntrada invalida!', False
