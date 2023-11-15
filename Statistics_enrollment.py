counter = 0

between2and4 = 0
between5and9 = 0
olderorequalto10 = 0

animals = float(input("hello!! how many animals do we have to register for today?"))

while counter < animals:
  counter += 1
  age = float(input("what age is this animal?     ."))
  print(".")
  if age >= 2 and (age < 5):
    between2and4 += 1
  elif age >= 5 and (age < 10):
    between5and9 += 1
  elif age >= 10:
    olderorequalto10 += 1
  other = str(input("is there any other animal waiting to be recorded? yes/no     ."))
  if other == "no":
    break

percentage1 =  (float(between2and4)*100)/float(counter)
percentage2 =  (float(between5and9)*100)/float(counter)
percentage3 =  (float(olderorequalto10)*100)/float(counter)

print(".")
print(f"the total number of animals is {counter}, there are {between2and4} between 2 and less than 5 years, a {percentage1}%. {between5and9} that are between 5 and less than 10 years, a {percentage2}%, and {olderorequalto10} that are 10 years or older, a {percentage3}% :)")
