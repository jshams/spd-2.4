def recursive_fizz_buzz(start, end):
    if start > end:
        return []
    if start % 15 == 0:
        result = ['FizzBuzz']
    elif start % 3 == 0:
        result = ['Fizz']
    elif start % 5 == 0:
        result = ['Buzz']
    else:
        result = [start]
    return result + recursive_fizz_buzz(start + 1, end)


def test_fizz_buzz():
    results = recursive_fizz_buzz(1, 20)
    assert results == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7,
                       8, 'Fizz', 'Buzz', 11, 'Fizz', 13,
                       14, 'FizzBuzz', 16, 17, 'Fizz', 19,
                       'Buzz']
    print('Fizz Buzz passes current tests')


test_fizz_buzz()
