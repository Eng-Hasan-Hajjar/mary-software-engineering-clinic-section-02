patients = []
def add_patient():
    name = input("Patient name: ").strip()
    phone = input("Phone number: ").strip()
    if not name:
        print("Patient name is required.")
        return

    patient = {
        "name": name,
        "phone": phone
    }

    patients.append(patient)
    print("Patient added successfully.")


