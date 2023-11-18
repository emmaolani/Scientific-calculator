from stack import Stack


class CalculatorEngine:
    def __init__(self, expression):
        self.__stack = Stack()
        self.__expression = expression
        self.__result = []
        self.__stack_top = None

    def get_result(self):
        self.__calculate_exp()

        while self.__stack.show_size() > 0:
            op = self.__stack.pop()
            self.__compute_result(op)
            self.__stack_top = self.__stack.show_head()
        return self.__result

    def __calculate_exp(self):
        if len(self.__expression) > 0:
            for i in range(len(self.__expression)):
                if self.__expression[i]['precedence'] == '(':
                    self.__stack.push(self.__expression[i])
                    self.__stack_top = self.__stack.show_head()
                elif self.__expression[i]['precedence'] == ')':
                    condition = True
                    while condition:
                        if self.__stack_top is None:
                            condition = False
                        elif self.__stack_top['precedence'] == '(':
                            self.__stack.pop()
                            condition = False
                        else:
                            op = self.__stack.pop()
                            self.__compute_result(op)

                        self.__stack_top = self.__stack.show_head()
                elif self.__expression[i]['precedence'] is None:
                    self.__result.append(self.__expression[i]['value'])
                else:
                    if self.__stack_top is None:
                        self.__stack.push(self.__expression[i])
                        self.__stack_top = self.__stack.show_head()
                    elif self.__stack_top['precedence'] == '(':
                        self.__stack.push(self.__expression[i])
                        self.__stack_top = self.__stack.show_head()
                    else:
                        self.__push_operator_to_stack(self.__expression[i])

    def __push_operator_to_stack(self, operator):
        condition = True
        while condition:
            if self.__stack_top is None:
                self.__stack.push(operator)
                condition = False
            elif operator['precedence'] > self.__stack_top['precedence']:
                self.__stack.push(operator)
                condition = False
            elif operator['precedence'] == self.__stack_top['precedence']:
                op = self.__stack.pop()
                self.__compute_result(op)
            else:
                op = self.__stack.pop()
                self.__compute_result(op)

            self.__stack_top = self.__stack.show_head()

    def __compute_result(self, op):
        second_num = self.__result.pop()
        first_num = self.__result.pop()
        operator = op['value']

        if operator == '+':
            result = first_num + second_num
            self.__result.append(result)
        elif operator == '-':
            result = first_num - second_num
            self.__result.append(result)
        elif operator == '*':
            result = first_num * second_num
            self.__result.append(result)
        elif operator == '/':
            result = first_num / second_num
            self.__result.append(result)
