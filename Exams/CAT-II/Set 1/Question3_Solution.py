Patients = [
    ("P101",70,98,36.8),
    ("P102",105,94,37.5),
    ("P103",72,97,36.6),
    ("P104",115,91,38.2),
    ("P105",88,96,37.0),
]

# ---------(a)---------
# Algorithm:
'''
-> We will traverse through the list and check whether either condition is satisfied
-> If either condition is satisfied, we will print the Patient ID of that Patient
'''
# Program Start: 
for patient in Patients:
    if patient[1] > 100 or patient[2] < 95:
        print(patient[0])

# ---------(b)---------
# Algorithm:
'''
-> We will create an empty list named "High_Fever_Patients"
-> Then, we will traverse through the list and check whether a patient's body temperature is higher than 37.5C or not
-> If a patient's body temperature is higher than 37.5C, we will append the patient ID of that patient to High_Fever_Patients
'''
# Program Start:
High_Fever_Patients = []
for patient in Patients: 
    if patient[3] > (37.5):
        High_Fever_Patients.append(patient[0])

print(High_Fever_Patients)

# ---------(c)---------
# Algorithm:
'''
-> We will assign the Oxygen level of the first patient as the Lowest_O2
-> Then, we will traverse through the list and constantly compare every patient's O2 level with Lowest_O2, assigning the new value to it if comparison is true
-> Then, we will make a new list named "Lowest_O2_Patients"
-> Then, we will traverse through the Patients list to check if a patient's O2 level is same as Lowest_O2 and append the patient ID to Lowest_O2_Patients
'''
# Program Start: 
Lowest_O2 = Patients[0][2]

for patient in Patients:
    if patient[2] < Lowest_O2:
        Lowest_O2 = patient[2]

Lowest_O2_Patients = []

for patient in Patients:
    if patient[2] == Lowest_O2:
        Lowest_O2_Patients.append(patient[0])

print(Lowest_O2_Patients)

# Test Cases: 
'''
Upon running the program with the given inputs, the output will be:
(a):
-> P102
-> P104 
(b):
-> ['P104']
(c):
-> ['P104']
'''
