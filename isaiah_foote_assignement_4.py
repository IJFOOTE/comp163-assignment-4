student_name = "Isaiah"
current_gpa = 3.9
study_hours = 3
social_points = 24
stress_level = 100
print(f"welcome this is your starting stats{student_name, current_gpa,study_hours,social_points,stress_level}")

print("Choose your course load:")
print("A) Light (12 credits)")  
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa >= 3.0:
        study_hours = study_hours - 4 
        stress_level = stress_level - 20
    elif (current_gpa < 3.0) and (current_gpa > 2.5):
        study_hours = study_hours - 2
        stress_level = stress_level - 10
    elif current_gpa < 2.4:
        print("Harder path recommended")


elif choice == "B":
    if current_gpa >= 3.0:
        study_hours = study_hours - 2 
        stress_level = stress_level - 15
    elif (current_gpa < 3.0) and (current_gpa > 2.5):
        study_hours = study_hours - 1
        stress_level = stress_level - 5
    elif current_gpa < 2.4:
        study_hours = study_hours + 1
        stress_level = stress_level - 2
       

elif choice == "C":
    if current_gpa >= 3.0:
        study_hours = study_hours - 0  
        stress_level = stress_level - 0
    elif (current_gpa < 3.0) and (current_gpa > 2.5):
        study_hours = study_hours + 2
        stress_level = stress_level + 5
    elif current_gpa < 2.4:
        study_hours = study_hours + 4
        stress_level = stress_level + 10

else:
    print("invalid choice")

Easy_Classes = ["English","History","biology","geography"]
Hard_classes = ["Programming","Calculus","chemistry",]
all_classes = ["English","History","biology","geography","Programming","Calculus","chemistry",]

if choice == "A":
    choosen_class_1 = random.choice(all_classes)
    if choosen_class_1 in Easy_Classes:
        class_1 = True
    elif choosen_class_1 not in Easy_Classes:
        class_1 = False 

    choosen_class_2 = random.choice(all_classes)
    if choosen_class_2 in Easy_Classes:
        class_2 = True
    elif choosen_class_2 not in Easy_Classes:
        class_2 = False 

    choosen_class_3 = random.choice(all_classes)
    if choosen_class_3 in Easy_Classes:
        class_3 = True
    elif choosen_class_3 not in Easy_Classes:
        class_3 = False 
    
    choosen_class_4 = random.choice(all_classes)
    if choosen_class_4 in Easy_Classes:
        class_4 = True
    elif choosen_class_4 not in Easy_Classes:
        class_4 = False 
    
    if class_1 == True and class_2 == True and class_3 == True and class_4 == True:
        print("This is the easy course")
    elif class_1 == False or class_2 == False or class_3 == False or class_4 == False:
        print("pick again")
        
elif choice == "B":
    choosen_class_1 = random.choice(all_classes)
    if choosen_class_1 in Hard_Classes:
        class_1 = True
    elif choosen_class_1 not in Hard_Classes:
        class_1 = False 

    choosen_class_2 = random.choice(all_classes)
    if choosen_class_2 in Hard_Classes:
        class_2 = True
    elif choosen_class_2 not in Hard_Classes:
        class_2 = False 

    choosen_class_3 = random.choice(all_classes)
    if choosen_class_3 in Easy_Classes:
        class_3 = True
    elif choosen_class_3 not in Easy_Classes:
        class_3 = False 
    
    choosen_class_4 = random.choice(all_classes)
    if choosen_class_4 in Easy_Classes:
        class_4 = True
    elif choosen_class_4 not in Easy_Classes:
        class_4 = False 
    
    if class_1 == True and class_2 == True and class_3 == True and class_4 == True:
        print("this is the Medium course try your best")
    elif class_1 == False or class_2 == False or class_3 == False or class_4 == False:
        print("pick again")

elif choice == "C":


    choosen_class_1 = random.choice(all_classes)
    if choosen_class_1 in Hard_Classes:
        class_1 = True
    elif choosen_class_1 not in Hard_Classes:
        class_1 = False 

    choosen_class_2 = random.choice(all_classes)
    if choosen_class_2 in Hard_Classes:
        class_2 = True
    elif choosen_class_2 not in Hard_Classes:
        class_2 = False 

    choosen_class_3 = random.choice(all_classes)
    if choosen_class_3 in Hard_Classes:
        class_3 = True
    elif choosen_class_3 not in Easy_Classes:
        class_3 = False 
    
    choosen_class_4 = random.choice(all_classes)
    if choosen_class_4 in Hard_Classes:
        class_4 = True
    elif choosen_class_4 not in Easy_Classes:
        class_4 = False 
    
    if class_1 == True and class_2 == True and class_3 == True and class_4 == True:
        print("This is the hard course good luck")
    elif class_1 == False or class_2 == False or class_3 == False or class_4 == False:
        print("pick again")
