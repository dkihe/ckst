# Table of contents

* [About Project](#about-project)
* [The App](#the-app)
* [Languages](#languages)

# About Project

A browser-based password manager that generates unique, strong passwords.

# The App

The goal of our app is to be able to securely store and categorize login credentials, payment information, passports, wireless routers and more. The user can create vaults to separate personal information from work. Use autofill on websites so you never have to remember another password again.

# Languages

The languages we plan on using to develop this app is JavaScript, Python, HTML, and CSS.

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
    * Enhonce design of all pages

# Update (02/25/2020 - 03/08/2020)
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


# Update (04/11/2020)
## Progress
* Redid webpages to work better with Django
* Added new "passwordbank" page to hold user information
* Users are now able to signup for an account as well as login to their accounts

## Link
* https://github.com/dkihe/ckst/


## Pending
* Design new user account page
* Add ability for users to manage passwords and accounts in user account page

## Roles and Responsibilities
* Christopher Na 
  * Restructured models and layout of app.
  * Added authorizations for Users and Admin.
  * Added forms to enter in user information.
  * General UI modifications for appealing design.
    * Current/Next Task: Finish UI related tasks for the app
                         Add additional features/styling to Users and the Contact Form
                         Create the wiki Contact Us page
* Kainalu Kihe
  * Changed design of Signup and Login pages to reflect old design of webpages
    * Current/Next Task: Design User Accounts and Contact Us page
* Sabine Strasburger
  * Redid all webpages so that webpages are more inline with Django's workflow
  * Added functionality to pages so that users are able to Login/Signup
  * Added Django function that checks password strength 
    * Current/Next Task: Add admin capabilities to view database from Django backend
* Ty Gwartney
  * Created the User Account page and added basic design
  * Enabled the User Account page to load dummy data (account:password) from the database in a user-specific manner
    * Current/Next Task: Enable users to add new account:password entries to the database from the User Account page
    
