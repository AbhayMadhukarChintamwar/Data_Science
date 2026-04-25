import pandas as pd

data = {
    "Name":["Abhay","Swanand","Kittu"],
    "Age":[40,19,19],
    "City":["Hyderabad","Mumbai","Pune"]
}

df = pd.DataFrame(data) #Creating a DataFrame from the given data dictionary
print(df)