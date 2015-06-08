1i.
	* **order id - ** This column represents a unique identifier for the contents of 				  an entire meal for a customer. For example, every item with             				  order id 1 is part of an entire oder for customer 1.
	**quantity - **  Represents the number of one particular item that was order
	** item_name-** The name for a specific item
	** choice_description-** The customized selection for an item.
	** item_price-** price of an item
   ii. 1834. If order is unique to every order then using the tail command and 		 viewing the last order id we can derive the total amount of orders. 
   iii. ```wc -l chipotle.tsv ```. There are 4623 lines  
   iv. ```python
	import csv

 	file = open('chipotle.tsv', 'r')

	data = [row for row in csv.reader(file, delimiter = '\t') ]

	file.close()

	steak_count = 0
	chicken_count = 0
	
	for row in data:
    		if row[2] == 'Steak Burrito':
        		steak_count += 1
    		elif row[2] == 'Chicken Burrito':
        		chicken_count += 1
	print steak_count
	print chicken_count
	```
	Chicken Burritos are more popular with a count of 553 than Steak Burritos    	with a count of 368 
     
	v. ```python
		import csv


		file = open('chipotle.tsv', 'r')

		data = [row for row in csv.reader(file, delimiter = '\t') ]

		file.close()

		print data[1][2]

		steak_count = 0
		chicken_count = 0
		pinto = 0
		black_beans = 0
		
		for row in data:
		        if row[2] == 'Steak Burrito':
        		steak_count += 1
         
   	 		elif row[2] == 'Chicken Burrito':
        		chicken_count += 1
       	 		pinto += row[3].count('Pinto Beans')
        		black_beans += row[3].count('Black Beans')

		print pinto
		print black_beans
	```
	Black beans are ordered more for chicken burritos with a count of 282 vs. 	pinto beans with a count of 105
2. ```find . -name *.csv```

3. ``` grep -r 'dictionary' . | wc -w``` There are 12 occurrences of 'dictionary'

