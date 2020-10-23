""" https://www.codewars.com/kata/546f922b54af40e1e90001da """

def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz';

    sub_test = text.lower().replace(' ', '').replace('.', '').replace(',', '').replace('-', '').replace("'", '')
    output = ''

    for i in range(0, len(sub_test)):
        j = alphabet.index(sub_test[i]) + 1
        output += str(j) + ' '

    return output.strip()


print(alphabet_position("Hi, what's up"))