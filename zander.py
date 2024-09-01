zander_length = float(input("Enter the Zander's length in cm: "))

size_limit = 42

if zander_length < size_limit:
    difference = size_limit - zander_length
    print(f"The zander size is {difference} below the limit. Release it back into the lake")
else:
    print("The Zander meets the limit. You can keep it")



