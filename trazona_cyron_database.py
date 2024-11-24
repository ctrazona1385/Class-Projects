'''
This is my code for Homework 2

Author:Cyron Trazona
Due Date: 11/15/23

DSCI 1301 Section 2

'''

patient_info = {}

medication_info = {}

try:
    def add_patient():
        while True:
            new_patient = {}
            mrn = int(input('Please enter the patient\'s MRN number: \n'))
            new_patient['Name']= input('What is the name of the patient? \n')
            new_patient['Birthday']= int(input('What is the patient\'s date of birth? (In DDMMYYYY format)\n'))
            new_patient['Height'] = int(input('Please enter the patient\'s height in inches:\n' ))
            if new_patient['Height'] < 0:
                raise ValueError('Invalid height')
            new_patient['Weight'] = float(input('Please enter the patient\'s weight in kilograms: \n'))
            if new_patient['Weight'] < 0:
                raise ValueError('Invalid weight')
            new_patient['Allergies'] = input('Please list any patient allergies. If non type NA: \n')
            patient_info[mrn] = new_patient
            break


    def add_med():
        while True:
            new_med = {}
            ndc = int(input('Please enter the 11 digit NDC (no dashes and include all leading 0s): \n'))
            new_med['Name'] = input('What is the name of the drug? \n')
            new_med['Strength'] = input('What is the strength of the medication? \n')
            new_med['Class'] = input('Please indicate the class of the drug(c2-4, non-control,chemo, etc.): \n')
            new_med['Administration'] = input('How is the medicine administered? (IM,SQ,Orally,Topically, Etc.) \n')
            new_med['Cost'] = float(input('Please enter the cost per administration: \n'))
            medication_info[ndc] = new_med
            break

    def del_patient():
        mrn = int(input('Please enter the MRN of the patient you would like to delete: \n'))
        if mrn not in patient_info:
            mrn = int(input('MRN not found please re-enter: \n'))
        del patient_info[mrn]

    def del_med():
        ndc = int(input('Please enter the 11 digit NDC of the drug you would like to delete: \n'))
        if ndc not in medication_info:
            ndc = int(input('NDC not found please re-enter: \n'))
        del medication_info[ndc]

    def print_patient():
        while True:
            all_or1pt = input('Would you like to view all patient records? Y or N \n')
            if all_or1pt == 'Y' or all_or1pt == 'y':
                print(patient_info)
                break
            elif all_or1pt == 'N' or all_or1pt == 'n':
                pat_print = int(input('Please enter the MRN of the patient you would like to view: \n'))
                if pat_print not in patient_info:
                    pat_print = int(input('MRN not found please re-enter: \n'))
                print(patient_info[pat_print])
                break

    def print_med():
        while True:
            all_or1med = input('Would you like to view all the medicines in current inventory? Y or N: \n')
            if all_or1med == 'Y' or all_or1med == 'n':
                print(medication_info)
                break
            elif all_or1med == 'N' or all_or1med == 'n':
                med_print = int(input('Please enter the NDC of the medication you would like to view: \n'))
                if med_print not in patient_info:
                    med_print = int(input('MRN not found please re-enter: \n'))
                print(medication_info[med_print])
                break
            else:  
                print('Invalid option. \n')


    def update_patient():
        ptupd = int(input('Please enter the MRN of the patient who\'s profile you\'d like to update: \n'))
        if ptupd not in patient_info:
                ptupd = int(input('MRN not found please re-enter: \n'))
        updinfo = input('Please select which patient would you like to update? Name, Birthday, Height, Weight, or Allergies \n')
        if updinfo not in patient_info[ptupd]:
                updinfo = input('Invalid selection please try again: \n')
        while True:
            if ptupd in patient_info:
                patient_info[ptupd][updinfo] = input('Would you like to update it to?: \n')
                break
            else:
                print('There are no patients with that MRN. Please try again: \n')
                ptupd = int(input('Please enter the MRN of the patient who\'s profile you\'d like to update: \n'))

    def update_med():
        medupd = int(input('Please enter the NDC of the medication you\'d like to update: \n'))
        if medupd not in medication_info:
            medupd = int(input('MRN not found please re-enter: \n'))
        updmedinfo = input('Please select which medicine would you like to update? Name, Strength, Class, Administration, Cost \n')
        if updmedinfo not in medication_info[medupd]:
            updmedinfo = input('Invalid selection please try again: \n')
        while True:
            if medupd in medication_info:
                medication_info[medupd][updmedinfo] = input('Would you like to update it to?: \n')
                break
            else:
                print('There are no medications with that NDC. Please try again: \n')
                medupd = int(input('Please enter the NDC of the medication you\'d like to update: \n'))
except ValueError as excpt:
    print(excpt)
    command = input('Please make a selection: \n')




while True:
    command = input('Please make a selection: \n')
    if command == 'view patient' or command == 'vp':
        print_patient()
    elif command == 'add patient' or command == 'ap':
        add_patient()
    elif command == 'delete patient' or command == 'dp':
        del_patient()
    elif command == 'update patient' or command == 'up':
        update_patient()
    elif command == 'view med' or command == 'vm':
        print_med()
    elif command == 'add med' or command == 'am':
        add_med()
    elif command == 'delete med' or command == 'dm':
        del_med()
    elif command == 'update med' or command == 'um':
        update_med()
    elif command == 'quit' or command == 'q':
        print('Closing Records')
        break




