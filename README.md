# [SMARTY](https://smarty-jose.herokuapp.com/)

![SMARTY Mock up image](/assets/images/smartyMockUp.PNG)
This website app has been created with the purpose of giving any person the option of managing people. It's a basic app but it can't help any person who wants to have a better system.

---
## Table of Contents
* [User Experience](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Icons](#icons)
        * [Colors](#colors)
        * [Structure](#structure)
* [Wireframes](#wireframes)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#tools-and-libraries)
    * [Tools](#tools)
* [Information Architecture](#information-architecture)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience
### User Goals
  * A website with good and up to date content.
  * A website that manages to display well all colors on the screen. 
  * A good and well formated contact form on the website.
  * List of employees 

### User Stories
  * A user wants to easily find the details about the employee.
  * A user wants to easily edit or delete the details of any employee.
  * A user wants to quickly find what they are looking for.
  * A user wants to login and sign up easily.
  * A user wants to navigate smooth on the webiste displayed on tablets and cellphones.
  * A user wants to find different social medias associated to the website.

### Site Owners Goals
  * Advertise Smarty as a basic app for managing people.
  * With so many people working from home now. This app has been created with the idea of help people organize their employees accordingly with their department.
  * Have a basic professional app to manage people.

### User Requirements and Expectations
#### Requirements
  * Easy to navigate.
  * Appropriate Content about the service.
  * Good color contrast.
  * Accurate employee details.

#### Expectations
  * Proper information about locations.
  * Relevant social medias.
  * Links that dont brake.
  * Quick return from website owner.

### Design Choices
#### Fonts
  * The fonts chosen on this website came from [Google fonts](https://fonts.google.com/). This choice has been made because of the probability of working on any browser.

  #### Icons
  * Icons have been picked from [Font Awesome](https://fontawesome.com/).

#### Colors
  * Colors have been picked up from [Color Hunt](https://https://colorhunt.co/).
  * I also used the website [Coloors](https://coolors.co/) for make the colors pallet.

  ![Color Scheme](assets/images/palette.png)
  * #f57c00 - Main ton of orange 
  * #fff - White used for main text
  * rgb(233, 206, 156) - Flash when user logs out
  * rgb(233, 206, 156) - border form
  * rgba(1, 0, 3, 0.4) - Ton of black of box on home page

#### Structure
  * For the website structure I have been used [Materialize](https://materializecss.com/).
  
## Wireframes

I have decided to use [Balsamiq Wireframes](https://balsamig.com) to create 3 different wireframes for my website.

### [Desktop Wireframe](wireframes/csdesktop.png)
### [Tablet Wireframe](wireframes/ipad_wireframe.png)
### [Phone Wireframe](wireframes/phone_wireframe.png)


The wireframes really helped me to give me a perpespective on how the wesbite would be made out at the end. 

## Features
### 1. Existing Features
#### Navigation
The navigation bag that I hava come up with for the website is a basic navbar which comes from materializecss. It has the logo of the website on top left corner.
When the page is opened for the first time you will only have 3 buttons on the navbar which are home, sign in and sign up buttons.
And then once the user is logged in you will only have 5 buttons which are home, find employee, profile, new employee and log out.

#### Home
This page which is the main and first page when user firstly enters the website. On this page the user will see a big picture along with a setence/title within this big picture. Below this picure there are 2 sections which are the about section and the section that tries to explain a little bit what the app is about and then below these 2 sections there is the footer.

#### Log In
The sign in page is the page which the user can log in themselves.

#### Sign up 
The sign up page is the page which the user can register themselves for the first time.

#### Log out
The log out page is the page which the user can log themselves out of the page. Which it takes straigt away to the login page.

#### Find Employee
This page will show you all the employees.

#### Job Market
This page will show the 4 of the most wanted job market with details.

#### Profile
This page will show the user's profile.

#### New Employee
This page is the page designed to add the employees to their designated departments.

#### Departments 
This page will only be shown to the admin.

## Technologies used
### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5) - used to create the HTML base.
* [CSS](https://en.wikipedia.org/wiki/CSS) - used to give style to the HTML5 elements.
* [JavasCript(JQuery)](https://en.wikipedia.org/wiki/JavaScript) - used to 
incorporate behaviors to the website.
* [Python](https://www.python.org/) - used to create the back-end of the website.

### Libraries and Frameworks
* [Font Awesome](https://fontawesome.com/) - I used font Awesome for Icons.
* [Materialize](https://materializecss.com/) - I used Materialize for the website structure.
* [Google Fonts](https://fonts.google.com/) - I used Googgle Fonts to obtain a better font for the website text.

### Tools
* [Gitpod](https://www.gitpod.io/) - I used gitpod for better tracebility.
* [Github](https://github.com/) - I used github for creating my repository
* [Git](https://git-scm.com/) - I used git as version control for better record of my coding.
* [Balsamic](https://balsamiq.com/wireframes/) - I Used it to create the Wireframes
* [Ami Mockup Image](http://ami.responsivedesign.is/) - I used it to create the mockup image with the website displayed in 4 different device frames.
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [Javascript Validation](https://beautifytools.com/)
* [SweetAlert](https://sweetalertjs.js.org)
* [Heroku](https://id.heroku.com/login)
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
* [SweetAlert](https://sweetalert.js.org/guides/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/)
* [MongoDB](https://www.mongodb.com/)

## Information Architecture

MongoDB atlas was the platform used for storing data.

A diagram has been made.

![Smarty data diagram](/static/images/SMARTY.png)

## Testing
### Validators

These validators below were used in order to check the projects against syntax errors.

* [W3C HTML Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JSHint](https://jshint.com/)
* [PEP8](https://www.python.org/dev/peps/pep-0008/)

### Test User Storie
#### First look from user
A brief explanation about the website in regards to what the website is about.

![User first look](/static/images/userstories.PNG)

#### User able to register themselves
A user only needs to click on the "Sign up" button on navbar.

![Register](/static/images/register.PNG)

#### User able to look at a few job markets 
If a user wants to look at a few job markets for curiosity. There is a page that was buit including 4 job markets.

![Job Market](/static/images/job_market.PNG)

#### Access to the website on mobile and desktop
Any user should be able to access the website from mobile and it still be have a nice experience surfing on the website. The website should be responsive and it can not brake.

![Mobile](/static/images/phone.PNG)

#### Access to log in to the website
Any existing user who can provide the right username and password can have access to the website.

![Log In](/static/images/login.PNG)

In case the existing does not provid correct the either username or password. A red card will pop up on the screen warning the user.

![Error](/static/images/error.PNG)

#### Profile Page
After the user can provide the correct info to log in to the website. A profile page will be shown on the screen.

![Profile](/static/images/profile_.PNG)

#### A user can add employees to the website
Any user can add employee to the Smarty system.

![Add Employee](/static/images/addemployees.PNG)

There is another tab as well to insert employees documents. This tab is a future feature to be worked on.

![Add Document](/static/images/adddocuments.PNG)

#### Find employee by name or department
A user has the option to find an employee that has been added to Smarty system. It can be done by the employee's name or department.

![Find Employee](/static/images/findemployee.PNG)

#### Log out
A user when wants to log out of the website they can click on the "Log out" button on the navbar and then the page goes to the login page.

![Log out](/static/images/Log_out.PNG)




























