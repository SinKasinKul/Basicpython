
#-------------List------------------
users = ['val', 'bob', 'mia', 'ron', 'ned']
users.insert(3, 'joe')
users.append('amy')

num_users = len(users)
print("We have " + str(num_users) + " users.")

users.sort()
print(f'List is {users}')

users.sort(reverse=True)
print(f'List is {users}')

newest_user = users[-2]
print(f'List is {newest_user}') 
print(f'List is {users}')

del users[-1]
print(f'List is {users}') 
num_users = len(users)
print("We have " + str(num_users) + " users.")


users.remove('mia')
print(f'List is {users}') 
num_users = len(users)
print("We have " + str(num_users) + " users.")


most_recent_user = users.pop()
print(most_recent_user)
print(f'List is {users}') 
num_users = len(users)
print("We have " + str(num_users) + " users.")


first_user = users.pop(-1)
print(first_user)
users.insert(0, first_user)
print(f'List is {users}') 
num_users = len(users)
print("We have " + str(num_users) + " users.")

for user in users:
     print(user)
#-------------List------------------

