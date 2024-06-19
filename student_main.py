def task0():
    return 4

def task1(input_str):
    return len(input_str)

def task2(num1, term, num2):
    if term == '+':
        return num1+num2
    elif term == '-':
        return num1-num2
    elif term == '/':
        if num2 !=0:
            return num1 / num2
        else:
            return "Error"
    elif term == '//':
        if num2 != 0:
            return num1 // num2
        else:
            return "Error"
    elif term == '**':
        return num1**num2
    elif term == '*':
        return num1*num2
    else:
        return "Unknown operator"

def task3(number_list):
    if not isinstance(number_list, list):
        return "Error"
    else:
        if not number_list:
            return "The list is empty"
        else:
            return max(number_list)
