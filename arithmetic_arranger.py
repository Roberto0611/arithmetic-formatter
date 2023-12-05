#Code by: Roberto Ochoa Cuevas
def arithmetic_arranger(problems, answer_=False):

  #set arranged problems
  arranged_problems = []

  #First Rule of errors
  if len(problems) > 5:
    return 'Error: Too many problems.'
    
  #Initialize lines 
  line1_list, line2_list, line3_list, result_line_list = [], [], [], []
  
  for problem in problems:
    #Get nums individually
    num1, sign, num2 = problem.split()
    try:
      num1 = int(num1)
      num2 = int(num2)
      
    #Check if signs are correct
      if sign not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."

      #Check if numbers are correct
      if num1 > 9999 or num2 > 9999:
        return "Error: Numbers cannot be more than four digits."

      if sign == "+":
        result = num1 + num2
      else:
        result = num1 - num2

      #Arrange problems
      
      #Find the largest number
      length_num1 = len(str(num1))
      length_num2 = len(str(num2))
      
      max_length= max(length_num1, length_num2)
    
      line1_list.append(str(num1).rjust(max_length + 2))
      line2_list.append(sign + str(num2).rjust(max_length + 1))
      line3_list.append('-' * (max_length + 2))
      result_line_list.append(str(result).rjust(max_length + 2))
      
    #Check if there's only digits
    except ValueError:
      return 'Error: Numbers must only contain digits.'

  #Check if we want answer or not
  if answer_ is True:
    # Join lines list with 4 spaces :)
    arranged_problems.append('    '.join(line1_list))
    arranged_problems.append('    '.join(line2_list))
    arranged_problems.append('    '.join(line3_list))
    arranged_problems.append('    '.join(result_line_list) if result_line_list else '')
  else: #In case we don't want to return the answer
    arranged_problems.append('    '.join(line1_list))
    arranged_problems.append('    '.join(line2_list))
    arranged_problems.append('    '.join(line3_list))
  return '\n'.join(arranged_problems) #Return the problems 
#end of the code<3