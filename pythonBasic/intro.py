import pandas as pd

states = ['California', 'Texas', 'Florida', 'New York']
population = [3567893456, 3567893456, 3567893456, 3567893456]

#index from last element
print(states[-1])

#looping through entier list
for state in states:
    if state == "Florida":
        print(state)

#store the data in file
#method-1: using open()
with open('data.txt', 'w') as file:
    file.write("Data successfully scraped!")
#method-2: using pandas
dict_states = {'States': states, 'Population': population}
df_states = pd.DataFrame.from_dict(dict_states)
print(df_states)
df_states.to_csv('states.csv', index=False)

#Handling exception errors: Try-except
new_list = [2, 4, 6, 'California']
for element in new_list:
    try:
        print(element ** 2)
    except:
        print("An error occurred")

#While-Break
n = 4
while n > 0:
    print(n)
    n -= 1
    if n == 2:
        break
print('Loop ended')