# These are floats in a form of  a string variable 
temp1 = "72.5"
temp2 = "75.0"
temp3 = "68.5"
temp4 = "70.0"
temp5 = "71.5"
temp6 = "69.0"
temp7 = "74.0"

#Converting the strings into main floats.
temperatures = [float(temp1), float(temp2), float(temp3), float(temp4), float(temp5), float(temp6), float(temp7)]

average = sum(temperatures) / len(temperatures)
                                 
print(f"Average Temperature: {average:.3f}°F")                                 

