# Baking Hot! A website application for viewing and sharing baking recipes.

Site strapline: “Baking Hot! The No. 1 Spot For All Your Baking Recipes!”

For the site owners, the purpose of this website application is to earn revenue by advertising other company’s products such as baking ingredients and kitchen equipment.
 
In order to attract potential customers, the owners, will regularly publish free baking recipes on the site. They will also interact with external users’ comments and questions related to those recipes. 

For external users, the purpose of using this site is, not only to view existing recipes, but to share their own as well.

## UX
 
### Website Audience

The app is aimed at users, from beginners to advanced, who want to make a variety of home-made baked items, and are looking for free recipes and baking tips.

### User Stories

Initially, the site will have two types of User: Basic and Admin. It would be desirable to create other types of users, e.g. Trusted User, but the facility to do this will not be included in this phase. However, a Users collection will be included in the database. User records already in this collection imply a login facility exists and such users have already been created through a registration process.

User permissions:

- Basic Users: These will be assumed to have registered with the site and created login details. They will be able to add and update recipes and reviews.

- Admin Users: This is the site owner or his/her employees. They will have full control over the entire data content of the site, including creating, viewing, updating, archiving and deleting of any user data.

Note: Not all of the above permissions will be implemented in the first release via the website.

THIS RELEASE:

BASIC USER and ADMIN USER stories to be catered for:

I want to

- add my recipes

- view all recipes

- update my recipes

- hide my recipes

- delete my recipes

- add new recipe categories

- view all recipe categories

- update my recipe categories

- delete my recipe categories

FUTURE RELEASE:

Additional BASIC USER stories to be catered for:

I want to

- unhide my hidden recipes

- add a review to recipes added by others

- have my recipes reviewed by others

- view any reviews

- update my reviews of other users' recipes

- delete my reviews of other users' recipes

Additional ADMIN USER owner stories to be catered for:

I want to

- update any recipe

- hide any recipe

- unhide any hidden recipe

- delete any recipe

- add any review

- update any review

- delete any review

- create any user

- update any user

- delete any user (except Admin)

- delete any recipe category

### Wireframes

The files below are stored in the [_Project Documentation](https://github.com/kevald1963/milestone-3-recipe-application/tree/master/_Project%20Documentation) folder in GitHub.

- [Home page, narrow screen, Section 1.pdf](https://github.com/kevald1963/milestone-3-recipe-application/blob/master/_Project%20Documentation/Home%20page%2C%20narrow%20screen%2C%20Section%201.pdf)
- [Home page, narrow screen, Section 2.pdf](https://github.com/kevald1963/milestone-3-recipe-application/blob/master/_Project%20Documentation/Home%20page%2C%20narrow%20screen%2C%20Section%202.pdf)
- [Recipes page, narrow screen.pdf](https://github.com/kevald1963/milestone-3-recipe-application/blob/master/_Project%20Documentation/Recipes%20page,%20narrow%20screen.pdf)
- [Add Recipes page, narrow screen.pdf](https://github.com/kevald1963/milestone-3-recipe-application/blob/master/_Project%20Documentation/Add%20Recipes%20page,%20narrow%20screen.pdf)

### Database structure

The MongoDB document database will be used by this site for all data storage. Collections and related fields, identified for this phase are shown in the Excel spreadsheet below, stored in the [_Project Documentation](https://github.com/kevald1963/milestone-3-recipe-application/tree/master/_Project%20Documentation) folder in GitHub.

- [Database collections - Baking Hot.xlsx](https://github.com/kevald1963/milestone-3-recipe-application/blob/master/_Project%20Documentation/Database%20collections%20-%20Baking%20Hot.xlsx)

## Features

### Existing Features

- Common navigation bar:
 - Provides links to other pages within site. On narrow screens, links are collapsed into a 'hamburger' menu.

Note: All pages display sponsored image links for baking ingredients, equipment, starting kits, etc.

- Home page (index.html):
  - Explains purpose of site.
  - Displays a Recipe of the Day with a visually-appealing image.
  - Invites users to subscribe to weekly newsletter.

- Recipes page (recipes.html):
  - Lists all the recipes, in Category order, on the database, allowing View, Update, Hide and Delete operations for each.
  - Each recipe is displayed in a collapsible 'accordion' component and can be expanded to show summary details.

- View Recipe page (view_recipe.html):
  - Displays a single recipe, in read-only mode, showing all associated data such as Category, Description, Ingedients, Method, etc.
  - Button provided to navigate back to Recipes page.

- Edit Recipe page (edit_recipe.html):
  - Displays a single recipe, in write mode, allowing user to amend any associated recipe data.
  - Buttons provided to update changes or cancel without updating. Both navigate back to Recipes page.

- Hide button (on recipes.html):
  - Allows user to hide the recipe without deleting it. An information message is displayed explaining the recipe can shown again using the Archive page (not implemented in this release).
  - The Recipes page is refreshed after the Hide button is clicked, so that the recipe disappears from the page.

- Delete button (on recipes.html):
  - Allows user to permanently delete the recipe.
  - The Recipes page is refreshed after the Delete button is clicked, so that the recipe disappears from the page.

- Add Recipe page (add_recipe.html):
  - Displays a single recipe form, in write mode, allowing user to enter recipe data.
  - Buttons provided to insert changes or cancel without inserting. Both navigate back to Recipes page.

- Recipe Categories page (recipe_categories.html):
  - Lists all the recipe categories, in Category Name order, from the database, allowing Update and Delete operations for each.
  - Button provided at bottom of page to navigate to Add Recipe Category page.
  
- Edit Recipe Category page (edit_recipe.html):
  - Displays a single recipe category, in write mode, allowing user to amend it.
  - Buttons provided to update changes or cancel without updating. Both navigate back to Recipes Categories page.

- Add Recipe Categories page (recipe_categories.html):
  - Displays a single field for user to enter new Category Name.
  - Buttons provided to add new Category Name or cancel without inserting. Both navigate back to Recipe Categories page.

- Delete button (on recipe_categories.html):
  - Allows user to permanently delete the category.
  - The Recipe Categories page is refreshed after the Delete button is clicked, so that the category disappears from the page.

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

- [MongoDB](https://www.mongodb.com/)
  - A document database used to store all user data.

- [JQuery](https://jquery.com) / [JavaScript](https://www.w3schools.com/js/js_versions.asp)
  - Used to simplify DOM manipulation for numerical field validation, multi-line field creation / removal, etc.

- [Python]

- [Flask]

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

- Maximum temperatures for domestic ovens [The Engineering Tool Box](https://www.engineeringtoolbox.com/gas-cookers-d_130.html)

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
