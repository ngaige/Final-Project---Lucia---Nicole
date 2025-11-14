
Proposal Idea: 
Our project aims to create a Mad Libs style Python interactive application. To be able to make this happen we plan on using OpenAI's API to make different stories for each user so that the narrative is more dynamic and humorous. The users will be able to insert different inputs, such as names, nouns, verbs and adjectives to generate their own funny story. The goal of using OpenAI is that based on this inputs, the API can start customizing the story to have a funny context and twists following the same style of the Mad Libs game. 

Some of the topics we plan on exploring are Natural Language Generation, this will be through the use of OpenAI, the use of this API will help us in our project for prompt engineering and having a creative output without the need to repeat the same stories, but change it for each user. This leads to another topic wich is interactive story telling, where the narrative will be dictated by the user. Also, we plan to use Python programming fundamentals such as Flask, to be able to have an input, output, include randomization and APIs. Through the use of these topics we will be able to develop a Python Mad Libs style game which will enhance the use of AI for creative story telling and humor, we will also be able to prevent using some words that may not be friendly for story telling. Using these models we will then be able to establish a base story from templates we create and use the API to customize it to the inputs provided by each user for various elements required for the story. 

Finally, our Minimum Viable Product (MVP) would be to create at least five story templates to offer diversification in the output of the game. To make sure that it is a feasible option, we want to code the game in Python, to test it in the command line version, to test these templates and the logic of the story, and keep the MVP simple to make it easier to identify any errors that we need to debug. If this is successful we then will integrate it with the API, to improve the stories and the output it generates. If this is successful, then our next stretch goal, would be to create a web-based interface through Flask, to create an HTML template to make the game a web-page game that people can access. Ideally we would then promt design the code so that OpenAI can create the story that we want and create dynamic templates without needing to rely on the pre-defined ones. If this is succesful then we can create multiple tabs that change based on the gender of the story that the user wants to create. 


Learning Objectives: 
After discussing what we want to achieve from this project we determined we have three mutual goals we want to achieve through this project. The first is that we want to strengthen our API understanding and programming integration as we were having some trouble following the codes in class. We then want to learn how to leverage the OpenAI API to generate creative texts based on the prompt design we create and see if it would run in our project. Finally we also want to learn how to develop a collaborative HTTML web page through the use of Flask and get the program running and make it engaging for the user. 

In terms of individual goals we have each determined our goals below: 
- Nicole: I want to learn how to leverage the API to make sure that it creates user-friendly sotires and that it follows the aspect to be a funny story. I want to learn how programming integration works and learn how to draft it so that it helps us leverage the API as best as we can. I also want to determine if it is possible to create a 'Golden Story' through an if loop, where, if the user guesses a specific word correct it creates an individual story that lets yo

- Lucia: My learning objective for this project is that I want to learn how to create a beginner friendly story using Flask interface for users to play online. I want to better understand the coding of how the HTML web-page can present to the user different outputs based on the inputs that they placed in the game.

Implementation Plan:

In terms of libraries that we would need to use for the project we will be using OpenAI API, which will then make us use a dotenv file to control and manage the API that we will use. Then we will also need to use Flask, for web development and making the game public for the users. 

For our Execution Plan, we are planning on starting the project by doing some more research and testing the code (through trial and error) to make sure that the stories and their dynamic work. This will then lead us to develop the code, such as if loops and managing the format design for the API and test what the outputs will be based on the inputs of the user. In this part we will start integrating the API to make sure that it creates user friendly stories based on a specified template (such as make a story about a person telling a joke to its friends) and test different prompts to see if what output OpenAI creates. Trough that we will create a Flask code to get the webpage running and make the game accessible to the public. This will lead us to the Testing phase of our execution plan, where we test the stories through the webpage, and adjust the prompts or edit the codes if we find any errors. 


Project Schedule: 
- Week 1: Planning and Researching -> we will do more research of the Mad libs game, and explore potential ways to promt the design and test if OpenAI can create the stories we want to do. 
- Week 2: Build the Mads libs code with a base story to see if the code works and runs based on the inputs we place in the code. 
- Week 3: Integrate the OpenAI API to our code and test if it would change the story based on the inputs we place and if it will stick to a specific base story we create (such as the one of a friend telling a joke).
- Week 4: This week we would test the program through the webpage and see if it runs well, see if there is any mistake that we made or if we need to debug our code. 

Collaboration Plan: 
As we are a group of 2  we decided to work in a way we believe would be most beneficial. More specifically, we are splitting the tasks and will meet regularly to combine the work and make sure that the final project can be completed.

Nicole: Will focus on the technical side, such as building the main game logic in Python. Also, she will be setting up and calling the OpenAI API as well as handling the users' inputs and their outputs. 

Lucia: Will focus more on the creative side, such as designing the templates. She will write and refine the prompts and make sure that the story stays coherent and there is a strict structure. Also, Lucia will make sure that the story contains a nice structure and flow and creates a simple text.

Even though there is a division of the tasks, there will still be a 50/50 collaboration. Our plan is to meet at least twice a week and check the output together, revise the code, prompts, and the story elements in order to make sure it makes sense. OpenAI responses can change without being predictable, so it requires having a short cycle of testing and improvements. This  approach allows quick adjusting to take place, fix mistakes and keep the code and the story aligned. Through the use of GitHub, we will be able to control and avoid overwriting from both parts of our work.


Risks and Limitations: 
One of the biggest risks that we could encounter is the unpredictability of the OpenAI API. More specifically, our game will heavily rely on the model using a specific structure and tone that could lead to API not following the story format, having responses that can be too short or too long or having an inconsistent humor. Also, there could be some delays or rate limits that could affect the work. These issues could lead to affecting how fun the game will make users feel. The narrative is the central part of the project, which is why having unpredictable outputs may lead to a less enjoyable game experience. Another limitation that can be encountered is time. Basically, when creating the prompt of the project its engineering could take longer than expected, where small changes can affect the results. 

Additional Course Content: 
This project involves using external API. Some of the course topics that can be helpful are:

1. API Best Practices: This would help us understand how to handle API errors, manage rate limits, and how to write prompts that can lead to more predictable and accurate results.

2. Debugging and Testing: Due to all the steps that are required in our project (from user choice to output), we must learn more about the different debugging strategies in regard to Python, as well as how to be able to fix issues in a quick manner.

3. Basic UI / UX for Text Based Programs: This would be very beneficial because although our game is simple, it is important for us to understand how to be able to structure the user interactions and make the text layout clear and understandable for the final product.

4. Small Team Agile Workflow: Ever since we will be following a lightweight Agile structure, it would be very helpful to understand more about sprint planning, GitHub and the workflows and how small team collaboration makes an impact on it. This would lead to a more organized working environment throughout the project.