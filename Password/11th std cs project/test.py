import pandas as pd
df = pd.read_excel('Passwords.xlsx')
newData = pd.DataFrame([{'Account':'HackerRank','Password' :'akash487385'}])
df = df.append(newData,ignore_index=True)
index = df[df['Account']=='facebook'].index.values[0]
password = df._get_value(index, 'Password') 
df.to_excel("Passwords.xlsx" , index=False)
print(df)
print(password)
# rows , columns = df.shape
# print(rows)