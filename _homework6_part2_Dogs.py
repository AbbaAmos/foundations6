#!/usr/bin/env python
# coding: utf-8

# # Homework 6, Part Two: A dataset about dogs.
# 
# Data from [a FOIL request to New York City](https://www.muckrock.com/foi/new-york-city-17/pet-licensing-data-for-new-york-city-23826/)

# ## Do your importing and your setup

# In[1]:


pip install xlrd


# In[9]:


pip install openpyxl


# In[8]:


import pandas as pd
import matplotlib


# ## Read in the file `NYC_Dog_Licenses_Current_as_of_4-28-2016_xlsx` and look at the first five rows

# In[19]:


df = pd.read_excel('NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx')
df


# ## How many rows do you have in the data? What are the column types?
# 
# If there are more than 30,000 rows in your dataset, go back and only read in the first 30,000.

# In[20]:


df = df.count()
df


# ## Describe the dataset in words. What is each row? List two column titles along with what each of those columns means.
# 
# For example: “Each row is an animal in the zoo. `is_reptile` is whether the animal is a reptile or not”

# In[3]:


num_rows = df.count()
num_rows


# # Your thoughts
# 
# Think of four questions you could ask this dataset. **Don't ask them**, just write them down in the cell below. Feel free to use either Markdown or Python comments.

# In[ ]:





# # Looking at some dogs

# ## What are the most popular (primary) breeds of dogs? Graph the top 10.

# In[ ]:





# ## "Unknown" is a terrible breed! Graph the top 10 breeds that are NOT Unknown

# In[ ]:





# ## What are the most popular dog names?

# In[ ]:





# ## Do any dogs have your name? How many dogs are named "Max," and how many are named "Maxwell"?

# In[ ]:





# ## What percentage of dogs are guard dogs?
# 
# Check out the documentation for [value counts](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html).

# In[ ]:





# ## What are the actual numbers?

# In[ ]:





# ## Wait... if you add that up, is it the same as your number of rows? Where are the other dogs???? How can we find them??????
# 
# Use your `.head()` to think about it, then you'll do some magic with `.value_counts()`

# In[ ]:





# ## Fill in all of those empty "Guard or Trained" columns with "No"
# 
# Then check your result with another `.value_counts()`

# In[ ]:





# ## What are the top dog breeds for guard dogs? 

# In[ ]:





# ## Create a new column called "year" that is the dog's year of birth
# 
# The `Animal Birth` column is a datetime, so you can get the year out of it with the code `df['Animal Birth'].apply(lambda birth: birth.year)`.

# In[ ]:





# ## Calculate a new column called “age” that shows approximately how old the dog is. How old are dogs on average?

# In[ ]:





# # Joining data together

# In[ ]:





# ## Which neighborhood does each dog live in?
# 
# You also have a (terrible) list of NYC neighborhoods in `zipcodes-neighborhoods.csv`. Join these two datasets together, so we know what neighborhood each dog lives in. **Be sure to not read it in as `df`, or else you'll overwrite your dogs dataframe.**

# In[ ]:





# ## What is the most popular dog name in all parts of the Bronx? How about Brooklyn? The Upper East Side?

# In[ ]:





# ## What is the most common dog breed in each of the neighborhoods of NYC?

# In[ ]:





# In[ ]:





# ## What breed of dogs are the least likely to be spayed? Male or female?

# In[ ]:





# ## Make a new column called monochrome that is True for any animal that only has black, white or grey as one of its colors. How many animals are monochrome?

# In[ ]:





# ## How many dogs are in each borough? Plot it in a graph.

# In[ ]:





# ## Which borough has the highest number of dogs per-capita?
# 
# You’ll need to merge in `population_boro.csv`

# In[ ]:





# ## Make a bar graph of the top 5 breeds in each borough.
# 
# How do you groupby and then only take the top X number? You **really** should ask me, because it's kind of crazy.

# In[ ]:





# ## What percentage of dogs are not guard dogs?

# In[ ]:




