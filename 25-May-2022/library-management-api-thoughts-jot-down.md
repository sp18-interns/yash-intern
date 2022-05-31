Project - Library Management API 

Discussion:
1. What is API? Why API is used?
2. what are the entities(ex- the person who subscribes the book,person who handles the library,person who keeps the book in shelf of library,racks for books)
3. what all operations are done in library
4. books can be of more than one genre
5. authors, how to get books of a particular author
6. Database design is the fundamental step -> features->entities->database table

Today's discussion
7. Django- Model, View, Templates & URL
	Django REST framework - URL, View, Serializer

8. Extending upon point no. 3 above, the following operations are done in library:
	- When entering library , two types of registration/sign-up/login process, one for librarian,other for a) Person.
	- If Person enters or logs in with his details like name,address,phone,etc., then what next can he do?
	- If Person is new member, then he can
		- Apply for membership of library for particular time period.
		- Search for books in different categories like, by title of book,author of book,genre of book.
		- Based on availability, Get book issued and pay through checkout.
	- If Person is an existing member,then he can
		- Return book, reissue or extend book.
		- Search for books in different categories like, by title of book,author of book,genre of book.
		- Cancel membership or extend it.

	b) Librarian.
	- Librarian will enter through admin login.
	- Librarian should be able to view all details categorically
		- For Books
			- Filter by genre, title, author, no. of  total books in library, no. of total book copy of a particular book, 
		- For Persons
			- Check Person's Membership, no. of books isssued to that person,date and time of the books issued and upto which period, the max limit of books person can issue from library, amount payable by the person,
		- For Records
			- Inventory

			next steps:
			day 2 - freeze all feature sets to be implemented on day 7
			day 3- designing ERD and schema of the database
			day 5- start implementing APIs
			day 6 and 7- write code and test APIs