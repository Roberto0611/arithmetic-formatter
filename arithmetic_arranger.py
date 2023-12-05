def arithmetic_arranger(problems, answer_):

  #Variables
  arranged_problems = []
  input = problems
  operations = []
  results = []

  #Loops to get a list with a list of the operations
  for element in input:
    operations.append(element.split())

  #First Rule of errors
  NumberOfOperations = len(operations)
  if NumberOfOperations > 5:
    return 'Error: Too many problems.'

  #Get nums individually
  for operation in operations:
    try:
      num1 = int(operation[0])
      sign = operation[1]
      num2 = int(operation[2])
      
    #Check if signs are correct
      if sign not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."

      #Check if numbers are correct
      if num1 > 999 or num2 > 999:
        return "Error: Numbers cannot be more than four digits."

      if sign == "+":
        results.append(num1+num2)
      else:
        results.append(num1-num2)

      #Arrange problems
      
      #Find the largest number
      length_num1 = len(str(num1))
      length_num2 = len(str(num2))
      
      larger_num = max(length_num1, length_num2)

      #Set line 1 and line 2
      line1 = str(num1).rjust(larger_num + 2)
      line2 = sign + str(num2).rjust(larger_num + 1)

      #Set the dashes
      x = 0
      line3_list = []
      while x < larger_num + 2:
        line3_list.append("-")
        x = x + 1
      line3 = ''.join(line3_list)      
      
    #Check if there's only digits
    except ValueError:
      return 'Error: Numbers must only contain digits.'
      
  return arranged_problems
