task = print(input("Enter your task: "))
priority = print(input("Priority (high/medium/low): "))
time_bound = print(input("Is it time-bound? (yes/no): "))
value = "high"
match value:
    case "high":
        print("high priority")
    case "medium":
        print("medium priority")
    case "low":
        print("low priority")
    if time_bound == "yes":
        print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
