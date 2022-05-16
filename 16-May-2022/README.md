# Date 16-May-2022

## First Half

- 🔄Python Django- The Practical Guide : In Progress

### Videos

- 🔄16 Optional Django Summary and Quick Introduction: In Progress
  - ✅018 Querying Data: Completed
  - ✅019 Adding Image Upload: Completed
  - ✅020 Serving and Displaying Images: Completed

### Assignment

- Revised by watching previous videos to soldify what i learned.
- Watched and understood the videos. Also,practiced in the attached django_course_site project.

### Doubts

- How to store image in a database?

  ```
   If directly,it can be stored as binary data by using blob otherwise it can be stored as string by using URL of the image. The URL will specify where exactly the image is stored(either in filesysytem or in some database)

   As a general rule, and I’ll get to the exceptions in a moment, it’s a bad idea to store images directly in a database.

  Why? Firstly, unless you’re going to use the database to inspect the internals of the image, it’s just a lump of data (and often a pretty large one) that has to be managed by the DB, backed-up, carted around, and returned in queries. Secondly file systems are, not surprisingly, pretty well optimised for serving files. Today’s file systems do a pretty cool job of caching frequently used files for example

  So, if you’re writing a blog-engine, for example, it makes sense to use the file system to manage the files and the database to manage the data relating to them - In one sense, there’s a clue in the names - file system for files, database for data.

  Now, this comes with a cost - You have to manage the file - perhaps by creating a directory that contains uploaded files, and then a process for managing them (new versions, deletion etc). But there are plenty of patterns and examples out there that cover this petty nicely.

  You can certainly do point-in-time backups of filesystems, you can secure those files, and - as a rule and despite the other answer you’ve had - storing images in databases will make many things more complicated.

  So when should you use the DB to store binary data like images? I can only really think of one scenario, and that is where for contractual / legal / privacy purposes you need to really secure the binary, in which case you may opt to store the binary in the db, but that would definitely be the exception rather than the rule.

  ```

### Links Read

- [Storing image in database](https://www.quora.com/What-is-the-best-approach-to-store-image-into-SQLite)

## Second Half

- 🔄 Python Django- The Practical Guide: In Progress

### Videos

- ✅021 Configuring the Admin Area: Completed
- ✅022 Setting One-to-Many Relations: Completed

### Assignment

- Learnt about adding configuratons to the admin area by adding a derived class from admin library which contains built-in properties to enable some functionalities in admin area. This class is also used along with Meetup class as second argument of site registration function in admin.py.
- Learnt about relations between models(which eventually are made into tables by Django) by adding another model and using it as a foreign key in the previous one.

### Doubts

- Should images be stored in a database or in filesystem on a server?

  ```
  Generally databases are best for data and the file system is best for files. It depends what you're planning to do with the image though.

  If you're storing images for a web page then it's best to store them as a file on the server. The web server will very quickly find an image file and send it to a visitor. Sending files to visitors is the main job of a web server.

  If you were to store the same image in a database then the amount of steps to get to this image is greatly increased so the image will be slower to download. Also it will use up more server resources. The web server will have to connect to the database and then query the database to get the image, download the image from the database and then send the visitor the image.

  This will also tie up the database a little bit while it sends the image. It might not be a problem if your web site is not high traffic but as soon as you start getting a lot of visitors then you'll quickly notice the slowness. Storing files isn't really what databases were made for even though they can do it.

  There are sometimes good reasons to store images in a database but there aren't too many. Some uses I've seen for storing images in a database are things like sensitive images such as a photo of an employee's or customer's face that will never be used externally. In this case the database gives you a way to tightly control access to the images.

  ```

- Need to learn about relations (one-to-many,many-to-one,etc.) in depth.

## Links Read

- [Storing image in database or in filesystem in server](https://teamtreehouse.com/community/storing-image-in-database-compare-with-storing-at-the-folder-server#:~:text=Generally%20databases%20are%20best%20for,send%20it%20to%20a%20visitor.)
