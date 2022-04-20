import pandas as pd

#Reading the file into a dataframe
data=pd.read_csv('D3_Heart_Dataset.csv')
#Displaying the read contents
# print(data)

#Finding datatype of data
# print( type(data) )

# print( data.info())
#This information shows that each column has 918 entries.
#Non of the columns contain any 'null' value.
#There are 5 attributes with datatype of 'object'/'string'.

#The following method is used to count the possible values in a column
# print( data['ExerciseAngina'].value_counts() )
#This shows that there are two possible values for this attribute: 'Y' or 'N'.
#Also there are 547 entries for 'N' and 371 entries for 'Y'.

#The simplest way to encode 'ExerciseAngina' as dummy varaibale is to use the replace method.
data['ExerciseAngina']=data['ExerciseAngina'].replace('Y',1)
data['ExerciseAngina']=data['ExerciseAngina'].replace('N',0)
# print( data)
#Observe that values of the column 'ExerciseAngina' have been cahnged to 0 and 1.

# print( data['ChestPainType'].value_counts())
#This column contains 4 different values ASY, NAP, ATA, TA

data['ChestPainType']=data['ChestPainType'].replace('TA',1)
data['ChestPainType']=data['ChestPainType'].replace('ATA',2)
data['ChestPainType']=data['ChestPainType'].replace('NAP',3)
data['ChestPainType']=data['ChestPainType'].replace('ASY',4)
# print( data['ChestPainType'])

#get_dummies is a simple method in pandas which can achieve this task.
print( pd.get_dummies(data, columns=['Gender']))
#The resulting table has two dummy variable encoded columns Gender_F and Gender_M, in place of one column Gender

#All the cahnges that we have made so far are done on the dataframe, and not in the original csv file.
#The to_csv method can be used to save the dataframe into a csv file.
data.to_csv('D3_Heart_Dataset_Clean.csv')