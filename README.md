# La Casa del Gelat – Stock Controller:

La Casa del Gelat, Stock Controller, is an app designed to allow a closer management of a real life ice cream shop located in Olot, Catalunya. This is my family’s shop and therefore it seemed like a good idea to put my work into practice for something that could be useful in the real world.

In a sense, it’s an app that allows for a centralized source of information that can contain all of the recipes, stocked ingredients and it also allows for calculations on the amount of ingredients needed in an event.

You can find the live link for this website here: https://lpewton-stock-controller.herokuapp.com.

## TABLE OF CONTENTS:

  * TABLE OF CONTENTS:
  * User Experience (UX):
    + App purpose
    + App goals
    + Target
    + Displays
    + Colors and design
    + User Stories
  * Roles
  * Database Schema:
    + Ingredient
    + Recipe
    + Custom User
  * Features
  * Features left to implement
  * Unfixed bugs
  * Major Issues Found
  * Manual Testing:
    + Ingredient
    + Recipes
    + Website
    + User Stories Completion
    + Security Measures
  * Validator Testing
  * Technologies Used
  * Deployment:
    + In the terminal
    + In settings.py
    + In ElephantSQL
    + In the Heroku app
    + In the app
  * Credits

## User Experience (UX):

### App purpose:
The purpose of the Stock Controller is to provide a centralized hub of information that is essential to the shop, like the recipes and ingredients that are needed, as well as keeping a closer eye on the stock. 

Another issue the app helps with is keeping a close eye on the stock, providing a clear visual idea of the ingredients that are about to run put.

Finally, the app helps with he calculation of how many ingredients are needed for a certain event with an X number of recipes, as well as giving the user the costs and profits that this will provide.

### App goals:
One of the issues faced on the day to day in this shop was that the stock ran out and it was not know until it was too late, which caused major delays and headaches. If each employee of the shop marks on the website when an ingredient has been removed it provides a visual indication that can be seen without even being present in the shop and can avoid headaches.

Furthermore, another issue found in the shop was the fact that all the information on recipes, costs, profits… was located in different folder and finding resources could prove difficult. With this app the problem is solved as the recipes, profits and costs are all accessible in one location.

Finally, another thing that wasn’t an issue but does make life easier was added. The shop also does events (weddings, birthdays, parties…), in which the clients request a certain amount of recipes for the day. The app has also has the capacity to see how many ingredients would be required for these recipes, and what the total cost and profit for them would be.

### Target:
The target for this app are the employees of La Casa del Gelat. That is why it’s only accessible if the user is authorized. As this app is for education purposes, the credentials are the following:

![Screen Shot 2023-05-15 at 01 39 33](https://github.com/lpewton/stock-controller/assets/114712846/decc1924-b155-4f2f-9aa7-897f8b8ab56d)


### Displays:
The layout of the app is clear, communicative and there is an easy intuition on how to find the information.

### Colors and design:
Since this is a practical site that is not available to all users the design was very minimalistic. The colors for the shop have been added in the heading and the rest are basic colors to alert the user of relevant information. 

For instance, in the ingredients page if an ingredient is about to run out (there is less than 1000g or 1000 mililiters of it left) the ingredient will display as red. If it's beginning to run out it will be displayed in yellow and if there is a comfortble quantity of this ingredient it will be shown in green. 


### User Stories:
The Agile methodology has been used during this app’s creation. This has been done by having biweekly meetings with the shop manager, addressing their needs and using the to create user stories. All these user stories have come directly from the manager and their needs. They can be found below:

1. As a **stock manager:**
- I can **calculate how much stock I need to make an X number of recipes** so that **I know how much to buy for an event**.
- I can **add, remove or edit ingredients** so that **I can keep the list updated**.
- I can **see how much stock is available** so that **I know if I need to buy any**.
- I can **add and remove recipes** so that **I can keep track of what is available**.
- I can **see how much profit each recipe generates** so that **I can evaluate the most productive recipes and determine a price for them**.
- I can **visualize a list of items that have run out** so that **I know what we need**.
- I can **add expiration dates to the ingredients** so that **they disappear when they expire**.
- I can **see how much stock I need for a recipe** so that **I know how much I need to buy**.

2. As a **cook:**
- I can **see a list of the recipes with its ingredients** so that **I know how to make a recipe**.

3. As a **scooper:**
- I can **add and remove units from the stock** so that **it can remain updated**.

## Roles and registration:
As this application i meant for a buisness, different roles have been applied to the users. From the scooper, cooks and stock-controller. Each one of these roles has their own visibility permissions.

For instance, the administrators can see, add and edit all entries. The cooks cannot sign users up, add or edit ingredients. And the scoopers can only alter and see the stock.

As for the registration, the app still has a fully functioning registration system. However, as it will be a private app, the only users authorized to register new accounts are the stock-controllers and the superusers. This is purely for security and confidentiality reasons.

## Database Schema:
### Ingredient:
![Screen Shot 2023-05-09 at 01 13 05](https://user-images.githubusercontent.com/114712846/236965927-71d25145-812e-4308-9153-f67ee7d26413.png)

### Recipe:
![Screen Shot 2023-05-09 at 01 13 17](https://user-images.githubusercontent.com/114712846/236965947-f5284ec6-46de-4eca-b6eb-6d937f8d5b62.png)

### Custom User:
![Screen Shot 2023-05-09 at 01 13 26](https://user-images.githubusercontent.com/114712846/236965965-b8c79b84-a232-4972-a5a7-91f182e7c4f3.png)

## Features:
### Landing page:
What the user sees before they log in.

![Screen Shot 2023-05-09 at 17 22 32](https://github.com/lpewton/stock-controller/assets/114712846/5af0b854-2834-4426-98f5-dcfe4987300b)

### Log In page:
Where the user logs in.

![Screen Shot 2023-05-09 at 17 23 16](https://github.com/lpewton/stock-controller/assets/114712846/5c784fbd-3983-479e-8ad4-c9ed4689eaaa)

### Stock items page:
The stock is displayed here and the user can add and edit ingredients. They can also add and remove them from the stock.

![Screen Shot 2023-05-15 at 01 41 32](https://github.com/lpewton/stock-controller/assets/114712846/99583a8d-82fb-4b58-9707-2411b390ef2e)

### New Ingredient form:
Where the user can add an ingredient to the stock list.

![Screen Shot 2023-05-15 at 01 42 35](https://github.com/lpewton/stock-controller/assets/114712846/7cb2870c-1cc1-4b90-be1b-6cdb622553b3)

### Edit Ingredient form:
Where the user can edit an ingredient.

![Screen Shot 2023-05-15 at 01 43 03](https://github.com/lpewton/stock-controller/assets/114712846/e4693cb3-2309-4e53-a3b3-72e483dc68bd)

### Stock List page:
Where all the stock is shown with the total stock value.

![Screen Shot 2023-05-15 at 01 41 03](https://github.com/lpewton/stock-controller/assets/114712846/d4ed8f3b-00a4-43fb-8aba-0088b9aa306a)

### Recipes page:
All the recipes are shown here.

![Screen Shot 2023-05-15 at 01 43 26](https://github.com/lpewton/stock-controller/assets/114712846/0cf8745a-b799-4744-897b-72306acf861e)

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

![Screen Shot 2023-05-15 at 01 44 20](https://github.com/lpewton/stock-controller/assets/114712846/136ff3e7-ad4c-4e58-820d-d4d1fd773478)

### Log Out page:
Where the user logs out.

![Screen Shot 2023-05-15 at 01 44 39](https://github.com/lpewton/stock-controller/assets/114712846/6b98d947-b988-44a0-9d72-69ff49e0065d)

## Features left to implement:
- A new page that contains a list of all the ingredients that are in red, so there is a visual representation of the ingredients that need to be purchased
- Add expiration dates to the ingredients so that the user knows when he can’t count on them and, eventually, have them disappear automatically from the list
- Get the app to send an email to the providers to order ingredients automatically when they run out

## Unifxed bugs:
- The new recipes form is a bit complex, I tried to make it easier by expaining the procedure in steps and in the future I would like to simplify the process. However, with the time-frame I had and working with the models, it was not possible for me to do so at this moment.

## Major Issues Found:
1. Bootstrap not working initially:
- Through revision of everything I had done to insert the modals, I realized I had been using the Bootstrap 4 code for my app
- I then changed what needed to be modified and did not repeat that mistake again

2.	Migration issues:
- The app wasn’t migrating some updates on models because a certain element did not exist
- With the help of the tutor support, I reset the table manually from my ElephantSQL database

3.	Not being able to provide the total stock cost:
- I was not able to put the total stock cost for one ingredient, and showed behind every ingredient
- With the {{ ingredient_list.0.total_cost }} I was able to show the total cost for only the first ingredient in the list (which will always be there), as it was the same for all ingredients

4. Customuser superuser did not have any permissions on the admin panel:
- Every time a superuser was created, they could not enter the admin panel or couldn't modify any entries there
- The database was corrupted. All migrations were deleted and SQL database was reset manually

## Manual Testing:
### INGREDIENT:
- Names are unique
- Cannot set a negative value for units
- No blank names
- Units Cannot have decimals
- Should be lowercase sensitive
- Cannot reach -1 in stock

### RECIPES:
- Ingredient quantities cannot be repeated
- Names are unique
- Ingredient quantities have to be positive
- No blank names
- Cannot reach -1 in stock
- Cannot set a negative value for units

## WEBSITE:
| Test  | Result | Status |
| ------------- | ------------- | ------------- |
| User can log in  | All user types (scooper, cook and stock-controller) can log in  | PASSED |
| User can see pages when logged in  | All user types (scooper, cook and stock-controller) can see the pages correctly, if they are not logged in, they are shown the log in option  | PASSED |
| Ingredient quantities can be altered  | Ingredient quantities can be altered, but not under zero, and display as red when they reach zero | PASSED |
| Ingredient colors work correctly  | Ingredient colors change according to the qquantity of them left | PASSED |
| User can add ingredients to stock  | Only stock managers can add new ingredients, and they are added correctly through form validation and error messages | PASSED |
| There is double confirmation before deleting an ingredients or recipes  | A modal pops up to ensure that deletion is intentional, the deleted item is the correct one and all the buttons work correctly | PASSED |
| User can delete ingredients in stock  | Only stock managers can delete ingredients, and they are deleted correctly through form validation and error messages | PASSED |
| User can only delete ingredients in stock if they're not part of any recipes | Error message appears if you try to delete an ingredient that's part of a recipe | PASSED |
| Pagination works correctly | Pagination displays the correct features and only appears when needed | PASSED |
| All numbers are calculated correctly on stock-list  | Numbers in stock-list reflect the correct numbers that they should | PASSED |
| Search ingredient and recipes works correctly  | Each search engine works correctly and can search by name or provider | PASSED |
| All recipes are shown in recipes page  | Recipes code shows correctly when loading the page | PASSED |
| Recipes quantities can be altered  | Recipes quantities can be altered, but not under zero, and display as red when they reach zero | PASSED |
| Add ingredient quantities can be used to create new recipes  | Form works as expected, without issues | PASSED |
| New recipes can be created  | They can be created and are displayed in the recipes page correctly after | PASSED |
| User can add recipes to the recipes calculation form  | Form only accepts integers and over zero, if not, it will display an error message | PASSED |
| Recipes in recipes calculation form cannot be repeated  | If a recipe is put in twice, the sum of it will be shown in the recipes list | PASSED |
| Reset button works correctly in recipes calculation form  | All recipes in the recipes calculation form are deleted correctly when that is clicked | PASSED |
| Calculate ingredients button leads to the correct page  | Calculate ingredients button works as expected | PASSED |
| Ingredients result page shows the correct ammounts  | It shows the correct ammount and also does not allow ingredients to be repeated within it, it sums their quantities | PASSED |
| Sign up page allows managers to register new employees  | New employees of every working type can be registered here and the procedure is successful | PASSED |
| Logout page allows users to be logged out  | Logout page works as expected | PASSED |
| Users have to be authorised and the correct worker type to access pages  | If user is not logged in or the correct worker type, they will be redirected to the home page | PASSED |


### USER STORIES COMPLETION:
1. As a **stock manager:** I can **add, remove or edit ingredients** so that **I can keep the list updated**: 
- These features were tested through many devices and browsers, along with the testing validations metioned above. 
2. As a **stock manager:** I can **add and remove recipes** so that **I can keep track of what is available**.
- These features were also tested through many devices and browsers, along with the testing validations metioned above.
3. As a **stock manager:** I can **see a list of how much stock is available** so that **I know if I need to buy any**:
- The list exists and is responsive throughout all device sizes.
4. As a **stock manager:** I can **calculate how much stock I need to make an X number of recipes** so that **I know how much to buy for an event**:
- This was also accomplished by creating different scenarios, calculating the ingredients manually and then comparing them. The results are always the same.
5. As a **stock manager:** I can **see how much profit each recipe generates** so that **I can evaluate the most productive recipes and determine a price for them**.
- Again, the profits were calculated manually and then compared to the ones the app gave. the results were always the same.
6. As a **cook:** I can **see a list of the recipes with its ingredients** so that **I know how to make a recipe**.
- The recipe list and recipe detail pages are available for only the cook and stock controller to see, as intended, and it's responsive to all devices.
As a **scooper:** I can **add and remove units from the stock** so that **it can remain updated**.
- This was tested manually from many browsers, with many device sizes. It worked every time. 

In conclusion, all completed user stories work properly and as intended, and the non-completed user stories will be finalised in the near future to make this app as useful as possible.

### SECURITY MEASURES:
All app functions were tested several times to make sure they worked under many conditions.

Also, the ingredients and recipes are protected so that ingredients can only be deleted if they are not part of a recipe. Finally, when deleting ingredients, the user is offered double confirmation to make sure they make no mistakes.

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
1. Add app to installed apps

### In ElephantSQL:
1. Create an external database

### In the Heroku app:
1. Create a new Heroku app
2. In config vars, add the following variables:
- SECRET_KEY: Insert secret key here
- PORT: 8000
- CLOUDINARY_URL: API environment variable
- DATABASE_URL: value supplied by Heroku

### In the app:
1. Create an env.py file
2. Link the database, cloudinary and secret key to the env.py file
3. Add the database url, cloudinary url and secret key to the settings.py file
4. Add the Heroku app to allowed hosts
5. Create the Procfile file
6. Push the project to Github
7. Connect the heroku app to the github repository and click on deploy

## Credits:
A lot of this project was based on the projects shown at the Full Stack Software Developement Professional Diploma at Code Institute. Especially the *I think therefore I Blog* and *Hello Django* projects.

I also got a some of the ideas and coding techniques from participating in Code Institute hackathons and Stack Overflow.

I would like to thank the shop manager for allowing me to use the buisness as a test for my learning carreer and for taking the time to meet with me when we did. 

Finally, I would also like to thank my tutor, Martina Terlevic, and the Code Institute tutor assistants for helping me through the tough times while developing the app.

### Disclaimer:
Please bear in mind that, as per petition of the manager to mantain the privacy of their recipes, they are all missing one or two ingredients, so please do not try making them at home.
