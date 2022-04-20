import pandas as pd
#Reading the file into a dataframe using pandas method 'read_csv'
data=pd.read_csv('D1_Movie_Revenue_Dataset.csv')
#Displaying the read contents
# print(data)

#Finding datatype of data
# print(type(data))
#The data has been read as a dataframe

# print(data.info())
#This information shows that each column has 6169 entries.
#Non of the columns contain any 'null' value, however we kmow that there are some unwanted values ('unknown' and 0) in some columns.
#Datatype of only first column is 'integer', and remaining are 'object' showing that these are read as strings.

#lets rexplore the new clean file in python.
#run the following two methods and observe the information these methods provide.
clean_data=pd.read_csv('D1_Movie_Revenue_Dataset_Clean.csv')
print(clean_data.info())
print(clean_data.describe())