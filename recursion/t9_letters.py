number_letters = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi',
                  '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                  '9': 'wxyz', '0': ' '}


def t9_letters(numbers, all_combos=None):
    if all_combos is None:
        all_combos = ['']
    if len(numbers) == 0:
        return all_combos
    new_combos = []
    for perm in all_combos:
        for letter in number_letters[numbers[0]]:
            new_combos.append(perm + letter)
    return t9_letters(numbers[1:], new_combos)


def test_t9_letters():
    # test on empty input
    empty_inp = t9_letters('')
    assert empty_inp == ['']
    # test on one number
    three = ['d', 'e', 'f']
    assert t9_letters('3') == three
    # test on two numbers
    seven_eight = ['pt', 'pu', 'pv', 'qt', 'qu',
                   'qv', 'rt', 'ru', 'rv', 'st', 'su', 'sv']
    assert t9_letters('78') == seven_eight
    # test on three number input
    two_five_six = ['ajm', 'ajn', 'ajo', 'akm', 'akn', 'ako', 'alm', 'aln',
                    'alo', 'bjm', 'bjn', 'bjo', 'bkm', 'bkn', 'bko', 'blm',
                    'bln', 'blo', 'cjm', 'cjn', 'cjo', 'ckm', 'ckn', 'cko',
                    'clm', 'cln', 'clo']
    assert t9_letters('256') == two_five_six
    # test with space (0)
    six_zero_nine = ['m w', 'm x', 'm y', 'm z', 'n w',
                     'n x', 'n y', 'n z', 'o w', 'o x', 'o y', 'o z']
    assert t9_letters('609') == six_zero_nine


if __name__ == '__main__':
    test_t9_letters()
