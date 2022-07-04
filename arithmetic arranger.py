def arithmetic_arranger(problems,res=False):
    
    equation_list = []
    
    if len(problems) > 4:
        return "Error: Too many problems."
        
    for problem in problems:
        equation = problem
        equation = problem.split()
        #check digits
        try:
            equation[0] = int(equation[0])
            equation[2] = int(equation[2])
        except:
            return "Error: Numbers must only contain digits."
        equation[0] = str(equation[0])
        equation[2] = str(equation[2])
        #check operators
        if not equation[1] == "+" and not equation[1] == "-":            
            return "Error: Operator must be '+' or '-'."
        #check the operands length
        if len(equation[0]) > 4 or len(equation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    
        spaces = " "
        if len(equation[2]) > len(equation[0]) :
            spaces = " "
        else:
            spaces = " " * (len(equation[0])-len(equation[2]) + 1)    
        equation.append(spaces.join(equation[1:]))
        del equation[1]
        del equation[1]
        
        equation.append("-")

        try:
            if len(equation[2]) < len(max(equation, key=len)) : equation[2] = "-" * len(max(equation, key=len))
        except:
            pass
          
        if res == True:
            equation.append(str(eval(problem)))
        else : pass
        
        equation_list.append(equation)
        

        
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    for equation in equation_list:
        row1= row1 + str(equation[0]).rjust(len(equation[1]))
        row1= row1 + "    "
        row2= row2 + str(equation[1])
        row2= row2 + "    "
        row3= row3 + str(equation[2])
        row3 = row3 + "    "
        if res == True:
            row4 = row4 + str(equation[3]).rjust(len(equation[1]))
            row4 = row4 + "    "
            solution = (f"{row1}\n{row2}\n{row3}\n{row4}")
        else:
            solution = (f"{row1}\n{row2}\n{row3}")
            
    #return arranged_problems
    return solution



#create a list of cases to test the program
tests = [['3801 - 2', '123 + 49'],['1 + 2', '1 - 9380'],['3 + 855', '3801 - 2', '45 + 43', '123 + 49'],['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'],['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87'],['3 / 855', '3801 - 2', '45 + 43', '123 + 49'],['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'],['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']]


#looping through all the possible cases
for test in tests:
    print(arithmetic_arranger(test))
    print("----------------------------------------------------------------------------")
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))

