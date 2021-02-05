data = []
count = 0
with open('reviews.txt','r') as p:
	for line in p:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
			count = 0


print(len(data))
