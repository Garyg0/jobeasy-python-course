# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'My name is Gary Walker'

char_1 = 'a'
count = 0

index = 0
while index < len(string_1):
    if string_1[index] == char_1:
        count += 1
    index += 1

result_1 = count





# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 1264234
number_to_string = str(number_1)
mult = 1

index = 0
while index < len(number_to_string):
    mult *= int(number_to_string[index])
    index +=1

result_2 = mult


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 7131752354
number_to_string_2 = str(number_2)
result_3 = ''

index = len(number_to_string_2) - 1

while index >= 0:
    result_3 += number_to_string_2[index]
    index -= 1

result_3 = int(result_3)

