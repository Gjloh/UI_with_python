import csv
import datetime as dt
from operator import itemgetter #allows for easier sorting

# Check validity of dates
def check_date(x):
    now = dt.date.today()
    now = str(now).replace("-", "")
    while True:
        # date_format = False
        date = None
        try:
            date = input("Please enter {} [YYYYMMDD]:".format(x))
            try:
                dt.datetime.strptime(date, '%Y%m%d')
            except ValueError:
                print("The date {} is invalid. Please try again.".format(date))
                # date_format = True
                continue
            if int(date) <= 20151231 or int(date) > int(now):
                raise ValueError
        except ValueError:
            print("Sorry, the date {} is out of range.".format(date))
            continue
        else:
            return date

# check input
def check_input(prompt):
    while True:
        try:
            result = input("{}".format(prompt))
            if not result:
                raise ValueError
        except ValueError:
            print("Sorry, invalid input.")
            continue
        else:
            return result

#check input length
def check_length(prompt,length):
    while True:
         try:
            result = int(input("{}".format(prompt)))
            if not result:
                raise ValueError
            if len(str(result)) != length:
                raise ValueError
         except ValueError:
            print("Sorry, invalid input. Please only input {} numeric characters.".format(length))
            continue
         else:
            return result

#check input is numeric
def check_num(prompt):
    while True:
        try:
            result = float(input("{}".format(prompt)))
            if not result:
                raise ValueError
        except ValueError:
            print("Sorry, invalid input.")
            continue
        else:
            return result

#check string input length
def check_str_length(prompt, length):
    while True:
         try:
            result = input("{}".format(prompt))
            if not result:
                raise ValueError
            if len(result) != length:
                raise ValueError
         except ValueError:
            print("Sorry, invalid input. Please only input {} characters.".format(length))
            continue
         else:
            return result

# GLOBAL VAR FOR NEW_DATA
new_data = []
username = 0
usertelno = 0

# FOR RETRIEVING DATA
def retrieve_data():
    global new_data
    # prompt user for project
    project = 0
    l_count = 0
    while project == 0:
        proj_input = check_input("Please enter project ID:")

        #verify project number entered is valid (in database)
        for i in range(len(new_data)):
            if userid[0] == 'M' or userid[0] == 'm':
                if proj_input.upper() == new_data[i][10]:
                    project = new_data[i][10]
            elif userid[0] == 'S' or userid[0] == 's':
                if proj_input.upper() == new_data[i][10] and userid == new_data[i][12]:
                    project = new_data[i][10]
        if project == 0:
            print("Project not found.")

    # prompt user for dates
    start_date = check_date('start date')
    end_date = check_date('end date')

    #printing headers
    if userid[0] == 'M' or userid[0] == 'm':
        print("{:8s}\t{:13s}\t{:4s}\t{:8s}\t{:50s}\t{:6s}\t{:8s}\t{:3s}\t{:>10s}\t{:>10s}\t{:5s}\t{:5s}\t{:13s}\t{:12s}\t{:8s}".format( \
            headers_1[0], headers_1[1], headers_1[2], headers_1[3], headers_1[4], headers_1[5], headers_1[6], \
            headers_1[7], headers_1[8], headers_1[9], headers_1[10], headers_1[11], headers_1[12], headers_1[13], headers_1[14]))
        print("{:8s}\t{:13s}\t{:4s}\t{:8s}\t{:50s}\t{:6s}\t{:8s}\t{:3s}\t{:>10s}\t{:>10s}\t{:5s}\t{:5s}\t{:13s}\t{:12s}\t{:8s}".format( \
            headers_2[0], headers_2[1], headers_2[2], headers_2[3], headers_2[4], headers_2[5], headers_2[6], \
            headers_2[7], headers_2[8], headers_2[9], headers_2[10], headers_2[11], headers_2[12], headers_2[13], headers_2[14]))
    else:
        print("{:8s}\t{:13s}\t{:4s}\t{:8s}\t{:50s}\t{:6s}\t{:8s}\t{:3s}\t{:>10s}\t{:>10s}\t{:5s}\t{:5s}".format( \
            headers_1[0], headers_1[1], headers_1[2], headers_1[3], headers_1[4], headers_1[5], headers_1[6], \
            headers_1[7], headers_1[8], headers_1[9], headers_1[10], headers_1[11]))
        print("{:8s}\t{:13s}\t{:4s}\t{:8s}\t{:50s}\t{:6s}\t{:8s}\t{:3s}\t{:>10s}\t{:>10s}\t{:5s}\t{:5s}".format( \
            headers_2[0], headers_2[1], headers_2[2], headers_2[3], headers_2[4], headers_2[5], headers_2[6], \
            headers_2[7], headers_2[8], headers_2[9], headers_2[10], headers_2[11]))

    #sort data according to date
    sorted_data = sorted(new_data, key=itemgetter(1), reverse=False)
    #sort data according to DocRef
    sorted_data = sorted(sorted_data, key=itemgetter(0), reverse=True)

    #for sales manager: can view all sales related data
    if userid[0] == 'M' or userid[0] == 'm':
        for line in sorted_data:
            if project.upper() == line[10]:
                if int(start_date) <= line[0] and int(end_date) >= line[0]:
                    if line[1][0] == "I" or line[1][0] == "B":
                        print("{:8d}\t{:13s}\t{:4s}\t{:8s}\t{:50s}\t{:6s}\t{:8s}\t{:3s}\t{:10.2f}\t{:10.2f}\t{:5s}\t{:5s}\t{:13s}\t{:12s}\t{:8s}".format(line[0],\
                                 line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11],\
                                line[12], line[13], line[14]))
                        l_count += 1

    #for normal users
    for line in sorted_data:
        if userid.upper() == line[12]:
            if project.upper() == line[10]:
                if int(start_date) <= line[0] and int(end_date) >= line[0]:
                    if line[1][0] == "I": #sales persons can only view invoices (sales-related data)
                        print("{:8d}\t{:13s}\t{:4s}\t{:8s}\t{:50s}\t{:6s}\t{:8s}\t{:3s}\t{:10.2f}\t{:10.2f}\t{:5s}\t{:5s}\t".format(line[0],\
                                line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],line[10],line[11]))
                        l_count += 1


    #Check number of lines printed
    if l_count == 0:
        print("No data retrieved.")
    elif l_count == 1:
        print("1 line of data retrieved.")
    else:
        print("{} lines of data retrieved.".format(l_count))

# FOR APPENDING DATA
def append_data():
    global new_data
    global username
    global usertelno
    newdocdate = check_date('document date')
    newdocdate = int(newdocdate)

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    docref_start = 'BCDIJbcdij'
    while True:
        try:
            newdocref = check_input("Please enter the DocRef:")
            if not newdocref:
                raise ValueError
            if not any(newdocref.startswith(x) for x in docref_start):
                raise ValueError
        except ValueError:
            print("Sorry, invalid input")
            continue
        else:
            break
    newdocref = newdocref.upper()

    #if DocRef starts with B: accr1minus1 = -1
    #if DocRef starts with I: accr1minus1 = 1
    if newdocref[0] == "B":
        newaccrlsminus1 = -1
    elif newdocref[0] == "I":
        newaccrlsminus1 = 1
    else:
        while True:
            try:
                newaccrlsminus1 = int(input("Credit or debit transaction? [1: debit | -1: credit]: "))
                if not newaccrlsminus1:
                    raise ValueError
                if newaccrlsminus1 != 1 and newaccrlsminus1 != -1:
                    raise ValueError
            except ValueError:
                print("Sorry, invalid input.")
                continue
            else:
                break

    while True:
        try:
            newaccode = check_input("Please enter the Customer Account Code:")
            if not newaccode:
                raise ValueError
            if not any(newaccode.startswith(x) for x in alphabet):
                raise ValueError
        except ValueError:
            print("Sorry, invalid input")
            continue
        else:
            break
    newaccode = newaccode.upper()
    newcustname = check_input("Please enter the Customer Name:")
    newcustname = newcustname.title()
    newpostcode = check_length("Please enter the Postal Code:", 6)
    newtelno = check_length("Please enter the Phone Number:", 8)
    while True:
        try:
            newaccur = check_str_length("Please enter the currency used:", 3)
            if newaccur.upper() != "USD" and newaccur.upper() != "SGD":
                raise ValueError
        except ValueError:
            print("Sorry, invalid input.")
            continue
        else:
            break
    newaccur = newaccur.upper()

    newaccurwtaxamt = check_num("Please enter the transaction amount on the customer's monthly statement:")

    if newaccur == "SGD":
        newhomewtaxamt = newaccurwtaxamt

    else:
        while True:
            try:
                newhomewtaxamt = check_num("Please enter the converted S$ amount based on the transaction date exchange rate:")
                if (newhomewtaxamt / newaccurwtaxamt) > 1.5 or (newhomewtaxamt / newaccurwtaxamt) < 1.2:
                    #assumes USD:SGD will be in the range of 1.2 to 1.5, prevents invalid input
                    #assumption based on historical USD:SGD rates
                    raise ValueError
            except ValueError:
                print("Sorry, invalid input")
                continue
            else:
                break

    p = 'pP'
    while True:
        try:
            newprojcode = check_str_length("Please enter the Project Code:", 5)
            if not any(newprojcode.startswith(x) for x in p):
                raise ValueError
        except ValueError:
            print("Sorry, invalid input")
            continue
        else:
            break
    newprojcode = newprojcode.upper()

    while True:
        try:
            newlocation = int(input("Please enter the Location: [1 to 5]"))
            if not newlocation:
                raise ValueError
            if newlocation >5 or newlocation <1:
                raise ValueError
        except ValueError:
            print("Sorry, invalid input.")
            continue
        else:
            break
    s ='sS'
    if userid_input[0] != 'M' and userid_input[0] != 'm':
        #if it's not a manager, use the current userid as the sales person id
        newsalesid = userid_input.upper()
        newsalesname = username
        newsalestelno = usertelno

    else:
        while True:
            try:
                newsalesid = check_str_length("Please enter the Salesperson ID:", 4)
                if not any(newsalesid.startswith(x) for x in s):
                    raise ValueError
            except ValueError:
                print("Sorry, invalid input")
                continue
            else:
                break
        newsalesid = newsalesid.upper()

        for i in range(len(new_data)):
            if newsalesid.upper() == new_data[i][12]:
                print("Salesperson {} exists in database.".format(newsalesid.upper()))
                newsalesname = new_data[i][13]
                newsalestelno = new_data[i][14]
                break

        else:
            while True:
                try:
                    newsalesname = check_input("Please enter the Salesperson Name:")
                    if not newsalesname.isalpha():
                        raise ValueError
                except ValueError:
                    print("Sorry, invalid input")
                    continue
                else:
                    break
            newsalesname = newsalesname.capitalize()
            #make first letter Upper, the rest lower case
            newsalestelno = check_length("Please enter the Salesperson Phone Number:", 8)

    newdata = [str(newdocdate), newdocref, str(newaccrlsminus1), newaccode, newcustname, str(newpostcode),
               str(newtelno), newaccur, str(newaccurwtaxamt), str(newhomewtaxamt), newprojcode, str(newlocation),
               newsalesid, newsalesname, str(newsalestelno)]

    with open("state_cust_B_student_forAB.csv", "a", newline = '') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(newdata)

    #reimport data from file into program
    with open("state_cust_B_student_forAB.csv", "r") as data_file:
        count = 0
        data_csv = csv.reader(data_file)

        new_data.clear()
        for data in data_csv:
            if count > 0 and len(data) > 1:
                new_data.append(
                    [int(data[0]), data[1], data[2], data[3], data[4], data[5], data[6], data[7], float(data[8]),
                     float(data[9]), data[10], data[11], data[12], data[13], data[14]])
            count += 1

    print("Data input done.")


with open("state_cust_B_student_forAB.csv", "r") as data_file:
    data_csv = csv.reader(data_file)
    count = 0
    headers_1 = ['Doc Date', 'Doc Ref', '1/-1', 'Ac Code', 'Customer Name', 'Postal', 'Tel No', 'Ac',\
               'Ac Cur', 'Home', 'Proj', 'Loc', 'Sales Person', 'Sales Person','Sales']
    headers_2 = ['', '', '', '', '', 'Code', '', 'Cur',\
                 'WTaxAmt', 'WTaxAmt', 'Code', '','Code','Name','Contact']

    for data in data_csv:
        # [0]DocDate   DocRef  AcCrIsMinus1    AcCode  CustomerName
        # [5]PostalCode    TelNo   AcCur   AcCurWTaxAmt     HomeWTaxAmt
        # [10]ProjectCode   Location   SalesPerson    SalesPersonName    SalesContact
        if count > 0 and len(data) > 1:
            new_data.append([int(data[0]), data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                             float(data[8]), float(data[9]), data[10], data[11], data[12], data[13], data[14]])
        count += 1
    # print(new_data)

    #GETTING USER INPUT
    #var to save user data in case user wants to append
    userid = 0
    username = None
    usertelno = None

    while userid == 0:
        userid_input = check_input("Please enter user ID:")

    #verify userid in database
        for i in range(len(new_data)):
            if userid_input[0] != 'M' and userid_input[0] != 'm': #no manager user id given in the database
            #assumes that manager is given user id that starts with 'M'
                if userid_input.upper() == new_data[i][12]:
                    userid = new_data[i][12]
                    username = new_data[i][13]
                    usertelno = new_data[i][14]
        #print welcome screen
        if userid_input[0] != 'M' and userid_input[0] != 'm':
            if userid != 0:
                print("Welcome {}!".format(userid))
            else:
                print("Invalid user ID. Please try again.")
        else:
            print("Welcome manager {}.".format(userid_input.upper()))
            userid = userid_input.upper() #assign manager id to userid


while True: #to continue the whole program
    # Get user input: retrieve data or input data?
    while True: #checking user input
        try:
            choice = input("Would you like to retrieve or input data? [R/I]:")
            if not choice:  # avoids empty user input
                raise ValueError
            if choice.upper() != "R" and choice.upper() != "I":
                raise ValueError
        except ValueError:
            print("Sorry, invalid input.")
            continue
        else:
            break

    if choice.upper() == "R":
        retrieve_data()

    elif choice.upper() == "I":
        append_data()

    while True:
        try:
            cont = input("Would you like to continue? [Y/N]:") #checks if user wants to continue
            if not cont:
                raise ValueError
            if cont.upper() != "Y" and cont.upper() != "N":
                raise ValueError
        except ValueError:
            print("Sorry, invalid input.")
            continue
        else:
            break

    if cont.upper() == "N":
        print("Goodbye. Have a great day.")
        break




