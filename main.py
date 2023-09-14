def leapyear(year):
  if (year % 4 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a year : "))
if leapyear(year):
  print("%d is leap year" % (year))
else:
  print("%d is not leap year" % (year))
