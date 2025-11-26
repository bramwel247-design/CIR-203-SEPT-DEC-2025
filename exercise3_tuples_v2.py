patient_info = ("Jane Doe", 40, 118, 78)
print("Patient record:", patient_info)

print("\nPatient age:", patient_info[1])
print("Heart rate:", patient_info[3])

print("\nTuples help keep records unchanged because they cannot be modified directly.")

editable = list(patient_info)
editable[3] = 82
patient_info = tuple(editable)
print("\nRecord after updating heart rate:", patient_info)

group = (
    ("Jane Doe", 40, 118, 78),
    ("Sam Kari", 33, 112, 74),
    ("Omar Ali", 55, 135, 80),
    ("Grace W.", 29, 115, 71),
    ("Victor K.", 47, 128, 79)
)

all_names = [person[0] for person in group]
print("\nNames of all patients:", all_names)
