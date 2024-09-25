print('Choose a data type to perform operations on:')
print('1. Strings')
print('2. Numbers')
print('3. Booleans')
print('4. Additional Data Types (List, Tuple, Dictionary)')

choice = input('Enter the number of your choice (1-4): ')

if choice == '1':
    sentence_string = 'Learning Python is fun!'
    print(sentence_string[9:15])
    print(sentence_string.upper())
    print(sentence_string.replace('fun', 'awesome'))

elif choice == '2':
    try:
        input_number_one = float(input('Enter the first number: '))
        input_number_two = float(input('Enter the second number: '))
    except ValueError:
        print('Invalid Input. Try again...')

    addition_result = input_number_one + input_number_two
    subtraction_result = input_number_one - input_number_two
    multiplication_result = input_number_one * input_number_two
    power_result = input_number_one ** input_number_two
    print(f"Addition: {addition_result}")
    print(f"Subtraction: {subtraction_result}")
    print(f"Multiplication: {multiplication_result}")

    if input_number_two != 0:
        division_result = input_number_one / input_number_two
        print(f"Division: {division_result}")
    else:
        raise ZeroDivisionError('Division by zero is not allowed. Try again...')
    print(f"Power: {input_number_one} raised to the power of {input_number_two} = {power_result}")

elif choice == '3':
    is_python_fun = True
    is_sunny = False

    and_result = is_python_fun and is_sunny
    or_result = is_python_fun or is_sunny
    not_result_python = not is_python_fun
    not_result_sunny = not is_sunny

    print(f"Logical AND (is_python_fun AND is_sunny) result: {and_result}")
    print(f"Logical OR (is_python_fun OR is_sunny) result: {or_result}")
    print(f"Logical NOT (not is_python_fun) result: {not_result_python}")
    print(f"Logical NOT (not is_sunny) result: {not_result_sunny}")

    greater_than_result = 10 > 5
    equality_result = 5 == 5
    inequality_result = 10 != 5
    less_than_equal_result = 4 <= 10

    print(f"Comparison (10 > 5): {greater_than_result}")
    print(f"Comparison (5 == 5): {equality_result}")
    print(f"Comparison (10 != 5): {inequality_result}")
    print(f"Comparison (4 <= 10): {less_than_equal_result}")

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':
    mixed_data_types_list = ['Python', 1, 3.50, True]
    mixed_data_types_list.append('Appended string')
    print('List operations:')
    print(f'Appended list: {mixed_data_types_list}')
    print(f'4th List Element: {mixed_data_types_list[3]}')
    print()

    mixed_data_types_tuple = ('apple', 'orange', 'banana', 'kiwi')
    print('Tuple operations:')
    print(f'Tuple length: {len(mixed_data_types_tuple)}')
    print('Attempting to change the first element of the tuple...')
    try:
        mixed_data_types_tuple[0] = 'dragonfruit'
    except TypeError:
        print("Operation failed - tuples are immutable!")
    print()

    mixed_data_types_dictionary = {
        'name': 'Ivan',
        'age': '18',
        'city': 'Sofia'
    }
    print('Dictionary operations:')
    print(f'Value of the age key: {mixed_data_types_dictionary.get("age")}')
    print('Adding new key-value pair to the dictionary...')
    mixed_data_types_dictionary['occupation'] = 'Doctor'
    print(f'Updated dictionary: {mixed_data_types_dictionary}')


else:
    raise Exception('Invalid Input. Try again...')
