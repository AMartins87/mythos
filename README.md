
# INTRODUCTION 

Mythos is full-stack framework project built using Django, Python, HTML and CSS. It's a blog-style website where users can read about local myths and legends from all over the world. The objective is for users to be allowed to post, like and comment on blog posts.

Live project can be found [here](https://mythoi.herokuapp.com/).


## USER STORIES

As a site user and site admin I want to be able to login/logout of my account so I can interact with the site’s posts and users

# External user’s goal:
## *As a site user:*
    - I can click on a post so I can read it in full
    - I want to be able to write my own posts and comment on other stories so I can exchange opinions and ideas with other users and the blog owner (*this attracts more traffic and makes the site social*)
    - I want to be able to like posts so I can show the users and site admin I have liked their content 

# Site owner's goal:
## *As a site admin:*
    - I can create/publish new posts so that I can keep the blog updated and relevant to its purpose
    - I can edit/delete posts so I can correct typos or incorrect information which I may have provided

## FEATURES 
# Main Page
    - Navbar (on every page for ease of navigation)
        - Add Story
        - Register
        - Login
        - Contact Us
    
    - Footer
        - Copyright information
        - Social media links for YouTube, Twitter, Facebook

# Colour Scheme

# Wireframes
Wireframes were created using Balsamiq.

![Home Page](media/wireframes/Wireframes%20_Home_Page.png)
![Story Page](media/wireframes/Wireframes_Registration_Page.png)
![Registration Page](media/wireframes/Wireframes_Registration_Page.png)
![Login Page](media/wireframes/Wireframes_Login_Page.png)
![Contact Page](media/wireframes/Wireframes_Contact_Page.png)



## TESTING
# Manual Testing

# Validator Testing

-   **HTML** (No errors were returned when passing through the official W3C validator) 
    ![W3C Validator]()

-   **CSS** (No errors were found when passing through the official Jigsaw validator)
    ![Jigsaw Validator]()

-   **PEP8** (All python code was checked via [PEP8](http://pep8online.com/) with no errors reported.)
    ![PEP8]()



## BUGS
# Fixed bugs
After creating a model for adding posts and installing ckeditor, I tried to migrate but it was coming up with an error messages and my page has crashed as well. 

![Bug images]()

I reverted all migrations I made till this point, using a command *./manage.py migrate blog zero*, then I proceeded with *python manage.py makemigrations > python manage.py migrate* and all was ok then. 


## Unfixed bugs


## DEPLOYMENT
This project was created in GitHub and deployed to Heroku. 

### Following steps were taken in deployment of this project: 

1.  Using the CI full template, new repository was created and named Mythos
2.  When in the new repository, following Django packages and supporting libraries were installed by using the command *pip3 install* : **Gunicorn, Psycopg, Cloudinary**.
3.  *Requirements.txt* file was created and updated
4.  Project and app were created, app was added to my *settings.py* file into INSTALLED_APPS section
5.  First migration and testing of the server
6.  After the first migration, new app was created in Heroku, add-on of Postgres database was added to app resources
7.  Database attachment in GitPod by creating *env.py* and adding Postgres database link, SECRET_KEY and my Cloudinary link
8.  Entered Secret Key, Cloudinary and Postgres database to Config Vars in Heroku
9.  Created templates, media and static files on top level of the directory
10.  Created Procfile and added my gunicorn code
11.  All changes added with add, commit and push commands in Github
12. Deployed content manually through Heroku 



## CREDITS

https://www.w3schools.com/ 
https://getbootstrap.com/docs/5.0
https://docs.djangoproject.com/en/4.0/
https://www.geeksforgeeks.org/form-as_p-render-django-forms-as-paragraph/

Images
https://unsplash.com/photos/GtTNR-nxbK4 - mermaid by Naja Bertolt Jensen, Unsplash

https://www.pexels.com/photo/low-angle-view-on-person-wearing-costume-of-ancient-god-9969537/ - Person with facemask by Amar Preciado, Pexels

https://www.pexels.com/photo/the-trojan-horse-6474435/ - Trojan horse by KEMAL HAYIT, Pexels

https://www.dailyartmagazine.com/hero-mythical-creatures-spiders-in-art/ - spider

https://pixels.com/featured/tunnel-thru-blooming-almond-trees-sheila-fitzgerald.html - almond trees
