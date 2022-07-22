#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import csv
import pandas as pd

def Validate_email(username):
        if re.search('^[a-z|A-Z][a-z0-9|A-Z]+[\._]?[a-z0-9|A-Z]+[@]\w+[.]\w{2,3}$', username)==None:
            print("Please provide valid Email ID.")
            return False
  
        df=pd.read_csv("credentials.csv")
        df = df[df['EmailId'].str.contains(username,case=False)]
        if df.empty:
                return True
        else:
                print("Username Already exist..Try another Id")
                return False

def Validate_password(password):
    lower_case= re.search('[a-z]', password)
    upper_case= re.search('[A-Z]', password)
    numeric= re.search('[0-9]', password)
    special_char= re.search('[!@_$.]', password)
    space= re.search('^\S*$', password)
    if len(password)<6:
        print("Password too short!")
        return False
    elif len(password)>12:
        print("Password too long!")
        return False
    elif  lower_case==None or upper_case==None or numeric==None or special_char==None or space==None:
        print("please provide password with atleast one uppercase, one lowercase and one special charcter[!@_$.]")
        return False
    else:
        return True

    
def Register(username,password):
        if Validate_email(username)==True and Validate_password(password)==True:
            print("Great! You have been registered")
            df = pd.DataFrame({'EmailId':[username], 'PWD': [password]})
            df.to_csv('credentials.csv', mode='a',index=False, header=False)
            
            
def Login(username,password):
        df=pd.read_csv("credentials.csv")
        df = df[df['EmailId'].str.contains(username)]
        df= df[df['PWD'].str.contains(password)]
        if not df.empty:
            print("you have sucessfully login")
            return True
        else:
            print("invalid credentials!")
            return False


def Retrieve(username):
                df=pd.read_csv("credentials.csv")
                df = df[df['EmailId'].str.contains(username,case=False)]
                print(df)
                if not df.empty:
                    print(df["PWD"])
                else:
                    print("username doesnt exist! please register first")

                    
def Reset(username):
    df=pd.read_csv("credentials.csv")
    dF = df[df['EmailId'].str.contains(username,case=False)]
    if not dF.empty:
            password=input("Enter your new password ")
            if Validate_password(password)==True:
                    df.loc[df["EmailId"].str.contains(username, case=False, regex=False), "PWD"] = password
                    df.to_csv('credentials.csv',index=False, header=True)
            else:
                    print("Please enter a valid password ")
    else:
            print("No user found! please register first ")

                
ask=input("press Y for registration and N for login ")

if ask=="Y" or ask =="y":
    username,password=map(str,input("Enter your username and password seperated by space" ).split(" "))
    Register(username,password)

elif ask=="N" or ask=="n":
    username,password=map(str,input("Enter your username and password seperated by space  " ).split(" "))
    check=Login(username,password)
    if check==False:
        
        ask=input("press Y to retrieve your password and N for resetting your password ")
        if ask=="Y" or ask=="y":
            username=input("Enter your username ")
            Retrieve(username)
        elif ask=="N" or ask=="n":   
            username=input("Enter your username ")
            Reset(username)
else:
    print("Please reply with y or N ")

