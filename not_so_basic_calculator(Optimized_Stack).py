class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)
        self.top = elem

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            val = self.stack[-1]
            self.stack.pop()
            if self.isEmpty():
                self.top = -1
            else:
                self.top = self.stack[-1]
        return val

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def input_to_expr(input_string):
    numbers = [str(x) for x in range(10)]
    expression = []
    i = 0
    while i < len(input_string):
        if input_string[i] not in numbers:
            expression.append(input_string[i])
        else:
            word = ""
            c = i
            while c < len(input_string) and (input_string[c] in numbers):
                word += input_string[c]
                c += 1
            expression.append(word)
            i = c
            continue
        i += 1
    return expression


print('''Enter the expression in the following format:
9+((88/20)*5)-2+997''')
input_string_raw = input("Enter the expression: \n")

input_string = input_to_expr(input_string_raw)
#print(input_string)

precedence_table = {'+': [1, 2], '-': [1, 2], '*': [3, 4], '/': [5, 6], '(': [7, 0], ')': [0, -1], '#': [-2, -2]}

def isOperator(ele):
    if ele in precedence_table:
        return True
    return False

def infix_to_postfix(string):
    post = []
    stack = Stack()
    stack.push('#')
    i = 0
    while i != len(string):
        if isOperator(string[i]):
            if string[i] == ')' and stack.top == "(":
                stack.pop()
                i += 1
            elif precedence_table[string[i]][0] > precedence_table[stack.top][1]:
                stack.push(string[i])
                i += 1
            else:
                post.append(stack.pop())
        else:
            post.append(string[i])
            i += 1
    while stack.isEmpty() != 1:
        post.append(stack.pop())
    return post[:-1]

def identifier(opr):
    if opr == '/':
        return 1
    if opr == '*':
        return 2
    if opr == '+':
        return 3
    if opr == '-':
        return 4

def evaluate(expression):
    stack = Stack()
    i = 0
    while i < len(expression):
        if isOperator(expression[i]):
            b = float(stack.pop())
            a = float(stack.pop())
            val = a
            call = identifier(expression[i])
            if call == 1:
                val = divide(a,b)
            elif call == 2:
                val = multiply(a,b)
            elif call == 3:
                val = add(a,b)
            elif call == 4:
                val = subtract(a,b)
            stack.push(val)
        else:
            stack.push(expression[i])
        i += 1
    return stack.top


postfix_string  = infix_to_postfix(input_string)
print(evaluate(postfix_string))
