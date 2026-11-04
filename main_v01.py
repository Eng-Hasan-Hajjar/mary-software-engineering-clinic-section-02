patients = []
appointments = []

def add_patient():
    name = input("Patient name: ").strip()
    phone = input("Phone number: ").strip()

    if not name:
        print("Patient name is required.")
        return

    patients.append({"name": name, "phone": phone})
    print("Patient added successfully.")


def view_patients():
    if not patients:
        print("No patients found.")
        return

    print("\nPatients:")
    for index, patient in enumerate(patients, start=1):
        print(f"{index}. {patient['name']} - {patient['phone']}")

def add_appointment():
    patient_name = input("Patient name: ").strip()
    doctor_name = input("Doctor name: ").strip()
    date = input("Appointment date: ").strip()

    appointments.append({
        "patient": patient_name,
        "doctor": doctor_name,
        "date": date
    })
    print("Appointment added successfully.")

def view_appointments():
    if not appointments:
        print("No appointments found.")
        return
    print("\nAppointments:")
    for index, appointment in enumerate(appointments, start=1):
        print(
            f"{index}. {appointment['patient']} -> "
            f"{appointment['doctor']} | {appointment['date']}"
        )

def show_menu():
    print("\n=== Clinic Management System ===")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Add Appointment")
    print("4. View Appointments")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()


        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            add_appointment()
        elif choice == "4":
            view_appointments()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
