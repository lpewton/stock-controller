# La Casa del Gelat – Stock Controller:

La Casa del Gelat, Stock Controller, is an app designed to allow a closer management of a real life ice cream shop located in Olot, Catalunya. This is my family’s shop and therefore it seemed like a good idea to put my work into practice for something that could be useful in the real world.

In a sense, it’s an app that allows for a live control over the shop's stock as well as a centralized source of information that contains all of the recipes, stocked ingredients and their qualities. Finally, it also allows for calculations on the amount of ingredients needed for an event.

You can find the live link for this website here: https://lpewton-stock-controller.herokuapp.com.

## TABLE OF CONTENTS:
  * [User Experience (UX):](#user-experience-ux)
    + [App purpose](#app-purpose)
    + [App goals](#app-goals)
    + [Target](#target)
    + [Displays](#displays)
    + [Colors and design](#colors-and-design)
    + [User Stories](#user-stories)
  * [Roles and Registration](#roles-and-registration)
  * [Database Schema:](#database-schema)
    + [Ingredient](#ingredient)
    + [Recipe](#recipe)
    + [Custom User](#custom-user)
  * [Features](#features)
  * [Requirements.txt](#requirementstxt)
  * [Features left to implement](#features-left-to-implement)
  * [Unfixed bugs](#unfixed-bugs)
  * [Major Issues Found](#major-issues-found)
  * [Manual Testing:](#manual-testing)
    + [Ingredient](#ingredient-model)
    + [Recipes](#recipes-model)
    + [Website](#website)
    + [User Stories Completion](#user-stories-completion)
    + [Security Measures](#security-measures)
  * [Validator Testing](#validator-testing)
  * [Technologies Used](#technologies-used)
  * [Deployment:](#deployment)
    + [In the terminal](#in-the-terminal)
    + [In settings.py](#in-settingspy)
    + [In ElephantSQL](#in-elephantsql)
    + [In the Heroku app](#in-the-heroku-app)
    + [In the app](#in-the-app)
  * [Credits](#credits)

## User Experience (UX):

### App purpose:
The purpose of the Stock Controller is to provide a centralized hub of information that is essential to the shop, like the recipes and ingredients that are needed, as well as keeping a closer eye on the stock. 

Another issue the app helps with is keeping a close eye on the stock, providing a clear visual idea of the ingredients that are about to run out.

Finally, the app helps with the calculation of how many ingredients are needed for a certain event with an X number of recipes, as well as giving the user the costs and profits that this will provide.

### App goals:
One of the issues faced on the day to day in this shop was that the stock ran out and it was not known until it was too late, which caused major delays and headaches. If each employee in the shop marks on the website when an ingredient has been used up it provides a visual indication that can be seen without even being present in the shop and can avoid a lot of headaches.

Furthermore, another issue found in the shop was the fact that all the information on recipes, costs, profits… was located in different folders and finding resources could prove difficult. With this app the problem is solved as the recipes, profits and costs are all accessible in one single location.

Finally, another thing that wasn’t an issue but does make life easier was added. The shop also does events (weddings, birthdays, parties…), in which the clients request a certain amount of recipes for the day. Therefore, it has also has the capacity to see how many ingredients would be required for these recipes, and what the total cost and profit for them would be.

### Target:
The target for this app are the employees of La Casa del Gelat. That's why it’s only accessible if the user is authorized. The current credentials are the following:

| Role  | Username | Password |
| ------------- | ------------- | ------------- |
| Superuser  | admin | casagelat |
| Stock-Controller  | manager | casagelat |
| Cook  | cook | casagelat |
| Scooper  | scooper | casagelat |

### Displays:
The layout of the app is clear, communicative and there is an easy intuition on how to find the information.

### Colors and design:
Since this is a practical site that is not available to all users the design was very minimalistic. The colors for the shop have been added in the heading and the rest are basic colors to alert the user of relevant information. 

For instance, if an ingredient is about to run out (there is less than 1000g or 1000 mililiters of it left) the ingredient will display as red. If it's beginning to run out it will be displayed in yellow and if there is a comfortable quantity of this ingredient it will be shown in green. 

### User Stories:
The Agile methodology has been used during this app’s creation. This has been done by having biweekly meetings with the shop manager, addressing their needs and using the to create user stories. All these user stories have come directly from the manager and their needs. They can be found below:

1. As a **stock manager:**
- I can **calculate how much stock I need to make an X number of recipes** so that **I know how much to buy for an event** (SHOULD HAVE). 
- I can **add, remove or edit ingredients** so that **I can keep the list updated**. (MUST HAVE)
- I can **see how much stock is available** so that **I know if I need to buy any**. (SHOULD HAVE)
- I can **add and remove recipes** so that **I can keep track of what is available**.(MUST HAVE)
- I can **see how much profit each recipe generates** so that **I can evaluate the most productive recipes and determine a price for them**. (COULD HAVE)
- I can **visualize a list of items that have run out** so that **I know what we need**. (COULD HAVE)
- I can **add expiration dates to the ingredients** so that **they disappear when they expire**. (WON'T HAVE)
- I can **see how much stock I need for a recipe** so that **I know how much I need to buy**. (MUST HAVE)
- I can **determine the user's roles** so that **I can control who can see what in the app**. (MUST HAVE)

2. As a **cook:**
- I can **see a list of the recipes with its ingredients** so that **I know how to make a recipe**. (MUST HAVE)

3. As a **scooper:**
- I can **add and remove units from the stock** so that **it can remain updated**.(MUST HAVE)

## Roles and registration:
As this application is meant for a buisness, different roles have been applied to the users. These are the scooper, cooks and stock-controller. Each one of these roles has their own visibility permissions.

For instance, the administrators can see, add and edit all entries. The cooks cannot sign users up, add or edit ingredients. And the scoopers can only alter and see the stock.

As for the registration, the app has a fully functioning registration system. However, as it will be a private app, the only users authorized to register new accounts are the stock-controllers and the superusers. This is purely for security and confidentiality reasons.

## Database Schema:
### Ingredient:
| Entry  | Type |
| ------------- | ------------- | 
| Name  | Char Field | 
| Unit Price  | Float Field | 
| Unit Weight  | Integer |
| Units  | Integer | 
| Type  | Integer(Choices) | 
| Supplier  | Char Field | 

### Recipe:
| Entry  | Type |
| ------------- | ------------- | 
| Recipe Name  | Char Field | 
| Ingredient  | ManytoMany Field | 
| Notes | Char Field |
| Tubs  | Integer | 

### Custom User:
| Entry  | Type |
| ------------- | ------------- | 
| Username  | Username Field | 
| Password  | Password Field | 
| Worker Type  | Char Field(Choices) |

## Features:
### Landing page:
What the user sees before they log in.

![Screen Shot 2023-05-16 at 01 18 06](https://github.com/lpewton/stock-controller/assets/114712846/617891d5-ba94-44bc-9877-e8a7c2638308)

### Log In page:
Where the user logs in.

![Screen Shot 2023-05-09 at 17 23 16](https://github.com/lpewton/stock-controller/assets/114712846/5c784fbd-3983-479e-8ad4-c9ed4689eaaa)

### Stock items page:
The stock is displayed here and the user can add and edit ingredients. They can also add and remove them from the stock.

![Screen Shot 2023-05-16 at 01 19 58](https://github.com/lpewton/stock-controller/assets/114712846/6dc4e5fa-01da-4c79-9185-2f141758718a)

### New Ingredient form:
Where the user can add an ingredient to the stock list.

![Screen Shot 2023-05-16 at 12 11 59](https://github.com/lpewton/stock-controller/assets/114712846/a3e0eced-1892-4713-a1e4-6d4edc76ccad)

### Edit Ingredient form:
Where the user can edit an ingredient.

![Screen Shot 2023-05-16 at 12 12 38](https://github.com/lpewton/stock-controller/assets/114712846/444a0563-45ff-464b-886c-a69296d97090)

### Stock List page:
Where all the stock is shown with the total stock value.

![Screen Shot 2023-05-15 at 01 41 03](https://github.com/lpewton/stock-controller/assets/114712846/d4ed8f3b-00a4-43fb-8aba-0088b9aa306a)

### Recipes page:
All the recipes are shown here.

![Screen Shot 2023-05-16 at 16 07 37](https://github.com/lpewton/stock-controller/assets/114712846/464a332b-4ddb-4da4-bc0e-b19a88456390)

### New Recipe form:
Form to add a new recipe.

![Screen Shot 2023-05-15 at 01 43 56](https://github.com/lpewton/stock-controller/assets/114712846/57615511-943f-413f-80e0-3e92511c7284)

### Ingredients Calculation page:
Where the user can add the recipes of the ingredients they want to calculate.

![Screen Shot 2023-05-15 at 01 41 59](https://github.com/lpewton/stock-controller/assets/114712846/1f49f53b-f913-46ad-ba2c-5a15dc8de968)

### Ingredients Result page:
Where the ingredients the user needs for your recipes are shown.

![Screen Shot 2023-05-15 at 01 47 53](https://github.com/lpewton/stock-controller/assets/114712846/e6ae57cd-876a-4c40-9b7b-d118cc021f25)

### Sign an Empoyee Up page:
Where the user signs a new employee up.

![Screen Shot 2023-05-16 at 16 07 15](https://github.com/lpewton/stock-controller/assets/114712846/df69fb56-b46e-4868-89d0-5db0a102a5cf)

### Log Out page:
Where the user logs out.

![Screen Shot 2023-05-15 at 01 44 39](https://github.com/lpewton/stock-controller/assets/114712846/6b98d947-b988-44a0-9d72-69ff49e0065d)

### 404 page:
The user is redirected here when the page isn't found. It contains a button that send them to the stock page.

![Screen Shot 2023-05-16 at 00 33 29](https://github.com/lpewton/stock-controller/assets/114712846/966d34be-a281-4ff9-95a4-33434145b70f)

### User not Authorized page:
This is displayed when an unauthorized user tries to enter a page through the URL.

![Screen Shot 2023-05-16 at 15 45 43](https://github.com/lpewton/stock-controller/assets/114712846/e1b758bb-ce03-4ceb-b221-6c3038909500)

## Requirements.txt:
All needed requirements.txt have been added to the app so it works properly. The main vital ones and also the ones added to improve the functionality of the website. 

It's necessary to mention that there were some migration issues and while trying to solve the situation some extra packages were installed to try and resolve the issue. After it was solved, to preserve the integrity of the app I decided best not to remove them to not accidentally delete something important. As a result of that, there are some installed packages that don't have a functionality in requirements.txt. I am aware that this is not the best practice, and it's something I strive to not repeat in the next project.

## Features left to implement:
- A new page that contains a list of all the ingredients that are in red, so there is a visual representation of the ingredients that need to be purchased
- Add expiration dates to the ingredients so that the user knows when he can’t count on them and, eventually, have them disappear automatically from the list
- Get the app to send an email to the providers to order ingredients automatically when they run out

## Unfixed bugs:
- The new recipes form is a bit complex, I tried to make it easier by expaining the procedure in steps but in the future I would like to simplify the process. However, with the time-frame I had and working with the models, it was not possible for me to do so at this moment.

## Major Issues Found:
1. Bootstrap not working initially:
- Through revision of everything I had done to insert the modals, I realized I had been using the Bootstrap 4 code for my app
- I then changed what needed to be modified and did not repeat that mistake again

2.	Migration issues:
- The app wasn’t migrating some updates on models because a certain element did not exist
- With the help of the tutor support, I reset the table manually from my ElephantSQL database.

3.	Not being able to provide the total stock cost:
- I was not able to put the total stock cost for one ingredient, and showed behind every ingredient
- With the {{ ingredient_list.0.total_cost }} I was able to show the total cost for only the first ingredient in the list (which will always be there), as it was the same for all ingredients

4. Customuser superuser did not have any permissions on the admin panel:
- Every time a superuser was created, they could not enter the admin panel or couldn't modify any entries there
- The database was corrupted. All migrations were deleted and SQL database was reset manually

## Manual Testing:
### INGREDIENT MODEL:
- Names are unique
- Cannot set a negative value for units
- No blank names
- Units cannot have decimals
- Should be lowercase sensitive
- Cannot reach -1 in stock

### RECIPES MODEL:
- Names are unique
- Cannot set a negative value for tubs
- No blank names
- Tubs cannot have decimals
- Names should be lowercase sensitive
- Cannot reach -1 in stock
- Ingredient quantities cannot be repeated
- Ingredient quantities have to be positive

All form validations have been tested combining customised code and the automatic django validation systems. All of them work properly.

## WEBSITE:
| Test  | Result | Status |
| ------------- | ------------- | ------------- |
| User can log in  | All user types (scooper, cook and stock-controller) can log in  | PASSED |
| User can see pages when logged in  | All user types (scooper, cook and stock-controller) can see the pages correctly, if they are not logged in, they are shown the log in option  | PASSED |
| All pages are responsive  | All pages are fully responsive in all screen sizes | PASSED |
| User can only see the pages they're allowed to see  | All user types (scooper, cook and stock-controller) can only see the pages they're allowed to  | PASSED |
| Ingredient units can be altered  | Ingredient unit quantities can be altered, but not under zero, and display as red when they reach less than 1000g or ml | PASSED |
| Ingredient colors work correctly  | Ingredient colors change according to the qquantity of them left | PASSED |
| User can add ingredients to stock  | Only stock managers can add new ingredients, and they are added correctly through form validation and error messages | PASSED |
| User can edit ingredients in the stock  | Only stock managers can edit ingredients qualities, and they are correctly edited through form validation and error messages | PASSED |
| There is double confirmation before deleting an ingredients or recipes  | A modal pops up to ensure that deletion is intentional, the deleted item is the correct one and all the buttons work correctly | PASSED |
| User can delete ingredients in stock  | Only stock managers can delete ingredients, and they are deleted correctly through form validation and error messages | PASSED |
| User can only delete ingredients in stock if they're not part of any recipes | Error message appears if you try to delete an ingredient that's part of a recipe | PASSED |
| Pagination works correctly | Pagination displays the correct features and only appears when needed | PASSED |
| All numbers are calculated correctly on stock-list  | Numbers in stock-list reflect the correct numbers that they should | PASSED |
| Search ingredient and recipes works correctly  | Each search engine works correctly and can search by name or provider | PASSED |
| All recipes are shown in recipes page  | Recipes code shows correctly when loading the page | PASSED |
| Recipes quantities can be altered  | Recipes quantities can be altered, but not under zero, and display as red when they reach zero | PASSED |
| Ingredient quantities can be added and used to create new recipes  | Form works as expected, without issues | PASSED |
| Ingredient quantities are deleted when recipes are  | If the recipe is deleted, its ingredient quantities are deleted as well, proveded they're not part of another recipe | PASSED |
| New recipes can be created  | They can be created and are displayed in the recipes page correctly after | PASSED |
| User can add recipes to the recipes calculation form  | Form only accepts integers and over zero, if not, it will display an error message | PASSED |
| Recipes in recipes calculation form cannot be repeated  | If a recipe is put in twice, the sum of it will be shown in the recipes list | PASSED |
| Reset button works correctly in recipes calculation form  | All recipes in the recipes calculation form are deleted correctly when that is clicked | PASSED |
| Calculate ingredients button leads to the correct page  | Calculate ingredients button works as expected | PASSED |
| Ingredients result page shows the correct ammounts  | It shows the correct ammount | PASSED |
| Ingredients are not repeated in ingredients result page | Page does not allow ingredients to be repeated within it, it sums their quantities | PASSED |
| Sign up page allows managers to register new employees  | New employees of every working type can be registered here and the procedure is successful | PASSED |
| Logout page allows users to be logged out  | Logout page works as expected | PASSED |
| Users have to be authorised and the correct worker type to access pages  | If user is not logged in or the correct worker type, they will be redirected to the home page | PASSED |
| Messages work correctly  | All messages are displayed correctly and when they are meant to be | PASSED |
| 404 page works correctly  | 404 page displays properly and is sensitive to the user's worker type, the "back to stock" button redirects them correctly to the stock page | PASSED |

### USER STORIES COMPLETION:
1. As a **stock manager:** I can **add, remove or edit ingredients** so that **I can keep the list updated**:
- These features were tested through many devices and browsers, along with the testing validations metioned above. 
2. As a **stock manager:** I can **add and remove recipes** so that **I can keep track of what is available**:
- These features were also tested through many devices and browsers, along with the testing validations metioned above.
3. As a **stock manager:** I can **see a list of how much stock is available** so that **I know if I need to buy any**:
- The list exists and is responsive throughout all device sizes.
4. As a **stock manager:** I can **calculate how much stock I need to make an X number of recipes** so that **I know how much to buy for an event**:
- This was also accomplished by creating different scenarios, calculating the ingredients manually and then comparing them. The results are always the same.
5. As a **stock manager:** I can **see how much profit each recipe generates** so that **I can evaluate the most productive recipes and determine a price for them**:
- Again, the profits were calculated manually and then compared to the ones the app gave. The results were always the same.
6. As a **stock-controller** I can **see how much stock I need for a recipe** so that I **know how much I need to buy:**
- All recipes show the correct amounts of stock, as created by the user.
7. As a **cook:** I can **see a list of the recipes with its ingredients** so that **I know how to make a recipe**.
- The recipe list and recipe detail pages are available for only the cook and stock controller to see, as intended, and it's responsive to all devices.
8. As a **scooper:** I can **add and remove units from the stock** so that **it can remain updated**. 
- This was tested manually from many browsers, with many device sizes. It worked every time. 
9. As a **manager** I can **determine the user's roles** so that **I can control who can see what in the app**.
- The user roles exist and determine the visibilities of the user. They have been tested thoroughly.

In conclusion, all completed user stories work properly and as intended, and the non-completed user stories will be finalised in the near future to make this app as useful as possible.

### SECURITY MEASURES:
All app functions were tested several times to make sure they worked under many conditions.

Also, the ingredients and recipes are protected so that ingredients can only be deleted if they are not part of a recipe. Finally, when deleting ingredients or recipes, the user is offered double confirmation to make sure they make no mistakes.

Users can only access their pages when they are logged in and in the correct worker type user. If not, they will be redirected to the home page.

## Validator Testing:
- All HTML templates passed the W3C validator (https://validator.w3.org) without any issues except the {% %} tags.
- All CSS passed the Jigsaw validator (https://jigsaw.w3.org) with no errors found.
- The lighthouse test could not be performed on this app as it's an authenticated required app and it will only register the login page.
- All python code passed the Code Institute Python Linter (https://pep8ci.herokuapp.com/) without any issues.
- The app could be opened from Mozzila Firefox, Chrome and Safari without any issues.

## Technologies Used:
- HTML5
- CSS3
- Bootstrap 5
- Python
- Django
- ElephantSQL

## Deployment:
### In the terminal:
1. Install Django and gunicorn: pip3 install 'django<4' gunicorn
2. Install supporting libraries: pip3 install dj_database_url==0.5.0 psycopg2
3. Install Cloudinary Libraries: pip3 install dj3-cloudinary-storage
4. Create requirements file
5. Create Project
6. Create App 
7. Create requirements file: pip3 freeze --local > requirements.txt
8. Create Project: django-admin startproject STOCK-CONTROLLER 
9. Create App: python3 manage.py startapp stock_controller_app
10. Migrate Changes: python3 manage.py migrate

### In settings.py:
1. Add app to installed apps, at the bottom of the list
2. Set DEBUG = True (For security reasons, it's important to set it back to False at the end of the project)

### In ElephantSQL:
1. Create an external database

### In the Heroku app:
1. Create a new Heroku app
2. In config vars, add the following variables:
- SECRET_KEY: Insert your secret key here
- PORT: 8000
- CLOUDINARY_URL: API environment variable
- DATABASE_URL: value supplied by SQL

### In the app:
1. Create an env.py file in the root directory
2. Link the database, cloudinary and secret key to the env.py file
3. Add the database url, cloudinary url and secret key to the settings.py file, always through the env.py file for security
4. Add the Heroku app to allowed hosts
5. Create the Procfile file
6. Push the project to Github
7. Connect the heroku app to the github repository and click on deploy

## Credits:
A lot of this project was based on the projects shown at the Full Stack Software Developement Professional Diploma at Code Institute. Especially the *I think therefore I Blog* and *Hello Django* projects.

I also got a some of the ideas and coding techniques from participating in Code Institute hackathons and Stack Overflow. For instance, the code for the search recipe and ingredients was learnt from my March hackathon *Women in tech* team.

I would like to thank the shop manager for allowing me to use the buisness as a test for my learning carreer and for taking the time to meet with me when we did. 

Finally, I would also like to thank my tutor, Martina Terlevic, and the Code Institute student support team for helping me through the tough times while developing the app.

### Disclaimer:
Please bear in mind that, as per petition of the manager to mantain the privacy of their recipes, they are all missing one or two ingredients, so please do not try making them at home.