import pandas as pd
import matplotlib.pyplot as plt



#Checking if file is exist or not
try:
    df1=pd.read_csv("contacts.csv",index_col='contactid')
except FileNotFoundError:
    df=pd.DataFrame([],columns=['contactid',"name","number","gender","type","state"])
    df.to_csv("contacts.csv",index=None)
    # df1=pd.read_csv("contacts.csv",index_col='contactid')



#Defined the intro for welcoming the user when its starts
def intro():
    print("================================")
    print("WELCOME TO CONTACT MANAGEMENT SYSYEM")
    print("Made By Harshit Jain & Kartikay Khana")
    
    
    
#Defined the Menu for user
def Menu():
    print("1. -----------> To Show All Contact.")
    print("2. -----------> To Add New Contact.")
    print("3. -----------> To Update Contact.")
    print("4. -----------> To Delete Contact.")
    print("5. -----------> To Search Category-Wise Contacts.")
    print("6. -----------> To see visulation of Contacts.")
    
    opt = int(input("Enter respective number, you want to perform : "))
    if opt==1:
        showAll()
    elif opt==2:
        addNewContact()
    elif opt==3:
        updateContact()
    elif opt==4:
        deleteContact()
    elif opt==5:
        searchContact()
    elif opt==6:
        visualiseContact()
#Function1 : to show all contact that are present in csv in dataframe   
def showAll():
    df = pd.read_csv(r'contacts.csv')#read the csv file
    isDataAvailable = pd.read_csv("contacts.csv",index_col='contactid')
    if (len(isDataAvailable.index)>0):
        print(df)
        print('file opened')   
        Menu()
    else:
        print("No Data Founded! Please insert Some Data First")
        Menu()
    
#Function2 : Add New Contact   
def addNewContact():
    checkId = pd.read_csv("contacts.csv",index_col='contactid')
    id = int(input("Enter Id : "))
    if id not in list(checkId.index):
        name = input("Enter name : ")
        number = int(input("Enter number : "))
        gender = input("Enter m for Male and f for Female : ")
        type = input("Enter w for work type or p for Personal type : ")
        state = input("Enter State : ")
        numbertoString = str(number)
        isNumberCorrect = len(numbertoString)
        if isNumberCorrect==10:
            checkId.loc[int(id),:] = [name,number,gender,type,state]
            checkId.to_csv('contacts.csv')
            print("New Contact Inserted!")
            Menu()    
        else:
            print("Number is Not Correct please enter again.")
            addNewContact()    
    else:
        print("Contact already exists!")
        addNewContact()
    
def updateContact():
    checkId = pd.read_csv("contacts.csv",index_col='contactid')
    id = int(input("Enter Id which you want to update : "))
    print(checkId.loc[[id],:])
    print("Enter the Following Column name to update")
    print("name for Updating name")
    print("number for Updating number")
    print("gender for Updating gender")
    print("type for Updating type")
    print("state for Updating state")
    column = input("Enter Column Name : ")
    updatedValue = input("Enter Correct value : ")
    checkId.loc[id,column]=updatedValue
    checkId.to_csv('contacts.csv')
    print("Contact Updated!")
    print(checkId.loc[[id],:])
    Menu()    
       

def deleteContact():
    checkId = pd.read_csv("contacts.csv",index_col='contactid')
    print(checkId)
    id = int(input("Enter Id which you want to delete: "))
    checkId = checkId.drop(id,axis=0)
    print(checkId)
    checkId.to_csv('contacts.csv')
    print("Contact Deleted!")
    print(checkId)
    Menu()    

#Defined search algorithm
def searchContact():
    checkId = pd.read_csv("contacts.csv")
    print("1. Search by Name.")
    print("2. Search by Type.")
    print("3. Search by Gender.")
    print("4. Search by State.")
    n = int(input("Enter Number by which you want to search : "))
    if n == 1:
        name = input("Enter Name to search contact : ")
        try:
            print(checkId[(checkId['name'].str.contains(name))])
        except :
            print("No Such Contact found with this name!")
    elif n==2:
        type = input("Enter w for Work type Contacts or p for Personal Contact : ")
        try:
            print(checkId[(checkId['type'].str.contains(type))])
        except :
            print("No Such Contact found with this type!")
    elif n==3:
        gender = input("Enter m for Male Contacts or f for Female Contacts : ")
        try:
            print(checkId[(checkId['gender'].str.contains(gender))])
        except :
            print("No Such Contact found with this gender!")     
            
    elif n==4:
        state = input("Enter state name to find Contacts : ")
    try:
        print(checkId[(checkId['state'].str.contains(state))])
    except :
        print("No Such Contact found with this state!")          
    Menu() 


#Defined search algorithm
def visualiseContact():
    checkId = pd.read_csv("contacts.csv")
    lines= len(checkId.contactid)
    print("1. See by Type.")
    print("2. See by Gender.")
    print("3. See by State.")
    n = int(input("Enter Number by which you want to See : "))
    if n == 1:
        try:
            plt.bar(checkId.type,checkId)
            plt.xticks(checkId.type, color='orange')
            plt.yticks(checkId.contactid, color='orange')
            plt.xlabel('Type of Contacts', color='black')
            plt.xlabel('No. of Contacts', color='black')
            plt.legend()
            plt.show()
        except :
            print("No Such Contact found with this name!")
    elif n==2:
        type = input("Enter w for Work type Contacts or p for Personal Contact : ")
        try:
            print(checkId[(checkId['type'].str.contains(type))])
        except :
            print("No Such Contact found with this type!")
    elif n==3:
        gender = input("Enter m for Male Contacts or f for Female Contacts : ")
        try:
            print(checkId[(checkId['gender'].str.contains(gender))])
        except :
            print("No Such Contact found with this gender!")              
    Menu() 

Menu()