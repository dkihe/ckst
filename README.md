# Table of contents
* [About Project](#about-project)
* [The App](#the-app)
* [Languages](#languages)

# About Project
A browser-based password manager that generates unique, strong passwords.

# The App
The goal of our app is to be able to securely store and categorize login credentials, payment information, passports, wireless routers and more. The user can create vaults to separate personal information from work. Use autofill on websites so you never have to remember another password again.

# Languages
The languages we plan on using to develop this app are JavaScript, Python, HTML, and CSS.

# Completed
* Database setup
  * One model/table for users enabled - username and password
  * One model/table for user account data - registered accounts and password
* Created Login page
  * Login form 
    * Username and password 
    * Function to hide password
    * Form checker
 * Created the User Account page
    * Lists users accounts and passwords associated with each account
 * Created the About page
    * Overview of the app and website

# Pending
* Account authorization
  * Verify the user account:password from the Login page
* Sign-up Page
  * Page used to sign up for a new account using a username and password
  * Add newly created accounts to the database
* Admin page
  * Allow for overview of backend/database data

# Team Contribution
* Christopher Na 
  * Created database using SQLite
  * Styled sign-in page
  * Next Task:
    * Setup database to work with Sign-in page (add new users)
    * Get data from database to load properly for the User Homepage
* Kainalu Kihe
  * Created sign-in page
  * Created sign-in page functionality for the frontend
  * Next Task:
    * Start work on Login Page and Sign-up page
    * Create login verification function
* Sabine Strasburger
  * Initialized project using Django
  * Created homepage and template files
  * Next Task:
    * Create dummy accounts to test with user home page
    * Create function to check password strength when creating new account
* Ty Gwartney
  * Drew diagrams detailing each page needed for the application
  * Planned application functionality and user flow
  * Next Task:
    * Start work on User Account page
    * Enhance design of all pages

#  Part II
## Update (03/08/2020)
## Progress
* Changed the entire layout and design of the webpage
* Added new pages such as a Sign-up page, a User Account page and an About page
* Added more functionality to the login and signup pages (form validation)

## Link
* https://github.com/dkihe/ckst/

## Pending
* Give functionality to User page
* Add admin capabilities to backend
* Create user accounts and store user data on the database
* Allow users to add new accounts and password entries to the database
* Finalize design for user page

## Roles and Responsibilities
* Christopher Na 
  * Completed Contact page and database workflow
  * Design changes to pages for a cohesive color scheme
    * Current/Next Task: User account authorization and finalization of data associated with accounts
* Kainalu Kihe
  * Completed Signup page (front end)
  * Created Signup page functionality (form validation, password checker)
    * Current/Next Task: Add design and functionality to the User Account page
* Sabine Strasburger
  * Redesigned entire website (Homepage, Login, About, Signup)
    * Current/Next Task: Add admin capabilities to view database from Django backend
* Ty Gwartney
  * Created the User Account page and added basic design
  * Enabled the User Account page to load dummy data (account:password) from the database in a user-specific manner
    * Current/Next Task: Enable users to add new account:password entries to the database from the User Account page


#  Part III
## Update (04/11/2020)
## Progress
* Redid webpages to work better with Django
* Added new "passwordbank" page to hold user information
* Users are now able to signup for an account as well as login to their accounts
* Users can add new account:password entries
* Users can view their account:password entries

## Link
* https://github.com/dkihe/ckst/

## Pending
* Design new user account page
* Add ability for users to manage passwords and accounts from the Userhome page

## Roles and Responsibilities
* Christopher Na 
  * Restructured models and layout of app.
  * Added authorizations for Users and Admin.
  * Added forms to enter in user information.
  * General UI modifications for appealing design.
    * Current/Next Task: Finish UI related tasks for the app, 
                         add additional features/styling to Users and the Contact Form, 
                         create the wiki Contact Us page
* Kainalu Kihe
  * Changed design of Signup and Login pages to reflect old design of webpages
    * Current/Next Task: Re-style the PasswordBank, NewEntry, and ContactUs page
* Sabine Strasburger
  * Redid all webpages so that webpages are more inline with Django's workflow
  * Added functionality to pages so that users are able to Login/Signup
  * Added Django function that checks password strength 
  * Redirected submitted 'contact us' form to print to terminal as a simulated email
    * Current/Next Task: Add admin capabilities to view database from Django backend
* Ty Gwartney
  * Updated the UserAccount page, now the PasswordBank, set to work with newly authenticated users
  * Fixed bug where the Password Bank was displaying all users data instead of user-specific data
  * Created a New Entry page where users can add new database entries in "Account: Password" tuples
  * Enabled Admin capabilities for editing User account data
    * Current/Next Task: Enable users to delete account:password entries from the database, possibly integrate the NewEntry and PasswordBank pages
    
# Part IV
## Update (4/26/2020)
## Progress
* Added finishing touches - new page design, new site tour, enabled users to delete old entries.

## Roles and Responsibilities
* Christopher Na
   * Finished UI related tasks for the app, added additional features/styling to Users and the Contact Form.
   * Created the application Wiki page.
   * Added working delete buttons to the PasswordBank.
* Kainalu Kihe
  * Re-styled the entire website: changed the color scheme and text font, created a navigation bar, and fixed data tables.
* Sabine Strasburger
  * Updated the About page to feature a tour of the website.
* Ty Gwartney
  * Added the navigation bar to the NewEntry page.
  * Added short comments to the .py pages.
  
## Technical Notes
 * App specifications
    * To be able to use this application, you must have the most current version of Python 3 and Django installed.
        * To install the most current version of python:
             * brew install python
        * To install Django simply:
             * python -m pip install Django
 * How to install
    * Download the zip file of the repository, and unzip it
    * In the terminal cd to the downloaded repository
    * Then type:
        * For devices with Python 2 as default:
             * python manage.py runserver 
        * For devices with Python 3 as default:
             * python3 manage.py runserver
    * Go to the URL provided
    * Now you are able to use the application
    * To stop running your application, simply go to your terminal and press the keys CTRL-C

## Developer Notes
 * We used the Django web application framework to develop Tutare. The biggest challenge was properly making use of Django's built in features. More than once, we designed and implemented aspects of our project, only later to discover that Django had built in functions we could used instead that would have saved us time and effort. Other challenges included authenticating users, formatting and designing each page to work with the application code, and displaying user data from the database.
 
## Links
* Online Repository: https://github.com/dkihe/ckst
* Final Project Documentation File: https://github.com/dkihe/ckst/blob/master/documentation.txt
* Release Version: https://github.com/dkihe/ckst/releases
* Wiki Page: https://github.com/dkihe/ckst/wiki
