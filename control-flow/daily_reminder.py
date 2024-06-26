task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if time_bound == "yes":
    match priority:
        case "high":
            message = "a high priority task that requires immediate attention today!"
        case "medium":
            message = "a high priority task that requires intermidate attention"
        case "low":
            message = "a low priority task. Consider completing it when you have free time."
else:
    message = "is a low priority task. Consider completing it when you have free time."

print(f"{task} is {message}")
