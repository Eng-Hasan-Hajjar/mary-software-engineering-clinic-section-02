appointments = []

def add_appointment():
    patient_name = input("Patient name: ").strip()
    doctor_name = input("Doctor name: ").strip()
    date = input("Appointment date: ").strip()

    appointment = {
        "patient": patient_name,
        "doctor": doctor_name,
        "date": date
    }

    appointments.append(appointment)
    print("Appointment added successfully.")

def view_appointments():
    if not appointments:
        print("No appointments found.")
        return

    for index, appointment in enumerate(appointments, start=1):
        print(
            f"{index}. {appointment['patient']} -> "
            f"{appointment['doctor']} | {appointment['date']}"
        )


add_appointment()

view_appointments()
