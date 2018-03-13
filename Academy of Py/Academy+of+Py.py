
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


file1='schools_complete.csv'
file2='students_complete.csv'
school=pd.read_csv(file1)
student=pd.read_csv(file2)
passingscore=70


# In[3]:


#Total Schools
schoolnames=[]
for i in school['name']:
    if i not in schoolnames:
        schoolnames.append(i)
numsch=len(schoolnames)


# In[4]:


#Total students with unique ids
studentid=[]
for i in student['Student ID']:
    if i not in studentid:
        studentid.append(i)
numstu=len(studentid)


# In[5]:


#Finds Duplicate Student Names
#studentnames=[]
#studentduplicates=[]
#for i in student['name']:
#    if i not in studentnames:
#        studentnames.append(i)
#    else:
#        studentduplicates.append(i)
#studentduplicates


# In[6]:


#Total Budget
totalbudget=0
for i in school['budget']:
    totalbudget=totalbudget+i


# In[7]:


#Average Math Score
avgmath=sum(student['math_score'])/len(student['math_score'])


# In[8]:


#Average Reading Score
avgread=sum(student['reading_score'])/len(student['reading_score'])


# In[9]:


# %Passing Math
counter=0
for i in student['math_score']:
    if i>passingscore:
        counter+=1
mathpass=counter/len(student['math_score']*100)


# In[10]:


# %Passing Reading
counter=0
for i in student['reading_score']:
    if i>passingscore:
        counter+=1
readpass=counter/len(student['reading_score']*100)


# In[11]:


#Overall Passing Rate
overall=(mathpass+readpass)/2


# In[12]:


#District Summary
d={'Total Schools':[numsch],'Total Students':[numstu], 'Total Budget':["${:.2f}".format(totalbudget)],'Average Math Score':[avgmath],'Average Reading Score':[avgread],'% Passing Math':[mathpass],'% Passing Reading':[readpass],'Overall Passing Rate':[overall]}
e=pd.DataFrame(data=d)
cols=['Total Schools','Total Students', 'Total Budget','Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','Overall Passing Rate']
e=e[cols]
e


# In[13]:


#School Summary
schoolnames=[i for i in school['name']]
schooltypes=[i for i in school['type']]
a=student.groupby(['school'])['name'].count()
totalstudents=[a[i] for i in schoolnames]
budgets=[i for i in school['budget']]
budgetstr=["${:.2f}".format(i) for i in budgets]
psb=[budgets[i]/totalstudents[i] for i in range(numsch)]
perstudentbudget=["${:.2f}".format(budgets[i]/totalstudents[i]) for i in range(numsch)]
a=student.groupby(['school']).mean()
avgmathsch=[a['math_score'][i] for i in schoolnames]
avgreadsch=[a['reading_score'][i] for i in schoolnames]
mathrate=[]
readrate=[]
for i in schoolnames:
    b=student.groupby(['school']).get_group(i)
    readcounter=0
    mathcounter=0
    for j in b['reading_score'].keys():
        if b['reading_score'][j]>=passingscore:
            readcounter+=1
        if b['math_score'][j]>=passingscore:
            mathcounter+=1        
    mathrate.append(100*mathcounter/totalstudents[schoolnames.index(i)])
    readrate.append(100*readcounter/totalstudents[schoolnames.index(i)])
overallrate=[(mathrate[i]+readrate[i])/2 for i in range(numsch)]
d={'School Name':schoolnames,'School Type':schooltypes,'Total Students':totalstudents,'Total School Budget':budgets,'Per Student Budget':perstudentbudget,'Average Math Score':avgmathsch,'Average Reading Score':avgreadsch,'% Passing Math':mathrate,'% Passing Reading':readrate,'Overall Passing Rate':overallrate}
chart=pd.DataFrame(data=d)
cols=['School Name','School Type','Total Students','Total School Budget','Per Student Budget','Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','Overall Passing Rate']
chart=chart[cols]
chart=chart.set_index('School Name')
chart


# In[14]:


d={'School Name':schoolnames,'School Type':schooltypes,'Total Students':totalstudents,'Total School Budget':budgets,'Per Student Budget':psb,'Average Math Score':avgmathsch,'Average Reading Score':avgreadsch,'% Passing Math':mathrate,'% Passing Reading':readrate,'Overall Passing Rate':overallrate}
important=pd.DataFrame(data=d)
cols=['School Name','School Type','Total Students','Total School Budget','Per Student Budget','Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','Overall Passing Rate']
important=important[cols]
important=important.set_index('School Name')


# In[15]:


#Top Performing Schools By Passing Rate
top=pd.DataFrame(important.nlargest(5,'Overall Passing Rate'))
top


# In[16]:


#Worst 5 Passing Rate
bottom=pd.DataFrame(important.nsmallest(5,'Overall Passing Rate'))
bottom


# In[17]:


#Math Scores By Grade
grades=['9th','10th','11th','12th']
mathscoresbygrade=[]
readscoresbygrade=[]
for i in schoolnames:
    b=student.groupby(['school']).get_group(i)
    c=b.groupby(['grade']).mean()
    mathscoresbygrade.append([c['math_score'][i] for i in grades])
    readscoresbygrade.append([c['reading_score'][i] for i in grades])
p=pd.DataFrame(mathscoresbygrade, columns=['9th','10th','11th','12th'])
p.index=schoolnames
p


# In[18]:


#Reading Scores By Grade
p=pd.DataFrame(readscoresbygrade, columns=['9th','10th','11th','12th'])
p.index=schoolnames
p


# In[19]:


e=important
labels=['<$585','$585-615','$616-645','$645-675']
a=pd.cut(e['Per Student Budget'],[0,585,615,645,675],labels=labels)
e['Per Student Budget']=a


# In[20]:


#Scores By Spending
avgmaths=[]
avgreads=[]
passmaths=[]
passreads=[]
for i in labels:
    f=e.groupby('Per Student Budget').get_group(i)
    dummy=0
    readdummy=0
    passmath=0
    passread=0
    for i in range(len(f['Average Math Score'])):
        dummy=dummy+f['Average Math Score'][i]*f['Total Students'][i]
        readdummy=readdummy+f['Average Reading Score'][i]*f['Total Students'][i]
        passmath=passmath+f['% Passing Math'][i]*f['Total Students'][i]
        passread=passread+f['% Passing Reading'][i]*f['Total Students'][i]
    avgmaths.append(dummy/f['Total Students'].sum())
    avgreads.append(readdummy/f['Total Students'].sum())
    passmaths.append(passmath/f['Total Students'].sum())
    passreads.append(passread/f['Total Students'].sum())
overall=[(passmaths[i]+passreads[i])/2 for i in range(len(passreads))]


# In[21]:


#Scores By Spending
d={"Average Math Score":avgmaths,"Average Reading Score":avgreads,"% Passing Math":passmaths,"% Passing Reading":passreads,"Overall Passing Rate":overall}
e=pd.DataFrame(data=d,index=labels)
e


# In[22]:


#Scores By Size
labels=["<1000","1000-2000","2000-5000"]
a=pd.cut(important['Total Students'],[0,1000,2000,5000],labels=labels)
e=important
e['Size']=a
avgmaths=[]
avgreads=[]
passmaths=[]
passreads=[]
for i in labels:
    f=e.groupby('Size').get_group(i)
    dummy=0
    readdummy=0
    passmath=0
    passread=0
    for i in range(len(f['Average Math Score'])):
        dummy=dummy+f['Average Math Score'][i]*f['Total Students'][i]
        readdummy=readdummy+f['Average Reading Score'][i]*f['Total Students'][i]
        passmath=passmath+f['% Passing Math'][i]*f['Total Students'][i]
        passread=passread+f['% Passing Reading'][i]*f['Total Students'][i]
    avgmaths.append(dummy/f['Total Students'].sum())
    avgreads.append(readdummy/f['Total Students'].sum())
    passmaths.append(passmath/f['Total Students'].sum())
    passreads.append(passread/f['Total Students'].sum())
overall=[(passmaths[i]+passreads[i])/2 for i in range(len(passreads))]
d={"Average Math Score":avgmaths,"Average Reading Score":avgreads,"% Passing Math":passmaths,"% Passing Reading":passreads,"Overall Passing Rate":overall}
e=pd.DataFrame(data=d,index=labels)
e


# In[23]:


#Scores By School Types
e=important
labels=['Charter',"District"]
avgmaths=[]
avgreads=[]
passmaths=[]
passreads=[]
for i in labels:
    f=e.groupby('School Type').get_group(i)
    dummy=0
    readdummy=0
    passmath=0
    passread=0
    for i in range(len(f['Average Math Score'])):
        dummy=dummy+f['Average Math Score'][i]*f['Total Students'][i]
        readdummy=readdummy+f['Average Reading Score'][i]*f['Total Students'][i]
        passmath=passmath+f['% Passing Math'][i]*f['Total Students'][i]
        passread=passread+f['% Passing Reading'][i]*f['Total Students'][i]
    avgmaths.append(dummy/f['Total Students'].sum())
    avgreads.append(readdummy/f['Total Students'].sum())
    passmaths.append(passmath/f['Total Students'].sum())
    passreads.append(passread/f['Total Students'].sum())
overall=[(passmaths[i]+passreads[i])/2 for i in range(len(passreads))]
d={"Average Math Score":avgmaths,"Average Reading Score":avgreads,"% Passing Math":passmaths,"% Passing Reading":passreads,"Overall Passing Rate":overall}
e=pd.DataFrame(data=d,index=labels)
e

