# Flask Blog Application

This is a blog application developed with Flask. The application allows users to register, log in, add, update, and delete blog posts. Additionally, users can search and view other blog posts.

## Setup

If Flask is not installed, install Flask:  
```pip install Flask```

If Flask-MySQLdb is not installed, install Flask-MySQLdb:
```pip install Flask-MySQLdb```

If Passlib is not installed, install Passlib:
```pip install passlib```

## Starting the Application

Flask yüklü değilse, Flask'ı yükleyin:
pip install Flask

Flask-MySQLdb yüklü değilse, Flask-MySQLdb'yi yükleyin:
pip install Flask-MySQLdb


## Starting the Application

To run the Flask blog application, navigate to the directory where the application is located in the terminal.

Start the application by running the following command:
python app.py


Visit http://localhost:5000 in your browser to use the blog application.

## User Registration

To register a new user, go to http://localhost:5000/register. Enter your name, username, email, and password. Click the "Register" button to complete the registration.

## User Login

To log in, go to http://localhost:5000/login. Enter your username and password. Click the "Log In" button to access your account.

## Adding a Blog Post

After logging in, go to http://localhost:5000/addfilm. Enter the title and content of the blog post. Click the "Add Film" button to save your blog post.

## Updating a Blog Post

After logging in, view your blog posts at http://localhost:5000/dashboard. To edit a post, click the "Edit" button next to the desired blog post. Update the title and content as needed. Click the "Update" button to save the changes.

## Deleting a Blog Post

After logging in, view your blog posts at http://localhost:5000/dashboard. To delete a post, click the "Delete" button next to the desired blog post. The blog post will be removed

## Searching for Blog Posts

On the homepage (http://localhost:5000), there is a search bar in the top-right corner. Enter the keyword you want to search for and click the "Search" button. The search results will be displayed.

## Logging Out

To log out, go to http://localhost:5000/logout.


