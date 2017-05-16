import sys

num_dict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
            6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
            11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
            15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
            19 : 'nineteen', 20 : 'twenty',
            30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
            70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}

def get_input(expression):
    if not expression:
        raise ValueError("Number must be non-empty")

    return eval(expression)

def turn_number_to_words(number, num_dict):

    if number in range(0, 20):
        return num_dict[number]

    if number in range(20, 100):
        decade = 10 * (number // 10)
        second_digit = number % 10

        return num_dict[decade] + ' ' + num_dict[second_digit] if second_digit != 0 \
            else num_dict[number]

    if number in range(100, 1000):
        hundreds = num_dict[number // 100] + ' hundred'
        rest = turn_number_to_words(number % 100, num_dict)
        return hundreds if number % 100 == 0 else hundreds + ' and ' + rest

    if number in range(1000, 1000000):
        thousands = turn_number_to_words(number // 1000, num_dict) + ' thousand '
        rest = turn_number_to_words(number % 1000, num_dict)
        return thousands if number % 1000 == 0  else thousands + rest

    if number in range(1000000, 1000000000):
        millions = turn_number_to_words(number // 1000000, num_dict) + ' milllion '
        rest = turn_number_to_words(number % 1000000, num_dict)

        return millions if number % 1000000 == 0 else millions + rest

    if number in range(1000000000, 1000000000000):

        billions = turn_number_to_words(number // 1000000000, num_dict) + ' billion '
        rest = turn_number_to_words(number % 1000000000, num_dict)

        return billions if number % 1000000 == 0 else billions + rest

    if number in range(1000000000000, 1000000000000000):

        trillions = turn_number_to_words(number // 1000000000000, num_dict) + ' trillion '
        rest = turn_number_to_words(number % 1000000000000, num_dict)

        return trillions if number % 1000000000000 == 0 else trillions + rest

    if number in range(1000000000000000, 1000000000000000000):
        quadrillions = turn_number_to_words(number // 1000000000000000, num_dict) + ' quadrillion '
        rest = turn_number_to_words(number % 1000000000000000, num_dict)
        return quadrillions if number % 1000000000000000 == 0 else quadrillions + rest

    else:
        return 'Number too large, sorry'


expression = ''.join(sys.argv[1:])
number = get_input(expression)
print (turn_number_to_words(number, num_dict))



#for function testing:
# test_numbers = [1, 15, 21, 30, 101, 9000, 89332, 789123, 267367867827637056]
# for i in test_numbers:
#     print (i, turn_number_to_words(i, num_dict))