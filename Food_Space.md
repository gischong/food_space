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
 -  Allow users to add a username instead of displaying email as author of recipe
 -  Add in recipe count(er) for each category on categories page
 -  Add prep time/cook time/total time and serving amount as input options for recipes
 -  Add "profile page" navigation to top right nav bar when user is logged in
 -  Allow user to upload a profile picture while displaying empty default if non is given
 -  Add cooking news from other sites and cooking guides links
 -  Fix print error "no recipe found" when search result comes back empty after a search

# Heads Up!
 - Firebase query for posts is slow. This can be seen when loading posts. My best speculations of this is because of the querying to both Realtime Database and Storage(recipe picture) to retrieve post data.

# License
Use it as you would like. 


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
