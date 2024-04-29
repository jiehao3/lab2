def calculate_bmi(height, weight):   
     
    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 
    bmi = (weight/(height**2))
    print ("BMI is " + str(bmi))
    if (bmi<18.5):
        print("Underweight")
        return -1
    elif (bmi<=25.0 and bmi>=18.5):
        print("Normal Weight")
        return 0
    else:
        print("Overweight")
        return 1

 
x = calculate_bmi(weight=57, height=1.73)    
print (x)