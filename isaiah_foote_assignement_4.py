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
Medium_classes = ["English","History","Programming","chemistry",]
all_classes = ["English","History","biology","geography","Programming","Calculus","chemistry",]

if choice == "A" or "B":
    Easy_Class_selection = Easy_Classes + Medium_classes
    print(Easy_Class_selection)
elif choice == "B" or C:
    Medium_Class_selection = Easy_Classes + Medium_classes + Hard_classes
    print(Medium_Class_selection)
elif choice == "C":
    Hard_Class_selection = Medium_classes + Hard_classes
    print(Hard_Class_selection)

classes = input("pick your classes")
if classes in all_classes:
    print("you picked avalible courses")

if classes not in all_classes:
    print("that course is not avalible")

final_choice = None
final_stats = study_hours, social_points, stress_level, current_gpa

if final_choice is None:
    final_choice = "Burnout Risk"
if choice is not None and classes in all_classes:
    if social_points > 40 and stress_level < 10:
        final_choice = "Social Butterfly Scholar"
        
elif study_hours > 15 and stress_level < 40:
        final_choice = "Dedicated Student"

elif study_hours > 15 and stress_level > 40:
        final_choice = "Extremely Hard Working Student"

elif final_choice is not None:
    print(f"Final Outcome: {final_choice}")
else:
    print("Final Outcome: Undetermined (Probably due to invalid initial choice).")

print(f"Final Stats (Study Hours, Social Points, Stress Level, GPA): {final_stats}")
