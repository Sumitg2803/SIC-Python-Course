'''
**What are pandas in python?
    *Pandas is a data analysis library in python
    *Pandas is used for data manipulation and analysis
    *Pandas is used for data cleaning and preprocessing
    *Pandas is used for data visualization
    *Pandas is used for data storage and retrieval
    *Pandas is used for data analysis and machine learning
    *Pandas is used for data visualization and data presentation
    *Pandas is used for data analysis and data mining
    *Pandas is used for data analysis and data warehousing
    *Pandas is used for data analysis and data integration

    *Data ko analysis karte hai using pnda lib
    *panda is open source python lib used for data analysis, data manipulation, data cleaning, handel the structure data

**Why pandas require?
    *python alone is not sufficient for large dataset
    *pandas helps to produce large dataset easily 
    *clean missing or incorrect data
    *analyse data quickly
    *handel real world data

**Features of pandas
    *Data structure
    *Data analysis
    *Data visualization
    *Data cleaning
    *Data preprocessing
    *Data storage and retrieval
    *Data analysis and machine learning
    *Data visualization and data presentation
    *Data analysis and data mining
    *Data analysis and data warehousing
    *Data analysis and data integration
    *handel the incorrect data
    *handel the duplicate data
    *handel the data types
    *handel the data quality
    *handel the data consistency
    *handel the data validation
    *handel the data transformation
    *handel the data integration
    *handel the data visualization
    *handel the data analysis
    *handel the data preprocessing
    *handel the data storage and retrieval
    *handel the data analysis and machine learning
    *handel the data visualization and data presentation
    *handel the data analysis and data mining
    *handel the data analysis and data warehousing
    *handel the data analysis and data integration

    *fast and effiecient
    *easy data handeling
    *powerful data analysis tool
    *support multiple file format
    *handel the missing data

panda mainly use two dataframe
1.) series
2.) dataframe

'''

# #example
# import pandas as pd
# data = pd.Series([1,2,3,4,5])
# print(data)
# print(type(data))

# #example
# import pandas as pd
# data = ({
#     "Name": ["Sumit", "Prathmesh", "Rahul", "Sonal", "Pratik", "Kumari"],
#     "Age": [21, 22, 23, 24, 25, 26],
#     "Gender": ["Male", "Male", "Male", "Female", "Male", "Female"],
#     "City": ["Pune", "Mumbai", "Pune", "Mumbai", "Pune", "Mumbai"]
# })
# df=pd.DataFrame(data)
# print(df)
# print(type(df))

# #average marks calculator
# import pandas as pd

# data = {
#     "name":["sumit", "prathmesh", "rahul", "sonal", "pratik", "kumari"],
#     "marks":[45, 46, 47, 48, 49, 50]
# }
# df=pd.DataFrame(data)
# print(df)
# print("Average Marks: ", df["marks"].mean())

# #filling marks at missing values and getting average
# import pandas as pd

# data = {
#     "name":["sumit", "prathmesh", "rahul", "sonal", "pratik", "kumari"],
#     "marks":[45, 46, None, 48, 49, 50]
# }
# df=pd.DataFrame(data)
# print("Before filling")
# print(df)

# df["marks"] = df["marks"].fillna(0)
# print("After filling")
# print(df)
# print("Average Marks: ", df["marks"].mean())

# #example: 👇👇 
# import pandas as pd

# data= {
#     "Name":["Amit", "Neha", "Rahul", "Sumit", "Pratik", "Kumari"],
#     "Marks":[60, 80, None, 100, 70, 80],
#     "Gender":["Male", "Female", "Male", "Male", "Male", "Female"],
#     "Department":["CSE", "IT", "CSE", "IT", "CSE", "IT"]
# }

# df=pd.DataFrame(data) 
# print(df)

# #print first 3 rows
# print("\nFirst 3 rows:\n")
# print(df.head(3))

# #shape and data type
# print("\nShape:", df.shape)
# print("\nData Types:\n",df.dtypes)

# #handing missing values
# print("\nHandling misssing values:\n")
# df["Marks"] = df["Marks"].fillna(0)
# print(df)

# #add result column
# print("\nAdd result column:\n")
# df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 75 else "Fail")
# print(df)

# #filter pass students
# print("\nFilter pass students:\n")
# pass_student = df[df["Result"]== "Pass"]
# print(pass_student)

# #filter fail students
# print("\nFilter fail students:\n")
# fail_student = df[df["Result"]== "Fail"]
# print(fail_student)

# #finding average marks
# print("\nAverage marks:\n")
# print(df["Marks"].mean())

# #sorting values in ascending order
# print("\nSorting values:\n")
# df_sorted = df.sort_values(by="Marks", ascending=True)
# print(df_sorted)

# #sorting values in descending order
# print("\nSorting values in descending order:\n")
# print(df.sort_values(by="Marks", ascending=False))

# #group by department
# print("\nGroup by department:\n")
# print(df.groupby("Department").sum())

# #save report to CSV
# df_sorted.to_csv("sorted_report.csv", index=False)

'''
**some students marks are missing- 
    *create dataframe, 
    *idetify missing value,
    *replace missing with 0,
    *display student who score more than 70
'''
import pandas as pd

data1 = {
    "Name": ["Rohan", "Sumit", "Kumari", "Rajkumari", "Atharv", "Priya"],
    "Marks": [45, 46, None, 48, 49, 50],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Female"],
    "Department": ["CSE", "IT", "CSE", "IT", "CSE", "IT"]
}

#dataframe
df1=pd.DataFrame(data1)
print(df1)

#identify missing value
missing=df1.isnull()


'''
Student result analysis
    a college has student result data with missing marks
    *create dataframe
    *filling missing marks with avg marks
    *add new coloum result - if 'marks>75' == pass else 'fail'
    *display only pass student
    *department wise avg marks
'''
