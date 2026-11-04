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








def view_patients():
    if not patients:
        print("No patients found.")
        return

    print("\nPatients:")
    for index, patient in enumerate(patients, start=1):
        print(f"{index}. {patient['name']} - {patient['phone']}")



add_patient()
view_patients()