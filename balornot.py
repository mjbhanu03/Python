usr = list(input("Enter String: "))
status = "Not Balanced"
matched = False
count = 0

for i in usr:
  
  if i == '{':
    for j in range(count, len(usr)):
      if usr[j] != '}':
        matched = True
        break

      elif j+1 == len(usr) and matched == True:
        status = "Balanced"

  elif i == '[':
    for j in range(count, len(usr)):
      if usr[j] == ']':
        matched = True
        break
      elif j+1 == len(usr) and matched == True:
        status = "Balanced"

  elif i == '(':
    for j in range(count, len(usr)):
      if usr[j] == ')':
        matched = True
        break
      elif j+1 == len(usr) and matched == True:
        status = "Balanced"
  
  count += 1 


  # Not Completed