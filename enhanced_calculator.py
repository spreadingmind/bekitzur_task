import sys

num_dict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
            6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
            11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
            15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
            19 : 'nineteen', 20 : 'twenty',
            30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
            70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
order_dict = {1: '', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion', 1000000000000: 'trillion'}

test_numbers = [0, 12, 89, -187, -87600, 123554, 212334556, -78927512221, 100200300400587887800]


def get_input(expression):
    if not expression:
        raise ValueError("Number must be non-empty")
    return eval(expression)

def add_sign(main_function):
    def change_output(number, num_dict, order_dict):
        is_positive = number >= 0
        try:
            words = main_function(abs(number), num_dict, order_dict)
        except KeyError:
            return ('Number too large')
        sign = '' if is_positive else 'minus '
        return sign + words
    return change_output

@add_sign
def turn_positive_number_to_words(number, num_dict, order_dict):

    def small_number_to_words(number):

        if number in range(0, 20):
            return num_dict[number]

        if number in range(20, 100):
            decade = 10 * (number // 10)
            second_digit = number % 10
            return num_dict[decade] + ' ' + num_dict[second_digit] if second_digit != 0 \
                else num_dict[number]

        if number in range(100, 1000):
            hundreds = num_dict[number // 100] + ' hundred'
            rest = small_number_to_words(number % 100)
            return hundreds if number % 100 == 0 else hundreds + ' and ' + rest

    if number < 1000:
        return small_number_to_words(number)
    else:
        order = 1
        step = 1000
        word_representation = ''
        while number > 0:
            word_representation = small_number_to_words(number % step) + ' ' +\
                                  order_dict[order] + ' ' + word_representation
            number //= step
            order *= step
        return word_representation

def get_output(test_number):
    return turn_positive_number_to_words(test_number, num_dict, order_dict)

expression = ''.join(sys.argv[1:])
number = get_input(expression)
print (get_output(number))

# for i in test_numbers:
#     print (i, get_output(i))