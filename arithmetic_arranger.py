def arithmetic_arranger(problems, answer_):

  #Variables
  arranged_problems = []
  input = problems
  operations = []
  results = []

  #Loops to get a list with a list of the operations
  for element in input:
    operations.append(element.split())

  #Check for any error

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

      print(num1, sign, num2)

    #Check if there's only digits
    except ValueError:
      return 'Error: Numbers must only contain digits.'

  return operations
