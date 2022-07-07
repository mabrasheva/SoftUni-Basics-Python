days = int(input())
doctors = 7
treated_patients_per_day = 0
untreated_patients_per_day = 0
treated_patients_all_days = 0
untreated_patients_all_days = 0

for day in range(1, days + 1):
    if (day % 3 == 0) and (untreated_patients_all_days > treated_patients_all_days):
        doctors += 1
    patients = int(input())
    if patients <= doctors:
        treated_patients_per_day = patients
        treated_patients_all_days += treated_patients_per_day
    else:
        treated_patients_per_day = doctors
        treated_patients_all_days += treated_patients_per_day
        untreated_patients_per_day = patients - doctors
        untreated_patients_all_days += untreated_patients_per_day

print(f"Treated patients: {treated_patients_all_days}.")
print(f"Untreated patients: {untreated_patients_all_days}.")
