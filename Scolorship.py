age = int(input())
year = int(input())
income = int(input())
arrear = int(input())
score = float(input())
attendance = float(input())

if (age >= 18 and age < 21) and (year >= 2021) and (score >= 60.0) and (attendance >= 80.0):
    if (arrear <= 2) and (income <= 200000):
        print("Eligible")
    elif (arrear > 2) and (income <= 200000):
        if (score >= 80.0) and (attendance >= 90.0):
            print("Partially Eligible")
        else:
            print("Not Eligible")
    elif (arrear > 2) and (200000 < income < 250000):
        if (score >= 80.0) and (attendance >= 90.0):
            print("Partially Eligible")
        else:
            print("Not Eligible")
    elif (arrear <= 2) and (200000 < income < 250000):
        if (score >= 80.0) and (attendance >= 90.0):
            print("Partially Eligible")
        else:
            print("Not Eligible")
    else:
            print("Not Eligible")
else:
    print("Not Eligible")
