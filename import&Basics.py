import os
import pandas as pd

#Basics for web scraping
# 1. create a list
states=["Odisha","Chhattisgarh","Goa","Punjab"]
population=[223,555,666,777]
# 2. create a list
dict={'states':states,'population':population}

# 3. create dataframe
df=pd.DataFrame.from_dict(dict)
print(df)

df.to_csv('states.csv', index=False)    # create a states.csv file, false- removes index, true- shows index-default

print(states[3])
print(states[-3])

# 4. for loops
for states in states:
        print(states)

# 5. for loops
for states in states:
    # 5.1 if Statement
    if states=="Goa":
         print(states)
    print(states)

# 6. Export data in python
with open('test.txt','w') as file:        # file-random name, open - a function that takes a file name and mode
        file.write("Data scraped successfully!")
        # create a file test.txt with a statement above

