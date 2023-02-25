#!/usr/bin/env python
# coding: utf-8

# # Assignment_23-02-2023

# ## 1. Create a Pandas Series that contains the following data: 4,8,15,16,23,and 42. Then, Print the Series.
# 
# ### Ans:-
# 

# In[1]:


import pandas as pd
data = [4,8,15,16,23,42]
series = pd.Series(data)
print(series)


# ## 2. Create a variable of list type containing 10 elements in it, and apply pandas. Series functionon the variable print it.
# 
# ### Ans:-
# 

# In[2]:


my_list =['Manas',1980,'padmaja',1957,'Jagadish','1955','Sejal',2014,'Sunandini',1988]
series =pd.Series(my_list)
print(series)


# In[3]:


type (my_list)


# ## 3. Create a Pandas Dataframe that contains the following data:
# |Name|      |Age|     |Gender|
# |----|      |---|     |------|
# |Alice|     |25 |     |Female|
# |Bob|       |30 |     |Male  |
# |Claire|    |27 |     |Female|
# 
# ## Then, print the dataframe.

# In[4]:


import pandas as pd
df=pd.read_csv('C:\\Users\\MANAS RANJAN PANDEY\\Desktop\\Pandas.csv')


# In[5]:


df.head()


# In[6]:


df.dtypes


# In[7]:


import pandas as mp
df=mp.read_csv('C:\\Users\\MANAS RANJAN PANDEY\\Desktop\\Pandas.csv')


# In[8]:


df.dtypes


# In[9]:


type(df[['Name','Age','Gender']])


# In[10]:


df[['Name','Age','Gender']]


# ## 4.What is 'Data Frame' in pandas and how is it different from pandas. Series? Explain with an example.
# 
# ### Ans:-
# 
#             In Pandas, a DataFrame is a two-dimensional labeled data structure that consists of rows and columns. It is 
#             similar to a spreadsheet or a SQL table. You can think of a DataFrame as a collection of Pandas Series objects
#             that share the same index.
#             
#             A Pandas Series, on the other hand, is a one-dimensional labeled array that can hold any data type
#             (integer, string, float, Python objects, etc.) and has an associated label, called an index.
#             
#             
# 

# In[11]:


import pandas as pd
## Create a Series
s = pd.Series([1,2,3,4,5,6],name='numbers')

## Create a DataFrame
df=pd.DataFrame({'name':['Manas','Tapas','Sejal','Sunandini','Jagadish','Padmaja'],
                'Age':[42,36,9,34,69,67],
                'Gender':['M','M','F','F','M','F'],
                'numbers':s})
print("Series: ")
print(s)
print()

print("Data Frame: ")
print(df)


#  ###      
#              As you can see, the Series only has one column of data with an index, while the DataFrame has multiple columns
#              of data with row and column indices. The DataFrame is a more complex data structure that can hold multiple 
#              Series and is better suited for data analysis and manipulation.

# ## 5. What are some common functions you can use to manipulation data in pandas Data Frame? Can you give an example of when you might use one of these functions?
# 
# ### Ans :-
# 
#             Pandas provides a wide range of functions that can be used to manipulate data in a DataFrame. Here are some 
#             common functions that you can use:
# 
#     1.head():- This function returns the first n rows of a DataFrame. It is useful for quickly checking the structure and
#               content of a DataFrame.
#               
#     2.describe():- This function generates descriptive statistics of a DataFrame, including count, mean, standard deviation, 
#                   minimum, maximum, and quartiles.
#                   
#     3.sort_values():- This function sorts a DataFrame by one or more columns in ascending or descending order.
#     
#     4.groupby():- This function groups a DataFrame by one or more columns and applies a function to each group.
#     
#     5.pivot_table():- This function creates a pivot table from a DataFrame.
# 

# In[12]:


## Example of all the above manipulation data in Pandas.

df=pd.read_csv('C:\\Users\\MANAS RANJAN PANDEY\\Desktop\\Pandas.csv')


# In[13]:


print(df.head(6))


# In[14]:


# generate descriptive statistics
print(df.describe())


# In[15]:


# sort by age in descending order
print(df.sort_values('Name',ascending=True))


# In[16]:


print(df.sort_values('Name',ascending=False))


# In[17]:


# group by gender and calculate the mean age

print(df.groupby('Gender')['Age'].mean())


# In[18]:


# create a pivot table that shows the mean age by gender and name

print(pd.pivot_table(df,values ='Age',index='Name',columns='Gender',aggfunc='mean'))


# ### 
#         These are just a few examples of the many functions available in pandas for data manipulation. The specific 
#         function(s) you use will depend on your particular data analysis needs.

# ## 6. Which of the following is mutable in nature series, Data Frame, Panel?
# 
# ### Ans:-
# 
#             In Pandas, both Series and DataFrame are mutable, meaning that you can modify their content. However, Panel 
#             is not mutable, as it has been deprecated since version 0.25.0 and replaced with MultiIndex functionality in 
#             DataFrames.
#             
#             

# In[19]:


## Create a dataframe
data={'name':['Manas','Tapas','Sejal'],
     'age':[42,36,9]}
df=pd.DataFrame(data)


# In[20]:


print(df)


# In[21]:


## add a new column
df['gender']=['M','M','F']

print(df)


# ### 
#         To modify a Series or DataFrame, you can directly modify its values, add or delete rows or columns, or use Pandas 
#         built-in functions to apply transformations to the data. Note that modifying a Series or DataFrame in place can have
#         unintended consequences, so it's important to keep track of your changes and make sure they are correct.

# ## 7. Create a Data Frame using multiple series.Explain with an example.
# 
# ### Ans:-
# 
#             In Pandas, you can create a DataFrame using multiple Series. A Series is a one-dimensional labeled array that
#             can hold any data type, such as integers, floats, strings, or even other Python objects.
# 

# In[22]:


## Example of how to create a DataFrame using multiple Series:

names = pd.Series(['Manas','Tapas','Sunandini','Sejal','Jagadish','Padmaja'])
ages = pd.Series([42,34,9,69,67])
genders = pd.Series(['M','M','F','F','M','F'])

# create a DataFrame using the three Series
df=pd.DataFrame({'name':names,'age':ages,'gender': genders})
print(df)

