# Pandas Assignment


```python
Q1. How do you load a CSV file into a Pandas DataFrame?
Ans:
    Import a CSV file using the read_csv() function from the pandas library. 
    Set a column index while reading your data into memory. 
    Specify the columns in your data that you want the read_csv() function to return. 
    Read data from a URL with the pandas.
```


```python
Q2. How do you check the data type of a column in a Pandas DataFrame?
Ans:
    To check the data type in pandas DataFrame we can use the “dtype” attribute. 
    The attribute returns a series with the data type of each column. 
    And the column names of the DataFrame are represented as the index of the resultant series object and the corresponding data types are returned as values of the series object.
```


```python
Q3. How do you select rows from a Pandas DataFrame based on a condition?
Ans:
    You can perform basic operations on Pandas DataFrame rows like selecting, deleting, adding, and renaming.
    Create a Pandas DataFrame with data.
    Selecting rows using loc[].
    Select rows based on condition using loc.
    Using 'loc' and '!'
    Combine multiple conditions with & operator.
    Selected columns using loc
```


```python
Q4. How do you rename columns in a Pandas DataFrame?
Ans:
    4 Ways to Rename Pandas Columns
    Method 1: using rename() function.
    Method 2: assigning list of new column names.
    Method 3: replacing the columns string.
    Method 4: using set_axis() function.
```


```python
Q5. How do you drop columns in a Pandas DataFrame?
Ans:
    Use del Keyword to Drop First Column
    
    Alternatively, you can also use del df[df. columns[0]] to remove the first column of the Pandas DataFrame. 
    Here, it will select all columns except the first column of DataFrame.
```


```python
Q6. How do you find the unique values in a column of a Pandas DataFrame?
Ans:
    To select the unique values from a specific column in a Pandas dataframe you can use the unique() method. 
    This is simply appended to the end of the column name, e.g. df['column_name']. 
    unique() and returns a Python list of the unique values.
```


```python
Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
Ans:
    (1) Count NaN values under a single DataFrame column: df['column name'].isna().sum()
    (2) Count NaN values under an entire DataFrame: df.isna().sum().sum()
    (3) Count NaN values across a single DataFrame row: df.loc[[index value]].isna().sum().sum()
```


```python
Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
Ans:
    In order to fill missing values in an entire Pandas DataFrame, we can simply pass a fill value into the value= parameter of the . fillna() method. 
    The method will attempt to maintain the data type of the original column, if possible.
```


```python
Q9. How do you concatenate two Pandas DataFrames?
Ans:
    We'll pass two dataframes to pd. concat() method in the form of a list and mention in which axis you want to concat, i.e. axis=0 to concat along rows, axis=1 to concat along columns.
```


```python
Q10. How do you merge two Pandas DataFrames on a specific column?
Ans:
    Pandas DataFrame merge() Function Syntax
    These are similar to SQL left outer join, right outer join, full outer join, and inner join. on: Column or index level names to join on. 
    These columns must be present in both the DataFrames. 
    If not provided, the intersection of the columns in both DataFrames are used.
```


```python
Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?
Ans:
    Groupby() is a powerful function in pandas that allows you to group data based on a single column or more. 
    You can apply many operations to a groupby object, including aggregation functions like sum(), mean(), and count(), as well as lambda function and other custom functions using apply().
```


```python
Q12. How do you pivot a Pandas DataFrame?
Ans:
    CREATE YOUR OWN PANDAS PIVOT TABLE IN 4 STEPS
    1. Download or import the data that you want to use.
    2. In the pivot_table function, specify the DataFrame you are summarizing, along with the names for the indexes, columns and values.
    3. Specify the type of calculation you want to use, such as the mean. 
    4. Use multiple indexes and column-level grouping to create a more powerful summary of the data. 
```


```python
Q13. How do you change the data type of a column in a Pandas DataFrame?
Ans:
    Change column type in pandas using DataFrame.apply() 
    to_numeric, pandas. to_datetime, and pandas. to_timedelta as arguments to apply the apply() function to change the data type of one or more columns to numeric, DateTime, and time delta respectively.
```


```python
Q14. How do you sort a Pandas DataFrame by a specific column?
Ans:
    Sorting Your DataFrame on a Single Column. 
    To sort the DataFrame based on the values in a single column, you'll use . sort_values() . By default, this will return a new DataFrame sorted in ascending order.
```


```python
Q15. How do you create a copy of a Pandas DataFrame?
Ans:
    pandas.DataFrame.copy
```


```python
import pandas as pd

data = [['dom', 10], ['abhi', 15], ['celeste', 14]]
df = pd. DataFrame(data, columns = ['Name', 'Age'])

df_deep_copy = df. copy(deep=True)

print("Original Dataframe - \n")
```

    Original Dataframe - 
    
    


```python
Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
Ans:
    To filter Pandas DataFrame by multiple conditions use DataFrame. loc[] property along with the conditions. 
    Make sure you surround each condition with a bracket. 
    Here, we will get all rows having Fee greater or equal to 24000 and Discount is less than 2000 and their Courses start with 'P' from the DataFrame.
```


```python
Q17. How do you calculate the mean of a column in a Pandas DataFrame?
Ans:
    To calculate the mean of whole columns in the DataFrame, use pandas.Series.mean() with a list of DataFrame columns. 
    You can also get the mean for all numeric columns using DataFrame.mean(), use axis=0 argument to calculate the column-wise mean of the DataFrame.
```


```python
Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
Ans:
    Standard deviation is calculated using the function.std(). 
    However, the Pandas library creates the Dataframe object and then the function.std() is applied on that Dataframe 
```


```python
Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
Ans:
    Print the input DataFrame, df.Initialize two variables, col1 and col2, and assign them the columns that you want to find the correlation of. 
    Find the correlation between col1 and col2 by using df[col1]. corr(df[col2]) and save the correlation value in a variable, corr.
```


```python
Q20. How do you select specific columns in a DataFrame using their labels?
Ans:
    You can use the following methods to select columns by name in a pandas DataFrame:
    Method 1: Select One Column by Name df. loc[:, 'column1']
    Method 2: Select Multiple Columns by Name df. loc[:, ['column1', 'column3', 'column4']]
    Method 3: Select Columns in Range by Name df. loc[:, 'column2':'column4']
```


```python
Q21. How do you select specific rows in a DataFrame using their indexes?
Ans:
    To select the rows, the syntax is df. loc[start:stop:step] ; where start is the name of the first-row label to take, stop is the name of the last row label to take, and step as the number of indices to advance after each extraction; for example, you can use it to select alternate rows.
```


```python
Q22. How do you sort a DataFrame by a specific column?
Ans:
    Sorting Your DataFrame on a Single Column. 
    To sort the DataFrame based on the values in a single column, you'll use .sort_values().By default, this will return a new DataFrame sorted in ascending order.
```


```python
Q23. How do you create a new column in a DataFrame based on the values of another column?
Ans:
    You can add/append a new column to the DataFrame based on the values of another column using df. assign() , df. apply() , and, np. where() functions and return a new Dataframe after adding a new column.
```


```python
Q24. How do you remove duplicates from a DataFrame?

Ans:
    Pandas DataFrame drop_duplicates() Method
    
    The drop_duplicates() method removes duplicate rows. 
    Use the subset parameter if only some specified columns should be considered when looking for duplicates.
```


```python
Q25. What is the difference between .loc and .iloc in Pandas?
Ans:
    Loc and iloc are two functions in Pandas that are used to slice a data set in a Pandas DataFrame. 
    The function .loc is typically used for label indexing and can access multiple columns, while .iloc is used for integer indexing.
```


```python

```


```python

```


```python

```
