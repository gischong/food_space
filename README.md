# Food_Space

# Description
  - Food_Space is a personal website project that allows users to post and share their own recipes.

# What's it built with?
  - Flask(Python)
  - Firebase
  - HTML/CSS
  
# Features
 - Full CRUD(create, read, update, delete) functionalities for recipe posts
 - Realtime updates of recipe posts through Firebase
 - No comments for negative energies. Only positive vibes!
 
# Installation
  - Flask - https://flask.palletsprojects.com/en/1.1.x/installation/  
pip install Flask
  - pyrebase - https://github.com/thisbejim/Pyrebase  
pip install pyrebase
 - After cloning this repository and installing the above, cd into the project directory where main.py is located.
 - Run:  
  $env:FLASK_APP = "main.py"   
  flask run
 - Then head to http://127.0.0.1:5000/ where the site is running

# Roadmap
 -  Add in like/dislike system and show percentage of likes vs dislikes
 -  Add in "heart"(favorites) button for users to keep track of recipes they like
 -  Filter and display recipes by newest/oldest/most popular(most hearts)/top rated(highest percentage of likes) function
 -  Add in pagination for recipes
 -  Check input validations(password length/complexity, profanity filters)
 -  Add in login attempts
 -  Add optional profile pictures users can choose from(no upload from user end)
 -  Allow user to reset password(current 'reset password' button isn't working)
 -  Add cooking news from other sites and cooking guides links
 -  Fix print error "no recipe found" when search result comes back empty after a search

# Heads Up!
 - Firebase query for posts is slow. This can be seen when loading posts. My best speculation for why this is happening is due to the querying time of retrieving data from BOTH Realtime Database and Storage(pictures) for the recipe posts.

# License
Use it as you would like.
