task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if time_bound == "yes":
    match priority:
        case "high":
            Reminder = "a high priority task that requires immediate attention today!"
        case "medium":
            Reminder = "a high priority task that requires intermidate attention"
        case "low":
            Reminder = "a low priority task. Consider completing it when you have free time."
else:
        
        Reminder = "is a low priority task. Consider completing it when you have free time."

print(f"Note: \'{task}\' is {Reminder}")