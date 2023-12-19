
def patient_info(name, age, new_patient=True):
    print(f"We checked in a patient named {name}")
    print(f"He is {age} years old")

    if new_patient:
        print("He is a new patient")
    else:
        print("He is a returning patient")

patient_info("John Smith", 20, new_patient=True)
