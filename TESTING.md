# MYTHOS - TESTING

Testing.md document records all reports from validators and gives a brief summary of manual testing which got carried out.

# Manual Testing

I have tested the site functionality and created couple of normal user accounts. All of the below was tested and worked as planned. The app was tested on desktop PC, laptop and iPhone 8 and iPhone 12 without any issues. It was responsive and very easy to navigate.

- Login and registration
- Added a post with and without an image
- Editedg and deleted a post as an author
- Commented on a post
- Used the like button
- Filled in the contact form 

# Validator Testing

**HTML** (No errors were returned when passing through the official W3C validator) 
    ![W3C Validator](/media)

**CSS** (No errors were found when passing through the official Jigsaw validator)

    ![Jigsaw Validator](/media/testing/w3c_css_validation_di.JPG)

**PEP8** (All python code was checked via [PEP8](http://pep8online.com/) with no errors reported.)
    
  ## Blog app
  ### admin.py
  ![PEP8 admin.py](/media/testing/pep8_admin_blog.JPG)

  ### forms.py
  ![PEP8 forms.py](/media/testing/pep8_forms_blog.JPG)

  ### models.py
  ![PEP8 models.py](/media/testing/pep8_models_blog.JPG)

  ### urls.py
  ![PEP8 urls.py](/media/testing/pep8_urls_blog.JPG)

  ### views.py
  ![PEP8 views.py](/media/testing/pep8_views_blog.JPG)

# Accessibility

I checked that the chosen colors and fonts are easy to read. All pages have passed through the Lighthouse reporting tool in Chrome developer tools on both mobile and desktop.

- [Contrast checker - body text](/media/testing/contrast_checker_text.JPG)
- [Contrast checker -links](/media/testing/contrast_checker_links.JPG)
- [Contrast checker - hover selector](/media/testing/contrast_checker_hover.JPG)

**Lighthouse Testing**

  ### Desktop
  ![Lighthouse_desktop](/media/testing/lighthouse_desktop_mp.JPG)

  ### Mobile
  ![Lighthouse_mobile](/media/testing/lighthouse_mobile_mp.JPG)


