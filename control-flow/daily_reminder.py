task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if time_bound == "yes":
    match priority:
        case "high":
            reminder = "a high priority task that requires immediate attention today!"
        case "medium":
            reminder = "a high priority task that requires intermidate attention"
        case "low":
            reminder = "a low priority task. Consider completing it when you have free time."
else:
        
        reminder = "is a low priority task. Consider completing it when you have free time."

note= f"Note: \'{task}\' is {reminder}"
print(note)

