import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cust=pd.read_csv("GAM_customer.csv",index_col='SRNO.')                                #import csv
apple=pd.read_csv('apple data.csv',index_col='years')
google=pd.read_csv('google data.csv',index_col='years')
microsoft=pd.read_csv('microsoft data.csv',index_col='years')
datas=pd.read_csv('datas.csv',index_col='criteria')
topic='1.MARKET CAPITAL\n 2.SHARE PRICE\n3.CEO SCORE\n4.NO.EMPLOYEES\n5.NO. OF PRODUCTS\n6.NO.OF COUNTRIES IN WHICH IT WORKS\n7.ANNUAL REVENUE\n8.GROSS PROFIT'
def welcome():                                                           #welcome page
    print('welcome tell us who are you')
    print('1.OWNER                         2.USER')
    who=int(input('enter your choice'))
    if who==1:
        owner()
    elif who==2:
        cust_registration()
def cust_registration():
    print('                                         WELCOME TO COMAPARABLY!!!!')
    print('                          1. LOGIN IF OLD USER')
    print('                          2. SIGN IN IF NEW USER')
    print('                          3.EXIT')
    sign=int(input('enter you choice:'))
    if sign==1:
        login()
    if sign==2:
        signin()
    elif sign==3:
        Exit()
def login():
        idno=input('enter you id')
        for x in cust['ID']:
            if x==idno:
                home()
                break
            else:
                print('incorrect response')
                cust_registration()
def signin():
        name=input('enter you name(BLOCK LETTERS)')
        age=input('enter you age')
        gender=input('enter your gender(M/F)')
        srno=len(cust.index)+1
        cust.loc[srno]=[name,age,gender,str(srno)+name[:3]+age[0:1]+gender]           #for unique id
        print('YOUR ID FOR FUTURE IS :',cust.ID[srno])
        cust.to_csv("GAM_customer.csv")
        home()
def home():
    print('WELCOME BACK DATA ANALYST!!!')
    print('HOW WOULD YOU LIKE TO SEE THE DATA')
    print('1.INDIVIDUAL')
    print('2.COMPARE ALL COMPANIES')
    print('3.EXIT')
    hom_ch=int(input('enter your choice:'))
    if hom_ch==1:
        company()
    elif hom_ch==2:
        comparison()
    elif hom_ch==3:
        Exit()
def company():
    print('1.GOOGLE\n2.APPLE\n3.MICROSOFT')
    com_ch=int(input('WHICH COMPANY'))
    if com_ch==1:
        c=google
    elif com_ch==2:
        c=apple
    elif com_ch==3:
        c=microsoft
    print(topic)
    print('WHICH DATA WOULD YOU LIKE TO SEE')                  #displaying individual datas
    comp_ch=int(input('enter your choice'))
    if comp_ch==1:
        print(c['market capital (in billions)'])
    if comp_ch==2:
        print(c.iloc[:,7:9])     
    if comp_ch==3:
        print(datas.loc['CEO ':'CEO score'])
    if comp_ch==4:
        print(c.iloc[:,3:5])
    if comp_ch==5:
        print(datas.loc['no. of products','microsoft'])
    if comp_ch==6:
        print(datas.loc['no. of countries','microsoft'])
    if comp_ch==7:
        print(c.iloc[:,1:3])
    if comp_ch==8:
        print(c.iloc[:,5:7])
    print('1.WANT TO GO BACK')
    print('press any other key to exit')
    fin_ch=int(input('enter your response'))
    if fin_ch==1:
        company()
    else:
        Exit()
def comparison():
    print('WHICH DATA DO YOU WANT TO SEE')
    print('1.market capital\n2.annual revenue\n3.ann revenue growth%\n4.no. of employee\n5.emp growth%\n6.gross profit')
    print('7.gross profit growth%\n8.average stock price\n9.share price change%\n10.brand value\n11. no. of products\n12.no. of countries')
    gra_ch=int(input('enter you choice'))
    if gra_ch==1 or gra_ch==2 or gra_ch==4 or gra_ch==6 or gra_ch==8:
        x=google.index
        yg=google.iloc[:,gra_ch-1]
        ya=apple.iloc[:,gra_ch-1]
        ym=microsoft.iloc[:,gra_ch-1]
        plt.plot(x,yg,label='GOOGLE',linestyle='solid')
        plt.plot(x,ya,label='APPLE',linestyle='dashed')
        plt.plot(x,ym,label='MICROSOFT',linestyle='dotted')
        plt.xlabel('years')
        plt.title('APPLE vs GOOGLE vs MICROSOFT')
        plt.legend()
        plt.show()
        
    if gra_ch==3 or gra_ch==5 or gra_ch==7 or gra_ch==9:
        x=google.index
        Yg=google.iloc[:,gra_ch-1]
        Ya=apple.iloc[:,gra_ch-1]
        Ym=microsoft.iloc[:,gra_ch-1]
        plt.bar(x,Yg,width=0.2,label='GOOGLE',hatch='*')
        plt.bar(x+0.2,Ya,width=0.2,label='APPLE',hatch='-')
        plt.bar(x+0.4,Ym,width=0.2,label='MICROSOFT',hatch='O')
        plt.xlabel('years')
        plt.title('APPLE vs GOOGLE vs MICROSOFT')
        plt.legend()
        plt.show()
    if gra_ch==10:
        y=datas.columns
        x=datas.iloc[2,:]
        plt.barh(y,x,hatch='O')
        plt.xlabel('brand value')
        plt.ylabel('company')
        plt.show()
    if gra_ch==11:
        y=datas.columns
        x=datas.iloc[3,:]
        plt.barh(y,x,hatch='*')
        plt.xlabel('')
        plt.ylabel('company')
        plt.show()
    if gra_ch==12:
        y=datas.columns
        x=datas.iloc[4,:]
        plt.barh(y,x,hatch='-')
        plt.xlabel('')
        plt.ylabel('company')
        plt.show()
def owner():
    print('WELCOME BACK CREATOR')
    print('1.SEE YOUR COSTUMER\' DATA')
    print('2.CHANGE DATA')
    print('3.BACK')
    own_ch=int(input('enter your choice'))
    if own_ch==1:
        print(cust)
    if own_ch==2:
        mod_comp()
    if own_ch==3:
        welcome()
def mod_comp():
    print('1.ADD\n2.DELETE')
    mod_ch=int(input('enter your choice'))
    if mod_ch==1:
        add()
    if mod_ch==2:
        delete()
def add():
    print('WHICH COMPANY? \n1.GOOGLE\n2.APPLE\n3.MICROSOFT')
    add_ch=int(input('enter your choice'))
    if add_ch==1:
        c=google
    if add_ch==2:
        c=apple
    if add_ch==3:
        c=microsoft
    year=int(input('enter year'))
    print('enter data column wise[market capital,annual revenue,ann revenue,growth% ,no. of emp,emp growth%,gross profit, growth%,avg share,change%] ')
    a_data=[]
    for i in range(1,10):
        d=float(input('enter data'))
        a_data.append(d)
    c.loc[year]=a_data
    print(c)
    if add_ch==1:
        c.to_csv('google data.csv')
    if add_ch==2:
        c.to_csv('apple data.csv')
    if add_ch==3:
        c.to_csv('microsoft data.csv')
    print('successfully added')
    owner()
def delete():
    print('WHICH COMPANY? \n1.GOOGLE\n2.APPLE\n3.MICROSOFT')
    del_ch=int(input('enter year'))
    if del_ch==1:
        c=google
    if del_ch==2:
        c=apple
    if del_ch==3:
        c=microsoft
    print(c)
    year=int(input('enter year'))
    c=c.drop([year])
    print(c)
    if del_ch==1:
        c.to_csv('google data.csv')
    if del_ch==2:
        c.to_csv('apple data.csv')
    if del_ch==3:
        c.to_csv('microsoft data.csv')
    print('succesfully deleted the row')
    owner()
def Exit():
    print('THANK YOU COME AGAIN LATER')
welcome()
