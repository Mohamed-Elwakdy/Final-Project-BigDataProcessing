
### Introduction About The Dataset 


In this project, the APDM’s advanced wearable sensors, Opalsand Mobility Lab have been used to collect, analyze, and store outcome measures. This process takes less than five minutes and the number of sensors is 3 or 6.

The used dataset contains many h5 files that can be openedusing Python. There are many variables that are used in this dataset.  Each file in this dataset contains variables about somebody who is walking or standing.

Here, I worked on one nested data structure h5 file which contains the features of one walking person. Walking corridor must be at least7 meters in length. The data size of each independent variable (feature) is not the same. 

This table contains the node paths and the number of rows of each node path: 


Events/Gait/Lower Limb/All Steps Left 

Events/Gait/Lower Limb/All Steps Right 
 
Events/Gait/Lower Limb/Cycle Validity with Heel Strike Times  


### Gait Cycle Analysis 

###                               ![Image of screencapture](images/CycleAnalysis.jpg)
                                           Figure.1 Gait Cycle Analysis

### Import packages


|    Package Name  | Description |
| ------------- | --------------------- |
|pandas  |pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language|
|hdfdict|hdfdict helps h5py to dump and load python dictionaries|
|h5py | The h5py package is a Pythonic interface to the HDF5 binary data format with storing huge amounts of numerical data, and easily manipulate that data from NumPy|
|xlsxwriter|XlsxWriter is a Python module that can be used to write text, numbers, formulas and hyperlinks to multiple worksheets|


### Read h1 File (Getting the headers/keys)

```
f =  h5py.File("walking5.h5",'r')
for name in f:
    print(name)
res = hdfdict.load("walking5.h5")
print(res.keys())

```

### Collect Into DataFrames

All fields in this data set has been collected into datafrmes where the number of columns for each dataframe is not constant. We iterate through all the dataframes dictionary items and create a new
sheet. 

Each sheet contains a Dataframe. For example, sheet 1 contaion Dataframe1, sheet2 contains Dataframe 2, sheet3 contains Dataframe 3, sheet4 contains Dataframe 4, sheet5 contains Dataframe 5 and sheet6 contains Dataframe 6
The number of columns and rows in each sheet is not the same. 

```
dfd = {} # {1:df1,5:df2,113:df3<-add col}
         # Key indicates to the number of rows for each Dataframe

def print_attrs(name, obj):
    global dfd
    if '<class \'h5py._hl.dataset.Dataset\'>' == str(type(obj)):
        k= str(len(obj))
        if k not in dfd.keys():
            df = pd.DataFrame()
            df[name] = obj
            dfd[k] = df
            #print(name,"Adding new key for len ", k)
        else:
            df = dfd[k]
            df[name] = obj
            dfd[k] = df
            #print(name,"Adding col to dfd index ", k)
        #print(dfd.keys())
    for key, val in obj.attrs.items():
        print("    %s: %s" % (key, val),type(val))

```

####################


### Anticipatory Postural Adjustment 

Anticipatory postural adjustments are defined as the activation of postural muscles in a feedforward manner before a voluntary movement begins.

### Fields Description of the Anticipatory postural adjustments

The measures of the Anticipatory postural adjustments including 'First Step Duration' and 'First Step Range of Motion'.

|    Field Name  | Description |
| ------------- | --------------------- |
| First Step Duration |The duration of the period spanning from the end of the APA to the initial contact of the ﬁrst step|
|First Step Range of Motion | The integrated angular velocity of the stepping foot from the end of the APA to the initial contact of the step 

The features of Anticipatory postural adjustments variable are put into two data frames where the number of rows are 2 rows. 

```
First_Step_Duration = res['Measures']['Anticipatory Postural Adjustment']['First Step Duration']
df4 = pd.DataFrame(First_Step_Duration)
df4.columns = ['AnticipatoryPosturalAdjustmentFirstStepDuration']

First_Step_Range_of_Motion = res['Measures']['Anticipatory Postural Adjustment']['First Step Range of Motion'] 
df5 = pd.DataFrame(First_Step_Range_of_Motion)
df5.columns = ['AnticipatoryPosturalAdjustmentFirstStepRangeofMotion']

```

### Lower Limb

The leg region is the part of the lower limb that lies between the knee and the rounded medial and lateral prominences 
that flank the ankle joint. It connects the knee and foot.

Gait measures are detected, analyzed, and averaged over the extent of the walking duration of the subject. All measures are assessed for asymmetry and variability.


###                             ![Image of screencapture](images/GaitCycleDuration.jpg)
                                  Figure.2 Full Body Gait Measures: Gait Cycle Analysis

###                             ![Image of screencapture](images/DoubleSupport.jpg)
                                 Figure.3 Full Body Gait Measures: Double Support 

###                             ![Image of screencapture](images/TeminalDoubleSupport.jpg)                                                                    Figure.4 Full Body Gait Measures: Terminal Double Support 

### Fields Description of Lower Limb 

The measures of the Lower Limb including the Cycle Duration, Gait Speed, Double Support, Step Duration, Stride Length and Swing.  

|    Field Name  | Description |
| ------------- | --------------------- |
| Cycle Duration  |The duration of a full gait cycle, measured from the left foot’s initial contact to the next initial contact of the left foot|
|Gait Speed | The forward speed of the subject, measured as the forward distance traveled during the gait cycle divided by the gait cycle duration
|Double Support | The percentage of the gait cycle in which both feet are on the ground
|Step Duration| The duration of a step, measured as the period from initial contact of one foot to the next initial contact of the opposite foot
|Stride Length| The forward distance travelled by a foot during a gait cycle
|Swing| The percentage of the gait cycle in which the foot is not on the ground

The features of the Lower Limb variable are put into data frames. The size of these data frames is not the same where the number of columns are not constant while the number of rows are 25 rows. 

```
Measures_Gait_LowerLimb_GaitCycleDuration= res['Measures']['Gait']['Lower Limb']['Gait Cycle Duration']
df12 = pd.DataFrame(Measures_Gait_LowerLimb_GaitCycleDuration)
df12.columns = ['GaitLowerLimbGaitCycleDurationInSecondsStart','MeasuresGaitLowerLimbGaitCycleDurationInSecondsEnd']

Measures_Gait_LowerLimb_Gait_Speed= res['Measures']['Gait']['Lower Limb']['Gait Speed']
df13 = pd.DataFrame(Measures_Gait_LowerLimb_Gait_Speed)
df13.columns = ['GaitLowerLimbGaitSpeed1','MeasuresGaitLowerLimbGaitSpeed2']

Measures_Gait_LowerLimb_NumberStepsInTurn= res['Measures']['Gait']['Lower Limb']['No. Steps in Turn']
df14 = pd.DataFrame(Measures_Gait_LowerLimb_NumberStepsInTurn)
df14.columns = ['GaitLowerLimbNumberStepsInTurnPerMinute1', 'MeasuresGaitLowerLimbNumberStepsInTurnPerMinute2']
```
### Upper Limb

The upper limb or upper extremity is the region in the body extending from the deltoid region up to and including the hand, including the arm, axilla and shoulder.

###                                ![Image of screencapture](images/Upperlimb.jpg)
         Figure.5 Sensor Configuration and Measures: Balance, Lower Limb Gait, Upper Limb Gait, Turning and Sit to Stand  

### Fields Description of the Upper Limb  
The measures of the Upper Limb including the Arm Swing Velocity and Arm Swing Range of Motion. 

|    Field Name  | Description |
| ------------- | --------------------- |
| Arm Swing Velocity  |The maximum rotational velocity of the arm swing|
|Arm Swing Range of Motion | The angular range of the arm swing|

The features of Upper Limb variable are put into two data frames. The number of rows are 25 row.

```
Measures_Gait_UpperLimb_MaximumVelocity = res['Measures']['Gait']['Upper Limb']['Maximum Velocity']
df23 = pd.DataFrame(Measures_Gait_UpperLimb_MaximumVelocity)
df23.columns = ['MaximumRotationalVelocityofTheArmSwing1','MaximumRotationalVelocityofTheArmSwing2']

Measures_Gait_UpperLimb_RangeofMotion = res['Measures']['Gait']['Upper Limb']['Range of Motion']
df24 = pd.DataFrame(Measures_Gait_UpperLimb_RangeofMotion)
df24.columns = ['TheAngularRangOfTheArmSwing1','TheAngularRangOfTheArmSwing2']
``` 
### Turning Analysis

Postural measures are detected, analyzed, and averaged over the extent of the walking duration of the subject.

### Fields Description of the Turning 

The measures of the Turning including the Angle, Duration and Velocity.

|    Field Name  | Description |
| ------------- | --------------------- |
|Angle|The rotational angle of the turn|
|Duration|The duration of the turn|
|Velocity|The peak angular velocity of the turn|


###                                ![Image of screencapture](images/TurningAnalysis.jpg)
                                        Figure.6 Postural Measures: Turning Analysis 

The features of Turning variable are put into data frames. The number of rows is 21 rows. 

```
Measures_Turns_Angle = res['Measures']['Turns']['Angle']
df25 = pd.DataFrame(Measures_Turns_Angle)
df25.columns = ['TheRotationalAngleOfTheTurnInDegree']

Measures_Turns_PeakVelocity = res['Measures']['Turns']['Peak Velocity']
df26 = pd.DataFrame(Measures_Turns_PeakVelocity)
df26.columns = ['PeakAngularVelocityOfTheTurn']

Measures_Turns_Steps = res['Measures']['Turns']['Steps']
df27 = pd.DataFrame(Measures_Turns_Steps)
df27.columns = ['NumberOfStepsInTurns','TimeOfTurnsBasedOnTheNumberOfSteps']
```

### Collect the data frames in groups

The Data frames, which have the same number of rows, have been collected in one group with converting them to many CSV files. 

```
df_Group1 = pd.concat([df1, df2, df3], axis=1, sort=False)
df_Group2 = pd.concat([df4, df5], axis=1, sort=False)
df_Group3 = pd.concat([df6, df7, df8,df9,df10,df11], axis=1, sort=False) 

Group1_ConvertCSV= df_Group1.to_csv (r'Group1-DataFrame.csv', index = False, header=True)
Group2_ConvertCSV= df_Group2.to_csv (r'Group2-DataFrame.csv', index = False, header=True)
Group3_ConvertCSV= df_Group3.to_csv (r'Group3-DataFrame.csv', index = False, header=True)
```
### Collect all groups in many spreadsheets

The groups, which have different number of rows, have been collected in many spreadsheets for one excel file. 

```
writer = pd.ExcelWriter('Combined in many sheets.xlsx')
df_Group1.to_excel(writer, sheet_name='sheet1', index=False)
df_Group2.to_excel(writer, sheet_name='sheet2', index=False)
Groups_combine_3_4_5.to_excel(writer, sheet_name='sheet3', index=False)
df_Group6.to_excel(writer, sheet_name='sheet4', index=False)
df_Group7.to_excel(writer, sheet_name='sheet5', index=False)
writer.save()

```
