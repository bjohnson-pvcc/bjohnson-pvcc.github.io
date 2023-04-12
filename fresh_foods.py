import datetime

pay_rates = (16.50, 15.75, 19.50)
deduction_rates = (.12, .03, .062, .0145)

while True:
    item = input("Enter job category code and the number of hours worked separated by a space, if you are done just type \"DONE\": ")
    if item == 'DONE':
        break
    code = item[0]
    hours = item[1:]
    #print(code, hours)
    code = code.upper()
    if code == 'C':
        gross_pay = 16.5*int(hours)
    elif code == 'S' or code == 'J':
        gross_pay = 15.75*int(hours)
    elif code == 'M':
        gross_pay = 19.5*int(hours)
    else:
        print("Invalid entry for job category code")
        break
    fed = deduction_rates[0]*gross_pay
    state = deduction_rates[1]*gross_pay
    social = deduction_rates[2]*gross_pay
    medicare = deduction_rates[3]*gross_pay
    net = gross_pay - fed - state - social - medicare

    print("-------------------------------------------------------------")
    print("                        FRESH FOODS")
    print("-------------------------------------------------------------")
    print("Hours Worked:                                          {:>10}".format(hours))
    print("Gross Pay:                                            ${:>10}".format(str(round(gross_pay,2))))
    print("Federal Deduction:                                    ${:>10}".format(str(round(fed, 2))))
    print("State Deduction:                                      ${:>10}".format(str(round(state, 2))))
    print("Social Security Deduction:                            ${:>10}".format(str(round(social, 2))))
    print("Medicare:                                             ${:>10}".format(str(round(medicare, 2))))
    print("Total Deductions:                                     ${:>10}".format(str(round(abs(net-gross_pay), 2))))
    print("Net Pay:                                              ${:>10}".format(str(round(net, 2))))
    print("-------------------------------------------------------------")
    print("--------------------HAVE A GREAT DAY ;D----------------------")
    print("-------------------------------------------------------------")
    print(str(datetime.datetime.now()))