#ale we couldn't figure out how to make a co-op github repository but we shared the codes via replit and then pasted them here
#atte: Abril and Val

counter = 0
sales_commission = 0

base_salary = float(input("hello!!! wwhat is the base salary for your salespeople?     ."))
print(".")
salespeople = float(input("ok, now; how many salespeople do we need to calculate the income of?     ."))


while counter < salespeople:
  counter += 1
  name = str(input("what is your name? :)     ."))
  print(".")
  commission = float(input(f"i understand that the average of monthly sales in your area ranges from 3500 to 7000. It's ok if you sold less than that or more than that or in between. How many sales did you do, {name}?     ."))
  print(".")
  if commission < 3500:
    sales_commission += float(commission)*0.07
  elif commission > 3500 and (commission < 7000):
    sales_commission += float(commission)*0.10
  elif commission > 7000:
    sales_commission += float(commission)*0.15
  total_salary = float(base_salary)+float(sales_commission)
  print(f"ok, {name}!! your total salary is {total_salary}")
  other = str(input("is there another seller waiting for their calculations?? yes/no     .")).lower()
  if other == "no":
    print(".")
    break

print("thank you, that was all :)")
