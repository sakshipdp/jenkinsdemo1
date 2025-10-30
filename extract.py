import pandas as pd 

print("extract data")
data = {
  'id' : [101,102,103],
  'name' : ['ram','raj','raja'],
  'age' : [29,34,42]
}
df = pd.DataFrame(data)

print(df)
