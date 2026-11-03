employees = {
    "E1": (True, 3),
    "E2": (False, 4),
    "E3": (True, 1),
    "E4": (True, 5)
}

def eligible(training, experience):
    return training and experience >= 2

print("EMPLOYEE ELIGIBILITY")
print("--------------------")

for emp, details in employees.items():

    training, experience = details

    result = eligible(training, experience)

    print(emp, ":", "Eligible" if result
          else "Not Eligible")
