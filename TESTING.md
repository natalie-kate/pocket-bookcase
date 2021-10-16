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

The W3C Markup Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no syntax errors in the project.

-   ## [W3C Markup Validator](https://validator.w3.org/) 

    ### Initial testing
    - index.html

    ![Initial index.html test](static/images/testing-images/validations/index-html.png)

    - about.html

    ![Initial about.html test](static/images/testing-images/validations/about-html.png)

    - contact.html

     ![Initial contact.html test](static/images/testing-images/validations/contact-html.png)

     I was getting warnings for using aria-checked on my radio buttons, I googled it and seems common practice to do so and couldn't see an alternative so I left them in.
  
    - edit-account.html

     ![Initial edit-account.html test](static/images/testing-images/validations/edit-account-html.png)

    - edit-user.html

     ![Initial edit-user.html test](static/images/testing-images/validations/initial-edit-user.png)

     Had an extra closing div and form tag so removed them.

    - manage-genres.html

     ![Initial manage-genres.html test](static/images/testing-images/validations/initial-manage-genres.png)

     Had misplaced a " and so this was causing some issues, put in the correct place. Duplicate id error was coming from forgetting that a list was getting iterated and so numerous genres were getting the same id. So changed to what I had done in other pages and made the id's the genre names.

    - manage-users.html

     ![Initial manage-users.html test](static/images/testing-images/validations/initial-manage-users.png)

     Hadn't left a space after an attribute which due to iteration meant numerous lines were missing a space.

    - profile.html

     ![Initial profile.html test](static/images/testing-images/validations/initial-profile-html.png)

     Had two divs for each of the profile bookshelves as the same id. These were the books and if there weren't any the link to the library. As they wouldn't both get shown at the same time it hadn't occurred to me that it would be an issue. Put both divs in one div with conditions to dictate which got shown when the collapsible was toggled.

    - profile-add.html

     ![Initial profile-add.html test](static/images/testing-images/validations/profile-add.png)

    - register.html

     ![Initial register.html test](static/images/testing-images/validations/register-html.png)

    - sign-in.html

     ![Initial sign-in.html test](static/images/testing-images/validations/sign-in-html.png)

    - edit-book.html

     ![Initial edit-book.html test](static/images/testing-images/validations/update-book-html.png)

     Same issue as contact.html, with the aria-checked attribute.

    - add-book.html

     ![Initial add-book.html test](static/images/testing-images/validations/add-book-html.png)

     Same issue as contact.html, with the aria-checked attribute.

    - 404.html

     ![Initial 404.html test](static/images/testing-images/validations/404-html.png)

    - 500.html

      Issues raised by inputting the 500.html code was due to the templating language and therefore raised errors of needing a head, doctype, language etc.
    
    ### Final testing (for those that needed fixed)

    - manage-genres.html
    
     ![Final manage-genres.html test](static/images/testing-images/validations/manage-genres-html.png)

   - manage-users.html
    
     ![Final manage-users.html test](static/images/testing-images/validations/manage-users-html.png)

   - profile.html
    
     ![Final profile.html test](static/images/testing-images/validations/profile-html.png)

   - edit-user.html
    
     ![Initial edit-user.html test](static/images/testing-images/validations/edit-user-html.png)

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

- #### First Time Visitor 

        1. As a first time visitor, I want to easily understand the main purpose of the site. 
        2. As a first time visitor, I want to be able to intuitively use the site.
        3. As a first time visitor, I expect to see an attractive, visually appealing site.
        4. As a first time visitor, I expect an accessible site.
        5. As a first time visitor, I expect the site to look good on my mobile device.
        6. As a first time visitor, I want to easily search the books.
        7. As a first time visitor, I want to easily register.

   - #### Returning Visitor Goals

        1. As a returning visitor, I want to add books to my "bookshelves".
        2. As a returning visitor, I want to follow on social media so I can hear of any new features.
        3. As a returning visitor, I want to be able to add books to the applications library.
        4. As a returning visitor, I want to be able to change my password.
        5. As a returning visitor, I want to be able to rate the app.
        6. As a returning visitor, I want to get feedback so I know that something has went through or if i've been redirected, why.

   - #### Frequent Visitor Goals

        1. As a frequent visitor, I want to be able to edit a book that I've added to the applications library.
        2. As a frequent visitor, I want to be able to contact the owner with suggestions.
        3. As a frequent visitor, I want to be able to move or delete books on my "bookshelves".
        4. As a frequent visitor, I want to be able to update my profile.
        5. As a frequent visitor, I want to be able to change my account information
        6. As a frequent visitor, I don't want to have never ending scrolling up or down.

   - #### Admin goals
      
        1. As admin, I want to be able to add, delete or edit a book.
        2. As admin, I want to be able to add, delete or edit a genre.
        3. As admin, I want to be able to delete a user.
        4. As admin, I want to be able to make another user an admin.
        5. As admin, I want to be able to reset a users password if they're having trouble logging in.


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