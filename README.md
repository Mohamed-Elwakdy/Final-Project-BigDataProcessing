
### Introduction About The Dataset 


PDM Wearable Technology has created a testing platform/product called Mobility Lab for research.  A subject can be tested and a report can be generated in less than 5 minutes.  The tests use Opal wearable sensors (3 or 7 sensors). 

The used dataset contains many h5 files that can be opened using Python. Almost 100 variables are used in this dataset. The 90+  movement variables for each subject are collected in one file. One file was used for this project.

The h5 file which contains the features of one walking person. Walking corridor must be at least7 meters in length. 


This table contains the node paths and the number of rows of each node path: 

|    Node Paths  | Number of Rows |
| ------------- | --------------------- |
|	Events/Gait/Lower Limb/Initial Contact	|	25	|
|	Events/Gait/Lower Limb/Initial Contact Next	|	25	|
|	Events/Gait/Lower Limb/Midswing	|	25	|
|	Events/Gait/Lower Limb/Toe Off	|	25	|
|	Measures/Gait/Joint/Back/Abduction/Maximum	|	25	|
|	Measures/Gait/Joint/Back/Abduction/Minimum	|	25	|
|	Measures/Gait/Joint/Back/Abduction/ROM	|	25	|
|	Measures/Gait/Joint/Back/Flexion/Maximum	|	25	|
|	Measures/Gait/Joint/Back/Flexion/Minimum	|	25	|
|	Measures/Gait/Joint/Back/Flexion/ROM	|	25	|
|	Measures/Gait/Joint/Back/Rotation/Maximum	|	25	|
|	Measures/Gait/Joint/Back/Rotation/Minimum	|	25	|
|	Measures/Gait/Joint/Back/Rotation/ROM	|	25	|
|	Measures/Gait/Lower Limb/Cadence	|	25	|
|	Measures/Gait/Lower Limb/Double Support	|	25	|
|	Measures/Gait/Lower Limb/Elevation at Midswing	|	25	|
|	Measures/Gait/Lower Limb/Gait Cycle Duration	|	25	|
|	Measures/Gait/Lower Limb/Gait Speed	|	25	|
|	Measures/Gait/Lower Limb/Initial Double Support	|	25	|
|	Measures/Gait/Lower Limb/Initial+Mid Swing	|	25	|
|	Measures/Gait/Lower Limb/Lateral Step Deviation	|	25	|
|	Measures/Gait/Lower Limb/Lateral Swing Max	|	25	|
|	Measures/Gait/Lower Limb/Maximum Pitch	|	25	|
|	Measures/Gait/Lower Limb/Pitch at Initial Contact	|	25	|
|	Measures/Gait/Lower Limb/Pitch at Mid Swing	|	25	|
|	Measures/Gait/Lower Limb/Pitch at Toe Off	|	25	|
|	Measures/Gait/Lower Limb/Single Limb Support	|	25	|
|	Measures/Gait/Lower Limb/Stance	|	25	|
|	Measures/Gait/Lower Limb/Step Duration	|	25	|
|	Measures/Gait/Lower Limb/Stride Length	|	25	|
|	Measures/Gait/Lower Limb/Swing	|	25	|
|	Measures/Gait/Lower Limb/Terminal Double Support	|	25	|
|	Measures/Gait/Lower Limb/Terminal Swing	|	25	|
|	Measures/Gait/Lower Limb/Toe Out Angle	|	25	|
|	Measures/Gait/Lower Limb/Toe Out Angle Max	|	25	|
|	Measures/Gait/Lower Limb/Toe Out Angle Min	|	25	|
|	Measures/Gait/Lumbar/Coronal Average Angle	|	25	|
|	Measures/Gait/Lumbar/Coronal Maximum Angle	|	25	|
|	Measures/Gait/Lumbar/Coronal Minimum Angle	|	25	|
|	Measures/Gait/Lumbar/Coronal Range of Motion	|	25	|
|	Measures/Gait/Lumbar/Sagittal Average Angle	|	25	|
|	Measures/Gait/Lumbar/Sagittal Maximum Angle	|	25	|
|	Measures/Gait/Lumbar/Sagittal Minimum Angle	|	25	|
|	Measures/Gait/Lumbar/Sagittal Range of Motion	|	25	|
|	Measures/Gait/Lumbar/Transverse Average Angle	|	25	|
|	Measures/Gait/Lumbar/Transverse Maximum Angle	|	25	|
|	Measures/Gait/Lumbar/Transverse Minimum Angle	|	25	|
|	Measures/Gait/Lumbar/Transverse Range of Motion	|	25	|
|	Measures/Gait/Trunk/Coronal Maximum Angle	|	25	|
|	Measures/Gait/Trunk/Coronal Minimum Angle	|	25	|
|	Measures/Gait/Trunk/Coronal Range of Motion	|	25	|
|	Measures/Gait/Trunk/Relative Coronal Range of Motion	|	25	|
|	Measures/Gait/Trunk/Relative Sagittal Range of Motion	|	25	|
|	Measures/Gait/Trunk/Relative Transverse Range of Motion	|	25	|
|	Measures/Gait/Trunk/Sagittal Average Angle	|	25	|
|	Measures/Gait/Trunk/Sagittal Maximum Angle	|	25	|
|	Measures/Gait/Trunk/Sagittal Minimum Angle	|	25	|
|	Measures/Gait/Trunk/Sagittal Range of Motion	|	25	|
|	Measures/Gait/Trunk/Transverse Average Angle	|	25	|
|	Measures/Gait/Trunk/Transverse Maximum Angle	|	25	|
|	Measures/Gait/Trunk/Transverse Minimum Angle	|	25	|
|	Measures/Gait/Trunk/Transverse Range of Motion	|	25	|
|	Measures/Gait/Upper Limb/Foot Phase Difference	|	25	|
|	Measures/Gait/Upper Limb/Maximum Velocity	|	25	|
|	Measures/Gait/Upper Limb/Range of Motion	|	25	|
|	Events/Gait/Lower Limb/All Steps Left	|	113	|
|	Events/Gait/Lower Limb/All Steps Right	|	113	|
|	Events/Gait/Lower Limb/Cycle Validity with Heel Strike Times	|	113	|
|	Events/Turns/Start	|	21	|
|	Measures/Turns/Angle	|	21	|
|	Measures/Turns/Duration	|	21	|
|	Measures/Turns/Peak Velocity	|	21	|
|	Measures/Turns/Steps	|	21	|
|	Measures/Gait/Lower Limb/No. Steps in Turn	|	22	|
|	Measures/Gait/Lower Limb/Total Turn Angle	|	22	|
|	Measures/Gait/Lower Limb/Turn Direction	|	22	|
|	Measures/Gait/Lower Limb/Turn Duration	|	22	|
|	Measures/Gait/Lower Limb/Turn Per Step	|	22	|
|	Measures/Gait/Lower Limb/Turn Rate	|	22	|
|	Processed/Joint Angles/Back/Middle/Quaternion	|	15744	|
|	Processed/Joint Angles/Back/Middle/X	|	15744	|
|	Processed/Joint Angles/Back/Middle/Y	|	15744	|
|	Processed/Joint Angles/Back/Middle/Z	|	15744	|
|	Log/Info	|	1	|
|	Measures/Anticipatory Postural Adjustment/APA Duration	|	1	|
|	Measures/Anticipatory Postural Adjustment/First Step Duration	|	1	|
|	Measures/Anticipatory Postural Adjustment/First Step Range of Motion	|	1	|
|	Measures/Anticipatory Postural Adjustment/Maximum AP Acceleration	|	1	|
|	Measures/Anticipatory Postural Adjustment/Maximum ML Acceleration	|	1	|
|	Measures/Duration	|	1	|
|	Measures/Gait/Lower Limb/Lateral Step Variability	|	1	|
|	Measures/Gait/Lower Limb/N	|	1	|
|	Measures/Turns/N	|	1	|





### Gait Cycle Analysis 

###                               ![Image of screencapture](images/CycleAnalysis.jpg)
                           Figure.1 Gait Cycle Analysis (source:  APDM Wearable Technologies)

### Import packages

```
import pandas as pd
import hdfdict
import numpy as np
import h5py,time

```

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

All fields has been collected into datafrmes where the number of columns for each dataframe is not constant. We iterate through all the dataframes dictionary items and create a sheet for each dataframe. Also, we split each column has more than one item to many column with removing all parentheses.

```
dfd = {} 

def print_attrs(name, obj):
    global dfd
    if '<class \'h5py._hl.dataset.Dataset\'>' == str(type(obj)):
        k= str(len(obj))
        if k not in dfd.keys():
            df = pd.DataFrame()
        else:
            df = dfd[k]
        df[name] = obj                           
        df = pd.concat([pd.DataFrame(df[c].tolist()).add_prefix(c) for c in df.columns], axis=1)
        dfd[k] = df
        #print(dfd.keys())
    for key, val in obj.attrs.items():
        print("    %s: %s" % (key, val),type(val))

```

### Collect All Dataframes in an Excel file 

All Dataframes collected in spreadsheets for one Excel file. Each sheet contains a Dataframe. For example, sheet 1 contaion Dataframe1, sheet2 contains Dataframe 2, sheet3 contains Dataframe 3, sheet4 contains Dataframe 4, sheet5 contains Dataframe 5 and sheet6 contains Dataframe 6. 
The number of columns and rows for each sheet is not the same. 

```

writer = pd.ExcelWriter('hd5excelout6.xlsx', engine = 'xlsxwriter')
for k, df in dfd.items():
    print(k,len(df))
    df.columns = df.columns.str.replace(r'\d+', '')
    df.to_excel(writer, sheet_name = 'sheet_len_'+k)
writer.save()
writer.close()

```

### Lower Limb

The leg region is the part of the lower limb that lies between the knee and the rounded medial and lateral prominences 
that flank the ankle joint. It connects the knee and foot.

The features of the Lower Limb variable are put into data frames. Gait measures are detected, analyzed, and averaged over the extent of the walking duration of the subject. All measures are assessed for asymmetry and variability.

### Fields Description of Lower Limb 

The measures of the Lower Limb including the Cycle Duration, Gait Speed, Double Support, Step Duration, Stride Length and Swing.  

|    Field Name  | Description |
| ------------- | --------------------- |
|Cycle Duration |The duration of a full gait cycle, measured from the left foot’s initial contact to the next initial contact of the left foot|
|Gait Speed | The forward speed of the subject, measured as the forward distance traveled during the gait cycle divided by the gait cycle duration|
|Double Support | The percentage of the gait cycle in which both feet are on the ground|
|Step Duration| The duration of a step, measured as the period from initial contact of one foot to the next initial contact of the opposite foot|
|Stride Length| The forward distance travelled by a foot during a gait cycle|
|Swing| The percentage of the gait cycle in which the foot is not on the ground|
|Cadence|The number of steps per minute, counting steps made by both feet|
|Foot Clearance | The height of the foot sensor measured at midswing, relative to its start position while standing|
|Lateral Step Variability | In a series of 3 consecutive foot placements of the same foot, the variability of perpendicular deviations of the middle foot placement from the line connecting the ﬁrst and third |
|Circumduction|The amount that the foot travels perpendicular to forward movement while swinging forward during an individual stride| 
|Foot Strike Angle |The angle of the foot at the point of initial contact. The pitch of the foot when ﬂat is zero and positive when the heel contacts ﬁrst|
|Toe Off Angle|The angle of the foot as it leaves the ﬂoor at push-off. The pitch of the foot when ﬂat is zero|
|Stance|The percentage of the gait cycle in which the foot is on the ground|
|Toe Out Angle|The lateral angle of the foot during the stance phase, relative to the forward motion of the gait cycle. Positive angle is outward rotation|


###                             ![Image of screencapture](images/GaitCycleDuration.jpg)
               Figure.2 Full Body Gait Measures: Gait Cycle Analysis (source:  APDM Wearable Technologies)


###                             ![Image of screencapture](images/DoubleSupport.jpg)
               Figure.3 Full Body Gait Measures: Double Support (source:  APDM Wearable Technologies)


###                             ![Image of screencapture](images/TeminalDoubleSupport.jpg)   
               Figure.4 Full Body Gait Measures: Terminal Double Support (source:  APDM Wearable Technologies)


###                             ![Image of screencapture](images/SPATIALANALYSIS.jpg)  
               Figure.5 Full Body Gait Measures: Special Analysis (source:  APDM Wearable Technologies)


###                             ![Image of screencapture](images/CIRCUMDUCTION.jpg) 
               Figure.6 Full Body Gait Measures: Circumduction (source:  APDM Wearable Technologies)


###                             ![Image of screencapture](images/ELEVATIONATMIDSWING.jpg)
               Figure.7 Full Body Gait Measures: Elevation at Midswing (source:  APDM Wearable Technologies)
  

###                             ![Image of screencapture](images/FootContactAngles.jpg)   
               Figure.8 Full Body Gait Measures: Foot Contact Angles (source:  APDM Wearable Technologies)

 

### Upper Limb

The upper limb or upper extremity is the region in the body extending from the deltoid region up to and including the hand, including the arm, axilla and shoulder.
The features of Upper Limb variable are put into onme Dataframe


### Fields Description of the Upper Limb 
 
The measures of the Upper Limb including the Arm Swing Velocity and Arm Swing Range of Motion. 

|    Field Name  | Description |
| ------------- | --------------------- |
| Arm Swing Velocity  |The maximum rotational velocity of the arm swing|
|Arm Swing Range of Motion | The angular range of the arm swing|


###                                ![Image of screencapture](images/Upperlimb.jpg)
                Figure.9 Sensor Configuration and Measures: Balance, Lower Limb Gait, Upper Limb Gait, 
                          Turning and Sit to Stand (source:  APDM Wearable Technologies)
  


### Fields Description of the Trunk Range of Motion

The measures of the Trunk Range of Motion including the Coronal, Sagittal and Transverse. 


|    Field Name  | Description |
| ------------- | --------------------- |
| Coronal   |The angular range of the thoracic spine in the sagittal plane (pitch) |
|Sagittal  | The angular range of the arm swing|
|Transverse|The angular range of the thoracic spine in the transverse plane (yaw)|


###                                ![Image of screencapture](images/TRUNKRANGEOFMOTION.jpg)
                             Figure.10 Trunk Range of Motion (source:  APDM Wearable Technologies) 


### Lumbar Range of Motion

All postural sway measures are assessed using the Opal movement sensor placed on a subject’s lumbar.  All metrics are reported in Coronal, Sagittal and Transverse planes.

### Fields Description of the Lumbar Range of Motion

The measures of the Lumbar Range of Motion including the Coronal, Sagittal and Transverse. 


|    Field Name  | Description |
| ------------- | --------------------- |
| Coronal   |The angular range of the lumbar spine in the coronal plane (roll)|
| Sagittal  | The angular range of the lumbar spine in the sagittal plane (pitch) |
|Transverse|The angular range of the lumbar spine in the transverse plane (yaw)|


###                                ![Image of screencapture](images/LumbarRangeofMotion.jpg)
                            Figure.11 Lumbar Range of Motion (source:  APDM Wearable Technologies)  


### Fields Description of Sit To Stand/ Stand To Sit

The measures of the Sit To Stand/ Stand To Sit including the Sit To Stand and Stand To Set.

#### Sit To Stand

|    Field Name  | Description |
| ------------- | --------------------- |
| Duration   |The duration of the sit to stand transition|
| Lean Angle  | The angular range of motion of the trunk during the sit to stand transition|

 
#### Stand To Sit

|    Field Name  | Description |
| ------------- | --------------------- |
| Duration   |The duration of the stand to sit transition|
| Lean Angle  | The angular range of motion of the trunk during the stand to sit transition|

###                                ![Image of screencapture](images/SitToStandAndStandToSet.jpg)
                                               Figure.12 Sit To Stand/Stand To Set  



### Turning Analysis

Postural measures are detected, analyzed, and averaged over the extent of the walking duration of the subject.

### Fields Description of the Turning 

The measures of the Turning including the Angle and Duration and Velocity.

|    Field Name  | Description |
| ------------- | --------------------- |
|Angle|The rotational angle of the turn|
|Duration|The duration of the turn|
|Velocity|The peak angular velocity of the turn|


###                                ![Image of screencapture](images/TurningAnalysis.jpg)
                              Figure.13 Turning Analysis (source:  APDM Wearable Technologies) 


### postural sway

All postural sway measures are assessed using the Opal movement sensor placed on a subject’s lumbar.  All metrics are reported in Coronal, Sagittal and Transverse planes.

### Fields Description of the postural sway

The measures of the postural sway including the Sway Area, RMS Sway, Coronal RMS Sway and Sagittal RMS Sway. 

|    Field Name  | Description |
| ------------- | --------------------- |
|Sway Area |The area of an ellipse covering 95% of the sway angle in both the coronal and sagittal planes |
|RMS Sway |The root mean square (RMS) of the sway angle in both the coronal and sagittal planes|
|Coronal RMS Sway |The root mean square (RMS) of the sway angle in the coronal plane |
|Sagittal RMS Sway|The root mean square (RMS) of the sway angle in the sagittal plane |


###                                ![Image of screencapture](images/POSTURALSWAY1.jpg)
                  Figure.14 Planar Acceleration, Sway Area and Rotation (source:  APDM Wearable Technologies)

###                                ![Image of screencapture](images/POSTURALSWAY2.jpg)
                       Figure.15 RMS Sway and Mean Velocity (source:  APDM Wearable Technologies) 


### Anticipatory Postural Adjustment 

Anticipatory postural adjustments are defined as the activation of postural muscles in a feedforward manner before a voluntary movement begins.

### Fields Description of the Anticipatory postural adjustments

The measures of the Anticipatory postural adjustments including 'First Step Duration' and 'First Step Range of Motion'.

|    Field Name  | Description |
| ------------- | --------------------- |
| First Step Duration |The duration of the period spanning from the end of the APA to the initial contact of the ﬁrst step|
|First Step Range of Motion | The integrated angular velocity of the stepping foot from the end of the APA to the initial contact of the step 




