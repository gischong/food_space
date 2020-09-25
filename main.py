import pyrebase, collections, os, sys
from flask import Flask, render_template, redirect, request, session, url_for
app = Flask(__name__)
app.secret_key = 'scx93icmw23v!@C!@$d5%!@#$'

firebaseConfig = {
    "apiKey": "AIzaSyAKpcQfdcpSfOtYkZue9YtwISGg08v2iT0",
    "authDomain": "foodspace-f7c1d.firebaseapp.com",
    "databaseURL": "https://foodspace-f7c1d.firebaseio.com",
    "projectId": "foodspace-f7c1d",
    "storageBucket": "foodspace-f7c1d.appspot.com",
    "messagingSenderId": "475857318770",
    "appId": "1:475857318770:web:f9fa049dd3876b6830e3eb",
    "service_account": "C:\\Users\\gilbe\\Desktop\\food_space\\foodspace-f7c1d-firebase-adminsdk-fqegq-8f6e900389.json"
}

firebase = pyrebase.initialize_app(firebaseConfig)
# reference to firebase realtime database
database = firebase.database()
# reference to firebase storage
storage = firebase.storage()

cats = ['Breakfast & Brunch', 'Lunch', 'Dinner', 'Appetizer & Snacks', 'Bread', 'Dessert', 'Drinks', 'Main Dish', 'Salad', 
            'Side Dish', 'Soups, Stews, and Chilis', 'Diet & Healthy', 'Holiday & Seasonal']

# Landing/Welcome page
@app.route('/')
def index():
    return render_template('index.html')

# Shows all existing recipes and other cooking news?
@app.route('/home')
def home():
    # get all recipes in Recipes database
    allrecipes = database.child("Recipes").get()
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("images/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    #for recipe in allrecipes.each():
    #    print(recipe.key(), recipe.val())
    # val() returns a PyreResponse object containing query data
    if (allrecipes.val() == None):
        return render_template('home.html')
    else:
        return render_template('home.html', recipes=allrecipes, title='Home', p1=url0, p2=url1 )

# Display all existing recipes
@app.route('/recipes')
def recipes():
    # get all recipes in Recipes database
    allrecipes = database.child("Recipes").get()
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("images/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    # val() returns a PyreResponse object containing query data
    if (allrecipes.val() == None):
        return render_template('recipes.html')
    else:
        return render_template('recipes.html', recipes=allrecipes, title='Home', p1=url0, p2=url1)

# Categories
@app.route('/categories')
def categories():
    global cats
    allrecipes = database.child("Recipes").get()
    return render_template('categories.html', title='Categories', categories=cats, recipes=allrecipes)

# Displays all recipes with the same categories
@app.route('/categories/<category_clicked>', methods=['GET'])
def category_specific(category_clicked):
    #print(category_clicked)
    # get all recipes in Recipes database
    allrecipes = database.child("Recipes").get()
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("images/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    #for recipe in allrecipes.each():
    #    print(recipe.key(), recipe.val())
    # val() returns a PyreResponse object containing query data
    if (allrecipes.val() == None):
        print("well shit... no recipes")
        return render_template('category_specific.html')
    else:
        print("are there recipes? this should work")
        return render_template('category_specific.html', recipes=allrecipes, title='category', p1=url0, p2=url1, this_category=category_clicked)

@app.route('/search', methods=['GET','POST'])
def search(): 
    if (request.method == "POST"):
        # get search input
        searchInput = request.form['search_input']
        #print(searchInput)
        allrecipes = database.child("Recipes").get()
        # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
        # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
        # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
        img_url = storage.child("images/").get_url(None)
        split_url = img_url.split("2F")
        #print(img_url)
        #print(split_url[0], split_url[1])
        url0 = split_url[0]
        url1 = split_url[1]
        #for recipe in allrecipes.each():
        #    print(recipe.key(), recipe.val())
        # val() returns a PyreResponse object containing query data
        if (allrecipes.val() == None):
            return render_template('search_results.html')
        else:
            return render_template('search_results.html', recipes=allrecipes, title='Results', p1=url0, p2=url1, searchIn=searchInput )

@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Adds new credentials to firebase for new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        username = "n/a"
        imgname = "n/a"
        # creates database for user profiles
        profile = {
            "email": email,
            "password": password,
            "username": username,
            "profileimg": imgname
        }
        try:
            # create the user
            firebase.auth().create_user_with_email_and_password(email, password)
            # login the new user
            user = firebase.auth().sign_in_with_email_and_password(email, password)
            # session
            user_id = user['idToken']
            user_email = email
            session['usr'] = user_id
            session['email'] = user_email
            database.child("Profiles").push(profile)
            return redirect('home')
        except:
            return render_template('register.html', title='Register', message='This email is already in use. Please try another one.')
    return render_template('register.html', title='Register')

# Login if user exists
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        try:
            # login the user
            user = firebase.auth().sign_in_with_email_and_password(email, password)
            # session
            user_id = user['idToken']
            user_email = email
            session['usr'] = user_id
            session['email'] = user_email
            return redirect('home')
        except:
            return render_template("login.html", title='Login')
    return render_template('login.html', title='Login')

# Logs user out
@app.route('/logout')
def logout():
    firebase.current_user = None
    session.clear()
    return redirect('home')

# User profile page
@app.route('/myprofile')
def myprofile():
    userdata = database.child("Profiles").get()
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("profile/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    return render_template('myprofile.html', profile=userdata, title='My Profile', p1=url0, p2=url1)

# Edit profile page
@app.route('/editprofile/<id>', methods=['GET', 'POST'])
def editprofile(id):
    if (request.method == 'POST'):
        username = request.form['username']
        profileimage = request.files['image']
        imgname = profileimage.filename
        profile = {
            "username": username,
            "profileimg": imgname
        }
        try:
            database.child("Profiles").child(id).update({"username": username, "profileimg": imgname})
            storage.child("profile/"+imgname).put(profileimage)
            return redirect('/myprofile')
        except:
            return redirect('/myprofile')
    user_deets = database.child("Profiles").order_by_key().equal_to(id).limit_to_first(1).get()
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("profile/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    return render_template('editprofile.html', profile=user_deets, title='My Profile', p1=url0, p2=url1)

def resetpassword():
    firebase.auth.send_password_reset_email("email")
    return redirect('myprofile')

# Page shows all the user's own recipes they posted
# User can add or edit their recipes here 
@app.route('/myrecipes')
def myrecipes():
    # get the current user's email to compare to recipes in database
    user_email = session['email']
    #print(user_email)
    # get all recipes in Recipes database
    allrecipes = database.child("Recipes").get()
    #print(allrecipes)
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("images/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    # val() returns a PyreResponse object containing query data
    if (allrecipes.val() == None):
        return render_template('myrecipes.html')
    else:
        return render_template('myrecipes.html', recipes=allrecipes, title='My Recipes', p1=url0, p2=url1)

# adds a new recipe post
@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    global cats
    if (request.method == 'POST'):
        recipename = request.form['recipe_name']
        description = request.form['description']
        ingredients = request.form['ingredients']
        directions = request.form['directions']
        category = request.form['category']
        recipeimg = request.files['image']
        imgname = recipeimg.filename
        preptime = request.form['preptime']
        cooktime = request.form['cooktime']
        servingsize = request.form['servingsize']
        #print(imgname)
        recipe = {
            "recipename": recipename,
            "description": description,
            "ingredients": ingredients,
            "directions": directions,
            "category": category,
            "image": imgname,
            "preptime": preptime,
            "cooktime": cooktime,
            "servingsize": servingsize,
            "author": session["email"] 
        }
        try:
            database.child("Recipes").push(recipe)
            storage.child("images/"+imgname).put(recipeimg)
            return redirect('/myrecipes')
        except:
            return render_template('addrecipe.html', message="didnt work dumb dumb")
    return render_template('addrecipe.html', categories=cats)

@app.route('/addimg', methods=['GET','POST'])
def addimg():
    if (request.method == 'POST'):
        recipeimg = request.files['image']
        print(recipeimg)
        # get image filename
        #recipeimg.save(recipeimg.filename)
        imgname = recipeimg.filename
        print(imgname)
        # creates a "dumb" image file path for child(path)
        storage.child("images/"+imgname).put(recipeimg)
        return redirect('/home')
    return render_template('addimg.html')

# gets the details(ingredients/directions) of a recipe post through id
@app.route('/details/<id>')
def details(id):
    recipe_deets = database.child("Recipes").order_by_key().equal_to(id).limit_to_first(1).get()
    #print(recipe_deets)
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("images/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    return render_template("details.html", data=recipe_deets, p1=url0, p2=url1)

# edit recipe post
@app.route('/editrecipe/<id>', methods=['GET', 'POST'])
def editrecipe(id):
    if (request.method == 'POST'):
        recipename = request.form['recipe_name']
        description = request.form['description']
        ingredients = request.form['ingredients']
        directions = request.form['directions']
        recipeimg = request.files['image']
        # pryrebase doesn't have a delete file method for storage. So only upload new one for recipe
        imgname = recipeimg.filename
        preptime = request.form['preptime']
        cooktime = request.form['cooktime']
        servingsize = request.form['servingsize']
        recipe = {
            "recipename": recipename,
            "description": description,
            "ingredients": ingredients,
            "directions": directions,
            "image": imgname,
            "preptime": preptime,
            "cooktime": cooktime,
            "servingsize": servingsize,
            "author": session["email"]
        }
        try:
            database.child("Recipes").child(id).update(recipe)
            storage.child("images/"+imgname).put(recipeimg)
            return redirect('/myrecipes')
        except:
            return render_template('myrecipes.html', message= 'edit didnt work dumbass')
    # get values for specific recipe to display
    recipe_deets = database.child("Recipes").order_by_key().equal_to(id).limit_to_first(1).get()
    # DISCLAIMER: NOT a good way to get image path from firebase storage --> firebase image path url can change in future versions!!!
    # https://firebasestorage.googleapis.com/v0/b/storage-url.appspot.com/o/images% |2F| |example.jpg| ?alt=media
    # split the base image path url into two parts --> then filled in the delimiter(2F) and combined it for image src
    img_url = storage.child("images/").get_url(None)
    split_url = img_url.split("2F")
    #print(img_url)
    #print(split_url[0], split_url[1])
    url0 = split_url[0]
    url1 = split_url[1]
    return render_template('editrecipe.html', data=recipe_deets, p1=url0, p2=url1 )

# delete recipe post
@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    database.child("Recipes").child(id).remove()
    return redirect('/myrecipes')

# have a likesDetail table that stores the post_id, user_id, and liked status(true/false)
# have likesSummary table that stores the post_id and the number of likes it has
def likesDetail(id):
    # which user liked which post
    # triggered by the click of the liked button
    # on insert
        # if the post_id doesn't exist in this table database
            # AND if post_id like == true
                # insert new row of post_id and likes # amount
        # else if post_id exist in this table database
            # 'update' the post_id's likes += 1(adding the number of likes)

    # on update
        # if post_id doesn't exist in likes_summary
            # do nothing
        # else if post_id exists in likes_summary
            # if user previously liked this post --> now dislikes it
                # update likes_summary table where post_id likes -= 1
            # else if user previously dissliked this post and now likes it 
                # update likes_summary table where post_id likes +=1
    return


def likesSummary():
    # get post id and the number of likes from it
    # for each like add 
    return

if __name__ == '__main__':
    app.run(debug=True)