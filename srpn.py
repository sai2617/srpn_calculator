#This is your SRPN file. Make your changes here.

#This value will store the stack
value = []

#This count will is used to run iterative logic for 'r' value
count = 0

#This is saving the lowest saturation value for checking saturation result
lowestSaturationPoint = "-2147483648"

#This is saving the maximum saturation value for checking saturation result
maximumSaturationPoint = "2147483647"

#This is hard coded values for r
rota = [
  1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335,
  719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027,
  783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426,
  304089172, 1303455736, 35005211, 521595368, 1804289383
]


#This function will check whether the value is in saturation limit
def saturation_result(result):
  if int(result) >= int(lowestSaturationPoint) and int(result) <= int(
      maximumSaturationPoint):
    value.append(int(result))
  if int(result) < int(lowestSaturationPoint):
    result = lowestSaturationPoint
    value.append(int(result))
  if int(result) > int(maximumSaturationPoint):
    result = maximumSaturationPoint
    value.append(int(result))


def process_command(command):
# This will split the command (input) from the main function
  tokenss = command.split(" ")
  
#This will run loop which helps to take values in horizontal as well as vertical
  for i in range(len(tokenss)):

#This will give addition value of the tokenss which is both splitted value in horizontal as well as vertical  
    if tokenss[i] == '+':
      
#checking the length of stack before doing operation
      if len(value) >= 2:
        value1 = value.pop()
        value2 = value.pop()
        result = value1 + value2

#This will check saturation limit from the function saturation_result        
        saturation_result(result)

#if length of stack before doing operation is less than 2 then it will print Stack Underflow.       
      else:
        print("Stack underflow.")

#This will give subtraction value   
    elif tokenss[i] == '-':
      if len(value) >= 2:
        value1 = value.pop()
        value2 = value.pop()
        result = value2 - value1
        saturation_result(result)
      else:
        print("Stack underflow.")

#This will give modulo value    
    elif tokenss[i] == '%':
      if len(value) >= 2:
        value1 = value.pop()
        value2 = value.pop()

#If value1 is zero then modulo can't work so exception      
        if value1 == 0:
          print("Exception: can't do modulo by 0.")
          saturation_result(value2)
          saturation_result(value1)

#If value1 is not zero modulo will work       
        else:
          result = value2 % value1
          saturation_result(result)
      else:
        print("Stack underflow.")

#This will give multiplication value
    elif tokenss[i] == '*':
      if len(value) >= 2:
        value1 = value.pop()
        value2 = value.pop()
        result = value2 * value1
        saturation_result(result)
      else:
        print("Stack underflow.")
        
#This will give power value
    elif tokenss[i] == '^':
      if len(value) >= 2:
        value1 = value.pop()
        value2 = value.pop()
        
#If value is less than 0 negative power
        if value1 < 0:
          print("Negative power.")
          saturation_result(value2)
          saturation_result(value1)

#Otherwise give power value        
        else:
          result = value2**value1
          saturation_result(result)
      else:
        print("Stack underflow.")

#This is giving divided by value    
    elif tokenss[i] == '/':
      if len(value) >= 2:
        value1 = value.pop()
        value2 = value.pop()
#If value1 is 0 then it cant divide by zero
        if value1 == 0:
          print("Divide by 0.")
          saturation_result(value2)
          saturation_result(value1)
#Else division value
        else:
          result = value2 / value1
          saturation_result(result)
      else:
        print("Stack underflow.")

#This will give final stack value
    elif tokenss[i] == '=':
      print(value[-1])

#This will print all values in stack    
    elif tokenss[i] == 'd':
      for i in range(len(value)):
        print(value[i])

#This will take the values even if the stack is empty assigned 
    elif tokenss[i] == '':
      pass

#This will write all values of r    
    elif tokenss[i] == 'r':
      global count
      if len(value) >= 23:
        print("Stack overflow.")
        return

      else:
        saturation_result(rota[count])
        count = count + 1
        
#This will comment the values after using this #
    elif tokenss[i] == '#':
      return 0

#This will give the negative value also impended if its numeric as it will check numeric values   
    elif tokenss[i].lstrip("-").isnumeric():

#if length of value is less than 23 then value will append      
      if len(value) < 23:
        saturation_result(tokenss[i])
        
#Otherwise it will print        
      else:
        print("Stack overflow.")

#This will print unrecognized operator if it is not in the range        
    else:
      print(f"Unrecognised operator or operand \"{tokenss[i]}\".")


#This is the entry point for the program.
#It is suggested that you do not edit the below,
#to ensure your code runs with the marking script
if __name__ == "__main__":
  while True:
    try:
      cmd = input()
      pc = process_command(cmd)
    except EOFError:
      exit()
