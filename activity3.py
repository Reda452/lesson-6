heaght=float(input("enter your heaght"))
weight=float(input("enter your weight"))
bmi=weight / (heaght/100)**2
print("bmi is ",bmi)
if bmi<=18.4:
    print("your are under weight")
elif bmi<=24.9:
    print ("your are healthy")
elif bmi<=29.9:
    print ("your are overweight")
elif bmi<=34.9:
    print ("your are severely overweight")
else:
    print ("you are obese")