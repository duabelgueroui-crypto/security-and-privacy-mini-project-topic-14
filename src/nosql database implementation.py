from mdb import patients_collection, appointments_collection, tests_collection

patients = [
    {"patient_id": "P001", "name": "Sara B.", "age": 25, "gender": "Female", "phone": "0662457890", "disease": "Flu"},
    {"patient_id": "P002", "name": "Ali H.", "age": 40, "gender": "Male", "phone": "0663123456", "disease": "Diabetes"},
    {"patient_id": "P003", "name": "Nadia K.", "age": 33, "gender": "Female", "phone": "0662987654", "disease": "Hypertension"}
]

for patient in patients:
    if not patients_collection.find_one({"patient_id": patient["patient_id"]}):
        patients_collection.insert_one(patient)

appointments = [
    {"appointment_id": "A100", "patient_id": "P001", "date": "2025-01-10", "time": "10:30", "status": "scheduled"},
    {"appointment_id": "A101", "patient_id": "P002", "date": "2025-01-11", "time": "11:00", "status": "done"},
    {"appointment_id": "A102", "patient_id": "P003", "date": "2025-01-12", "time": "09:45", "status": "scheduled"}
]

for app in appointments:
    if not appointments_collection.find_one({"appointment_id": app["appointment_id"]}):
        appointments_collection.insert_one(app)

tests = [
    {"test_id": "T10", "patient_id": "P001", "test_type": "Blood Test", "result": "Normal", "date": "2025-01-11"},
    {"test_id": "T11", "patient_id": "P002", "test_type": "X-Ray", "result": "Normal", "date": "2025-01-12"},
    {"test_id": "T12", "patient_id": "P003", "test_type": "ECG", "result": "Abnormal", "date": "2025-01-13"}
]

for test in tests:
    if not tests_collection.find_one({"test_id": test["test_id"]}):
        tests_collection.insert_one(test)

print("Initial data inserted successfully!")
