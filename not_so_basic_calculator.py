def addition(a,b):
    return a+b

def diff(a,b):
    return a-b


def mul(a,b):
    return a*b


def div(a,b):
    return a/b


def solveExpression(arr):
    exps = ['/', '*', '+', '-']
    holder = 0
    a = 'xxx'
    while len(arr) != 1:
        found = False
        for m in range(len(arr)):
            if arr[m] == exps[holder]:
                # print(f'yes {ele} == exps:  {exps[holder]}  index of ele: {arr.index(ele)}')
                found = True
                opr = m
                if holder == 0:
                    a = div(float(arr[opr-1]), float(arr[opr+1]))
                    # print(f'we got: {a}, coz divided {arr[opr - 1]} with {int(arr[opr + 1])}')
                elif holder == 1:
                    a = mul(float(arr[opr-1]), float(arr[opr+1]))
                    # print(f'we got: {a}, coz we multiplied {arr[opr-1]} with {int(arr[opr+1])}')
                elif holder == 2:
                    a = addition(float(arr[opr-1]), float(arr[opr+1]))
                    # print(f'we got: {a}, coz we added {arr[opr - 1]} with {int(arr[opr + 1])}')
                '''elif holder == 3:
                    a = diff(float(arr[opr-1]), float(arr[opr+1]))
                    # print(f'we got: {a}, coz we subtracted {arr[opr - 1]} with {int(arr[opr + 1])}')'''
                arr.pop(opr-1)
                arr.pop(opr)
                arr[opr-1] = a
                # print(arr)
                break
        else:
            found = False
            holder += 1
    return arr[0]

print('''Enter the expression in the following format:
9+((88/20)*5)-2+997''')
input_string = input("Enter the expression: \n")
numbers = [str(x) for x in range(10)]
expression = []
i = 0
while i < len(input_string):
    word = ""
    if input_string[i] == '-':
        expression.append('+')
        word += '-'
        c=i
        while input_string[c] not in numbers:
            c+=1
        i = c
    if input_string[i] in numbers:
        number_counter = i
        while number_counter < len(input_string) and input_string[number_counter] in numbers:
            word += str(input_string[number_counter])
            number_counter += 1
        expression.append(word)
        i = number_counter - 1
    else:
        if input_string[i] != ' ':
            expression.append(input_string[i])
    i += 1
k,t = 0,len(expression)
while k < t:
    if expression[k] == '+' and expression[k-1] == '(':
        expression.pop(k)
        t -= 1
    k += 1
print(expression)



expression.insert(0, '(')
expression.append(')')
print(expression)
while len(expression) != 1:
    note_index_open = 0
    note_index_close = 0
    for j in range(len(expression)):
        # print(f'element: {expression[j]}')
        if expression[j] == '(':
            note_index_open = j
        if expression[j] == ')':
            note_index_close = j
            break
    # print(f'open: {note_index_open}, close: {note_index_close}')
    val = solveExpression(expression[note_index_open+1:note_index_close])
    x = 0
    while x != (note_index_close-note_index_open):
        expression.pop(note_index_open)
        x += 1
    expression[note_index_open] = val
    print(expression)
print(expression[0])
