# Testing

## Contents 
   - [Automated Testing](#automated-testing)
      * [HTML validation](#w3c-markup-validator)
      * [CSS validation](#w3c-css-validator)
      * [JS validation](#jshint-javascript-validator)
      * [Lighthouse testing](#lighthouse-in-devtools)
   - [Testing User Stories](#testing-user-stories)
   - [Manual testing](#manual-testing)
   - [Bugs](#bugs)
      * [Found and Fixed](#found-and-fixed)
      * [Existing](#existing)


## Automated Testing

The W3C Markup Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no 
syntax errors in the project.

-   ## [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

    ### Initial testing
    - index.html

    ![Initial index html test](assets/readme-assets/validations/index-html-validation.png)

    - decision.html

    ![Initial decision html test](assets/readme-assets/validations/decision-html-validation.png)

    - contact.html

     ![Initial contact html test](assets/readme-assets/validations/contact-html-validation.png)

     Removed type attributes from scripts on all my pages which prevented me getting html errors on them as well as this was the first page I validated. 
     Removed type attribute from text-box and the extra anchor closing tag that was present.

     ![Initial contact html test, second picture](assets/readme-assets/validations/contact-html-validation.png)

     The role and aria-checked I had put on all my labels for the star ratings as I have hidden the actual checkboxes and styled the labels to be the stars so I tried to use accessible attributes on the labels which caused the error. Removed them.
  
    - 404.html

     ![Initial contact html test](assets/readme-assets/validations/404-html-validation.png)
    
    ### Final testing (for those that needed fixed)

    Fortuitously I only had the contact.html to fix so below is the final validation for it.
    
    ![Initial contact html test](assets/readme-assets/validations/contact-html-validation-final.png)


-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    
    ### Initial/final testing

    ![Initial contact html test](assets/readme-assets/validations/css-validation.png)
   
    The only errors were for bootstrap. There was a warning for my CSS which was that my button background color and border were the same colour. But as I wanted that border on the hover effect I kept it as is. When I tried to fix the warning by removing the border from the button and add it into the hover effect the button size naturally changed size which I didn't like the look of.
   

-   ## [JSHint JavaScript Validator](https://jshint.com/) 
    
    ### Initial testing
  
    - contact.js

    ![Initial contact javascript test](assets/readme-assets/validations/contactjs-validation-initial.png)

    Added in the missing semi-colon. The undefined variables I left, as one was $ for jquery and the other is emailjs so neither need defined.

    - decision.js

     ![Initial decision javascript test](assets/readme-assets/validations/decisionjs-validation.png)
     ![Initial decision javascript test](assets/readme-assets/validations/decisionjs-validation2.png)
     ![Initial decision javascript test](assets/readme-assets/validations/decisionjs-validation3.png)

     Fixed all the semi-colons. I had two read only warnings. This was due to me using length as a variable name so I renamed it which did the trick. Again $ for jquery was being flagged as well as google (for google maps) for being undefined so I added in /*globals $:false */ and /*globals google:false */ to stop them being flagged.
     The other undefined variables I went through and declared them all.
     It was flagging initMap as unused, this is due to it not being called in my JS file. It is called however by the Google Maps API when a going out result creates the script for it. So it has been left as is.

    ### Final testing

    - contact.js

     ![Final contact javascript test](assets/readme-assets/validations/contactjs-validation-final.png)

    - decision.js

     ![Final decision javascript test](assets/readme-assets/validations/decisionjs-validation-final.png)


-   ## [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) in devtools
    
    ### Initial scores 

    #### Landing page

    + Initial mobile

    ![Initial landing page scores for mobile](assets/readme-assets/lighthouse-testing/initial-mobile-index.png)

    #### Game page

    + Initial mobile

    ![Initial game page scores for mobile](assets/readme-assets/lighthouse-testing/initial-mobile-decision.png)

    #### Contact Page

    - Initial mobile
      + No issues to work on.

    #### 404 page

    - Initial mobile
      + Scores were all fine, best practices wasn't 100% though so added in meta description.

    ### Actions taken from initial test.

    - One of the image file paths was wrong affecting best practice scores. Amended.
    - The contrast between the brown writing and pink background of the buttons wasn't passing and so increased font-weight of all the buttons.
    - The result images were causing performance score to be low. As only one image is required for the result, added lazy loading to them.
    - Script loading was also impacting the lighthouse scores so added defer to them.
    - Changed cloudfare CDN's for font-awesome and bootstrap to the regular CDN's.

    ### Final test 

    #### Landing page

    + Final mobile (see report [here](assets/readme-assets/lighthouse-testing/mobile-landing-report.pdf))

    ![Final landing page scores for mobile](assets/readme-assets/lighthouse-testing/mobile-index.png)

    + Final Desktop (see report [here](assets/readme-assets/lighthouse-testing/desktop-index-report.pdf))

    ![Final landing page scores for desktop](assets/readme-assets/lighthouse-testing/desktop-index.png)

    #### Game page

    + Final mobile (see report [here](assets/readme-assets/lighthouse-testing/mobile-decision-report.pdf))

    ![Final evidence page scores for mobile](assets/readme-assets/lighthouse-testing/mobile-decision.png)

    + Final desktop (see report [here](assets/readme-assets/lighthouse-testing/desktop-decision-report.pdf))

    ![Final evidence page scores for desktop](assets/readme-assets/lighthouse-testing/desktop-decision.png)

    #### Contact Page

    + Final Mobile (see report [here](assets/readme-assets/lighthouse-testing/mobile-contact-report.pdf))

    ![Contact page scores for mobile](assets/readme-assets/lighthouse-testing/mobile-contact.png)

    + Final Desktop (see report [here](assets/readme-assets/lighthouse-testing/desktop-contact-report.pdf))

    ![Contact page scores for desktop](assets/readme-assets/lighthouse-testing/desktop-contact.png)

    #### 404 Page

    + Final Mobile (see report [here](assets/readme-assets/lighthouse-testing/mobile-404-report.pdf))

    ![Contact page scores for mobile](assets/readme-assets/lighthouse-testing/mobile-404.png)

    + Final Desktop (see report [here](assets/readme-assets/lighthouse-testing/desktop-404-report.pdf))

    ![Contact page scores for desktop](assets/readme-assets/lighthouse-testing/desktop-404.png)

## Testing User Stories 

- ### First Time Visitor 
   1. As a first time visitor, I want to easily understand the main purpose of the site. 
      - The overlay box on the landing page has the main title "Date Night" with an accompanying sentence of "Let us help you decide what to do". In addition there is a link to about in the nav to explain it more thoroughly.
   
      ![Picture showing title and accompanying sentence](assets/readme-assets/testing-images/title.png)
      ![Picture showing About modal](assets/readme-assets/testing-images/about-modal.png)

   2. As a first time visitor, I want to be able to intuitively use the site.
      - The layout is what users expect to see, nav menu at the top of all pages and social links at the bottom. In the event of an error the 404.html page has links back to home page and another to report error which takes them to the contact page. If the timer runs out there is a start again button that reloads the decision.html so the user doesn't have to go back to the home page to then restart the game.

      ![Picture showing nav menu](assets/readme-assets/testing-images/nav.png)
      ![Picture showing social links](assets/readme-assets/testing-images/social.png)
      ![Picture showing error message links](assets/readme-assets/testing-images/404.png)
      ![Picture showing start again button](assets/readme-assets/testing-images/time-out.png)

   3. As a first time visitor, I expect to see an attractive, visually appealing site.
      - Used landing page image to pick colours from to ensure a pleasing colour palette. Hover effects draw attention to links and call to action buttons. Hover effects being size increase for social links, colour change on the result links, nav links, image attribute links and main buttons. The same colours were consistently used across the site for predictability and doesn't look too busy which can be off putting. 

      ![Picture showing button hover effect](assets/readme-assets/testing-images/button.png)
      ![Picture showing link hover effect](assets/readme-assets/testing-images/link.png)
    
   4. As a first time visitor, I expect an accessible site.
      - Aria labels, screen reader only text and alternative text have been used throughout the site. Styled the outline of keyboard focus making it more obvious as to where they are on the page and colour ties in with the design of the page. All colour contrast scores were a pass in chrome dev tools and accessibility score was 100%. Added in a media query for reduce motion to remove the pulse effect of the timer at 0 and the transition effects on the social links and buttons. Kept colour change on button and introduced one for the social links so that interactivity is still noticeable.

       ![Picture showing keyboard focus](assets/readme-assets/testing-images/focus.png)

   5. As a first time visitor, I expect the site to look good on my mobile device.
      - Designed mobile first. As hover effects not in use, main landing page button has a shadow effect border giving it a more obvious button look and on screens smaller than 1000px the useful links in the result page have the underline text decoration that users are used to being indicative of a link.  Have ensured the site is responsive on all screen sizes by using bootstrap and media queries.

      ![Picture showing landing page on mobile](assets/readme-assets/testing-images/mobile-landing.png)
      ![Picture showing game page on mobile](assets/readme-assets/testing-images/mobile-game.png)
      ![Picture showing stay in result on mobile](assets/readme-assets/testing-images/mobile-in-result.png)
      ![Picture showing go out result on mobile](assets/readme-assets/testing-images/mobile-out-result.png)
      ![Picture showing contact page on mobile](assets/readme-assets/testing-images/mobile-contact.png)
      ![Picture showing landing page on tablet](assets/readme-assets/testing-images/tablet-landing.png)
      ![Picture showing game page on tablet](assets/readme-assets/testing-images/tablet-game.png)
      ![Picture showing stay in result on tablet](assets/readme-assets/testing-images/tablet-in-result.png)
      ![Picture showing go out result on tablet](assets/readme-assets/testing-images/tablet-out-result.png)
      ![Picture showing contact page on tablet](assets/readme-assets/testing-images/tablet-contact.png)
      ![Picture showing landing page on desktop](assets/readme-assets/testing-images/desktop-landing.png)
      ![Picture showing game page on desktop](assets/readme-assets/testing-images/desktop-game.png)
      ![Picture showing stay in result on desktop](assets/readme-assets/testing-images/desktop-in-result.png)
      ![Picture showing go out result on desktop](assets/readme-assets/testing-images/desktop-out-result.png)
      ![Picture showing contact page on desktop](assets/readme-assets/testing-images/desktop-contact.png)
      
   6. As a first time visitor, I want a quick and fun way to choose what to do for date night.
   - The about modal explains that there is only 8 decisions and 8 seconds for each so its definitely quick and the timer with the colour change adds a bit of excitement and more fun to it, the cartoon type result pictures add to the lightheartedness as well.

     ![Picture showing a result image](assets/readme-assets/testing-images/result-image.png)
     ![Picture showing timer](assets/readme-assets/testing-images/timer.png)

- ### Returning Visitor

   1. As a returning visitor, if my result is to go out to do something e.g cinema, I want to see where the cinemas are on google maps.
    - There is a use my location button or the user has another option of putting in another location in the search box and markers will appear to show them their options.
    - If geolocation is not supported or is blocked by their device settings then an alert box will appear.

     ![Picture showing a result image](assets/readme-assets/testing-images/markers.png)
     ![Picture showing the alert image](assets/readme-assets/testing-images/alert.png)

   2. As a returning visitor, if I have a going out result I want to be able to choose what area to search for my resulting place.
    - User can use the search box to search any area for their resulting activity.

     ![Picture showing search box](assets/readme-assets/testing-images/search-box.png)

   3. As a returning visitor, I want to be able to contact the owner with comments or questions.
     - The link to the contact form is in the nav menu at the top of the page throughout. There is a text area for any comments and questions. The contact form will not send without the required information being filled out. On successful submission a personalised modal will pop up, the send form button changes to Sent! and upon closing the modal the user will be taken back to the home page. So their is plenty of feedback that the form has sent.

     ![Picture showing form prompts](assets/readme-assets/testing-images/form-prompts.png)
     ![Picture showing the submit button text change](assets/readme-assets/testing-images/submit-button.png)
     ![Picture showing the submit button text change](assets/readme-assets/testing-images/submit-modal.png)

   4. As a returning visitor, I want to see social media links so that I can follow on my chosen platforms.
    - These are found at the bottom of the page throughout and they all open in their own tab.

    ![Picture showing social links](assets/readme-assets/testing-images/social.png)

- ### Frequent Visitor
   1. As a frequent visitor I don't want to be choosing between the same two options each time e.g restaurant vs. club. 
    - It was written in the function to use two random numbers each time, this is so that after the initial stay in or go out decision they aren't getting cinema or restaurant as decision 2 and then club or bar as decision 3 etc each time. This is so the game isn't predictable and boring. Below are images of 3 games showing the second decision of each. Staying in being the first decision that was made.

    ![Picture showing decision 2 example](assets/readme-assets/testing-images/game1.png)
    ![Picture showing decision 2 example 2](assets/readme-assets/testing-images/game2.png)
    ![Picture showing decision 2 example 3](assets/readme-assets/testing-images/game3.png)

   2. As a frequent visitor, I want to be able to contact the owner with suggestions of more options.
    - As previously covered in story 3 of frequent visitor, link to contact page is at the top throughout. In addition to what has already been covered, the information from the contact form is linked to my email and so any suggestions would come straight to me and with the email address completed by the user I could respond to them.
  
    ![Picture showing email received with the information from the contact form](assets/readme-assets/testing-images/emailjs.png)

   3. As a frequent visitor I want to use links to food delivery services if the result is takeaway.

    - As with all the staying in results, there are useful links to get your date night going. These all open in their own tab.

    ![Picture showing the useful links for the staying in results](assets/readme-assets/testing-images/tablet-in-result.png)

   4. As a frequent visitor I want to see information about the markers on the map.
    - When a marker is clicked on the map an info window pops up with the place name and address. When another marker is clicked the first window will close and the new information will appear.

    ![Picture showing the marker information](assets/readme-assets/testing-images/info-window.png)

## Manual Testing

-  The website was viewed with browsers: Google chrome, Safari, Microsoft Edge, Firefox, Opera and Internet Explorer. Viewed all pages on each and checked the following:
	- Nav links work from all three pages to all links.
	- Clicking on social links from all pages work, opening in a new tab
	- Clicking the start button loads the decisions.html and starts the timer.
   - Decision counter works correctly.
	- When the time runs out the start again button reloads decisions.html and timer starts.
	- Timer colour change and pulse effect at 0 works
	- For each result, correct information is shown.
	- All resource links open the correct page in a new tab.
	- For going out results, map shows instead of resources links
	- Map shows pins of results when location is either input in the search box or use my location button is used.
	- If geolocation not supported or blocked by users, alert box shows.
         + <span style="color: grey;">Alert box appearing below the map and so on mobile screens this wasn't obvious to the user and so moved it to pop up between the input box and map.</span>
	- When pin is clicked open info window with Name of place and address.
         + <span style="color: grey;">When clicking on a second marker the original info window didn't close. It had done previously, realised when I was tidying up my code I had declared the infoWindow variable in the function where previously I had declared it at the top of my JS and so I changed it back.</span>
	- The pictures that required an attribute had links that opened in a new tab to the correct places.
	- Hover effects work on social icons and all links and buttons.
         + <span style="color: grey;"> I had given one of my buttons a btn-hover instead of hover-btn class so fixed that. Had also not given the modal button the hover-btn class in contact.html so added that in too.</span>
	- Form will not submit without all three required personal details being completed and comment box. Can type in text area, On successful form submission, personalised modal appears, both close buttons take user back to home page and star rating works.
         + <span style="color: grey;">Realised that the star ratings were being skipped over by keyboard control and screen reader and so added in a tab-index</span>
	- Upon successful submission, receive an email with details taken from the form by email.js and send button has changed to sent.
         + <span style="color: grey;">I was getting a 412 error, when I went to my JS account it said I needed to reconnect my google account which as far as I could tell hadn't disconnected, created a new service which fixed the issue.</span>
	- 404.html back to home button works.
	- 404 report issue link takes user to contact form.
	- About modal close buttons work.
   - Friends, family and slack peer review used. Devices and browsers were iphone 11: Safari (x3), iphone XS Max: Safari, iphone 6: Chrome, iphone XR: safari, iphone 11 Pro: Safari, iphone 10: Safari, Samsung S20 FE: Chrome, Samsung S10 and Sony Xperia I3: Chrome. 
        + There was a few comments about seeing the same option more than once, once I explained you start with 8, choose 4, then from those 4 you choose 2 and then pick from those 2, so the max you'll see one option is 3 times, they then understood what was going on. So I put a note on the landing page so people would know to expect to see some options more than once.
        + Another comment was that when the hover effect was transitioning it affected the neighbouring social link icons. I changed the structure of the footer so that the individual links were in individual columns and so the other icons weren't jostled about when another was hovered over.
        + Comment that tissue mask in pamper night result text was a typo. This highlighted that this isn't a well known beauty product so changed the wording to be clearer
   - Chrome devtools used to test responsiveness throughout the development process see bugs found below. Viewed all pages on all of the available devices at the end of the project to ensure everything still looked good.
   - Viewed physically on Macbook air 13", Huawei tablet, HP Chrome book, Dell 21" HD screen, iphone 11, Dell 17" laptop and Pixel 4XL phone to ensure that after all issues found and resolved that there was nothing else appearing
  
## Bugs

   ### Found and Fixed 

   In addition to the issues found in manual testing, I also found the below.

   -  On iphone 11 had a massive gap between content and footer, played about with margins, trying to fix it. Realised I had put margin of 10vh on both top and bottom, when I just wanted it on the top. 
   -  Footer was taking up more room that it should, it was escaping the container. Because I had changed the footer to put the icons in their own columns (see manual testing) bootstrap padding had been introduced, removed this.
   -  Realised that once I'd picked going out or staying in the top button was coming up with the same option every time. When I looked at the function, realised that when I had changed a variable name from length to arrayLength after it been flagged by the JSHint, I had only changed two out of three of the placed it had been used.
   -  On mobile the map obviously being smaller meant that the default satellite/ terrain options at the top left of the map were taking up alot of room and when an info window was opened, the information was being overlapped. Changed map type options to a dropdown menu using the Google Maps API documentation.

   ### Existing

   -  Colours not supported on internet explorer so everything is pretty much white. Looked into fixes for this but the slack community advised against it due to Internet explorer no longer being supported.
   -  Still not happy with the view on mobile. On dev tools all the mobile views look fine, no scrolling required. I have everything bar the footer in a container, min-height: 90vh and footer being 10vh. But on my phone I'm not seeing the social icons in the same view as the nav menu. I don't know if its because newer mobiles have full size screens but have overlays at the top and bottom. and thats why I'm not seeing everything, because they are included in the 100vh maybe? I tried changing heights in dev tools which just gives gaps. So i thought it best to stick with a bit of vertical scrolling than gaps.

  ![iphone11 view](assets/readme-assets/testing-images/iphone.png)
  ![Second iphone11 view](assets/readme-assets/testing-images/iphone2.png)