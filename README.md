# Final Project - Lucia & Nicole
This is the final project for OIM3640

Project Members: 
    1. Lucia Prado 
    2. Nicole Gaige 

1. The main idea or goal for our project was to create a cretive, interactive and engaging experience by creating an AI style Mad libs story. This was a game we both used to play when we were little with our friends, however, the original game relied on fixed templates which cause the stories to repeat themselves after a certain amount of tries. Therefore, we decided to do this, as the idea of including OpenAI API would allow us to expand the game further and provide new, different stories every single time based on the style the user chooses. This allows our webpage to provide a more humerous, myesterious or romantic story that changes every single time and provides a personalized story to the inputs of the user. 

Our main goal was to create a webpage were users (mainly children as this is a childrens game, but also anyone that wants to participate), can type in random words they think of following the prompts, and receive instantly a unique AI story tailored to their inputs. This allows the story to be constantly evolving, compared to the previous game that used the fixed templates every single time and the only thing that changed where the inputs given by the user. This adds an element of surprise and enjoyment for the user as the can repeat the same style multiple times and get different stories so that the fun can continue!

Example run: 
- As shown on the first image, once you click on the link it takes you to a Welcome page, where there are blinking emojis, a fun backround and a brief description of what the game does. Then you click the button 'Start creating your Story' which will take you to the main page. 
![Welcome Page](images/welcome_page.png)

- After pressing the button, you are taken to the main webpage which introduces you to all of the input options. These being: Your name, noun, place, adjective, present and past tense verb, animal, golden word and story style. The story style is a drop down feature tha include several story styles to offer more alternatives to the user, these options are: adventure, mystery, fairy tale and silly. Finally the 'golden word' option, is an option we give users to try and find a golden word. This is a specific word we selected and if the user guesses right they unlock a new portal where they are deemed the 'Ultimate Adventurer' and offer kind of a winning recognition to the game. If the user inputs a word but doesn't guess the specific word, the AI model just runs a normal story like it does usually an no error message will appear. After typing all of the inputs and selecting the story style, the user can press the 'Generate Story' button which will create the final story. 
![Main Page](images/main_page.png)

- Finally, the user is taken to the result page, where it presents a title of 'Yout Story' and the user can see the AI generated story that includes all of the inputs the user gave in the previous section. And this is how users can play our game. It is supposed to be a playful, interactive an fun experience, allowing the user to learn, experiment and have fun. This was really fun experience we had while implementing programming tools we learned throughout the semester such as Flask, API Keys and prompt engeneering. 
![Story Page](images/result_page.png)

2. To acess, download and install our software please follow the next steps. 
- 1. First you need to download our project. To do this go to the Github page and clone the repository of Final-Project---Lucia---Nicole. You can also type ' git clone https://github.com/ngaige/Final-Project---Lucia---Nicole'. 
- 2. After this you need to make sure that all the Python dependencies we used in our code are installed. Therefore, you can go to Command Prompt and type 'pip install -r requirements.txt' which will ensure that you have everything installed and everything will work when you run the project. 
- 3. Set up your OpenAI API key. You need to create a .env file and add your OpenAI key. Set up within the file as 'OPENAI_API_KEY = ..." and place yout key there. Do not upload .env file in Github as it will leak the API key and then it won't work anymore. 
- 4. Finally to access the webpage you just run the application. To do this runn app.py in python and in the terminal it should appear a line that says '* Running on http://127.0.0.1:5000'. Click that link and it should take you to the webpage. After this, you are able to use the Webpage and follow the process of the Example Run given in the previous question and then you can get to read your own personalized AI generated story file. If there are any troubleshooting errors, such as stories not generating, flask server errors or HTML formatting looking wrong; I would suggest looking through the API Key, make sure all the dependencies are installed and refresh the webpage server to make sure it continues to work. 

3. These are the diagrams that best describe our project: 
![First Diagram](images/architecture_system.png)
![Second Diagram](images/data_flow_diagram.png)
![Third Diagram](images/web_works_diagram.png)

4. Project Schedule: We had approximately 5 weeks to complete this project. Ever since we are two members working on it, at the very beginning before starting our work, we decided to divide tasks and create a strict timeline. Firstly, on the first week, we had several meetings to brainstorm ideas of the topic of our project and the purpose. We would write all ideas down on a document that we created and shared. Aftwerwards, we made sure to setup and prepare the environment we were going to work on, as well as share (collaborate) the project in Github in order for us to be able to access it. On week 2, as a team, we built the main Python function and tested some story generation in order to make sure that the platform was ready to be used.  Week 4 we made sure to make final design asjustent and clean up some of the Python code, as well as fix the missing imports that would not make the project run smoothly. Fianlly, in week 5, as a team, we run through the project together to ensure everything works. We needed a little bit of more time because we encountered some issues on our API and had to perfeccion the project. Nevertheless, with the extra time that we were able to have, we were able to present a successful and well done work, full of creativity.  


5. Collaboration Plan: For this project, we split the work and had regular check in in order to work efficiently and smoothly. We divided thr work based on what we decided that each of us would work best on, and later combined everything. The tasks were divided the following way:
Nicole : Open AI / Pythong / Logic of the project. She was in charge of the story generation, being able to create the story on a seperate section and make the "Surprise Me" feauture. 
Lucia: Design / Feautures. She was in charge of making the layout of the project, creating the dropdown menu, choosing the desing and emojis that best fit with the layout, and make sure that the project looks clean. The way in which we collaborated on the work was based on weekly meetings to share our progress or any type of problems that we would encounter. Also. we made sure to share the Github folder where the push / pull request would allow to see the progress of our work, and we would communicate through constant text and calls in case one of us had a question or had an issue.   We are using an approach that is based on the alternative roles. Basically, we would take turns on working on different parts of the project. For example, one team member would start a code and the other would continue working on it and improving it. By doing this, we were able to be involved on all parts of the project and create a balance.  This worked for us because we were able to work on the parts that we are good at and we collaborated equally


6. Risks and Limitations: One of the biggest risk of the project was the technical issue with the OpenAI API error. Our key would not load fully and would limit the request. This led to our story generater to not be able to run smoothly, which made it very hard. Also, another risk that we had to overcome was trying to add too many feautures (color, emojis, images), whoch caused the story generator to change completely and we had to restart the code. 



7. Course topics: Some topics I think would be helpful are APO examples. I believe that ever since our project depends on OpenAi API a lot, by studying more and getting more guidance, we would have been able to solve a lot of issues in a quicker manner. Also, I believe that having more guidance and understanding of how Github works in collaboratio, it would be easier and more efficient. This would make all team member understand how to use the platform better and avoid making mistakes.


