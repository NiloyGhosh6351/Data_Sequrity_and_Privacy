import random
from faker import Faker

fake = Faker()

# Adjusting the generation of fake data with weight between 30 to 100 and height between 130 cm to 190 cm


def generate_final_patient_data(num_entries):
    common_diseases = [
        "Hypertension",
        "Diabetes",
        "Asthma",
        "Coronary heart disease",
        "Epilepsy",
        "Influenza",
        "Chickenpox",
        "Measles",
        "Mumps",
        "Common cold",
        "COVID-19",
        "Bronchitis",
        "Strep throat",
        "Tuberculosis"
    ]

    patients = []
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        # True for Male, False for Female
        gender = random.choice(['Male', 'Female'])
        age = random.randint(20, 90)
        weight = round(random.uniform(30.0, 100.0), 2)
        height = round(random.uniform(130.0, 190.0), 2)
        health_history = random.choice(common_diseases)
        patients.append((first_name, last_name, gender, age,
                        weight, height, health_history))
    return patients


def generate_sql_inserts(patient_data):
    sql_inserts = []
    for idx, patient in enumerate(patient_data, start=1):
        first_name, last_name, gender, age, weight, height, health_history = patient
        sql_insert = f"INSERT INTO patient_patient (id, first_name, last_name, gender, age, weight, height, health_history) VALUES ({idx}, '{first_name}', '{last_name}', '{gender}', {age}, {weight}, {height}, '{health_history}');"
        sql_inserts.append(sql_insert)
    return sql_inserts


# Generate 100 entries with final data adjustments
final_patient_data = generate_final_patient_data(100)

# Generate SQL INSERT statements
sql_inserts = generate_sql_inserts(final_patient_data)

# Write the SQL statements to a file
with open('patient_data.sql', 'w') as sql_file:
    for sql_insert in sql_inserts:
        sql_file.write(sql_insert + '\n')

print("SQL file 'patient_data.sql' generated successfully.")
