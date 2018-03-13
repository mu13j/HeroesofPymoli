
# coding: utf-8

# In[4]:


import json
import pandas as pd


# In[5]:


data=json.load(open('purchase_data.json'))


# In[6]:


dataframe=pd.DataFrame(data)
dataframe.head()


# In[7]:


#Player Count
players=[]
for i in dataframe['SN']:
    if i not in players:
        players.append(i)
TotalNumber=len(players)
d={'Total Players':[TotalNumber]}
pd.DataFrame(data=d)


# In[8]:


#Unique Items
UniqueItems=[]
for i in dataframe['Item ID']:
    if i not in UniqueItems:
        UniqueItems.append(i)
NumUniqueItems=len(UniqueItems)


# In[9]:


#Average Purchase Price
AvgPurchasePrice='${:,.2f}'.format(sum(dataframe['Price'])/len(dataframe))


# In[10]:


#Total Number of Purchases
NumPurchase=len(dataframe)


# In[11]:


#Total Revenue
Revenue='${:,.2f}'.format(sum(dataframe['Price']))


# In[17]:


#Purchasing Analysis (Total)
d={'Number of Unique Items':[NumUniqueItems],'Average Price':[AvgPurchasePrice],'Number of Purchases':[NumPurchase],'Total Revenue': Revenue}
e=pd.DataFrame(d)
cols=['Number of Unique Items','Average Price','Number of Purchases','Total Revenue']
e=e[cols]
e


# In[18]:


#Total Number of Men
genders=[]
players=[]
for i in range(len(dataframe['SN'])):
    if dataframe['SN'][i] not in players:
        genders.append(dataframe['Gender'][i])
        players.append(dataframe['SN'][i])
NumMen=genders.count('Male')


# In[19]:


#Percentage of Men
PercentMen=NumMen/TotalNumber


# In[20]:


#Total Number of Females
NumFem=genders.count('Female')

#Percentage of Female
PercentFem=NumFem/TotalNumber


# In[21]:


#Total Number of Other/Non-Disclosed
NumOther=TotalNumber-NumFem-NumMen

#Percentage of Other
PercentOther=NumOther/TotalNumber


# In[22]:


#Gender Demographics
d={'Percentage of Players':['{:,.2f}%'.format(PercentMen*100),'{:,.2f}%'.format(PercentFem*100),'{:,.2f}%'.format(PercentOther*100)],'Total Count':[NumMen,NumFem,NumOther]}
e=pd.DataFrame(data=d)
e=e.rename({0:'Male',1:'Female',2:'Other / Non-Disclosed'})
e


# In[22]:


mix=dict(zip(players,genders))
#list of each gender
females=[]
males=[]
other=[]
for i in mix.keys():
    if mix[i]=="Female":
        females.append(i)
    elif mix[i]=="Male":
        males.append(i)
    else:
        other.append(i)


# In[23]:


#Index Counts of Purchases For Each Gender
malepurchases=[]
femalepurchases=[]
otherpurchases=[]
for i in range(len(dataframe)):
    if dataframe['Gender'][i]=="Male":
        malepurchases.append(i)
    elif dataframe['Gender'][i]=="Female":
        femalepurchases.append(i)
    else:
        otherpurchases.append(i)


# In[24]:


#Purchase Counts For Each Gender
NumMalePurch=len(malepurchases)
NumFemPurch=len(femalepurchases)
NumOthPurch=len(otherpurchases)


# In[25]:


#Total Price of Purchases By Gender
malesum=0
for i in malepurchases:
    malesum=malesum+dataframe.iloc[i]['Price']
femalesum=0
for i in femalepurchases:
    femalesum=femalesum+dataframe.iloc[i]['Price']
othersum=0
for i in otherpurchases:
    othersum=othersum+dataframe.iloc[i]['Price']
malesums='${:,.2f}'.format(malesum)
femalesums='${:,.2f}'.format(femalesum)
othersums='${:,.2f}'.format(othersum)


# In[26]:


#Average Price of Purchases By Gender
maleavg=(malesum/NumMalePurch)
femavg=(femalesum/NumFemPurch)
othavg=(othersum/NumOthPurch)
maleavgs='${:,.2f}'.format(maleavg)
femavgs='${:,.2f}'.format(femavg)
othavgs='${:,.2f}'.format(othavg)


# In[30]:


#Normalized Totals
normmale=NumMalePurch/NumPurchase
normfem=NumFemPurch/NumPurchase
normother=NumOthPurch/NumPurchase


# In[31]:


#Puchasing Analysis (Gender)
d={'Purchase Count':['',NumFemPurch,NumMalePurch,NumOthPurch],"Average Purchase Price":['',femavgs,maleavgs,othavgs],'Total Purchase Value':['',femalesums,malesums,othersums],'Normalized Totals':['',normfem,normmale,normother]}
e=pd.DataFrame(data=d)
e=e.rename({0:'Gender',1:'Female',2:'Male',3:'Other'})
cols=['Purchase Count','Average Purchase Price','Total Purchase Value',"Normalized Totals"]
e=e[cols]
e


# In[32]:


#Age Demographics
kidsn=[]
tweensn=[]
teensn=[]
oldersn=[]
for i in range(len(dataframe)):
    if dataframe['Age'][i]<10 and dataframe['SN'][i] not in kidsn:
            kidsn.append(dataframe['SN'][i])
    elif dataframe['Age'][i]<=14 and dataframe['Age'][i]>=10 and  dataframe['SN'][i] not in tweensn:
            tweensn.append(dataframe['SN'][i])
    elif dataframe['Age'][i]<=19 and dataframe['Age'][i]>14 and dataframe['SN'][i] not in teensn:
            teensn.append(dataframe['SN'][i])
    elif dataframe['Age'][i]>19 and dataframe['SN'][i] not in oldersn:
            oldersn.append(dataframe['SN'][i])
numkid=len(kidsn)
numtween=len(tweensn)
numteen=len(teensn)
numold=len(oldersn)
perkid=numkid/TotalNumber
pertween=numtween/TotalNumber
perteen=numteen/TotalNumber
perold=numold/TotalNumber
d={'Percentage of Players':['{:,.2f}%'.format(perkid*100),'{:,.2f}%'.format(pertween*100),'{:,.2f}%'.format(perteen*100),'{:,.2f}%'.format(perold*100)],'Total Count':[numkid,numtween,numteen,numold]}
e=pd.DataFrame(data=d)
e=e.rename({0:'<10',1:'10-14',2:'15-19',3:'20+'})
e


# In[33]:


#Index Counts of Purchases For Each Age Group
kids=[]
tweens=[]
teens=[]
older=[]
for i in range(len(dataframe)):
    if dataframe['Age'][i]<10:
        kids.append(i)
    elif dataframe['Age'][i]<=14:
        tweens.append(i)
    elif dataframe['Age'][i]<=19:
        teens.append(i)
    else:
        older.append(i)


# In[34]:


#Purchase Counts by Age

NumKids=len(kids)
NumTween=len(tweens)
NumTeen=len(teens)
NumOld=len(older)


# In[35]:


#Total Purchase Value By Age
kidsum=0
tweensum=0
teensum=0
oldsum=0
for i in kids:
    kidsum=kidsum+dataframe.iloc[i]['Price']
for i in tweens:
    tweensum=tweensum+dataframe.iloc[i]['Price']
for i in teens:
    teensum=teensum+dataframe.iloc[i]['Price']
for i in older:
    oldsum=oldsum+dataframe.iloc[i]['Price']
    


# In[36]:


#Average Purchase Value By Age
kidavg=kidsum/NumKids
tweenavg=tweensum/NumTween
teenavg=teensum/NumTeen
oldavg=oldsum/NumOld


# In[37]:


#Normalized Total
normkid=NumKids/NumPurchase
normtween=NumTween/NumPurchase
normteen=NumTeen/NumPurchase
normold=NumOld/NumPurchase


# In[38]:


#Purchasing Analysis (Age)
d={'Purchase Count':[NumKids,NumTween,NumTeen,NumOld],'Average Purchase Price':[kidavg,tweenavg,teenavg,oldavg],'Total Purchase Value':[kidsum,tweensum,teensum,oldsum],"Normalized Totals":[normkid,normtween,normteen,normold]}
e=pd.DataFrame(data=d)
col=['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals']
e=e[col]
e['Average Purchase Price']=pd.Series(["${0:.2f}".format(val) for val in e['Average Purchase Price']])
e['Total Purchase Value']=pd.Series(["${0:.2f}".format(val) for val in e['Total Purchase Value']])
e=e.rename({0:'<10',1:'10-14',2:'15-19',3:'20+'})
e


# In[39]:


#Highest 5 Spenders SN
new=dataframe.groupby(['SN'])['Price'].sum()
spenders=pd.DataFrame(new.nlargest(5,'first'))
names=[spenders.index[i] for i in range(5)]


# In[44]:


#Purchase Count of 5 Spenders
firstcount=0
secondcount=0
thirdcount=0
fourthcount=0
fifthcount=0
for i in range(len(dataframe)):
    if dataframe['SN'][i]==names[0]:
        firstcount+=1
    elif dataframe['SN'][i]==names[1]:
        secondcount+=1
    elif dataframe['SN'][i]==names[2]:
        thirdcount+=1
    elif dataframe['SN'][i]==names[3]:
        fourthcount+=1
    elif dataframe['SN'][i]==names[4]:
        fifthcount+=1


# In[45]:


#Total Purchase Price
totals=spenders.Price
totals=[float(spenders.Price[i]) for i in range(5)]


# In[46]:


#Average Purchase Price
avgfirst=totals[0]/firstcount
avgsecond=totals[1]/secondcount
avgthird=totals[2]/thirdcount
avgfourth=totals[3]/fourthcount
avgfifth=totals[4]/fifthcount


# In[47]:


#Top Spenders
d={'Purchase Count':['',firstcount,secondcount,thirdcount,fourthcount,fifthcount],'Average Purchase Price':['',"${0:.2f}".format(avgfirst),"${0:.2f}".format(avgsecond),"${0:.2f}".format(avgthird),"${0:.2f}".format(avgfourth),"${0:.2f}".format(avgfifth)],'Total Purchase Value':['',"${0:.2f}".format(totals[0]),"${0:.2f}".format(totals[1]),"${0:.2f}".format(totals[2]),"${0:.2f}".format(totals[3]),"${0:.2f}".format(totals[4])]}
e=pd.DataFrame(data=d)
cols=['Purchase Count','Average Purchase Price','Total Purchase Value']
e=e[cols]
e=e.rename({0:'SN',1:names[0],2:names[1],3:names[2],4:names[3],5:names[4]})
e


# In[48]:


#Most Popular 5 Items
mostpopular=dataframe.groupby(['Item ID']).count()
largest=mostpopular.nlargest(5,'Price',keep='first')
ids=[largest.index[i] for i in range(5)]
count=[largest.Age[i] for i in ids]


# In[49]:


#Most Popular 5 Items Prices and Names
itemsnameid={}
itemprice={}
for i in range(len(dataframe['Item ID'])):
    if i not in itemsnameid.keys():
        itemsnameid[dataframe['Item ID'][i]]=dataframe['Item Name'][i]
for i in range(len(dataframe['Item ID'])):
    if i not in itemprice.keys():
        itemprice[dataframe['Item ID'][i]]=float(dataframe['Price'][i])
itemprices=[itemprice[i] for i in ids]


# In[50]:


#Most Popular Items
d={'Item ID':ids,'Item Name':[itemsnameid[i] for i in ids],'Purchase Count':count,'Item Price':itemprices,'Total Purchase Value':[float(itemprices[i]*count[i]) for i in range(5)]}
e=pd.DataFrame(data=d)
cols=['Item ID','Item Name', 'Purchase Count','Item Price','Total Purchase Value']
e=e[cols]
e.set_index(['Item ID','Item Name'])


# In[54]:


#Most Profitable Items
new=dataframe.groupby(['Item ID'])['Price'].sum()
profitable=pd.DataFrame(new.nlargest(5,'first'))
ids=[profitable.index[i] for i in range(5)]
names=[itemsnameid[i] for i in ids]
totalvalue=[profitable.Price[i] for i in ids]
count=[mostpopular.Age[i] for i in ids]
prices=[float(totalvalue[i]/count[i]) for i in range(5)]
prices


# In[55]:


d={'Item ID':ids,'Item Name':names,'Purchase Count':count,'Item Price':["${0:.2f}".format(prices[i]) for i in range(5)],'Total Purchase Value':["${0:.2f}".format(totalvalue[i]) for i in range(5)]}
e=pd.DataFrame(data=d)
cols=['Item ID','Item Name', 'Purchase Count','Item Price','Total Purchase Value']
e=e[cols]
e.set_index(['Item ID','Item Name'])

