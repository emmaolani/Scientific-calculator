from stack import Stack


class CalculatorEngine:
    def __init__(self, expression):
        self.stack = Stack()
        self.expression = expression
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }
        self.result = []
        self.stack_top = ''

    def scan_exp(self):
        if len(self.expression) > 0:
            for i in range(len(self.expression)):
                if self.expression[i] == '(':
                    self.stack.push(self.expression[i])
                elif self.expression[i] in (self.precedence.keys()):
                    if self.stack_top is None:
                        self.stack.push(self.expression[i])
                    elif self.stack_top == '(':
                        self.stack.push(self.expression[i])
                    else:
                        condition = True
                        while condition:
                            if self.stack_top is None:
                                condition = False
                            elif self.precedence[self.expression[i]] > self.precedence[self.stack_top]:
                                self.stack.push(self.expression[i])
                                self.stack_top = self.stack.show_head()
                                condition = False
                            elif self.precedence[self.expression[i]] == self.precedence[self.stack_top]:
                                op = self.stack.pop()
                                self.__compute_result(op)
                                self.stack_top = self.stack.show_head()
                            else:
                                pass

    def __compute_result(self, operator):
        pass


