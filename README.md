# Date Night 


Here is a link to the live project. (https://natalie-kate.github.io/date-night/)

This website was created for Milestone 2- Interactive Frontend Development project, as part of the Code Institutes diploma in Software development.<br>
I was inspired by my partners group of friends who were complaining about how indecisive their partners were when it came to making decisions about what to do, where to go etc and so Date Night was born.<br>
Now when they are asked "What do you want to do tonight?" the answer isn't "I don't know! What do you want to do?" its " Give me a minute and I'll tell you!."<br>
The premise is that you subconsciously know what you want to do, so asking a series of questions with only two options each, and a limited time to answer (so you can't overthink it) the options will be narrowed down and leave you with what you actually want.

![Image showing the website displayed on different screen sizes](assets/readme-assets/readme-images/responsive.png)

## Contents 

- [User Experience (UX)](#user-experience-ux)
   * [Strategy](#strategy)
   * [User Stories](#user-stories) 
   * [Scope](#scope)
      + [Current Features](#current-features)
      + [Features to implement in the future](#features-to-implement-in-the-future)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
     + [Colour Scheme](#colour-scheme)
     + [Typography](#typography)
     + [Imagery](#imagery)
- [Technologies](#technologies)
   * [Languages used](#languages-used)
   * [Frameworks, Libraries & Programs Used](#frameworks-libraries-&-programs-used)

- [Challenges](#challenges)

- [Testing](#testing)
   
- [Deployment](#deployment)

- [Credits](#credits)
   * [Code](#code)
   * [Content](#content)
   * [Media](#media)
   * [Acknowledgements](#acknowledgements)


## User Experience (UX)

   ### Strategy 
   - User goals 
     * As a user I want help deciding what to do for date night.
     * As a user I want to have fun  

   - Site owner/ business goals
     * As the site owner I want my site to be responsive to different screen sizes.
     * As the site owner I want my site to be accessible to my visitors.
     * As the site owner I want to build up a media presence so that future applications will
       have footfall immediately and with that, hopefully gain popularity and therefore could monetise future projects.

   ### User Stories

   - #### First Time Visitor 

        1. As a first time visitor, I want to easily understand the main purpose of the site. 
        2. As a first time visitor, I want to be able to intuitively use the site.
        3. As a first time visitor, I expect to see an attractive, visually appealing site.
        4. As a first time visitor, I expect an accessible site.
        5. As a first time visitor, I expect the site to look good on my mobile device.
        6. As a first time visitor, I want a quick and fun way to choose what to do for date night.

   - #### Returning Visitor Goals

        1. As a returning visitor, if my result is to go out to do something e.g cinema, I want to see where the cinemas are on Google Maps.
        2. As a returning visitor, if I have a going out result I want to be able to choose what area to search for my resulting place.
        3. As a returning visitor, I want to be able to contact the owner with comments or questions.
        4. As a returning visitor, I want to see social media links so that I can follow on my chosen platforms.

   - #### Frequent Visitor Goals

        1. As a frequent visitor I don't want to be choosing between the same two options each time e.g restaurant vs club. 
        2. As a frequent visitor, I want to be able to contact the owner with suggestions of more options.
        3. As a frequent visitor I want to use links to food delivery services if the result is takeaway.
        4. As a frequent visitor I want to see information about the markers on the map.

   ### Scope

   Within project conception, a list of features were compiled, these were the scored 
   between 1 & 5 for importance and feasibility/ viability which then decided which features 
   could be included for initial launch.    

   #### Current features 

-   Responsive on all device sizes

-   Accessible 

-   Easy to navigate (Single use learning)

-   Interactive elements 

-   Social Links (build up media presence)

-   Ability to contact owner 

-   Timer to ensure user answers the question instinctively and not over thinking it.

-  Timer changes colour as time goes down and flashes at 0 to warn user they are nearly out of time.

- When timer stops flashing 0, time is up, the user gets the option to start again.

- Option number counter so that the user can keep track of where they are.

-   If user gets result of getting food delivered there are links to Uber Eats, Deliveroo and Just Eat. Likewise with the other staying in results, there are useful links too.

-   If users initial option is Go out. Then their result will have a Google Map showing them where the cinema,
    or restaurants or clubs etc are. This can either be via the use my location button or by area of their choice via the input box.

-  On the map, the markers will show name and address of place when clicked and when another is clicked will close the current info and open the new one.

-   On successful submission of contact form there is a personalised confirmation modal and submit button changes to sent.

   #### Features to implement in the future

-   To add in another option on landing page to get help choosing what to eat. In addition when a users result is to order takeaway or go to restaurant then there would also be a link to the What to Eat decision making game. Out with scope of initial launch due to time constraints.
-   If user gets Stay in and try new recipe then have another decision game and depending on that result a recipe API will come back with options to try. Not implementing for initial launch due to time constraints.
-   To add in or remove options in the game depending on what's available in the users area. Would require to have result picture and result paragraph for most things which would be too time consuming for initial launch. Also think it is out of the developers skill level at the moment.

   ### Structure
-  We start with a landing page with a start button, this then takes the user to the beginning of the options and the timer will start. The user goes through the options until only one is left. The result page is opened, displaying the result, with accompanying picture and short paragraph, some will also have accompanying links or map.<br>
-  The About section is a modal outlining the premise of the game.
-  The contact form I chose to put on its own page instead of a modal as I wanted a decently sized text area for people to write in and to have a confirmation modal to pop up on successful submission.<br>
-  All pages will have nav links to Home, About and Contact at the top and social links at the bottom as this is what users expect to see.<br>

  ### Skeleton 

Wireframes were created on Balsamiq (see links below)

* [Mobile](assets/readme-assets/wireframes/ms2-mobile.pdf)
* [Tablet](assets/readme-assets/wireframes/ms2-tablet.pdf)
* [Desktop](assets/readme-assets/wireframes/ms2-desktop.pdf)

Changes from the wireframes to final site are minimal. 
- The planned desktop had a different layout in theory but in reality it didn't look right. For the staying in result which had a couple of links, they didn't take up enough room and just looked a bit strange. Again having the timer beside the options rather than above them didn't look great in practice either.
- Added in a decision counter below the option buttons so the user has feedback of where they are in the game.

 ### Surface

 -   #### Colour Scheme
        
        Found a picture for the background image and used that to pick colours from. 
        As its about finding your date night, I wanted the feel to be soft and romantic so I swapped out the default black for the dark warm brown.
        The darker pink brings the romantic element.
        The other two colours were picked to complement the main two colours, these were used where I needed contrast or to highlight.

        ![Colour scheme](assets/readme-assets/readme-images/colours.png)

-   #### Typography
         
      Used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site.
      I picked Lobster for the headings as its a bit more ornate than the usual fonts, bringing a special feel, its not just any night its "Date Night". 
      For the other text I used montserrat as it was among the popular pairings on the Google Fonts website. Montserrat looked the nicest with Lobster.
      
-   #### Imagery
      
       Picked the background image for its modern and simple design as I didn't want it to be distracting. The overlay muted the colours, so that the writing could still be clearly seen. 
       Used vectors for the result images. They have a fun aspect to them and they are all of similar design so they tie in together which would be harder to get with photos. These vectors required attribution so this is found directly below the vectors with the attribute required by [Freepik](https://www.freepik.com/).
       Also tried to pick vectors that weren't just of same sex couples where I could.

## Technologies 

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [Bootstrap v4.6.0](https://getbootstrap.com/docs/4.6.0/getting-started/introduction/)
    - Bootstrap was used for the initial layout and styling before customising it.
2. [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the Noto Sans KR and Montserrat. 
3. [Font Awesome](https://fontawesome.com/)
    - Social media icons in footer and section icons on evidence page.
4. [Git](https://git-scm.com/)
    - Version control.
5. [GitHub](https://github.com/)
    - For storing code and deploying the site.
6. [Gitpod](https://www.gitpod.io/)
    - Used for editing my code.
7. [Balsamiq](https://balsamiq.com/)
    - Wireframe creation
8. [TinyJPG](https://tinyjpg.com/)
    - TinyJPG was used to optimise the images I used on my site to minimise loading time.
9. [Am I responsive](http://ami.responsivedesign.is/)
    - This was used to generate the image at the top of this README.
10. [Chrome devtools](https://developer.chrome.com/docs/devtools/)
    - This was used massively throughout development to troubleshoot, try out changes before 
   changing code, to test responsiveness and for testing performance of the final site with lighthouse. 
11. [jQuery](https://jquery.com/)
    - JavaScript Library making writing JavaScript quicker and easier.
12. [Code pen](https://codepen.io/)
    - Used to try out snippets of code prior to implementing.
13. [Python tutor](http://pythontutor.com/visualize.html#mode=edit)
    - Used to troubleshoot JavaScript.
14. [Google maps API](https://developers.google.com/maps)
    - For the map seen in the results for the going out game.
15. [Emailjs](https://www.emailjs.com/)
    - Used to link the contact form to my emails

## Challenges 
   These are aspects of the development that took me a while to figure out due to inexperience.
   -  Had an issue with the submission modal popping up when the form wasn't completed properly and therefore not ready to submit. I had then taken what I thought I needed from code I'd used in MS1 for this issue and it wasn't working. Tried the full code i'd used in my MS1 just changing id's to the variables I'd assigned which also didn't work.<br> 
       + <span style="color: grey;">Solution: Removed the data-toggle and data-target attributes from the submit button, so that the modal wouldn't be triggered. The modal is now only triggered to show by the $('#submit-modal').modal('show'); within the event handler function. Also as you can see I reverted to the id as the variable wasn't working, haven't figured out why yet. My guess is that the modal I assigned to const at the beginning then was altered by changing the inner text in the event handler function and so the const I'd assigned didn't exist anymore.</span>
 -  Creating the timer function I attempted to create a for loop that I could see was working/counting down in [Python Tutor](http://pythontutor.com/visualize.html#mode=edit). I then used setTimeout to introduce a 1000ms pause after changing the innertext to the value of my timeLeft variable. This just waited a second before changing time left from 5 in my div to 0. I then changed to setInterval which I came across while researching for answers on slack and removed the for loop and instead added in timeleft -= 1. My timer now continued to count down below zero so I introduced an if statement. This initially didn't work as I had put it out with the setInterval function so my countdown then wasn't working at all. With some rejigging around and making it an if/else statement I got it working.<br> 
      + <span style="color: grey;">Solution: With the help of w3 and slack got it to work using setInterval, with if/else, -=1 (which seemed so obvious when I seen it) and using return to stop the function if my variables value was < 0.</span>
   -  When I implemented my event listeners on my option buttons, the timer would just show two seperate timers happening at the same time. Tried to stop the original one by passing timeleft= -1 into the timer function so that the if statement would come into play and stop it. This did not work. With research I realised I needed to create a stop function with clearInterval. This stopped the timer but when timer was restarted it started where it had been stopped.
       + <span style="color: grey;">Solution: Stop function with clear interval and when calling the timer function pass in timeLeft = 7 and reset the inner html to 8  </span>
   - Timer again, this time my colour change feature was being continued when the timer was restarted even though the colour change was tied to the value of time-left. It was like the previous timer had been restarted in the background and was overriding the current one, so was researching down the stop timer route again thinking I had done something wrong there. Tried numerous examples I'd found online, most had double the code that I had but that still didn't fix the issue. Also tried deleting the timer altogether and create a new one thinking that doing that would reset everything, that didn't work either Then looked at the colour change and tried many iterations of it. 
       + <span style="color: grey;">Solution: Turns out I was barking up the wrong tree I had transitions on my colour changes, once I removed them it worked fine. </span>
   - Wanted the footer to be at the bottom of the content and at the bottom of the screen even when the content isn't long to push it there. Tried sticky and fixes but when mobile was turned for horizontal viewing the footer would be messing up the layout or be in the middle of the screen. I tried giving footer a height which caused issues on the home page.
       + <span style="color: grey;">Solution: Put footer within its own container and the content in another, made content 90vh and footer 10vh, this still wasn't quite right so changed this to min height. </span>
   - Functions in general were a steep learning curve. I originally focused on the "staying in" side of the game and wrote everything apart from the timer in one big function and then for the going out I just copied it and changed the names for everything. I knew this wasn't right so I split my large function into smaller ones and called the next function in the previous one, this got rid of a lot of repetition too. I then was struggling with how to get variables available outside of its own function without making them all global. Realised I was missing the basic understanding required so went back revised, did some [w3 tutorials](https://www.w3schools.com/js/default.asp) and watched Steve Griffith YouTube videos on functions.
       + <span style="color: grey;">Solution: Smaller individual functions calling the next one and passing in the variables required. I also removed even more repetition when tidying up my final code, replacing it with two more functions. </span>
   - Was having an issue with my arrays, options that hadn't been getting chosen were coming up again, console.log of the array was giving me 2,3, 4 arrays, so figured this was due to the event listener for my buttons passing in the full array again. 
       + <span style="color: grey;">Solution: Once the game was started the buttons with id 1 & 2 were hidden and buttons 3 and 4 were shown this stops the event listener on buttons 1 & 2 starting another game when one is still in progress. </span>
   - Was getting buttons not changing text even when it hadn't been chosen so shouldn't have still been available in the array to be displayed and sometimes no option on the button at all. Console.log showed that the array length was sometimes only going down by one, which as the buttons are both assigned values before the console.log the array should always be reduced by two. When a choice is made, that option is pushed to the chosen options array and the other goes to the unchosen array so the unchosen is essentially discarded. I also used the length of the arrays to determine when the game was at a certain stage i.e down to last two options and I was finding that I was making way more choices than I should have been. Using console.log found that where the lengths of the 3 arrays should always equal 8 there were more due to blanks and duplicates of options. When selecting random options from array to be displayed a random number is generated using array length. I then splice it out the array before the second number is generated so that both buttons can't display the same option. Where the issue was arising was when I spliced the first option out, the array length is no longer the same so if the second random number was the last position in the array that position no longer exists when the first number is spliced out and so button 2 stayed the same introducing duplicates. If this occurred for the first two options displayed, this is where blanks where introduced.
      + <span style="color: grey;">Solution: Second option random number generated from the array length variable minus 1. </span>
   - Google Maps API, when trying to get the latitude and longitude of the input box area so that i could use it in the request for places. Tried let searchLat = places[0].geometry.location.lat; which didn't work took stack overflow to remind me to use ().
      + <span style="color: grey;">Solution: lat() and lng() </span>
   - Wireframes links were coming up as blank in Github. Checked the file path, which was fine, deleted them all and re-exported incase I had done something wrong the first time around. Upon uploading an error was coming up saying: "Detected unusual line terminators. This file contains one or more unusual line terminator characters, like Line Separator (LS) or Paragraph Separator (PS).It is recommended to remove them from the file. This can be configured via `editor.unusualLineTerminators`." This gave the option to fix which I did but didn't appear to do anything as was still not working in Github. Sean Young on slack pointed out that he could get the mobile one to work, it occurred to me that I may not have clicked the fix button on all of them.
      + <span style="color: grey;">Solution: Re-uploaded the files again, this time not "fixing" them did the trick.</span>

## Testing

Testing and results can be found [here](TESTING.md)

## Deployment

 - ### Creation 

    I created this repository by:<br>
    (a) Logging into Github and clicked the green new button.<br>
    (b) This took me to the page below. I selected the code institute template, input a repository name and clicked the 
    green create repository button.<br>

    ![image showing green new button](assets/readme-assets/readme-images/new.png)
    ![Image showing the create repository page](assets/readme-assets/readme-images/new-repo.png)

    (c) Opened new repository and clicked green Gitpod button to create a workspace in Gitpod for editing.

 - ### Github pages
    I deployed my project to Github pages by:

    (a) Logged in to Github and opened my [repository](https://github.com/natalie-kate/date-night)<br>
    (b) From here clicked settings, see picture below and selected pages.

    ![Image showing where pages is in settings](assets/readme-assets/readme-images/pages.png)

    (c) In pages under source branch I selected Master 
           and kept the default root and then clicked save.

    ![Image showing the Github pages options](assets/readme-assets/readme-images/source.png) <br>

    (d) After a minute or two the page has now published and the site address is available in the Github page section.

    ![Image showing that the site has been successfully published](assets/readme-assets/readme-images/published.png)

 - ### Forking
   (a) To fork my project sign in to Github and go to my [repository](https://github.com/natalie-kate/date-night)<br>
   (b) Above and to the right of the settings there are three options and the far right one says Fork, select this.<br>
   (c) The fork is now in your repositories.


 - ### Clone
   To clone my project sign in to Github and go to my [repository](https://github.com/natalie-kate/date-night)<br>
   * Clone using command line
     + Next to the green Gitpod button is a button that says code, select this. There is a few options as to how you 
       would like to clone, if you choose https, SSH or Github CLI, select the clipboard icon to copy the URL.
     + In your workspace that you've created, in the terminal , type git clone, paste the URL and enter.

     ![Image showing the cloning options](assets/readme-assets/readme-images/clone.png)
   * Desktop Github
     + If you choose to clone by selecting open with desktop Github, it will guide you through the clone with prompts.<br>

For more information or troubleshooting see the Github documentation 
[here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)
   
## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library used for the layout and styling and modals.
-   [Google Maps API](https://developers.google.com/maps): For their code examples in the documentation for implementing different features.
-   [CSS-tricks](https://css-tricks.com/simple-styles-for-horizontal-rules/): Gradient effect idea on my horizontal rule and background on index.html footer.
-   [CSS-tricks](https://css-tricks.com/almanac/properties/t/transition/): Transition on social links, in particular the ease-out.
-   [Anthony on Stack Overflow](https://stackoverflow.com/questions/1232040/how-do-i-empty-an-array-in-javascript): Emptying my array after I had pushed the contents to my other array.
-   [ComFreek on Stack Overflow](https://stackoverflow.com/questions/18558417/get-first-word-of-string/18558427): Get the first word from a string for getting my class name from the option. i.e if winning option was TV binge then I wanted to show those elements with a class of tv.
-   [Josh Johnson on Stack Overflow](https://stackoverflow.com/questions/3248384/document-createelementscript-synchronously): To create the script containing the Google Maps only in the event of a going out result, as it will only be used half the time so didn't want to load it every time.
-   [Avinav on Stack Overflow](https://stackoverflow.com/questions/3926836/using-google-maps-api-v3-how-do-i-get-latlng-with-a-given-address): For reminding me to put () after lat and lng for it to work.
-   [Stephen Booher on Stack Overflow](https://stackoverflow.com/questions/8852765/jshint-and-jquery-is-not-defined): Code to put at top of JSHint so that it doesn't flag google and $ as undefined.
-   [Sherif on Stack Overflow](https://stackoverflow.com/questions/49425137/how-to-stop-timer-in-javascript/49425211): Assign a variable the setInterval function so you can use it to stop the function.
-   [W3 Schools](https://www.w3schools.com/js/js_timing.asp): setInterval method.
-   [Jamie on Slack](https://code-institute-room.slack.com/archives/C7HD37Q1F/p1620300631425700): Using -= 1 to get the timer to count down, had been trying to do it in an overly complicated way.
-   [Professor Steve Griffith](https://www.youtube.com/playlist?list=PLyuRouwmQCjkYdv4VjuIbvcMZVWSdOm58): Videos on functions that really helped me understand the concept of passing variable between functions.
-   [Kevin Powell](https://www.youtube.com/watch?v=CBw9-K6hYVA): Keyframes pulse idea for my timer when at 0.
-   Jo in Student Support: Made me realise that having an array for the not chosen options could be useful.


### Content

-   Content was created by Natalie Alexander.
    
-   README and TESTING layout and content from my MS1 which took inspirations and ideas from these excellent examples
    * [Code institute](https://github.com/Code-Institute-Solutions/SampleREADME)
    * [Daisy McGirr](https://github.com/Daisy-McG/MilestoneProject-1/blob/master/README.md)
    * [Richard Henyash](https://github.com/richardhenyash/artofnht/blob/darktheme/README.md)
    * [byllsa](https://github.com/byIlsa/Aloy-from-outcast-to-heroine)

### Media

 - [Olya Kobruseva](https://www.pexels.com/@olyakobruseva?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from Pexels for landing page background pictures.
 - [Freepik vectors](https://www.freepik.com/free-vector/young-couple-having-dinner-restaurant_1239556.htm#page=1&query=romantic%20dinner&position=36): Image for restaurant result.
 - [Freepik vectors](https://www.freepik.com/free-vector/couple-eating-popcorn-watching-tv_8356071.htm#page=1&query=couple%20watching%20tv&position=27): Image for tv result.
 - [Freepik vectors](https://www.freepik.com/free-vector/couple-eating-popcorn-watching-movie_8620588.htm#page=1&query=couple%20watching%20tv&position=9): Image for movie result.
 - [Freepik vectors](https://www.freepik.com/free-vector/modern-people-doing-cultural-activities_9156582.htm#page=1&query=pool%20hall&position=28): Image for pool hall result.
 - [Freepik vectors](https://www.freepik.com/free-vector/couple-cooking-together-house_7870433.htm#page=1&query=couple%20cooking&position=0): Image for cook together result.
 - [Freepik vectors](https://www.freepik.com/free-vector/board-game-collection_10258859.htm#page=1&query=board%20games&position=4): Image for games night result.
 - [pch vectors on freepik](https://www.freepik.com/free-vector/dating-couple-enjoying-romantic-dinner_7732606.htm#page=1&query=restaurant&position=25): Image for bar result.
 - [pch vectors on freepik](https://www.freepik.com/free-vector/smiling-tiny-woman-drinking-alcohol-happy-hours-flat-illustration_11235862.htm#page=1&query=cocktail%20menu&position=29): Image for cocktails result.
 - [pch vectors on freepik](https://www.freepik.com/free-vector/happy-young-people-dancing-club-isolated-flat-vector-illustration-cartoon-characters-enjoying-dance-disco-night-party-dj-scene-performance-entertainment-concept_11671774.htm#page=1&query=clubbing&position=25): Image for clubbing result
 - [pch vectors on freepik](https://www.freepik.com/free-vector/happy-young-couple-home_12291118.htm#page=1&query=couple%20massage&position=0): Image for pamper night.
 - [VectorPouch on Freepik](https://www.freepik.com/free-vector/bowling-alleys-with-balls-pins-scoreboards_6198139.htm#page=1&query=bowling&position=7): Image for bowling result.
 - [VectorPouch on Freepik](https://www.freepik.com/free-vector/quest-escape-asylum-room-with-people-searching-exit_5901244.htm#page=1&query=escape%20room&position=13): Image for escape room result.
 - [VectorPouch on Freepik](https://www.freepik.com/free-vector/vector-game-room-with-people-playing-digital-entertainment-modern-esports-concept_4015271.htm#page=1&query=video%20games&position=7): Image for video games result.
 - [Macrovector on Freepik](https://www.freepik.com/free-vector/jazz-horizontal-composition-with-flat-cartoon-style-characters-musicians-with-shadows-silhouettes-stage_6800093.htm#page=1&query=jazz%20band&position=19): Image for live music result.
 - [Macrovector on Freepik](https://www.freepik.com/free-vector/cinema-design-concept-with-set-square-compositions-with-female-characters-reels-camera-with-smartphone-illustration_13916940.htm#page=1&query=movies&position=42): Image for cinema result.
 - [Stories on Freepik](https://www.freepik.com/free-vector/way-concept-illustration_6982750.htm#page=1&query=takeaway&position=16): Image for takeaway result.

### Acknowledgements

-   Code institute.
-   Student Support
-   My mentor Spencer Barriball
-   My mini feb 2021 team on slack for their feedback and support.
-   The slack community.
