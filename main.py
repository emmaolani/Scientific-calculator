from Calculator import Calculator

enter_digits_and_OPERATOR = input('enter digit or operator: ')
calculator = Calculator()

while enter_digits_and_OPERATOR != '':
    if enter_digits_and_OPERATOR == 'del':
        calculator.delete()
    elif enter_digits_and_OPERATOR == 'clear':
        calculator.clear()
    else:
        calculator.store_input(enter_digits_and_OPERATOR)
    print(calculator.get_screen())
    enter_digits_and_OPERATOR = input('enter digit or operator: ')
