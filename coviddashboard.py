# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:05:30 2021

@author: jigar
"""

import requests
from tkinter import * 
response = requests.get('https://api.covid19india.org/data.json').json()

#Getting All India Data

xyz = response.get('cases_time_series')
y = xyz[-1]
Tconfirmed = y['totalconfirmed']
Dconfirmed = y['dailyconfirmed']
Date = y['dateymd']
Trecovered = y['totalrecovered']
Drecovered = y['dailyrecovered']
Ddeaths = y['dailydeceased']
Tdeaths = y['totaldeceased']

stws = response.get('statewise')
test1 = response.get('tested')

#Getting data for Gujarat

for key1 in stws:
    for gj in key1:
        if key1['state'] == "Gujarat":
           myState = key1

gActive =      myState['active'] 
gDeaths =      myState['deaths']
gConfirmed =   myState['confirmed']    
gUpdatedTime = myState['lastupdatedtime']  
gRecoovered  = myState['recovered']  

#Getting Other Informations also

testData = test1[-1]
flvacc1st = testData['frontlineworkersvaccinated1stdose']
flvacc2nd = testData['frontlineworkersvaccinated2nddose']
hcvacc1st = testData['healthcareworkersvaccinated1stdose']
hcvacc2nd = testData['healthcareworkersvaccinated2nddose']
o451st = testData['over45years1stdose']
o452nd = testData['over45years2nddose']
o601st = testData['over60years1stdose']
o602nd = testData['over60years2nddose']
r18_45 = testData['registration18-45years']
rabove45 = testData['registrationabove45years']
tVaccinated = testData['totalindividualsvaccinated']

#Placing Information on GUI

board = Tk()
board.title("Covid Dashboard")

#base frame creation which contains sub frames

baseFrame = Frame(board, highlightbackground='navy', highlightthickness='4',bg='gray10')
baseFrame.pack()

#Frame1 arrangements inside base frame (Vaccination Drive Insights)

frame1 = Frame(baseFrame, highlightbackground='green', highlightthickness='4',bg='gray10')
frame1.pack(side=LEFT,padx=10,pady=10)

Lflvacc1st = Label(frame1,text="Total Frontline workers vaccinated with 1st dose", fg='white',bg='gray10', font=('arial bold',12))
Lflvacc1st.grid(row=1,column=0,padx=10,pady=10)

Lflvacc1st_ = Label(frame1,text=flvacc1st,fg='white',bg='gray10',font=('arial bold',13))
Lflvacc1st_.grid(row=1,column=1,padx=5,pady=10)

Lflvacc2nd = Label(frame1,text="Total Frontline workers vaccinated with 2nd dose", fg='white',bg='gray10', font=('arial bold',12))
Lflvacc2nd.grid(row=2,column=0,padx=10,pady=10)

Lflvacc2nd_ = Label(frame1,text=flvacc2nd,fg='white',bg='gray10',font=('arial bold',13))
Lflvacc2nd_.grid(row=2,column=1,padx=5,pady=10)

Lhcvacc1st = Label(frame1,text="Total Healthcare workers vaccinated with 1st dose", fg='white',bg='gray10', font=('arial bold',12))
Lhcvacc1st.grid(row=3,column=0,padx=10,pady=10)

Lhcvacc1st_ = Label(frame1,text=hcvacc1st, fg='white',bg='gray10',font=('arial bold',13))
Lhcvacc1st_.grid(row=3,column=1,padx=5,pady=10)

Lhcvacc2nd = Label(frame1,text="Total Healthcare workers vaccinated with 2nd dose", fg='white',bg='gray10', font=('arial bold',12))
Lhcvacc2nd.grid(row=4,column=0,padx=10,pady=10)

Lhcvacc2nd_ = Lhcvacc1st_ = Label(frame1,text=hcvacc2nd, fg='white',bg='gray10',font=('arial bold',13))
Lhcvacc2nd_.grid(row=4,column=1,padx=5,pady=10)

Lo451st = Label(frame1,text="Total people >45 vaccinated with 1st dose", fg='white',bg='gray10', font=('arial bold',12))
Lo451st.grid(row=5,column=0,padx=10,pady=10)

Lo451st_ = Label(frame1,text=o451st, fg='white',bg='gray10',font=('arial bold',13))
Lo451st_.grid(row=5,column=1,padx=5,pady=10)

Lo452nd = Label(frame1,text="Total people >45 vaccinated with 2nd dose", fg='white',bg='gray10',font=('arial bold',12))
Lo452nd.grid(row=6,column=0,padx=10,pady=10)

Lo452nd_ = Label(frame1,text=o452nd, fg='white',bg='gray10',font=('arial bold',13))
Lo452nd_.grid(row=6,column=1,padx=5,pady=10)

Lo601st = Label(frame1,text="Total people >60 vaccinated with 1st dose", fg='white',bg='gray10', font=('arial bold',12))
Lo601st.grid(row=7,column=0,padx=10,pady=10)

Lo601st_ = Label(frame1,text=o601st, fg='white',bg='gray10',font=('arial bold',13))
Lo601st_.grid(row=7,column=1,padx=5,pady=10)

Lo602nd = Label(frame1,text="Total people >60 vaccinated with 2nd dose", fg='white',bg='gray10', font=('arial bold',12))
Lo602nd.grid(row=8,column=0,padx=10,pady=10)

Lo602nd_ = Label(frame1,text=o602nd, fg='white',bg='gray10',font=('arial bold',13))
Lo602nd_.grid(row=8,column=1,padx=5,pady=10)

Lr18_45 = Label(frame1,text="Total registered for vaccine 18-45",fg='white',bg='gray10',font=('arial bold',12))
Lr18_45.grid(row=9,column=0,padx=10,pady=10)

Lr18_45_ = Label(frame1,text=r18_45,fg='white',bg='gray10',font=('arial bold',13))
Lr18_45_.grid(row=9,column=1,padx=5,pady=10)

Lrabove45 = Label(frame1,text="Total registered for vaccine > 45",fg='white',bg='gray10',font=('arial bold',12))
Lrabove45.grid(row=10,column=0,padx=10,pady=10)

Lrabove45_ = Label(frame1,text=rabove45,fg='white',bg='gray10',font=('arial bold',13))
Lrabove45_.grid(row=10,column=1,padx=5,pady=10)

LtVaccinated = Label(frame1,text="Total Vaccinated",fg='white',bg='gray10',font=('arial bold',12))
LtVaccinated.grid(row=11,column=0,padx=10,pady=10)

LtVaccinated_ = Label(frame1,text=tVaccinated,fg='white',bg='gray10',font=('arial bold',12))
LtVaccinated_.grid(row=11,column=1,padx=5,pady=10)

D = Label(frame1, text="Vaccination Drive India Insights:",fg='white',bg='gray10',font=('arial bold',18))
D.grid(row=0,column=0,padx=20,pady=20,ipadx=40)






#frame2 gujarat data and Daily

frame2 = Frame(baseFrame, highlightbackground='gray10', highlightthickness='4',bg='gray10')
frame2.pack(side=RIGHT,padx=10,pady=10)

#frameG Gujarat Data inside frame2

frameG =  Frame(frame2, highlightbackground='green', highlightthickness='4',bg='gray10')
frameG.pack(padx=10,pady=10)

Gdata = Label(frameG,text="Gujarat Report:",fg='white',bg='gray10',font=('arial bold',14))
Gdata.grid(row=0,column=0,padx=10,pady=10)

LgActive = Label(frameG,text="Total Active Cases",fg='white',bg='gray10',font=('arial bold',12))
LgActive.grid(row=1,column=0,padx=10,pady=10)

LgActive_ = Label(frameG,text=gActive,fg='white',bg='gray10',font=('arial bold',12))
LgActive_.grid(row=1,column=1,padx=10,pady=10)

LgConfirmed = Label(frameG,text="Daily Confirmed Cases",fg='white',bg='gray10',font=('arial bold',12))
LgConfirmed.grid(row=2,column=0,padx=10,pady=10)

LgConfirmed_ =  Label(frameG,text=gConfirmed,fg='white',bg='gray10',font=('arial bold',12))
LgConfirmed_.grid(row=2,column=1,padx=10,pady=10)

LgDeaths = Label(frameG,text="Deaths",fg='white',bg='gray10',font=('arial bold',12))
LgDeaths.grid(row=3,column=0,padx=10,pady=10)

LgDeaths_ =  Label(frameG,text=gDeaths,fg='white',bg='gray10',font=('arial bold',12))
LgDeaths_.grid(row=3,column=1,padx=10,pady=10)

LgRecoovered =  Label(frameG,text="Recovered",fg='white',bg='gray10',font=('arial bold',12))
LgRecoovered.grid(row=4,column=0,padx=10,pady=10)

LgRecoovered_ =  Label(frameG,text=gRecoovered,fg='white',bg='gray10',font=('arial bold',12))
LgRecoovered_.grid(row=4,column=1,padx=10,pady=10)

LgUpdatedTime = Label(frameG, text="Last Updated ON",fg='white',bg='gray10' ,font=('arial bold',12))
LgUpdatedTime.grid(row=6,column=0,padx=10,pady=10)

LgUpdatedTime_ = Label(frameG,text=gUpdatedTime,fg='white',bg='gray10',font=('arial bold',12))
LgUpdatedTime_.grid(row=6,column=1,padx=10,pady=10)


#frame3 India Overview inside frame2 

frame3 = Frame(frame2, highlightbackground='green', highlightthickness='4',bg='gray10')
frame3.pack(padx=10,pady=10)

Ldaily = Label(frame3,text="Daily India Overview:",fg='white',bg='gray10',font=('arial bold',14))
Ldaily.grid(row=0,column=0,padx=10,pady=10)

LDconfirmed = Label(frame3,text="Daily Confirmed",fg='white',bg='gray10',font=('arial bold',12))
LDconfirmed.grid(row=1,column=0,padx=10,pady=10)

LDconfirmed_ =  Label(frame3,text=Dconfirmed,fg='white',bg='gray10',font=('arial bold',12))
LDconfirmed_.grid(row=1,column=1,padx=10,pady=10)

LDrecovered = Label(frame3,text="Daily recovered",fg='white',bg='gray10',font=('arial bold',12))
LDrecovered.grid(row=2,column=0,padx=10,pady=10)

LDrecovered_ =  Label(frame3,text=Drecovered,fg='white',bg='gray10',font=('arial bold',12))
LDrecovered_.grid(row=2,column=1,padx=10,pady=10)

LDdeaths = Label(frame3,text="Daily Deaths",fg='white',bg='gray10',font=('arial bold',12))
LDdeaths.grid(row=3,column=0,padx=10,pady=10)

LDdeaths_ =  Label(frame3,text=Ddeaths,fg='white',bg='gray10',font=('arial bold',12))
LDdeaths_.grid(row=3,column=1,padx=10,pady=10)

LDate = Label(frame3,text="Updated On",fg='white',bg='gray10',font=('arial bold',12))
LDate.grid(row=5,column=0,padx=10,pady=10)

LDate_ =  Label(frame3,text=Date,fg='white',bg='gray10',font=('arial bold',12))
LDate_.grid(row=5,column=1,padx=10,pady=10)




board['background'] = 'gray10'
board.mainloop()
