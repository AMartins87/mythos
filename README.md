
# INTRODUCTION 

Mythos is full-stack framework project built using Django, Python, HTML and CSS. It's a blog-style website where users can read about local myths and legends from all over the world. The objective is for users to be allowed to post, like and comment on blog posts.


## USER STORIES

As a site user and site admin I want to be able to login/logout of my account so I can interact with the site’s posts and users

# External user’s goal:
## *As a site user:*
    - I can click on a post so I can read it in full
    - I want to be able to write comments so I can exchange opinions and ideas with other users and the blog owner (*this attracts more traffic and makes the site social*)
    - I want to be able to like posts so I can show the users and site admin I have liked their content 

# Site owner's goal:
## *As a site admin:*
    - I can create/publish new posts so that I can keep the blog updated and relevant to its purpose
    - I can edit/delete posts so I can correct typos or incorrect information which I may have provided
    <!-- - I can delete site users’ comments if they are against guidelines -->

## FEATURES 
# Main Page
    - Navbar (on every page for ease of navigation)
        - Stories
        - Add Story
        - Register
        - Login
        - Contact Us
        <!-- - Community Guidelines -->
    
    - Footer
        - Copyright information
        - Social media links for YouTube, Twitter, Facebook

# Colour Scheme

# Wireframes
Wireframes were created using Balsamiq, they can be viewed [here](). *<-- insert link*


## TESTING
# Manual Testing

# Validator Testing


## BUGS
# Fixed bugs
After creating a model for adding posts and installing ckeditor, I tried to migrate but it was coming up with an error messages and my page has crashed as well. 

![Bug images]() - upload images of bugs

I reverted all migrations I made till this point, using a command ./manage.py migrate blog zero, then I proceeded with python manage.py makemigrations > python manage.py migrate and all was ok then. 


## Unfixed bugs


## DEPLOYMENT


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

