# La Casa del Gelat – Stock Controller:

La Casa del Gelat, Stock Controller, is an app designed to allow a closer management of a real life ice cream shop located in Olot, Catalunya. This is my family’s shop and therefore it seemed like a good idea to put my work into practice for something that could be practically useful in the real world.

In a sense, it’s an app that allows for a centralized source of information that can contain all of the recipes, stocked ingredients and it also allows for calculations on the amount of ingredients needed in an event.

You can find the live link for this website here: https://lpewton-stock-controller.herokuapp.com.

## TABLE OF CONTENTS:

- User experience (UX)


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
![Screen Shot 2023-05-09 at 00 42 58](https://user-images.githubusercontent.com/114712846/236966901-3bcfec08-e8ec-4907-88f6-04059936e413.png)

### Displays:
The layout of the app is clear, communicative and there is an easy intuition on how to find the information.

### User Stories:
The Agile methodology has been used during this app’s creation. This has been done by having biweekly meetings with the shop manager, addressing their needs and using the to create user stories. These can be found below:

1. As a **stock manager:**
- I can **calculate how much stock I need to make an X number of recipes** so that **I know how much to buy for an event**.
- I can **add, remove or edit ingredients and recipes** so that **I can keep the list updated**.
- I can **see how much stock is available** so that **I know if I need to buy any**.
- I can **be able to alter recipes** so that **I can fix mistakes and update recipes**.
- I can **see how much profit each recipe generates** so that ** can evaluate the most productive recipes and determine a price for them**.
- I can **visualize a list of items that have run out** so that **I know what we need**.
- I can **add expiration dates to the ingredients** so that **they disappear when they expire**.
- I can **see how much stock I need for a recipe** so that **I know how much I need to buy**.

2. As a **cook:**
- I can **see a list of the recipes with its ingredients** so that **I know how to make a recipe**.

3. As a **scooper:**
- I can **add and remove units from the stock** so that **it can remain updated**.

## Database Schema:
### Ingredient:
![Screen Shot 2023-05-09 at 01 13 05](https://user-images.githubusercontent.com/114712846/236965927-71d25145-812e-4308-9153-f67ee7d26413.png)

### Recipe:
![Screen Shot 2023-05-09 at 01 13 17](https://user-images.githubusercontent.com/114712846/236965947-f5284ec6-46de-4eca-b6eb-6d937f8d5b62.png)

### Custom User:
![Screen Shot 2023-05-09 at 01 13 26](https://user-images.githubusercontent.com/114712846/236965965-b8c79b84-a232-4972-a5a7-91f182e7c4f3.png)

## Colors and design:
Since this is a practical site that is not available to all users. The design was very minimalistic. The colors for the shop have been added in the heading and the rest are basic colors to alert the user of some information. 

## Features:
### Landing page:
![Screen Shot 2023-05-09 at 02 31 30](https://user-images.githubusercontent.com/114712846/236966092-f2501b9e-37d0-49b4-b7d7-1d22190ea93e.png)
### Log In page:
![Screen Shot 2023-05-09 at 02 31 45](https://user-images.githubusercontent.com/114712846/236966139-b83d99e5-2c13-445b-9995-9562ddb644db.png)
### Stock items page:
![Screen Shot 2023-05-09 at 02 32 11](https://user-images.githubusercontent.com/114712846/236966154-dbd4548e-01c3-437e-9106-fab5c0ac98ef.png)
### New Ingredient form:
![Screen Shot 2023-05-09 at 02 32 29](https://user-images.githubusercontent.com/114712846/236966170-0d42538f-0278-4757-a59c-31f12543bb61.png)
### Edit Ingredient form:
![Screen Shot 2023-05-09 at 02 32 49](https://user-images.githubusercontent.com/114712846/236966191-9355d02c-a90e-477b-a223-e77eaf42abf6.png)
### Stock List page:
![Screen Shot 2023-05-09 at 02 33 11](https://user-images.githubusercontent.com/114712846/236966200-7fcd9522-8db4-47b9-ae23-554cdcfda503.png)
### Recipes page:
![Screen Shot 2023-05-09 at 02 33 52](https://user-images.githubusercontent.com/114712846/236966340-750786cb-d187-4d40-9bb0-d4dab75103c5.png)
### New Recipe form:
![Screen Shot 2023-05-09 at 02 34 23](https://user-images.githubusercontent.com/114712846/236966358-215caec1-1489-476d-ab41-66ab762f77e6.png)
### Edit Recipe form:
### Ingredients Calculation form:
![Screen Shot 2023-05-09 at 02 34 39](https://user-images.githubusercontent.com/114712846/236966574-ce8aea38-2016-4bdf-b890-1e0de9dd5a40.png)
### Ingredients Result page:
![Screen Shot 2023-05-09 at 02 34 50](https://user-images.githubusercontent.com/114712846/236966601-f9152f81-f7be-41a2-b9c7-16847bf7a1cf.png)
### Sign an Empoyee Up page:
![Screen Shot 2023-05-09 at 02 35 00](https://user-images.githubusercontent.com/114712846/236966625-7b4f1c17-910c-455b-9353-b7e012958685.png)
### Log Out page:
![Screen Shot 2023-05-09 at 02 35 12](https://user-images.githubusercontent.com/114712846/236966848-2b72ef50-62eb-46e4-a35f-02a7e0eb891b.png)

## Features left to implement:
- A new page that contains a list of all the ingredients that are in red, so there is a visual representation of the ingredients that need to be purchased
- Add expiration dates to the ingredients so that theuser knows when he can’t count on them and, eventually, have them disappear automatically from the list
- Get the app to send an email to the providers to order ingredients automatically when they run out

## Major Issues Found:
1. Bootstrap modals not working:
- Through revision of everything I had done to insert the modals, I realized I had been using the Bootstrap 4 code for my app
- I then changed what needed to be modified and did not repeat that mistake again

2.	Migration issues:
- The app wasn’t migrating some updates on models because a certain element did not exist
- With the help of the tutor support, I reset the table manually from my ElephantSQL database

3.	Not being able to provide the total stock cost:
- I was not able to put the total stock cost for one ingredient, and showed behind every ingredient
- With the {{ ingredient_list.0.total_cost }} I was able to show the total cost for only the first ingredient in the list (which will always be there), as it was the same for all ingredients

## Manual Testing:
### INGREDIENT:
- Names are unique
- Cannot set a negative value for units
- No blank names
- Units Cannot have decimals
- Should be lowercase sensitive
- Cannot reach -1 in stock

### RECIPES
- Ingredient quantities cannot be repeated
- Names are unique
- Ingredient quantities have to be positive
- No blank names
- Cannot reach -1 in stock
- Cannot set a negative value for units

### GENERAL:
All app functions were tested several times to make sure they worked under many conditions.

## Validator Testing:

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

I also got a lot of ideas and coding techniques from participating in Code Institute hackathons, Stack Overflow and ChatGPT.

Finally, I would also like to thank my tutor, Martina Terlevic, and the Code Institute tutor assistants for helping me through the tough times while developing the app.
