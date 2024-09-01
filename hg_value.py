gender = input("Enter your biological gender (male/female): ")
hg_value = float(input("Now enter your hemoglobin value in g/l: "))

if gender == "female":
    if hg_value < 117:
        print("your hemoglobin value is low.")
    elif hg_value > 155:
        print("your hemoglobin value is high.")
    else:
        print("your hemoglobin value is normal.")
if gender == "male":
    if hg_value < 134:
        print("your hemoglobin value is low.")
    elif hg_value > 167:
        print("your hemoglobin value is high.")
    else:
        print("your hemoglobin value is normal.")