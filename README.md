

```python
import json
import pandas as pd
import numpy as np
from pprint import pprint

```


```python
data=json.load(open('purchase_data.json'))
```


```python
dataframe=pd.DataFrame(data)
dataframe.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Player Count
players=[]
for i in dataframe['SN']:
    if i not in players:
        players.append(i)
TotalNumber=len(players)
d={'Total Players':[TotalNumber]}
pd.DataFrame(data=d)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Unique Items
UniqueItems=[]
for i in dataframe['Item ID']:
    if i not in UniqueItems:
        UniqueItems.append(i)
NumUniqueItems=len(UniqueItems)
NumUniqueItems
```




    183




```python
#Average Purchase Price
AvgPurchasePrice='${:,.2f}'.format(sum(dataframe['Price'])/len(dataframe))
AvgPurchasePrice
```




    '$2.93'




```python
#Total Number of Purchases
NumPurchase=len(dataframe)
NumPurchase
```




    780




```python
#Total Revenue
Revenue='${:,.2f}'.format(sum(dataframe['Price']))
Revenue
```




    '$2,286.33'




```python
#Purchasing Analysis (Total)
d={'Number of Unique Items':[NumUniqueItems],'Average Price':[AvgPurchasePrice],'Number of Purchases':[NumPurchase],'Total Revenue': Revenue}
e=pd.DataFrame(d)
cols=['Number of Unique Items','Average Price','Number of Purchases','Total Revenue']
e=e[cols]
e.style
```




<style  type="text/css" >
</style>  
<table id="T_df4fc030_2582_11e8_9de9_b0359fc79ce0" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Number of Unique Items</th> 
        <th class="col_heading level0 col1" >Average Price</th> 
        <th class="col_heading level0 col2" >Number of Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_df4fc030_2582_11e8_9de9_b0359fc79ce0level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_df4fc030_2582_11e8_9de9_b0359fc79ce0row0_col0" class="data row0 col0" >183</td> 
        <td id="T_df4fc030_2582_11e8_9de9_b0359fc79ce0row0_col1" class="data row0 col1" >$2.93</td> 
        <td id="T_df4fc030_2582_11e8_9de9_b0359fc79ce0row0_col2" class="data row0 col2" >780</td> 
        <td id="T_df4fc030_2582_11e8_9de9_b0359fc79ce0row0_col3" class="data row0 col3" >$2,286.33</td> 
    </tr></tbody> 
</table> 




```python
#Total Number of Men
genders=[]
players=[]
for i in range(len(dataframe['SN'])):
    if dataframe['SN'][i] not in players:
        genders.append(dataframe['Gender'][i])
        players.append(dataframe['SN'][i])
NumMen=genders.count('Male')

NumMen
```




    465




```python
#Percentage of Men
PercentMen=NumMen/TotalNumber
PercentMen
```




    0.8115183246073299




```python
#Total Number of Females
NumFem=genders.count('Female')

#Percentage of Female
PercentFem=NumFem/TotalNumber
print(NumFem,PercentFem)
```

    100 0.17452006980802792
    


```python
#Total Number of Other/Non-Disclosed
NumOther=TotalNumber-NumFem-NumMen

#Percentage of Other
PercentOther=NumOther/TotalNumber
print(NumOther,PercentOther)
```

    8 0.013961605584642234
    


```python
#Gender Demographics
d={'Percentage of Players':['{:,.2f}%'.format(PercentMen*100),'{:,.2f}%'.format(PercentFem*100),'{:,.2f}%'.format(PercentOther*100)],'Total Count':[NumMen,NumFem,NumOther]}
e=pd.DataFrame(data=d)
e=e.rename({0:'Male',1:'Female',2:'Other / Non-Disclosed'})
e
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
other
```




    ['Assassa38',
     'Frichistasta59',
     'Tyaerith73',
     'Aillycal84',
     'Faralcil63',
     'Eurisuru25',
     'Aithelis62',
     'Euna48']




```python
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

```


```python
#Purchase Counts For Each Gender
NumMalePurch=len(malepurchases)
NumFemPurch=len(femalepurchases)
NumOthPurch=len(otherpurchases)

```


```python
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
print(malesum,femalesum,othersum)
```

    1867.68 382.91 35.74
    


```python
#Average Price of Purchases By Gender
maleavg=(malesum/NumMalePurch)
femavg=(femalesum/NumFemPurch)
othavg=(othersum/NumOthPurch)
maleavgs='${:,.2f}'.format(maleavg)
femavgs='${:,.2f}'.format(femavg)
othavgs='${:,.2f}'.format(othavg)
print(maleavg,femavg,othavg)
```

    2.95052132701 2.81551470588 3.24909090909
    


```python
#Normalized Totals
normmale=NumMalePurch/NumPurchase
normfem=NumFemPurch/NumPurchase
normother=NumOthPurch/NumPurchase
print(normmale,normfem,normother)
```

    0.8115384615384615 0.17435897435897435 0.014102564102564103
    


```python
#Puchasing Analysis (Gender)
d={'Purchase Count':['',NumFemPurch,NumMalePurch,NumOthPurch],"Average Purchase Price":['',femavgs,maleavgs,othavgs],'Total Purchase Value':['',femalesums,malesums,othersums],'Normalized Totals':['',normfem,normmale,normother]}
e=pd.DataFrame(data=d)
e=e.rename({0:'Gender',1:'Female',2:'Male',3:'Other'})
cols=['Purchase Count','Average Purchase Price','Total Purchase Value',"Normalized Totals"]
e=e[cols]
e
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Gender</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>0.174359</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>0.811538</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>0.0141026</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.32%</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01%</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20+</th>
      <td>75.22%</td>
      <td>431</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
#Purchase Counts by Age

NumKids=len(kids)
NumTween=len(tweens)
NumTeen=len(teens)
NumOld=len(older)
```


```python
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
print(kidsum,tweensum,teensum,oldsum)
    
```

    83.46 96.95 386.42 1719.5
    


```python
#Average Purchase Value By Age
kidavg=kidsum/NumKids
tweenavg=tweensum/NumTween
teenavg=teensum/NumTeen
oldavg=oldsum/NumOld
print(kidavg,tweenavg,teenavg,oldavg)
```

    2.98071428571 2.77 2.90541353383 2.94434931507
    


```python
#Normalized Total
normkid=NumKids/NumPurchase
normtween=NumTween/NumPurchase
normteen=NumTeen/NumPurchase
normold=NumOld/NumPurchase
print(normkid,normtween,normteen,normold)
```

    0.035897435897435895 0.04487179487179487 0.17051282051282052 0.7487179487179487
    


```python
#Purchasing Analysis (Age)
d={'Purchase Count':[NumKids,NumTween,NumTeen,NumOld],'Average Purchase Price':[kidavg,tweenavg,teenavg,oldavg],'Total Purchase Value':[kidsum,tweensum,teensum,oldsum],"Normalized Totals":[normkid,normtween,normteen,normold]}
e=pd.DataFrame(data=d)
col=['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals']
e=e[col]
e['Average Purchase Price']=pd.Series(["${0:.2f}".format(val) for val in e['Average Purchase Price']])
e['Total Purchase Value']=pd.Series(["${0:.2f}".format(val) for val in e['Total Purchase Value']])
e=e.rename({0:'<10',1:'10-14',2:'15-19',3:'20+'})
e
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>0.035897</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>0.044872</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>0.170513</td>
    </tr>
    <tr>
      <th>20+</th>
      <td>584</td>
      <td>$2.94</td>
      <td>$1719.50</td>
      <td>0.748718</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Highest 5 Spenders SN
new=dataframe.groupby(['SN'])['Price'].sum()
spenders=pd.DataFrame(new.nlargest(5,'first'))
names=[spenders.index[i] for i in range(5)]
```


```python
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
```


```python
#Total Purchase Price
totals=spenders.Price
totals=[float(spenders.Price[i]) for i in range(5)]
```


```python
#Average Purchase Price
avgfirst=totals[0]/firstcount
avgsecond=totals[1]/secondcount
avgthird=totals[2]/thirdcount
avgfourth=totals[3]/fourthcount
avgfifth=totals[4]/fifthcount
```


```python
#Top Spenders
d={'Purchase Count':['',firstcount,secondcount,thirdcount,fourthcount,fifthcount],'Average Purchase Price':['',"${0:.2f}".format(avgfirst),"${0:.2f}".format(avgsecond),"${0:.2f}".format(avgthird),"${0:.2f}".format(avgfourth),"${0:.2f}".format(avgfifth)],'Total Purchase Value':['',"${0:.2f}".format(totals[0]),"${0:.2f}".format(totals[1]),"${0:.2f}".format(totals[2]),"${0:.2f}".format(totals[3]),"${0:.2f}".format(totals[4])]}
e=pd.DataFrame(data=d)
cols=['Purchase Count','Average Purchase Price','Total Purchase Value']
e=e[cols]
e=e.rename({0:'SN',1:names[0],2:names[1],3:names[2],4:names[3],5:names[4]})
e
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>SN</th>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular 5 Items
mostpopular=dataframe.groupby(['Item ID']).count()
largest=mostpopular.nlargest(5,'Price',keep='first')
ids=[largest.index[i] for i in range(5)]
count=[largest.Age[i] for i in ids]
```


```python
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
```


```python
#Most Popular Items
d={'Item ID':ids,'Item Name':[itemsnameid[i] for i in ids],'Purchase Count':count,'Item Price':itemprices,'Total Purchase Value':[float(itemprices[i]*count[i]) for i in range(5)]}
e=pd.DataFrame(data=d)
cols=['Item ID','Item Name', 'Purchase Count','Item Price','Total Purchase Value']
e=e[cols]
e.set_index(['Item ID','Item Name'])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable Items
new=dataframe.groupby(['Item ID'])['Price'].sum()
profitable=pd.DataFrame(new.nlargest(5,'first'))
ids=[profitable.index[i] for i in range(5)]
names=[itemsnameid[i] for i in ids]
prices=[profitable.Price[i] for i in ids]
count=[mostpopular.Age[i] for i in ids]
totalvalue=[float(count[i]*prices[i]) for i in range(5)]
prices
```




    [37.259999999999998,
     29.75,
     29.699999999999999,
     29.220000000000002,
     28.879999999999999]




```python
d={'Item ID':ids,'Item Name':names,'Purchase Count':count,'Item Price':["${0:.2f}".format(prices[i]) for i in range(5)],'Total Purchase Value':["${0:.2f}".format(totalvalue[i]) for i in range(5)]}
e=pd.DataFrame(data=d)
cols=['Item ID','Item Name', 'Purchase Count','Item Price','Total Purchase Value']
e=e[cols]
e.set_index(['Item ID','Item Name'])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$37.26</td>
      <td>$335.34</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$29.75</td>
      <td>$208.25</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$29.70</td>
      <td>$178.20</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$29.22</td>
      <td>$175.32</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$28.88</td>
      <td>$231.04</td>
    </tr>
  </tbody>
</table>
</div>


