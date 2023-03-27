# Name: Brooks Johnson
# Prog Purpose: This program computes college tuition & fees based on number of credits
# BVCC Fee Rates are from: RTTps://www.pvce.edu/Tuition-and-fees
# NOTE: All fees are PER CREDIT
# In-state tuition: $155, Out-of-state tuition: $331.60
# Capital fee: $23.50 (out-of-state students only)
# Institution fee: $1.75
# Activity fee: $2.50

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 155
RATE_TUITION_OUT = 331.60
RATE_CAPITAL = 23.5
RATE_INSTITUTION = 1.75
RATE_ACTIVITY = 2.90

#define global variables

inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0

scholarshipamt = 0

tuitionfees = 0

capitalfees = 0

institutionfees = 0

activityfees = 0

totalowed = 0

balance = 0

########## define program functions ##########
def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() != "Y":
            another_student = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input ("Scholarship amount received: "))

def perform_calculations():
    global tuitionfees, capitalfees, institutionfees, activityfees1, totalowed, balance

    if inout == 1:
        tuitionfees = numcredits * RATE_TUITION_IN
        capitalfees = 0

    else:
        tuitionfees = numcredits * RATE_TUITION_OUT
        capitalfees = numcredits * RATE_CAPITAL

    institutionfees = numcredits * RATE_INSTITUTION
    activityfees = numcredits * RATE_ACTIVITY

    totalowed = tuitionfees + capitalfees + institutionfees + activityfees
    balance = totalowed - scholarshipamt

def display_results():
    print("\n-------------------------------------------------------------")
    print("Number of credits : " + str(numcredits))
    print("-------------------------------------------------------------")
    print('Tuition          $ ' + format(tuitionfees, '10,.2f'))
    print('Capital Fee      $ ' + format(capitalfees, '10,.2f'))
    print('Institution Fee  $ ' + format(institutionfees, '10,.2f'))
    print('Activity Fee     $ ' + format(activityfees, '10,.2f'))
    print('Total            $ ' + format(totalowed, '10,.2f'))
    print('Scholarship      $ ' + format(scholarshipamt, '10,.2f'))
    print('-------------------------------------------------------------')
    print('Balance Owed     $ ' + format(balance, '10,.2f'))
    print('-------------------------------------------------------------')
    print(str(datetime.datetime.now()))
    print ("NOTE: BVCC Fee Rates: https://wsw.pvec.edu/tuition-and-fees")

main()
