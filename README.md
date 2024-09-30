# South Roast: an e-commerce website for a local coffee roaster

![Website homepage on different devices](docs/am-i-responsive.png)

Developed by Benedict Amory Chambers
## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Goals](#site-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
3. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colours](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
4. [Technologies](#technologies)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#testing)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [JavaScript Validation](#javascript-validation)
    4. [Python Validation](#python-validation)
    4. [Accessibility](#accessibility)
    5. [Performance](#performance)
    6. [Compatibility](#compatibility)
    7. [Testing user stories](#testing-user-stories)
    8. [Testing user input](#testing-user-input)
    9. [Automated test](#automated-tests)
7. [Bugs](#bugs)
8. [Credits](#credits)
9. [Deployment](#deployment)
10. [Acknowledgements](#acknowledgements)

## Project Goals 

This is an e-commerce website for a fictional local coffee roasters that offers a variety of products and services, and encourages user interaction and repeat business by including social features and other benefits to registering for an account with the site. It focuses on making use of the Django framework to develop a full-stack website with a solid and user-friendly frontend, complete and facile backend integration, and that delivers a good experience for the user and site owner that meets the goals of both. 

### User Goals 

- Easy browsing of the products the user may be interested in purchasing
- A simple and easy checkout process to allow for easy purchases
- A way to view, update, and delete their data; both for previous orders and for community focused user-created content

### Site Goals

- Encourage browsing and repeat purchases by providing a pleasant and attractive user experience
- Build a relationship and familarity between the business and its customers 
- Allow for management of an online business presence to increase custom and make connections

### Developer Goals

- Create an accessible, responsive website that provides the full intended experience to a range of users
- Integrate a functional and sensible backend data model that serves the customer goals and the site owner needs
- Make good use of Django to build a complete, secure, full-stack website as a solo developer

## User Experience

### Target Audience

The target audiences for the website are new customers who are interested in the products offered, repeat customers who would like to further explore the products on offer and who would benefit from engaging with the business and its community more personally, and other local businesses who may be interested in establishing a beneficial wholesale relationship.

### User Stories
#### First Time User

1. Find out what the site has to offer and who it is for
2. Easily navigate around the site; access the Register, Community, About/Contact and Product pages
3. Search for products on the site
4. Add products to the shopping cart and easily update or remove them 
5. Checkout as a guest user 
6. Register for an account
7. Contact the business for a customer or wholesale query


#### Returning User

8. Log in to my account
9. Leave a review for a product
10. Post to the community tab
11. Review my previous orders
12. Update my default delivery info
13. Checkout more easily with my default delivery info
14. Delete my account

#### Site Owner:

15. Showcase all the products the business offers, sorted into categories
16. Allow for community engagement and feedback from customers
17. Easily add or remove products sitewide using the admin page
18. Ensure all orders are saved and completed properly

## Design 

### Design Choices

I have opted for a simple and consistent design across the site. Using bootstrap and custom classes, I have aimed at creating a cohesive style for the site that matches the tone of the business, as a small local coffee roasters. 

### Colours

In keeping with the coffee theme, I have chosen a dark brown background colour for headings and distinct sections, that stands out and complements the lighter brown coffee themed background. I chose to make this darker colour slightly transparent, so that it integrates a little better with the background image and with the soft aesthetic.

### Fonts

To maintain the professional consistency and cohesive aesthetic, I have used two fonts from the same family across the site. For the majority of the informative text, I used a simple and attractive font called [Cabin](https://fonts.google.com/specimen/Cabin). For display fonts in headings and logos, I used the friendly display variant, [Cabin Sketch](https://fonts.google.com/specimen/Cabin+Sketch).

### Structure

The site uses a persistent navigation bar to navigate between the main pages, with several more focused and detailed pages accessed from within the main pages.

1. Homepage - A landing page that demonstrates what the business is offering and establishes the site and user goals

2. Products - A complete list view of all products available. This can be filtered by a variety of categories to make finding the desired product easier. Additionally, in the navigation bar there is a search box by which the user can directly filter all products on the site with a search term.

3. Product Details - This page is accessed by selecting a product on the main Products page. It gives further information about the product offered, with reviews that are created by authorised users, and gives the option to add the product to the shopping cart for purchase.

4. Cart - Displays all products and quantities currently added to the user's cart, which is stored in the session. From here the user can update quantities or remove products.

5. Checkout - The checkout form for the site takes user details for completeing an order, and uses a Stripe card element to process payments securely, ensuring that orders can be completed and accessed even in the case of user or site error. 

6. Community Posts - This is a community focused page where users can post thoughts and images, engaging with the business and other customers. 

7. Account - Here the user can view their previous order history, update their default delivery info for easier checkouts, and delete their account if wished.

8. About/Contact - Simple breakdown of what the site offers both to regular and wholesale customers. Contains the contact form by which users can contact the business via email.

9. Sign In/Register - Pages for a new user to register an account or for an existing user to log back in to their account, built with django-allauth

10. 404 - Custom 404 page to redirect users to the homepage if they run into any errors on the site

### Wireframes
### Enttity Relationship Diagram

## Technologies

### Languages 

HTML5

CSS3

JavaScript

Python

### Frameworks and Tools

[django](https://www.djangoproject.com/)

[django-allauth](https://docs.allauth.org/en/latest/)

[django-star-ratings](https://pypi.org/project/django-star-ratings/)

[jquery](https://jquery.com/)

[Bootstrap](https://getbootstrap.com/)

[Visual Studio Code](https://code.visualstudio.com/)

[Git](github.com)

[Heroku](heroku.com)

[Google Fonts](https://fonts.google.com/)

[Balsamiq](https://balsamiq.com/)

[Obsidian](https://obsidian.md/)

[Font Awesome](https://fontawesome.com/)

[Favicon](https://favicon.io/)

[W3C Markup Validation Service](https://validator.w3.org/)

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

[JSHint](https://jshint.com/)

[CI Python Linter](https://pep8ci.herokuapp.com/)

[WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

[WAVE Web Accessibility Evaluation Tools](https://wave.webaim.org/)


## Features

### Header and Navigation

- The navigation bar is present at the top of every page to allow intuitive and easy navigation
- The navbar collapses into a convenient hamburger menu on smaller screen sizes, and displays different options for logged in users and guests
- Search Bar for filtering products by search terms
- Cart button that updates in real time to show how many items the user has in their cart and links to the cart view page

### Sign In and Registration

- Sign In and Registration pages use django-allauth forms to allow users to create a new account entry in the database and to access an account they have already created
- Form validation built in with django-allauth, along with additional options for forgotten passwords

### Products

- Complete list of products available that can be easily updated with new or deleted products in the admin panel
- Filtering options for products with different tags
- User created product reviews that can be posted and updated by authorised users from the details page

### Star Ratings

- Up-to-date average star ratings from user ratings on all products

### Checkout

- Stripe payments for easy and convenient payment processing on all orders
- Default delivery info option for registered users
- Webhooks to ensure orders can be processed and saved in the event of any errors

### User Profile

- Complete user order history that can be viewed in detail
- Default delivery information form that can be updated by the user

### Community Posts

- Community engagement page allowing for text and image posts for registered users

### Contact Form 

- Easy method to contact site owners for queries via email

## Testing

### HTML Validation

Validated with the W3C Markup Validation Service

### CSS Validation

Validated with the W3C CSS Validation Service

### JavaScript Validation

Validated with JSHint

### Python Validation

Validated with Code Institute's CI Python Linter

### Accessibility

Validated with the WAVE Web Accessibility Evaluation Tools

### Performance

Performance testing by Google Lighthouse in Google Chrome Developer Tools

### Compatibility
### Testing User Stories
### Testing User Input
### Automated Tests 

## Bugs

## Credits

### Media
### External Code

## Deployment

## Acknowledgements