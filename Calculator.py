class Calculator:
    def __init__(self):
        self.__screen = []
        self.__input_type = {
            'number': {
                1: 'int',
                2: 'nint',
                3: 'float',
                4: 'nfloat'
            },
            'operator': {
                1: '+',
                2: '-',
                3: '*',
                4: '/',
                5: '(',
                6: ')'
            }
        }
        self.__input = ''
        self.__cur_input_type = ''
        self.__prev_input_type = ''
        self.__should_sign = False
        self.__how_many_open_bracket = 0

    def __get_input_type(self):
        if self.__input in self.__input_type['operator'].values():
            return self.__validate_operator()
        else:
            return self.__validate_operand()

    def store_input(self, new_input):
        self.__input = new_input
        inp_type = self.__get_input_type()
        if inp_type in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            self.__cur_input_type = inp_type
            self.__insert_plus_minus()
            self.__prev_input_type = self.__cur_input_type
        elif inp_type in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__cur_input_type = inp_type
            self.__insert_multi_division()
            self.__prev_input_type = self.__cur_input_type
        elif inp_type == self.__input_type['operator'][5]:
            self.__cur_input_type = inp_type
            self.__insert_open_bracket()
            self.__prev_input_type = self.__cur_input_type
        elif inp_type == self.__input_type['operator'][6]:
            self.__cur_input_type = inp_type
            self.__insert_close_bracket()
            self.__prev_input_type = self.__cur_input_type
        elif inp_type in (self.__input_type['number'][1], self.__input_type['number'][3]):
            self.__cur_input_type = inp_type
            self.__insert_number()
            self.__prev_input_type = self.__cur_input_type
        elif inp_type in (self.__input_type['number'][2], self.__input_type['number'][4]):
            self.__display_err('negative number not allowed')
        else:
            self.__display_err(inp_type)

        # Updating previous input type
        self.__cur_input_type = ''

        print(self.__prev_input_type)
        print(self.__should_sign)

    def __insert_close_bracket(self):
        if self.__prev_input_type == '':
            self.__display_err('Invalid syntax')
            self.__cur_input_type = self.__prev_input_type
            return
        elif self.__prev_input_type in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            self.__display_err('Invalid syntax')
            self.__cur_input_type = self.__prev_input_type
            return
        elif self.__prev_input_type in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__display_err('Invalid syntax')
            self.__cur_input_type = self.__prev_input_type
            return
        elif self.__prev_input_type in (self.__input_type['operator'][5]):
            self.__display_err('Invalid syntax')
            self.__cur_input_type = self.__prev_input_type
            return
        elif self.__prev_input_type in (self.__input_type['operator'][6]):
            if self.__how_many_open_bracket > 0:
                self.__screen.append(self.__input)
                self.__how_many_open_bracket = self.__how_many_open_bracket - 1
            else:
                self.__display_err('Invalid syntax')
                self.__cur_input_type = self.__prev_input_type
            return
        elif self.__prev_input_type in self.__input_type['number'].values():
            if self.__how_many_open_bracket > 0:
                self.__screen.append(self.__input)
                self.__how_many_open_bracket = self.__how_many_open_bracket - 1
            else:
                self.__display_err('Invalid syntax')
                self.__cur_input_type = self.__prev_input_type
            return

    def __insert_open_bracket(self):
        self.__how_many_open_bracket = self.__how_many_open_bracket + 1
        if self.__prev_input_type == '':
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            if self.__should_sign:
                temp_inp = self.__screen[len(self.__screen)-1]
                self.__screen[len(self.__screen) - 1] = '0'
                self.__screen.append(temp_inp)
                self.__screen.append(self.__input)
                self.__should_sign = False
            else:
                self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in (self.__input_type['operator'][5]):
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in (self.__input_type['operator'][6]):
            self.__screen.append('*')
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in self.__input_type['number'].values():
            self.__screen.append('*')
            self.__screen.append(self.__input)
            return

    def __insert_multi_division(self):
        if self.__prev_input_type == '':
            return
        elif self.__prev_input_type in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            if self.__should_sign:
                self.__display_err('Invalid syntax')
                self.__cur_input_type = self.__prev_input_type
            else:
                self.__screen[len(self.__screen) - 1] = self.__input
            return
        elif self.__prev_input_type in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__screen[len(self.__screen) - 1] = self.__input
            return
        elif self.__prev_input_type in (self.__input_type['operator'][5]):
            self.__display_err('Invalid syntax')
            self.__cur_input_type = self.__prev_input_type
            return
        elif self.__prev_input_type in (self.__input_type['operator'][6]):
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in self.__input_type['number'].values():
            self.__screen.append(self.__input)
            return

    def __insert_plus_minus(self):
        if self.__prev_input_type == '':
            self.__screen.append('(')
            self.__screen.append(self.__input)
            self.__how_many_open_bracket = self.__how_many_open_bracket + 1
            self.__should_sign = True
            return
        elif self.__prev_input_type in (self.__input_type['operator'][1], self.__input_type['operator'][2],
                                        self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__screen[len(self.__screen) - 1] = self.__input
            return
        elif self.__prev_input_type in (self.__input_type['operator'][5]):
            self.__screen.append(self.__input)
            self.__should_sign = True
            return
        elif self.__prev_input_type in (self.__input_type['operator'][6]):
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in (self.__input_type['number'].values()):
            self.__screen.append(self.__input)
            return

    def __insert_number(self):
        if self.__prev_input_type == '':
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type == self.__input_type['operator'][1]:
            if self.__should_sign:
                self.__screen[len(self.__screen)-1] = self.__input
                self.__should_sign = False
            else:
                self.__screen.append(self.__input)
            return
        elif self.__prev_input_type == self.__input_type['operator'][2]:
            if self.__should_sign:
                temp_input = self.__screen[len(self.__screen)-1] + self.__input
                self.__screen[len(self.__screen)-1] = temp_input
                self.__input = temp_input
                self.__cur_input_type = self.__get_input_type()
                self.__should_sign = False
            else:
                self.__screen.append(self.__input)
            return
        elif self.__prev_input_type in ['*', '/', '(']:
            self.__screen.append(self.__input)
            return
        elif self.__prev_input_type == self.__input_type['operator'][6]:
            # throw error *****************************************
            self.__display_err('Invalid syntax')
            self.__cur_input_type = self.__prev_input_type
            return
        elif self.__prev_input_type in (self.__input_type['number'][1], self.__input_type['number'][2]):
            temp_input = self.__screen[len(self.__screen)-1] + self.__input
            self.__screen[len(self.__screen)-1] = temp_input
            self.__input = temp_input
            self.__cur_input_type = self.__get_input_type()
            return
        elif self.__prev_input_type in (self.__input_type['number'][3], self.__input_type['number'][4]):
            if self.__cur_input_type in (self.__input_type['number'][3], self.__input_type['number'][4]):
                self.__display_err('Invalid syntax')
                self.__cur_input_type = self.__prev_input_type
                return
            else:
                temp_input = self.__screen[len(self.__screen)-1] + self.__input
                self.__screen[len(self.__screen)-1] = temp_input
                self.__input = temp_input
                self.__cur_input_type = self.__get_input_type()
                return

    def __validate_operator(self):
        if self.__input == self.__input_type['operator'][1]:
            return self.__input_type['operator'][1]
        elif self.__input == self.__input_type['operator'][2]:
            return self.__input_type['operator'][2]
        elif self.__input == self.__input_type['operator'][3]:
            return self.__input_type['operator'][3]
        elif self.__input == self.__input_type['operator'][4]:
            return self.__input_type['operator'][4]
        elif self.__input == self.__input_type['operator'][5]:
            return self.__input_type['operator'][5]
        elif self.__input == self.__input_type['operator'][6]:
            return self.__input_type['operator'][6]

    def __validate_operand(self):
        try:
            is_it_integer = True
            # checking if number is a float or integer
            for number in self.__input:
                if number == '.':
                    is_it_integer = False
            if is_it_integer:
                int(self.__input)
                # checking if integer is negative and return type
                return self.__check_num_signed(self.__input_type['number'][1])
            else:
                float(self.__input)
                # checking if float is negative and return type
                return self.__check_num_signed(self.__input_type['number'][3])

        except ValueError:
            return 'invalid operand'

    def __check_num_signed(self, num_type):
        if self.__input[0] == self.__input_type['operator'][1]:
            # removing + sign from number if present and returning unsigned number
            # and setting class current input type
            temp_input = self.__input.split('+')
            self.__input = temp_input[1]
            return num_type
        elif self.__input[0] == self.__input_type['operator'][2]:
            # if number inputted is a negative number we print out an error
            if num_type == self.__input_type['number'][1]:
                num_type = self.__input_type['number'][2]
            else:
                num_type = self.__input_type['number'][4]
            return num_type
        else:
            # here we return number type because it is not signed
            return num_type

    def delete(self):
        if len(self.__screen) - 1 > 0:
            if self.__screen[len(self.__screen) - 1] == self.__input_type['operator'][5]:
                self.__how_many_open_bracket = self.__how_many_open_bracket - 1
            if self.__screen[len(self.__screen) - 1] == self.__input_type['operator'][6]:
                self.__how_many_open_bracket = self.__how_many_open_bracket + 1
            if self.__should_sign:
                self.__should_sign = False

            self.__screen.pop()
            self.__input = self.__screen[len(self.__screen) - 1]
            inp_type = self.__get_input_type()
            self.__prev_input_type = inp_type

            print(self.__prev_input_type)
            print(self.__should_sign)
        else:
            return

    def clear(self):
        self.__screen = []
        self.__input = ''
        self.__cur_input_type = ''
        self.__prev_input_type = ''
        self.__should_sign = False
        self.__how_many_open_bracket = 0

    def get_screen(self):
        return self.__screen

    @staticmethod
    def __display_err(msg):
        print(msg)
