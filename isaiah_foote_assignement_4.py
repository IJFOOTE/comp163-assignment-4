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
