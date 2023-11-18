class Calculator:
    def __init__(self):
        self.__input_list = []
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
        self.__input = {'value': '',
                        'type': ''
                        }
        self.__should_sign = False
        self.__how_many_open_bracket = 0

    def __get_input_type(self):
        if self.__input['value'] in self.__input_type['operator'].values():
            return self.__validate_operator()
        else:
            return self.__validate_operand()

    def store_input(self, new_input):
        self.__input['value'] = new_input
        inp_type = self.__get_input_type()
        self.__input['type'] = inp_type
        if inp_type in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            self.__insert_plus_minus()
        elif inp_type in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__insert_multi_division()
        elif inp_type == self.__input_type['operator'][5]:
            self.__insert_open_bracket()
        elif inp_type == self.__input_type['operator'][6]:
            self.__insert_close_bracket()
        elif inp_type in (self.__input_type['number'][1], self.__input_type['number'][3]):
            self.__insert_number()
        elif inp_type in (self.__input_type['number'][2], self.__input_type['number'][4]):
            self.__display_err('negative number not allowed')
        else:
            self.__display_err(inp_type)

        self.__input = {'value': '',
                        'type': ''
                        }
        print(self.__should_sign)

    def __insert_close_bracket(self):
        if len(self.__input_list) == 0:
            previous_input = None
        else:
            previous_input = self.__input_list[len(self.__input_list) - 1]
        self.__input['precedence'] = ')'

        if previous_input is None:
            self.__display_err('Invalid syntax')
            return
        elif previous_input['type'] in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            self.__display_err('Invalid syntax')
            return
        elif previous_input['type'] in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__display_err('Invalid syntax')
            return
        elif previous_input['type'] in (self.__input_type['operator'][5]):
            self.__display_err('Invalid syntax')
            return
        elif previous_input['type'] in (self.__input_type['operator'][6]):
            if self.__how_many_open_bracket > 0:
                self.__input_list.append(self.__input)
                self.__how_many_open_bracket = self.__how_many_open_bracket - 1
            else:
                self.__display_err('Invalid syntax')
            return
        elif previous_input['type'] in self.__input_type['number'].values():
            if self.__how_many_open_bracket > 0:
                self.__input_list.append(self.__input)
                self.__how_many_open_bracket = self.__how_many_open_bracket - 1
            else:
                self.__display_err('Invalid syntax')
            return

    def __insert_open_bracket(self):
        if len(self.__input_list) == 0:
            previous_input = None
        else:
            previous_input = self.__input_list[len(self.__input_list) - 1]

        self.__input['precedence'] = '('

        self.__how_many_open_bracket = self.__how_many_open_bracket + 1
        if previous_input is None:
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            if self.__should_sign:
                temp_inp = previous_input
                self.__input_list[len(self.__input_list) - 1] = {
                    'value': '0',
                    'type': self.__input_type['number'][1],
                    'precedence': None
                }
                self.__input_list.append(temp_inp)
                self.__input_list.append(self.__input)
                self.__should_sign = False
            else:
                self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in (self.__input_type['operator'][5]):
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in (self.__input_type['operator'][6]):
            temp_inp = {
                'value': '*',
                'type': self.__input_type['operator'][3],
                'precedence': 2
            }
            self.__input_list.append(temp_inp)
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in self.__input_type['number'].values():
            temp_inp = {
                'value': '*',
                'type': self.__input_type['operator'][3],
                'precedence': 2
            }
            self.__input_list.append(temp_inp)
            self.__input_list.append(self.__input)
            return

    def __insert_multi_division(self):
        if len(self.__input_list) == 0:
            previous_input = None
        else:
            previous_input = self.__input_list[len(self.__input_list) - 1]

        self.__input['precedence'] = 2

        if previous_input is None:
            return
        elif previous_input['type'] in (self.__input_type['operator'][1], self.__input_type['operator'][2]):
            if self.__should_sign:
                self.__display_err('Invalid syntax')
            else:
                self.__input_list[len(self.__input_list) - 1] = self.__input
            return
        elif previous_input['type'] in (self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__input_list[len(self.__input_list) - 1] = self.__input
            return
        elif previous_input['type'] in (self.__input_type['operator'][5]):
            self.__display_err('Invalid syntax')
            return
        elif previous_input['type'] in (self.__input_type['operator'][6]):
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in self.__input_type['number'].values():
            self.__input_list.append(self.__input)
            return

    def __insert_plus_minus(self):
        if len(self.__input_list) == 0:
            previous_input = None
        else:
            previous_input = self.__input_list[len(self.__input_list) - 1]

        self.__input['precedence'] = 1

        if previous_input is None:
            self.__input_list.append('(')
            self.__input_list.append(self.__input)
            self.__how_many_open_bracket = self.__how_many_open_bracket + 1
            self.__should_sign = True
            return
        elif previous_input['type'] in (self.__input_type['operator'][1], self.__input_type['operator'][2],
                                        self.__input_type['operator'][3], self.__input_type['operator'][4]):
            self.__input_list[len(self.__input_list) - 1] = self.__input
            return
        elif previous_input['type'] in (self.__input_type['operator'][5]):
            self.__input_list.append(self.__input)
            self.__should_sign = True
            return
        elif previous_input['type'] in (self.__input_type['operator'][6]):
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in (self.__input_type['number'].values()):
            self.__input_list.append(self.__input)
            return

    def __insert_number(self):
        if len(self.__input_list) == 0:
            previous_input = None
        else:
            previous_input = self.__input_list[len(self.__input_list) - 1]

        self.__input['precedence'] = None

        if previous_input is None:
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] == self.__input_type['operator'][1]:
            if self.__should_sign:
                self.__input_list[len(self.__input_list) - 1] = self.__input
                self.__should_sign = False
            else:
                self.__input_list.append(self.__input)
            return
        elif previous_input['type'] == self.__input_type['operator'][2]:
            if self.__should_sign:
                temp_input = {
                    'value': previous_input['value'] + self.__input['value'],
                    'type': '',
                    'precedence': None
                }
                self.__input = temp_input
                self.__input['type'] = self.__get_input_type()
                self.__input_list[len(self.__input_list) - 1] = self.__input
                self.__should_sign = False
            else:
                self.__input_list.append(self.__input)
            return
        elif previous_input['type'] in ['*', '/', '(']:
            self.__input_list.append(self.__input)
            return
        elif previous_input['type'] == self.__input_type['operator'][6]:
            # throw error *****************************************
            self.__display_err('Invalid syntax')
            return
        elif previous_input['type'] in (self.__input_type['number'][1], self.__input_type['number'][2]):
            temp_input = {
                'value': previous_input['value'] + self.__input['value'],
                'type': '',
                'precedence': None
            }
            self.__input = temp_input
            self.__input['type'] = self.__get_input_type()
            self.__input_list[len(self.__input_list) - 1] = self.__input
            return
        elif previous_input['type'] in (self.__input_type['number'][3], self.__input_type['number'][4]):
            if self.__input['type'] in (self.__input_type['number'][3], self.__input_type['number'][4]):
                self.__display_err('Invalid syntax')
                return
            else:
                temp_input = {
                    'value': previous_input['value'] + self.__input['value'],
                    'type': '',
                    'precedence': None
                }
                self.__input = temp_input
                self.__input['type'] = self.__get_input_type()
                self.__input_list[len(self.__input_list) - 1] = self.__input
                return

    def __validate_operator(self):
        if self.__input['value'] == self.__input_type['operator'][1]:
            return self.__input_type['operator'][1]
        elif self.__input['value'] == self.__input_type['operator'][2]:
            return self.__input_type['operator'][2]
        elif self.__input['value'] == self.__input_type['operator'][3]:
            return self.__input_type['operator'][3]
        elif self.__input['value'] == self.__input_type['operator'][4]:
            return self.__input_type['operator'][4]
        elif self.__input['value'] == self.__input_type['operator'][5]:
            return self.__input_type['operator'][5]
        elif self.__input['value'] == self.__input_type['operator'][6]:
            return self.__input_type['operator'][6]

    def __validate_operand(self):
        try:
            is_it_integer = True
            # checking if number is a float or integer
            for number in self.__input['value']:
                if number == '.':
                    is_it_integer = False
            if is_it_integer:
                int(self.__input['value'])
                # checking if integer is negative and return type
                return self.__check_num_signed(self.__input_type['number'][1])
            else:
                float(self.__input['value'])
                # checking if float is negative and return type
                return self.__check_num_signed(self.__input_type['number'][3])

        except ValueError:
            return 'invalid operand'

    def __check_num_signed(self, num_type):
        if self.__input['value'][0] == self.__input_type['operator'][1]:
            # removing + sign from number if present and returning unsigned number
            # and setting class current input type
            temp_input = self.__input['value'].split('+')
            self.__input['value'] = temp_input[1]
            return num_type
        elif self.__input['value'][0] == self.__input_type['operator'][2]:
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
        if len(self.__input_list) == 0:
            previous_input = None
        else:
            previous_input = self.__input_list[len(self.__input_list) - 1]

        if previous_input is not None:
            if previous_input['type'] == self.__input_type['operator'][5]:
                self.__how_many_open_bracket = self.__how_many_open_bracket - 1
            if previous_input['type'] == self.__input_type['operator'][6]:
                self.__how_many_open_bracket = self.__how_many_open_bracket + 1
            if self.__should_sign:
                self.__should_sign = False

            self.__input_list.pop()
        else:
            return

    def clear(self):
        self.__input_list = []
        self.__input = {'value': '',
                        'type': ''
                        }
        self.__should_sign = False
        self.__how_many_open_bracket = 0

    def get_values(self):
        show_screen = []
        for i in range(len(self.__input_list)):
            show_screen.append(self.__input_list[i]['value'])
        return show_screen

    def get_input_list(self):
        self.__change_to_number()
        self.__complete_bracket()
        return self.__input_list

    def __complete_bracket(self):
        while self.__how_many_open_bracket > 0:
            closed_bracket = {
                'value': ')',
                'type': self.__input_type['operator'][5],
                'precedence': ')'
            }
            self.__input_list.append(closed_bracket)
            self.__how_many_open_bracket = self.__how_many_open_bracket - 1

    def __change_to_number(self):
        for i in range(len(self.__input_list)):
            if self.__input_list[i]['type'] in ('int', 'nint'):
                self.__input_list[i]['value'] = int(self.__input_list[i]['value'])
            elif self.__input_list[i]['type'] in ('float', 'nfloat'):
                self.__input_list[i]['value'] = float(self.__input_list[i]['value'])

    @staticmethod
    def __display_err(msg):
        print(msg)
