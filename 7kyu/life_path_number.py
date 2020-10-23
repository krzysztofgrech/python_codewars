""" https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0/train/python """

def life_path_number(birthdate):
    tempArray = birthdate.split('-')
    
    life_number = 0
    date_part_number = 0

    for date_part in tempArray:
        for number in date_part:
            date_part_number += int(number)
            
        if date_part_number >= 10:
            date_part_number = sum(int(digit) for digit in str(date_part_number))

        life_number += date_part_number
        date_part_number = 0
        
    
    if life_number >= 10:
        life_number = sum(int(digit) for digit in str(life_number))

    if life_number == 10:
        life_number = 1;

    return life_number

print(life_path_number('1906-12-09'))