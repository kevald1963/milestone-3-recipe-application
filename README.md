# **Baking Hot! A website application for viewing and sharing baking recipes.**

Site strapline: “Baking Hot! The No. 1 Spot For All Your Baking Recipes!”

For the site owners, the purpose of this website application is to earn revenue by advertising other company’s products such as baking ingredients and kitchen equipment.
 
In order to attract potential customers, the owners, will regularly publish free baking recipes on the site. They will also interact with external users’ comments and questions related to those recipes. 

For external users, the purpose of using this site is, not only to view existing recipes, but to share their own as well.

## UX
 
### Website Audience

The app is aimed at users, from beginners to advanced, who want to make a variety of home-made baked items, and are looking for free recipes and baking tips.

### User Stories

Note: This section has been re-edited as the project nears completion. The initial user stories to be catered for were too ambitious.

Initially, the site will have two types of User: Basic and Admin. It would be desirable to create other types of users, e.g. Trusted User, but the facility to do this will not be included in this phase. However, a Users collection will be included in the database. User records already in this collection imply a login facility exists and such users have already been created through a registration process.

**User permissions:**

- Basic Users: These will be assumed to have registered with the site and created login details. They will be able to add and update recipes and reviews.

- Admin Users: This is the site owner or his/her employees. They will have full control over the entire data content of the site, including creating, viewing, updating, archiving and deleting of any user data.

Note: Not all of the above permissions will be implemented in the first release via the website.

**THIS RELEASE:**

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

**FUTURE RELEASES:**

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

**Note: All pages display sponsored image links for baking ingredients, equipment, starting kits, etc.**

- Common navigation bar:
  - Provides links to other pages within site. On narrow screens, links are collapsed into a 'hamburger' menu.

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

- Add Recipe page (edit_recipe.html):
  - Displays a single recipe form, in write mode, allowing user to enter recipe data.
  - Buttons provided to insert changes or cancel without inserting. Both navigate back to Recipes page.

- Recipe Categories page (recipe_categories.html):
  - Lists all the recipe categories, in Category Name order, from the database, allowing Update and Delete operations for each.
  - Button provided at bottom of page to navigate to Add Recipe Category page.
  
- Edit Recipe Category page (edit_recipe.html):
  - Displays a single recipe category, in write mode, allowing user to amend it.
  - Buttons provided to update changes or cancel without updating. Both navigate back to Recipes Categories page.

- Add Recipe Categories page (add_recipe_categories.html):
  - Displays a single field for user to enter new Category Name.
  - Buttons provided to add new Category Name or cancel without inserting. Both navigate back to Recipe Categories page.

- Delete button (on recipe_categories.html):
  - Allows user to permanently delete the category.
  - The Recipe Categories page is refreshed after the Delete button is clicked, so that the category disappears from the page.

### Features Left to Implement

Although I believe this project largely meets the project requirements, in reality it is only suitable as a prototype to 
demonstrate to users how such a system may work. It is nonetheless a good basis from which to develop the application further. 
Because the system allows the general public to create, read, update and delete data, it struck me that the real starting 
point for a professional version of this project would be to detail the terms and conditions that relate to data created by 
users and how it may be used, who owns it, ensuring quality of content, preventing abuse, trolling etc. These would then 
inform the design decisions to be taken.

The list of features left to implement could be endless, but my main priorities would be:

- A registration and login process, so different security levels can be applied to each user, in order to control their CRUD operations.
- A facility to allow recipe reviews with appropriate CRUD operations.
- A facility to allow users to upload their own images for recipes and personal profiles.
- A facility for Admin users to vet users' photos for suitability and appropriateness.
- A means of randomising the chosen Recipe of the Day on an automatic, scheduled basis.
- A sign-up page for the newsletter allowing users to personalise it to their needs e.g. types of recipes that interest them.
- A means of creating content for an email newsletter by easy selection from the recipe data held on the database.
- A sponsored links database collection storing links for web pages and associated images, along with appropriate CRUD facilities for their management.
- A means of randomising the display of the sponsored link images, across all pages, when a page is refreshed.

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
  - Used to simplify DOM manipulation for numerical field validation, multi-line field creation and removal, etc.

- [Python](https://www.python.org/)
  - Server side programming language to interface between database and HTML pages.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - To allow webpage redirection and rendering.

## Testing

Testing has been achieved through a mixture of automated and manual tests.

**Automated tests** 

These test the Python methods and was implemented using Python's unittest library. 

The tests can be run as follow from a terminal CLI: `python3 -m unittest -v test_run`

The `-v` flag enables verbose output to give a clearer picture of what tests have ran.

**Manual tests** 

The manual testplan is stored in the [_Project Documentation](https://github.com/kevald1963/milestone-3-recipe-application/tree/master/_Project%20Documentation) folder in GitHub.

- [Testplan - Baking Hot.xlsx](https://github.com/kevald1963/milestone-3-recipe-application/blob/master/_Project%20Documentation/Database%20collections%20-%20Baking%20Hot.xlsx)

Please note that a number of bugs were found during manual testing. Those that could not be fixed because of time constraints or a lack of technical knowledge 
have been detailed and flagged for next release.

## Deployment

The project is deployed on Heroku at (https://bakinghot.herokuapp.com)

Deployment process:

**On Heroku website:**
  - Create new app: 'bakinghot'

**On the terminal command line:**
  - Install Heroku on gitpod: `npm install -g heroku`.
  - Login to Heroku: `heroku login -i`. Enter username and password when prompted.
  - Initialise git repository: `git init`.
  - Link GitHub repository to app created in Heroku: `git remote add heroku https://bakinghot.herokuapp.com`.
  - Create requirements file: `pip3 freeze --local > requirements.txt`.
  - Create Procfile with main python file: `echo web: python run.py > Procfile`.
  - Set scale to a single dyno instance: `ps:scale web=1`.
  - Check git status to ensure files created/updated: `git status`.
  - Add the files: `git add .`.
  - Commit the files: `git commit -m "Deploy to Heroku."`.
  - Push project to Heroku: `git push -u heroku master`.
 
**On Heroku website:**
  - In Project Settings for application, set Config Vars:
    - IP: 0.0.0.0
    - PORT: 5000
    - MONGO_URI_BAKING_HOT: mongodb+srv://(user):(password)@myfirstCluster-0wjbq.mongodb.net/baking_hot?retryWrites=true&w=majority

## Credits

- Maximum temperatures for domestic ovens, from [The Engineering Tool Box](https://www.engineeringtoolbox.com/gas-cookers-d_130.html).
- Code snippet: Add and Remove Fields Dynamic and Simple with jQuery, from [Sanwebe.com](https://www.sanwebe.com/snippet/add-and-remove-fields-dynamic-and-simple-with-jquery). 
- Code snippet: Execute different Python code depending on condition sent from HTML form, from a Stack Overflow answer by user 'poply' at [Stack Overflow questions](https://stackoverflow.com/questions/19794695/flask-python-buttons/19794878). 
  Adapted to allow Cancel button implementation on Insert / Update forms so data not unnecessarily written to database if no changes made.

### Content
- The text for many of the recipes was copied from [Doves Farm](https://www.dovesfarm.co.uk/).

### Media
- The photo used on the Home page is obtained from [Doves Farm](https://www.dovesfarm.co.uk/)

### Acknowledgements
- I want to thank my mentor Reuben Ferrante for his enthusiasm, thoroughness and expertise which all helped me to complete this project.
