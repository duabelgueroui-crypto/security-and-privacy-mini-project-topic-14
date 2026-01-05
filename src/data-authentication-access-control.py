from pymongo import MongoClient

def test_user(username, password):
    print(f"\n--- Testing {username} ---")

    try:
        client = MongoClient(
            f"mongodb+srv://{username}:{password}@cluster0.fj7wjzc.mongodb.net/clinic_db?retryWrites=true&w=majority"
        )

        db = client["clinic_db"]
        patients = db["patients"]

        print("Reading patients:")
        for p in patients.find():
            print(p["name"])

        print("Trying to insert...")
        patients.insert_one({"patient_id": "P999", "name": "Hacker"})

        print("Insert SUCCESS")

    except Exception as e:
        print("Blocked:", e)

# Replace with your real passwords
test_user("admin1", "admin12025")
test_user("doctor1", "doctor12025")
test_user("nurse1", "nurse12025")
