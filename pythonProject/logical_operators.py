has_high_income = True
has_good_credit = True
has_criminal_rec = True

if has_high_income and has_good_credit:
    print ("Eligible for loan")

if has_high_income or has_good_credit:
    print ("Eligible for loan")

if has_good_credit and not has_criminal_rec:
    print ("Eligible for loan")


