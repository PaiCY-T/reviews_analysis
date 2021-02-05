data = []
count = 0
total_length = 0
with open('reviews.txt','r') as p:
	for line in p:
		data.append(line.strip())
		count += 1
		if count % 1000000 == 0 :
			print(len(data))
			count = 0
data_new = []
count = 0
for i in data:
	if len(i) > 100:
		data_new.append(i)
print(len(data_new))
