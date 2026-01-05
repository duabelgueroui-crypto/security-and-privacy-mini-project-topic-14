import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# رابط الاتصال مخزن في Environment Variable
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise Exception("MONGO_URI غير موجود")

client = MongoClient(MONGO_URI)
db = client["clinic_db"]

patients = db["patients"]
appointments = db["appointments"]
tests = db["tests"]

print("Secure connection to clinic_db established")
def sanitize_string(value):
    if not isinstance(value, str):
        raise ValueError("نوع المدخل غير مسموح")

    forbidden = ["$", "{", "}", "[", "]"]
    for char in forbidden:
        if char in value:
            raise ValueError("مدخل يحتوي على رموز غير مسموحة")

    return value.strip()
def add_patient(name, age, gender):
    name = sanitize_string(name)
    gender = sanitize_string(gender)

    if not isinstance(age, int) or age <= 0:
        raise ValueError("العمر غير صحيح")

    patient = {
        "name": name,
        "age": age,
        "gender": gender
    }

    patients.insert_one(patient)
    return "Patient added securely"
def get_patient_by_name(name):
    name = sanitize_string(name)

    return patients.find_one(
        {"name": name},
        {"_id": 1, "name": 1, "age": 1, "gender": 1}
    )
def add_appointment(patient_id, date, reason):
    if not ObjectId.is_valid(patient_id):
        raise ValueError("Patient ID غير صالح")

    date = sanitize_string(date)
    reason = sanitize_string(reason)

    appointment = {
        "patient_id": ObjectId(patient_id),
        "date": date,
        "reason": reason
    }

    appointments.insert_one(appointment)
    return "Appointment added securely"
def add_test(patient_id, test_name, result):
    if not ObjectId.is_valid(patient_id):
        raise ValueError("Patient ID غير صالح")

    test_name = sanitize_string(test_name)
    result = sanitize_string(result)

    test = {
        "patient_id": ObjectId(patient_id),
        "test_name": test_name,
        "result": result
    }

    tests.insert_one(test)
    return "Test added securely"
def delete_patient(patient_id):
    if not ObjectId.is_valid(patient_id):
        raise ValueError("ID غير صالح")

    patients.delete_one({"_id": ObjectId(patient_id)})
    appointments.delete_many({"patient_id": ObjectId(patient_id)})
    tests.delete_many({"patient_id": ObjectId(patient_id)})

    return "Patient and related data deleted securely"
try:
    msg = add_patient("Yasmine", 20, "Female")
    print(msg)

    patient = get_patient_by_name("Yasmine")
    print(patient)

except Exception:
    print("حدث خطأ أثناء العملية")

