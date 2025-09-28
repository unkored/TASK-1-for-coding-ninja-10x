"""● Student_ID
● Hours of Study per day
● Average Sleep Hours
● Daily Screen Time
● Attendance Percentage
● Extracurricular Activities (Yes/No)
● Stress Level (Low/Medium/High)
● CGPA (out of 10)"""

import csv
import numpy as np


no=0
dup = []



sid =[]
hr=[]
ash=[]
dst=[]
ap=[]
ext=[]
sl=[]
cg= []
f = open("student_wellbeing_dataset.csv","r")
lis = ["Student_ID","Hours_Study","Sleep_Hours","Screen_Time","Attendance","Extracurricular","Stress_Level","CGPA"]
a = f.readlines()



def format_changer():
    global lis
    
    for i in a:
    
        l = i.split(',')
        
        try:
            hr.append(float(l[1]))
        except:
            hr.append(None)
        try:
            sid.append(l[0])
        except:
            sid.append(None)
        try:
            ash.append(float(l[2]))
        except:
            ash.append(None)
        try:
            dst.append(float(l[3]))
        except:
            dst.append(None)
        try:
            ap.append(float(l[4]))
        except:
            ap.append(None)
        try:
            ext.append(l[5])
        except:
            ext.append(None)
        try:
            sl.append(l[6])
        except:
            sl.append(None)
        try:
            cg.append(float(l[7]))
        except:
            cg.append(None)




def format_checker():
    check = 0
    for i in range(10200):
        if (type(sid[0])==type("string") and type(hr[0])==type(1.1) and type(ash[0])==type(1.22) and type(dst[0])==type(1.33) and type(ap[0])==type(1.22) and type(ext[0])==type("string") and type(sl[0])==type("string") and type(cg[0])==type(1.23))  or (type(sid[0])==type(None) or type(hr[0])==type(None) or type(ash[0])==type(None) or type(dst[0])==type(None) or type(ap[0])==type(None) or type(ext[0])==type(None) or type(sl[0])==type(None) or type(cg[0])==type(None)):
            check = 1
    if check == 1:
        print("ready for analysis")
    else:
        print("sorry no ready")



def dupl():
    global no
    for i in a:
        l = i.split(',')
        b=sid.count(sid[no])
        if b > 2:
            dup.append([i,no])	    
        no+=1
    if b<2:
	    print("NO DUPLICATE DATA")
    	
    else:
	    print("IT CONTAINS DUPLICATE DATA")
     




def relation():
    
    # Coefficients matrix (4x4)
    A = np.array([[hr[0],ash[0],dst[0],cg[0]],
                  [hr[1],ash[1],dst[1],cg[1]],
    	    	  [hr[2],ash[2],dst[2],cg[2]],
	    	      [hr[3],ash[3],dst[3],cg[3]]])

    # Constants matrix
    solution = np.array([0, 0, 0, 0])

    print("The solution to the system of equations is:")
    print(f"x = {solution[0]:.4f}")
    print(f"y = {solution[1]:.4f}")
    print(f"z = {solution[2]:.4f}")
    print(f"w = {solution[3]:.4f}")

    
def compare_stress():

    l=h=m=0
    vall = 0
    valh = 0
    valm = 0
    for  j in range(len(sl)):
        if sl[j].lower() == "low":
            vall += cg[j]
            l += 1
        elif sl[j].lower() ==  "high":
            valh += cg[j]
            h += 1
        elif sl[j].lower() == "medium":
            valm += cg[j]
            m += 1

    a=vall/l 
    b=valm/m
    c=valh/h

    if (a>b) and (a>c):
        print("The  academic performance of students with low stress level is HIGH")
    elif (c>a) and (c>b):
        print("The  academic performance of students with high stress level is HIGH")
    elif (b>a) and (b>c):
        print("The academic performance of students with medium stress level is HIGH")
    else:
        print("The  academic performance of students with low ,medium and high stress level are equal")


def compare_ext():
    y=n=0
    valy = 0
    valn = 0
    
    for  j in range(len(sl)):
        if ext[j].lower() == "yes":
            valy += cg[j]
            y += 1
        elif ext[j].lower() ==  "no":
            valn += cg[j]
            n += 1
        
    a=valy/y 
    b=valn/n
    
    
    if (a>b) :
        print("The  academic performance of students in extracurricular activities is HIGH")
    elif (b>a) :
        print("The  academic performance of students those not participating in extracurricular activiries is HIGH")
    else:
        print("The  academic performance of students in both participating and not participating in extracurricular activities are equal")




def export():
    srs = []
    no = 0
    for i in range(len(sid)):
        try:
            if sid[i] is not None:
                a = sid[i]
                b = int(a[1:])  # Extracting number after 's' and converting to integer
                srs.append(b)  # Append to srs
    
        except:
            srs.append(99999+no)
            no+=1
    srsn = list(srs)
    srs.sort()
    nd = []
    f = open("export.csv",'w',newline='')
    writer=csv.writer(f)
    writer.writerow(lis)
    for i in range(10201):
        for j in range(10201):
            if ("S"+str(srs[i])) == sid[j]:
                nd = [sid[j],str(hr[j]),str(ash[j]),str(dst[j]),str(ap[j]),ext[j],sl[j],str(cg[j])]
                writer.writerow(nd)
    print("finished")

    

format_changer()
format_checker()
#relation()
compare_stress()
compare_ext()
export()

f.close()




