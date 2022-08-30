import math
import tokenize_p

tokens = list(tokenize_p.tokenize(open('hellow.py', 'rb').__next__))

operators = []
operands = []

operand_type = ['STRING', 'NUMBER']
not_operand = ['if', 'for', 'in', 'print', 'elif', 'else', 'while', 'range', 'not', 'break', 'continue', 'return','def', 'try', 'catch']
cyclomatic_complexity = ['if', 'elif', 'for', 'while']
complexity = 0

total_lines_of_code = 0 #update later

for tk in tokens:
    str_tk = str(tk).split(';')[0]
    # print(str_tk + " " + tk.string)
    # print(tk.start, tk.end)
    
    if str_tk == 'OP':
        operators += [tk.string]
    elif str_tk in operand_type:
        operands += [tk.string]
    elif str_tk == 'NAME' and (tk.string == 'TRUE' or tk.string == 'FALSE'):
        operands += [tk.string]
    elif str_tk == 'NAME' and tk.string not in not_operand:
        operands += [tk.string]
    elif str_tk == 'NL':
        total_lines_of_code -= 1
    elif str_tk == 'ENDMARKER':
        total_lines_of_code += tk.start[0]

    if tk.string in cyclomatic_complexity:
        complexity += 1



n1 = len(set(operators))
n2 = len(set(operands))
N1 = len(operators)
N2 = len(operands)

print('Unique operators ', set(operators))
print('-----------------------------------------------')
print('Unique operands ', set(operands))
print('-----------------------------------------------')
print('Cyclomatic complexity: ', complexity+1)
print('-----------------------------------------------')

print('Total lines of code excluding new lines and comments : ', max(0, total_lines_of_code))
print('-----------------------------------------------')
print("Number of Distinct Operators", n1)
print("Number of Distinct Operands", n2)
print("Number of Operators", N1)
print("Number of Operands", N2)
print('-----------------------------------------------')

#halstead metrics

N = N1 + N2
n = n1 + n2
V = N * math.log2(n)
D = (n1 / 2) * (N2 / n2) 
E = D * V
print('Halstead program length: ', N)
print('Halstead vocabulary: ', n)
print('Program volume: ', V)
print('Program difficulty ', D)
print('Programming effort ', E)

