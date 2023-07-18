import pandas as pd
# column = ["Mariya","Batman","Spongebob"]
# title_column = {"name" : column,
#                  "height" : [1.97,2.5,1.5],
#                  "weight":[12,4,6]}
# data = pd.DataFrame(title_column)
# print(data)

num = {"name" : ['shivani','priya','tanu','raju'],
        "surname" :['paridar','madloy','Gothi','patidar'],
        "DOB" :[24 , 30,26,15],
        "class" : ['1st','3rd','5th','UKG'],
       "totalmarks":[100,100,100,100],
       "marks" : [89,50,86,30]
       }
data = pd.DataFrame(num)
# select value from DataFrame
select_col = data["surname"][2]
select_value = data.iloc[1]

#mainpulate dataframe values
bml = []
#totalmarks/(marks**2)
for i in range(len(data)):
        bml_score =data["totalmarks"][i]/(data["marks"][i]**2)
        bml.append(bml_score)
data['bml'] = bml

# save  datafram to a file
data.to_csv('bml.csv',sep='\t')
print(data)