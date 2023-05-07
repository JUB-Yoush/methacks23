# Pomo-duino: 
---
A real-life Pomodo timer that tracks your study habits.

## Inspiration:

During MetHacks 2023, one of the group members brought an Arduino and we were wondering how we can dual software/hardware idea. We were leading to timers, for a simple hardware portion. We know that Pomodoro Techniques are out there already, but we decided to mix it up a bit by having a physical timer using an Arduino. This is because if we have it set up on our phones, it can be an easy distraction especially if we want proper studying hours! This is why we used an Arduino so we can eliminate distractions.

## What it does:
We have an Arduino Board, which is responsible for the timer. We made a Flask app that asks you which cycle you want to do (Long or Short Pomodoro) and select the type of work that this session is doing. When you click start, the Arduino timer starts. Once cycles are done, it is sent to a database that records your study sessions. It stores How many Pomodoro cycles you went through, your start time, your end time, and the type of work being done during those cycles. Once the cycles are done, the Arduino won’t display any timer anymore, indicating you have finished your session. 

## How we built it
We used an Arduino MEGA board for our main piece of hardware and 4 digit 7 Segment LEDs for displaying our Pomodoro timer and coded our project using C. We used resistors, a breadboard and jumper wires to create our circuit for our timer and connected it with our MEGA board.

For the software part, we used Python and Javascript for our frontend and backend. We used C to program the LED display. We used Python to communicate directly with the board. We used Flask to create a server and host our website and Sqlite for our database and mirror the timer for getting the info of each Pomodoro session and logging it to our front end.

## Challenges we ran into
From our hardware component, the first challenge we ran into was hardware connectivity issues as we discovered Arduino has different ports for different model computers ( MacOS, Windows and Linux) so we figured out how to connect the right port to the right computer model. We also ran into issues calibrating our initial 16x2 LCD display so we ended up swapping it for a 7-segmented 4-digit LED display instead. 

For our software component, we ran into issues fetching data from our server and showing it to our frontend app using Axios. 

## Accomplishments that we're proud of
This was the first time Jayden and Ian had ever done a hardware hackathon so me and Giuliano guided them on the basics of Arduino and how it works. We're proud that Pomo-duino is our first Hardware Hackathon project together as a team. We also learnt how to use SQLite and incorporate a database with Arduino all within 36 hours of hacking which is something we learnt a lot faster than we could've learnt in school.

## What we learned
We learned a lot of valuable skills making Pomoduino. One of the key things we learned was about back-end technologies and how to communicate using custom APIs. We discovered how to use Python to connect SQLite and Flask to create a website with a database, and we also learned how to call back-end Python functions from front-end JavaScript. This was especially useful in allowing us to create events in the database based on UI interaction.

Another skill we picked up was how to work with serial ports and connect Python to Arduino code. This was important in allowing us to integrate the physical clock into our project, and it gave us a deeper understanding of how hardware and software can interact. Finally, we learned about the different kinds of databases and their structure. This was important in helping us make informed decisions about which type of database to use for our project, and what to consider for future work 

## What's next for Pomoduino
Moving forward, there are a few key areas we would like to focus on to improve Pomoduino. One of the first things we want to do is revisit the Arduino clock we created for the project. While it worked well, we think we could improve on it by making it smaller and potentially soldered onto a single board. This would make it more efficient and easier to use.

In addition to improving the hardware, we would like to incorporate some AI into our project to help analyze the data. We think this would be a valuable addition as it would allow users to gain more insights from the data they are collecting. This could also potentially design study schedules or lesson plans based on the number of Pomodoros the user would like to do




