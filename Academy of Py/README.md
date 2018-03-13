

```python
import pandas as pd
import numpy as np
```


```python
file1='schools_complete.csv'
file2='students_complete.csv'
school=pd.read_csv(file1)
student=pd.read_csv(file2)
passingscore=70
```


```python
#Total Schools
schoolnames=[]
for i in school['name']:
    if i not in schoolnames:
        schoolnames.append(i)
numsch=len(schoolnames)
```


```python
#Total students with unique ids
studentid=[]
for i in student['Student ID']:
    if i not in studentid:
        studentid.append(i)
numstu=len(studentid)
```


```python
#Finds Duplicate Student Names
#studentnames=[]
#studentduplicates=[]
#for i in student['name']:
#    if i not in studentnames:
#        studentnames.append(i)
#    else:
#        studentduplicates.append(i)
#studentduplicates
```


```python
#Total Budget
totalbudget=0
for i in school['budget']:
    totalbudget=totalbudget+i
```


```python
#Average Math Score
avgmath=sum(student['math_score'])/len(student['math_score'])
```


```python
#Average Reading Score
avgread=sum(student['reading_score'])/len(student['reading_score'])
```


```python
# %Passing Math
counter=0
for i in student['math_score']:
    if i>passingscore:
        counter+=1
mathpass=counter/len(student['math_score']*100)
```


```python
# %Passing Reading
counter=0
for i in student['reading_score']:
    if i>passingscore:
        counter+=1
readpass=counter/len(student['reading_score']*100)
```


```python
#Overall Passing Rate
overall=(mathpass+readpass)/2
```


```python
#District Summary
d={'Total Schools':[numsch],'Total Students':[numstu], 'Total Budget':["${:.2f}".format(totalbudget)],'Average Math Score':[avgmath],'Average Reading Score':[avgread],'% Passing Math':[mathpass],'% Passing Reading':[readpass],'Overall Passing Rate':[overall]}
e=pd.DataFrame(data=d)
cols=['Total Schools','Total Students', 'Total Budget','Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','Overall Passing Rate']
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
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>$24649428.00</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>0.723921</td>
      <td>0.829717</td>
      <td>0.776819</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>$655.00</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>$639.00</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>$600.00</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>94.860875</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>$652.00</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>73.807983</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>$625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>$578.00</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>95.203679</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>$582.00</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>95.586652</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>$628.00</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>74.306672</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>$581.00</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>92.505855</td>
      <td>96.252927</td>
      <td>94.379391</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>$609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>95.270270</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>$583.00</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.333333</td>
      <td>96.611111</td>
      <td>94.972222</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>$637.00</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>$650.00</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>73.639992</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>$644.00</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>73.804308</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>$638.00</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.272171</td>
      <td>97.308869</td>
      <td>95.290520</td>
    </tr>
  </tbody>
</table>
</div>




```python
d={'School Name':schoolnames,'School Type':schooltypes,'Total Students':totalstudents,'Total School Budget':budgets,'Per Student Budget':psb,'Average Math Score':avgmathsch,'Average Reading Score':avgreadsch,'% Passing Math':mathrate,'% Passing Reading':readrate,'Overall Passing Rate':overallrate}
important=pd.DataFrame(data=d)
cols=['School Name','School Type','Total Students','Total School Budget','Per Student Budget','Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','Overall Passing Rate']
important=important[cols]
important=important.set_index('School Name')
```


```python
#Top Performing Schools By Passing Rate
top=pd.DataFrame(important.nlargest(5,'Overall Passing Rate'))
top
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
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>95.586652</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.272171</td>
      <td>97.308869</td>
      <td>95.290520</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>95.270270</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>95.265668</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>95.203679</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Worst 5 Passing Rate
bottom=pd.DataFrame(important.nsmallest(5,'Overall Passing Rate'))
bottom
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
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>73.639992</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>73.804308</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Reading Scores By Grade
p=pd.DataFrame(readscoresbygrade, columns=['9th','10th','11th','12th'])
p.index=schoolnames
p
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
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
  </tbody>
</table>
</div>




```python
e=important
labels=['<$585','$585-615','$616-645','$645-675']
a=pd.cut(e['Per Student Budget'],[0,585,615,645,675],labels=labels)
e['Per Student Budget']=a
```


```python
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
```


```python
#Scores By Spending
d={"Average Math Score":avgmaths,"Average Reading Score":avgreads,"% Passing Math":passmaths,"% Passing Reading":passreads,"Overall Passing Rate":overall}
e=pd.DataFrame(data=d,index=labels)
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
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$585</th>
      <td>93.702889</td>
      <td>96.686558</td>
      <td>83.363065</td>
      <td>83.964039</td>
      <td>95.194724</td>
    </tr>
    <tr>
      <th>$585-615</th>
      <td>94.124128</td>
      <td>95.886889</td>
      <td>83.529196</td>
      <td>83.838414</td>
      <td>95.005509</td>
    </tr>
    <tr>
      <th>$616-645</th>
      <td>71.400428</td>
      <td>83.614770</td>
      <td>78.061635</td>
      <td>81.434088</td>
      <td>77.507599</td>
    </tr>
    <tr>
      <th>$645-675</th>
      <td>66.230813</td>
      <td>81.109397</td>
      <td>77.049297</td>
      <td>81.005604</td>
      <td>73.670105</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;1000</th>
      <td>93.952484</td>
      <td>96.040317</td>
      <td>83.828654</td>
      <td>83.974082</td>
      <td>94.996400</td>
    </tr>
    <tr>
      <th>1000-2000</th>
      <td>93.616522</td>
      <td>96.773058</td>
      <td>83.372682</td>
      <td>83.867989</td>
      <td>95.194790</td>
    </tr>
    <tr>
      <th>2000-5000</th>
      <td>68.652380</td>
      <td>82.125158</td>
      <td>77.477597</td>
      <td>81.198674</td>
      <td>75.388769</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>93.701821</td>
      <td>96.645891</td>
      <td>83.406183</td>
      <td>83.902821</td>
      <td>95.173856</td>
    </tr>
    <tr>
      <th>District</th>
      <td>66.518387</td>
      <td>80.905249</td>
      <td>76.987026</td>
      <td>80.962485</td>
      <td>73.711818</td>
    </tr>
  </tbody>
</table>
</div>


