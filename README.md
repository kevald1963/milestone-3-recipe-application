# Baking Hot! A website application for viewing and sharing baking recipes.

Site strapline: “Baking Hot! The No. 1 Spot For All Your Baking Recipes!”

For the site owners, the purpose of this website application is to earn revenue by advertising other company’s products such as baking ingredients and kitchen equipment.
 
In order to attract potential customers, the owners, will regularly publish free baking recipes on the site. They will also interact with external users’ comments and questions related to those recipes. 

For external users, the purpose of using this site is, not only to view existing recipes, but to share their own as well.

## UX
 
### Website Audience

The app is aimed at users, from beginners to advanced, who want to make a variety of home-made baked items, and are looking for free recipes and baking tips.

### User Stories

Initially, the site will have two types of User: Basic and Admin. It would be desirable to create other types of users, e.g. Trusted User, but the facility to do this will not be included in this phase. However, a Users collection will be included in the database. User records already in this collection imply a login facility exists and such users are have already been created through a registration process.


User permissions:

- Basic Users: These will be assumed to have registered with the site and created login details. They will be able to post and update recipes and reviews.

- Admin Users: This is the site owner or his/her employees. They will have full control over the entire data content of the site, including creating, viewing, updating, archiving and deleting of any user data.

BASIC USER and ADMIN USER owner stories to be catered for: 

I want to

- post my recipes

- update my recipes

- ask questions about recipes posted by others

- answer other user’s questions about my recipes

- review recipes posted by others

- update my reviews

Additional ADMIN USER owner stories to be catered for: 

I want to

- update any recipe

- archive any recipe

- restore any archived recipes

- delete any recipe

- update any review

- delete any review

- create any user

- update any user

- archive any user 

- restore any archived user

- delete any user (except Admin)

### Wireframes

The files below are stored in the [_Project Documentation](https://github.com/kevald1963/milestone-3-recipe-application/tree/master/_Project%20Documentation) folder in GitHub.

- Home page, narrow screen.jpg
- Home page, wide screen.jpg

### Database structure

The MongoDB document database will be used by this site for all data storage. Collections and related fields, identified for this phase are shown in the Excel spreadsheet below, stored in the [_Project Documentation](https://github.com/kevald1963/milestone-3-recipe-application/tree/master/_Project%20Documentation) folder in GitHub.

- Database collections - Baking Hot.xlsx

## Features

### Existing Features

### Features Left to Implement

## Technologies Used

- [HTML5](https://www.w3.org/TR/html52/) 
  - To build page structure and content

- [CSS3](https://www.w3.org/standards/techs/css#w3c_all)
  - To style page structure and content.

- [Materialize 1.0.0](https://materializecss.com/)
  - To provide template components to easily create and style responsive elements like the navigation menu, buttons, banners, etc.

- [Google Fonts](https://fonts.google.com/)
  - For 'Roboto' font style used on all pages.

- [Font Awesome 5](https://fontawesome.com/icons?d=gallery)
  - Used to create 'icon' characters for menus, video and audio links, social media, external links, etc.

- [MongoDB](https://www.mongodb.com/)
  - A document database used to store all user data.

- [JQuery](https://jquery.com)
  - Used to simplify DOM manipulation.

- [JavaScript](https://www.w3schools.com/js/js_versions.asp) snippets added to:
  - clear modal forms after form is submitted

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)


### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
