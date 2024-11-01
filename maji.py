"""
This project has been done by 

150216 - Albert Oruma
167071 - Collins Gitonga
161061 - Nicole Muraguri

"""
from abc import ABC, abstractmethod

# Abstract Base Class
class Person(ABC):
    def __init__(self, name, age, id_number):
        self._name = name  # Encapsulated attributes
        self._age = age
        self._id_number = id_number
    
    @abstractmethod
    def get_role(self):
        pass

class Doctor(Person):
    def __init__(self, name, age, id_number, specialization):
        super().__init__(name, age, id_number)
        self.specialization = specialization
        self.appointments = []
    
    def get_role(self):
        return "Doctor"
    
    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        print(f"Appointment added for Dr. {self._name} with {appointment.patient._name} at {appointment.time}.")

    def view_appointments(self):
        print(f"\nAppointments for Dr. {self._name}:")
        if not self.appointments:
            print("No appointments scheduled.")
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient._name}, Time: {appointment.time}")

class Patient(Person):
    def __init__(self, name, age, id_number, medical_history=None):
        super().__init__(name, age, id_number)
        self.__medical_history = medical_history  # Private attribute
    
    def get_role(self):
        return "Patient"
    
    def book_appointment(self, doctor, time):
        appointment = Appointment(self, doctor, time)
        doctor.add_appointment(appointment)
        print(f"Appointment booked for {self._name} with Dr. {doctor._name} at {time}.")

    def get_medical_history(self):
        return self.__medical_history
    
    def update_medical_history(self, new_history):
        self.__medical_history = new_history

class Appointment:
    def __init__(self, patient, doctor, time):
        self.patient = patient
        self.doctor = doctor
        self.time = time

class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def show_doctors(self):
        print("\nDoctors in the hospital:")
        for doctor in self.doctors:
            print(f"- Dr. {doctor._name}, Specialization: {doctor.specialization}")
    
    def show_patients(self):
        print("\nPatients in the hospital:")
        for patient in self.patients:
            print(f"- {patient._name}, Age: {patient._age}")

# Initializing the hospital
hospital = Hospital()

# User Interface
def hospital_interface():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Show all doctors")
        print("2. Show all patients")
        print("3. Register a new doctor")
        print("4. Register a new patient")
        print("5. Book an appointment")
        print("6. View Doctor's appointments")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")

        if choice == '1':
            hospital.show_doctors()
        
        elif choice == '2':
            hospital.show_patients()
        
        elif choice == '3':
            name = input("Enter doctor's name: ")
            age = int(input("Enter doctor's age: "))
            id_number = input("Enter doctor's ID number: ")
            specialization = input("Enter doctor's specialization: ")
            doctor = Doctor(name, age, id_number, specialization)
            hospital.add_doctor(doctor)
            print(f"Doctor {name} has been registered successfully.")
        
        elif choice == '4':
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            id_number = input("Enter patient's ID number: ")
            medical_history = input("Enter patient's medical history (optional): ")
            patient = Patient(name, age, id_number, medical_history)
            hospital.add_patient(patient)
            print(f"Patient {name} has been registered successfully.")
        
        elif choice == '5':
            patient_name = input("Enter patient name for appointment: ")
            patient = next((p for p in hospital.patients if p._name == patient_name), None)
            if patient:
                doctor_name = input("Enter doctor's name for the appointment: ")
                doctor = next((d for d in hospital.doctors if d._name == doctor_name), None)
                if doctor:
                    time = input("Enter appointment time (e.g., '2:00 PM'): ")
                    patient.book_appointment(doctor, time)
                else:
                    print("Doctor not found.")
            else:
                print("Patient not found.")
        
        elif choice == '6':
            doctor_name = input("Enter doctor's name to view appointments: ")
            doctor = next((d for d in hospital.doctors if d._name == doctor_name), None)
            if doctor:
                doctor.view_appointments()
            else:
                print("Doctor not found.")
        
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Start the hospital interface
hospital_interface()

"""
SUMMARY OF THE HOSPITAL MANAGEMENT SYSTEM:
The Hospital Management System allows users to manage doctors, patients, and appointments in a hospital setting.
 The system provides the following functionalities:

1. Show Doctors and Patients: Displays lists of available doctors and patients.
2. Book an Appointment: Allows users to book an appointment by selecting a doctor, patient, and appointment time.
3. View Doctors Appointments: Lists all appointments scheduled with a specified doctor.
4. Register a New Doctor: Users can add a new doctor by providing their name, age, ID number, and specialization.
5. Register a New Patient: Users can add a new patient with their name, age, ID number, and medical history.
6. Exit Option: Ends the program.

Key Concepts Used
Encapsulation: Certain attributes (e.g., _name, _age, and __medical_history) are encapsulated for controlled access.
Inheritance: Doctor and Patient inherit from the Person abstract base class.
Polymorphism: get_role method is used in both Doctor and Patient with distinct implementations.
Abstraction: Person class is an abstract class that ensures all subclasses define a get_role method.
"""