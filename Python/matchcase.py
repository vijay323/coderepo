# day=input("Enter a day: ").strip()

# match day:
#     case "Monday":
#         print("1")
#     case "Tuesday":
#         print("2")
#     case "Wednesday":
#         print("3")
#     case "Thursday":
#         print("4")
#     case _:
#         print("Enter valid day")


Month=input("Enter the month: ").strip().capitalize()

match Month:
    case "December"|"January"|"February":
        print("Winter")
    case "March"|"April"|"May":
        print("Spring")
    case "June"|"July"|"August":
        print("Summer")
    case "September"|"October"|"November":
        print("Autumn")
    case _:
        print("Invalid Month")