def arithmetic_arranger(problems, solution=False): # By default not calculating the solution.

    answers = []  # Eval function is used for calculation below.
    spaces = []   # Spaces betweeen the numbers and equations.
    eqs = []      # List of list of equation [["3","+", "4"]].
    def Is_Equation_Correct():
      """
      Purpose of this function is to check if the equation fits the following conditions or not.
      """
      arranged_problems = ""              # Creating a string variable for the final equation.
      check = True                        # Defaulting check value to True.
      for prob in problems: 
        num1, op, num2 = prob.split(" ")
        # Checks if the equation contains only numbers.
        if num1.isdigit() and num2.isdigit():
          eqs.append([num1,op,num2])        # Adding equations.
          spaces.append(max(len(num1),len(num2)) + 2)  # Addding spaces.
          if solution: 
            answers.append(eval(prob))  # Adding answers.
        else:
          arranged_problems += "Error: Numbers must only contain digits.\n"
          check = False
        # Checks if a number has more than 4 digits.
        if len(num1) > 4 or len(num2) > 4:
          arranged_problems += "Error: Numbers cannot be more than four digits.\n"
          check = False

      # Checks if there more than 5 equations (problems).
      if len(eqs) > 5: 
        arranged_problems += "Error: Too many problems.\n"
        check = False
        
      # Checks if the equations contains * or /.
      if any([eq[1] in ["/", "*"] for eq in eqs]): 
        arranged_problems += "Error: Operator must be '+' or '-'.\n"
        check = False
      
      # If all the conditions are False than all the equations are correct i.e check == True. 
      if check: return (True, arranged_problems)
      return (False, arranged_problems)
    
    # Check for wrong equations
    check, arranged_problems = Is_Equation_Correct()
    # If cond is True i.e check than arrange the problems.
    if check:
      spaces_len = len(spaces)
      for i in range(spaces_len): # Arranging the first number.
        num = str(eqs[i][0])
        arranged_problems += " "*(spaces[i]-len(num)) + num
        if i < len(spaces)-1:
          arranged_problems += " "*4
      arranged_problems += "\n"

      for i in range(spaces_len): # Arranging the second number with the operator.
        num = str(eqs[i][2])
        arranged_problems += eqs[i][1] + " "*(spaces[i]-len(num)-1) + num
        if i < len(spaces)-1:
          arranged_problems += " "*4
        
      arranged_problems += "\n"
      for i in range(spaces_len):  # Adding the dashes.
        arranged_problems += "-"*spaces[i] 
        if i < len(spaces)-1:
          arranged_problems += " "*4
      
      if solution: # If solution is True arrange the solution else don't.
        arranged_problems += "\n"
        for i in range(spaces_len):
          ans = str(answers[i])
          arranged_problems += " "*(spaces[i]-len(ans)) + ans
          if i < len(spaces)-1:
            arranged_problems += " "*4
    return arranged_problems

print(arithmetic_arranger(["3 + 855", "5000 + 2", "45 + 43", "123 + 49"],True))

