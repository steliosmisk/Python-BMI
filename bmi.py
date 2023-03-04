def bmi(weight, height):
        bmi = weight / (height/100)**2
        if bmi <= 18.5:  
            print("You are underweight.")  
        elif bmi <= 24.9:  
            print("You are healthy.")  
        elif bmi <= 29.9:  
            print("You are over weight.")  
        else:  
            print("You are obese.")  
        return bmi

print("--Welcome to BMI Calculator--")
print("[1] Start")
print("[2] Exit")

user_choice = int(input("Enter (1/2): "))
while user_choice == 1:
    try:
        weight = int(input("[Kg] Enter your weight: "))
        height = int(input("[Cm]Enter your height: "))
        print("BMI Results:", bmi(weight, height))
        break
    except:
        print("Enter a valid value!")
