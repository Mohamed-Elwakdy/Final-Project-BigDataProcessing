import pandas as pd  
import h5py
import hdfdict

f =  h5py.File("C:/Clarkson University - Materials 2/IA 626 - Big Data Processing and Cloud Service/Final Project/Dr Ali - Materials for Final Project\Dr - Ali Sample/Walking/walking5.h5",'r')
for name in f:
    print(name)

res = hdfdict.load("C:/Clarkson University - Materials 2/IA 626 - Big Data Processing and Cloud Service/Final Project/Dr Ali - Materials for Final Project\Dr - Ali Sample/Walking/walking5.h5")
print(res.keys())


### Events/Gait/Lower Limb/

All_Steps_Left = res['Events']['Gait']['Lower Limb']['All Steps Left']
df1 = pd.DataFrame(All_Steps_Left)
df1.columns = ['GaitLowerLimbAllStepsLeft']

All_Steps_Right = res['Events']['Gait']['Lower Limb']['All Steps Right']
df2 = pd.DataFrame(All_Steps_Right)
df2.columns = ['GaitLowerLimbAllStepsRight']

Cycle_Validity_with_Heel_Strike_Times = res['Events']['Gait']['Lower Limb']['Cycle Validity with Heel Strike Times']
df3 = pd.DataFrame(Cycle_Validity_with_Heel_Strike_Times)
df3.columns = ['CycleValiditywithHeelStrikeTimes1','CycleValiditywithHeelStrikeTimes2','CycleValiditywithHeelStrikeTimes3','CycleValiditywithHeelStrikeTimes4']


### Measures/Anticipatory Postural Adjustment


First_Step_Duration = res['Measures']['Anticipatory Postural Adjustment']['First Step Duration']
df4 = pd.DataFrame(First_Step_Duration)
df4.columns = ['AnticipatoryPosturalAdjustmentFirstStepDuration']

First_Step_Range_of_Motion = res['Measures']['Anticipatory Postural Adjustment']['First Step Range of Motion'] 
df5 = pd.DataFrame(First_Step_Range_of_Motion)
df5.columns = ['AnticipatoryPosturalAdjustmentFirstStepRangeofMotion']


### Measures/Gait/Joint/Back

Measures_Gait_Joint_Back_Abduction_Maximum = res['Measures']['Gait']['Joint']['Back']['Abduction']['Maximum']
df6 = pd.DataFrame(Measures_Gait_Joint_Back_Abduction_Maximum)
df6.columns = ['GaitJointBackAbductionMaximum']

Measures_Gait_Joint_Back_Abduction_Minimum = res['Measures']['Gait']['Joint']['Back']['Abduction']['Minimum']
df7 = pd.DataFrame(Measures_Gait_Joint_Back_Abduction_Minimum)
df7.columns = ['GaitJointBackAbductionMinimum']

Measures_Gait_Joint_Back_Flexion_Maximum = res['Measures']['Gait']['Joint']['Back']['Flexion']['Maximum']
df8 = pd.DataFrame(Measures_Gait_Joint_Back_Flexion_Maximum)
df8.columns = ['GaitJointBackFlexionMaximum']

Measures_Gait_Joint_Back_Flexion_Minimum = res['Measures']['Gait']['Joint']['Back']['Flexion']['Minimum']
df9 = pd.DataFrame(Measures_Gait_Joint_Back_Flexion_Minimum)
df9.columns = ['GaitJointBackFlexionMinimum']

Measures_Gait_Joint_Back_Rotation_Maximum = res['Measures']['Gait']['Joint']['Back']['Rotation']['Maximum']
df10 = pd.DataFrame(Measures_Gait_Joint_Back_Rotation_Maximum)
df10.columns = ['GaitJointBackRotationMaximum']

Measures_Gait_Joint_Back_Rotation_Minimum = res['Measures']['Gait']['Joint']['Back']['Rotation']['Minimum']
df11 = pd.DataFrame(Measures_Gait_Joint_Back_Rotation_Minimum)
df11.columns = ['GaitJointBackRotationMinimum']

### Measures/Gait/Lower Limb

Measures_Gait_LowerLimb_GaitCycleDuration= res['Measures']['Gait']['Lower Limb']['Gait Cycle Duration']
df12 = pd.DataFrame(Measures_Gait_LowerLimb_GaitCycleDuration)
df12.columns = ['GaitLowerLimbGaitCycleDurationInSecondsStart','MeasuresGaitLowerLimbGaitCycleDurationInSecondsEnd']

Measures_Gait_LowerLimb_Gait_Speed= res['Measures']['Gait']['Lower Limb']['Gait Speed']
df13 = pd.DataFrame(Measures_Gait_LowerLimb_Gait_Speed)
df13.columns = ['GaitLowerLimbGaitSpeed1','MeasuresGaitLowerLimbGaitSpeed2']

Measures_Gait_LowerLimb_NumberStepsInTurn= res['Measures']['Gait']['Lower Limb']['No. Steps in Turn']
df14 = pd.DataFrame(Measures_Gait_LowerLimb_NumberStepsInTurn)
df14.columns = ['GaitLowerLimbNumberStepsInTurnPerMinute1', 'MeasuresGaitLowerLimbNumberStepsInTurnPerMinute2']

Measures_Gait_LowerLimb_StepDuration= res['Measures']['Gait']['Lower Limb']['Step Duration']
df15 = pd.DataFrame(Measures_Gait_LowerLimb_StepDuration)
df15.columns = ['GaitLowerLimbStepDurationOfOneFoot','MeasuresGaitLowerLimbStepDurationOfOppositeFoot']

Measures_Gait_LowerLimb_StrideLength= res['Measures']['Gait']['Lower Limb']['Stride Length']
df16 = pd.DataFrame(Measures_Gait_LowerLimb_StrideLength)
df16.columns = ['GaitLowerLimbStrideLength1','MeasuresGaitLowerLimbStrideLength2']

Measures_Gait_LowerLimb_Swing= res['Measures']['Gait']['Lower Limb']['Swing']
df17 = pd.DataFrame(Measures_Gait_LowerLimb_Swing)
df17.columns = ['GaitLowerLimbSwingFootisNotOnTheGround1inCm1','MeasuresGaitLowerLimbSwingFootisNotOnTheGround1inCm2']

Measures_Gait_LowerLimb_Swing= res['Measures']['Gait']['Lower Limb']['Swing']
df18 = pd.DataFrame(Measures_Gait_LowerLimb_Swing)
df18.columns = ['GaitLowerLimbSwingFootisNotOnTheGround1inCm1','MeasuresGaitLowerLimbSwingFootisNotOnTheGround1inCm2']

Measures_Gait_TerminalDoubleSupport= res['Measures']['Gait']['Lower Limb']['Terminal Double Support']
df19 = pd.DataFrame(Measures_Gait_TerminalDoubleSupport)
df19.columns = ['GaitTerminalDoubleSupportForOneFeet','MeasuresGaitTerminalDoubleSupportForOppositeFeet']

Measures_Gait_TurnDuration= res['Measures']['Gait']['Lower Limb']['Turn Duration']
df20= pd.DataFrame(Measures_Gait_TurnDuration)
df20 = df20[[0]]
df20.columns = ['Gait_TurnDuration']

Measures_Gait_TurnPerStep= res['Measures']['Gait']['Lower Limb']['Turn Per Step']
df21 = pd.DataFrame(Measures_Gait_TurnPerStep)
df21 = df21[[0]]
df21.columns = ['GaitTurnPerStep']

Measures_Gait_TurnRate= res['Measures']['Gait']['Lower Limb']['Turn Rate']
df22 = pd.DataFrame(Measures_Gait_TurnRate)
df22 = df22[[0]]
df22.columns = ['GaitTurnRate']

### Measures/Gait/Upper Limb

Measures_Gait_UpperLimb_MaximumVelocity = res['Measures']['Gait']['Upper Limb']['Maximum Velocity']
df23 = pd.DataFrame(Measures_Gait_UpperLimb_MaximumVelocity)
df23.columns = ['MaximumRotationalVelocityofTheArmSwing1','MaximumRotationalVelocityofTheArmSwing2']

Measures_Gait_UpperLimb_RangeofMotion = res['Measures']['Gait']['Upper Limb']['Range of Motion']
df24 = pd.DataFrame(Measures_Gait_UpperLimb_RangeofMotion)
df24.columns = ['TheAngularRangOfTheArmSwing1','TheAngularRangOfTheArmSwing2']


### Measures/Turns

Measures_Turns_Angle = res['Measures']['Turns']['Angle']
df25 = pd.DataFrame(Measures_Turns_Angle)
df25.columns = ['TheRotationalAngleOfTheTurnInDegree']

Measures_Turns_PeakVelocity = res['Measures']['Turns']['Peak Velocity']
df26 = pd.DataFrame(Measures_Turns_PeakVelocity)
df26.columns = ['PeakAngularVelocityOfTheTurn']

Measures_Turns_Steps = res['Measures']['Turns']['Steps']
df27 = pd.DataFrame(Measures_Turns_Steps)
df27.columns = ['NumberOfStepsInTurns','TimeOfTurnsBasedOnTheNumberOfSteps']


### collect the dataframes in many gropus based on the number of rows

df_Group1 = pd.concat([df1, df2, df3], axis=1, sort=False)

df_Group2 = pd.concat([df4, df5], axis=1, sort=False)

df_Group3 = pd.concat([df6, df7, df8,df9,df10,df11], axis=1, sort=False)

df_Group4 = pd.concat([df12,df13,df15,df16,df17,df18,df19], axis=1, sort=False)

df_Group5 = pd.concat([df23,df24], axis=1, sort=False)

df_Group6 = pd.concat([df14, df20, df21, df22], axis=1, sort=False)

df_Group7 = pd.concat([df25, df26, df27], axis=1, sort=False)


### Convert the groups of dataframes to CSV files

Group1_ConvertCSV= df_Group1.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Group1-DataFrame.csv', index = False, header=True)

Group2_ConvertCSV= df_Group2.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Group2-DataFrame.csv', index = False, header=True)

Group3_ConvertCSV= df_Group3.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Group3-DataFrame.csv', index = False, header=True)

Group4_ConvertCSV= df_Group4.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Group4-DataFrame.csv', index = False, header=True)

Group5_ConvertCSV= df_Group5.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Group5-DataFrame.csv', index = False, header=True)

Group6_ConvertCSV= df_Group6.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Group6-DataFrame.csv', index = False, header=True)

Group7_ConvertCSV= df_Group7.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Group7-DataFrame.csv', index = False, header=True)

## Combined 3 csv files in one csv file 


df_Group3  = pd.read_csv('C:/Clarkson University - Materials 2/IA 626 - Big Data Processing and Cloud Service/Final Project/Dr Ali - Materials for Final Project/Dr - Ali Sample/Walking/Group3-DataFrame.csv')

df_Group4  = pd.read_csv('C:/Clarkson University - Materials 2/IA 626 - Big Data Processing and Cloud Service/Final Project/Dr Ali - Materials for Final Project/Dr - Ali Sample/Walking/Group4-DataFrame.csv')

df_Group5  = pd.read_csv('C:/Clarkson University - Materials 2/IA 626 - Big Data Processing and Cloud Service/Final Project/Dr Ali - Materials for Final Project/Dr - Ali Sample/Walking/Group5-DataFrame.csv')

Groups_combine_3_4_5 = pd.concat([df_Group3,df_Group4,df_Group5], axis=1, sort=False)

Groups_combined= Groups_combine_3_4_5.to_csv (r'C:\Clarkson University - Materials 2\IA 626 - Big Data Processing and Cloud Service\Final Project\Dr Ali - Materials for Final Project\Dr - Ali Sample\Walking\Groups_combined.csv', index = False, header=True)

## Put dataframes (many groups) in many spreadsheets of one excel file 

writer = pd.ExcelWriter('C:/Clarkson University - Materials 2/IA 626 - Big Data Processing and Cloud Service/Final Project/Dr Ali - Materials for Final Project/Dr - Ali Sample/Walking/Combined in many sheets.xlsx')
df_Group1.to_excel(writer, sheet_name='sheet1', index=False)
df_Group2.to_excel(writer, sheet_name='sheet2', index=False)
Groups_combine_3_4_5.to_excel(writer, sheet_name='sheet3', index=False)
df_Group6.to_excel(writer, sheet_name='sheet4', index=False)
df_Group7.to_excel(writer, sheet_name='sheet5', index=False)
writer.save()



'''
Events/Gait/Lower Limb/All Steps Left # df1 = 113 rows
Events/Gait/Lower Limb/All Steps Right  # df2 = 113 rows
Events/Gait/Lower Limb/Cycle Validity with Heel Strike Times  # df3 = 113 rows 

--------------------------------
Measures/Anticipatory Postural Adjustment/First Step Duration # df4 = one row
Measures/Anticipatory Postural Adjustment/First Step Range of 
Measures/Duration # df5 = one row
---------------------------
Measures/Gait/Joint/Back/Abduction/Maximum # df6 = 25 rows 
Measures/Gait/Joint/Back/Abduction/Minimum # df7 = 25 rows 

Measures/Gait/Joint/Back/Flexion/Maximum   # df8 = 25 rows 
Measures/Gait/Joint/Back/Flexion/Minimum   # df9 = 25 rows 

Measures/Gait/Joint/Back/Rotation/Maximum  # df10 = 25 rows 
Measures/Gait/Joint/Back/Rotation/Minimum  # df11 = 25 rows

---------------------
Measures/Gait/Lower Limb/Gait Cycle Duration # df12 = 25 rows
Measures/Gait/Lower Limb/Gait Speed          # df13 = 25 rows
Measures/Gait/Lower Limb/No. Steps in Turn   # df14 = 22 rows
Measures/Gait/Lower Limb/Step Duration       # df15 = 25 rows 
Measures/Gait/Lower Limb/Stride Length       # df16 = 25 rows 
Measures/Gait/Lower Limb/Swing               # df17 = 25 rwos
Measures/Gait/Lower Limb/Terminal Double Support # df18 = 25 rows
Measures/Gait/Lower Limb/Terminal Double Support For One Feet # df19 = 25 rows 
Measures/Gait/Lower Limb/Turn Duration           # df20 = 22 rows
Measures/Gait/Lower Limb/Turn Per Step           # df21 = 22 rows
Measures/Gait/Lower Limb/Turn Rate               # df22 = 22 rows
----------------------------------

Measures/Gait/Upper Limb/Maximum Velocity        # df23 = 25 rows
Measures/Gait/Upper Limb/Range of Motion         # df24 = 25 rows

----------------------------------
Measures/Turns/Angle                             # df25 = 21 rows 
Measures/Turns/Peak Velocity                     # df26 = 21 rows 
Measures/Turns/Steps                             # df27 = 21 rows

'''
