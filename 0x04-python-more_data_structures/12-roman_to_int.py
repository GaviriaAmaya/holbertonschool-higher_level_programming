#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    aux = 0
    plus = 0
for i in roman_string:
    if roman.get(i) <= aux:
        plus = plus + roman.get(i)
    else:
        plus = plus + (roman.get(i) - (2 * aux))
    aux = roman.get(i)
