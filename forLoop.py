# For Loop1.py

for i in range(5):
	print('Hello',i)


users = ['val', 'bob', 'mia', 'ron', 'ned']
for f in users:
	print('Friend is : ',f)
	if f == 'bob':
		print('VIP Friend is : ',f)

alien_0 = {'color': 'green', 'points': 5}

#show key only
for f in alien_0:
	print(f);

#show All
for f in alien_0.items():
	print(f);

#show All
for a,b in alien_0.items():
	print('Key : ',a);
	print('value : ',b);

#show item only
for f in alien_0.items():
	print(f[1]);

#show key only
for f in alien_0.keys():
	print(f);

#show values only
for f in alien_0.values():
	print(f);

# Solt by enumerate for List
for i,f in enumerate(users,start=1000):
	print(i,f)

# Solt by enumerate for Dic.
for i,f in enumerate(alien_0.items()):
	print(i,f).

# Solt by enumerate for Dic. split
for i,(k,v) in enumerate(alien_0.items()):
	print(i,k,v)