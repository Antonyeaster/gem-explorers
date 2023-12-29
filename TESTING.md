# Testing

- [Testing](#testing)
  - [Validators](#validators)
    - [W3C HTML Validator](#w3c-html-validator)
    - [CSS Validator](#css-validator)
    - [JSHint Validator](#jshint-validator)
    - [CI Python Linter](#ci-python-linter)
      - [Admin](#admin)
      - [Forms](#forms)
      - [Models](#models)
      - [Project Urls](#project-urls)
      - [Settings](#settings)
      - [App Urls](#app-urls)
      - [Views](#views)
  - [Manual Testing](#manual-testing)
  - [Lighthouse Testing](#lighthouse-testing)
    - [Index Page](#index-page)
    - [Updated Index Page](#updated-index-page)
    - [Loaction Detail Page](#loaction-detail-page)
    - [Updated Loaction Detail Page](#updated-loaction-detail-page)
    - [About Page](#about-page)
    - [Contact Page](#contact-page)
    - [Updated Contact Page](#updated-contact-page)
    - [Webinar Page](#webinar-page)
    - [Updated Webinar Page](#updated-webinar-page)
    - [Webinar Detail Page](#webinar-detail-page)
    - [Updated Webinar Detail Page](#updated-webinar-detail-page)
    - [Booking Page](#booking-page)
    - [Updated Booking Page](#updated-booking-page)
  - [Bugs](#bugs)
    - [Resolved Bugs](#resolved-bugs)
    - [Known Bugs](#known-bugs)

## Validators

### W3C HTML Validator

After entering my code into the validator, I did receive some information errors, which consisted of forward slashes on tags that do not require a closing tag. This happened while using the built in format tool. Other errors that occurred were button nesting in incorrect places, this was a simple fix and was quickly rectified.

![W3C HTML Validator](/documentation/testing/w3-html-validator.png)

### CSS Validator

The CSS validator returned with no errors.

![CSS Validator](/documentation/testing/css-validator.png)

### JSHint Validator

The JSHint validator also came back with no errors; however, I did have to use the comment **jshint esversion: 6** to get rid of one warning. I found the solution to this [here](https://stackoverflow.com/questions/27441803/why-does-jshint-throw-a-warning-if-i-am-using-const)

![JSHint](/documentation/testing/jshint.png)

### CI Python Linter

All tests came back with no errors except a white space here and there.

#### Admin

![Admin](/documentation/testing/ci-python-linter-admin.png)

#### Forms

![Forms](/documentation/testing/ci-python-linter-forms.png)

#### Models

![Models](/documentation/testing/ci-python-linter-models.png)

#### Project Urls

![Project Urls](/documentation/testing/ci-python-linter-project-urls.png)

#### Settings

![Settings](/documentation/testing/ci-python-linter-settings.png)

#### App Urls

![App Urls](/documentation/testing/ci-python-linter-urls.png)

#### Views

![Views](/documentation/testing/ci-python-linter-views.png)

## Manual Testing

All testing was done manually. The link below provides the individual tests that have been done. The tests were based on the user story acceptance criteria, each point within the criteria has been tested and supplied with an expected outcome. This then leads to the test result and the sprint number to which the user story was applied.

All tests passed successfully, confirming the implemented features are working as they should.

[Manual Testing Gem Explorers](/documentation/testing/manual-testing.pdf)

To completly test my website I used multiple browsers including Google Chrome, Microsoft Edge, Firefox and Safari. Tested on devices such as, Iphone 15 Pro Max, Iphone 12 Pro, Ipad and HP laptop.

I also used Chrome dev tools to test each page at different sizes to test responsiveness.

Testing has also been done by family and friends, making sure to reach as many devices as possible. I have received very positive feedback from these, with minor styling issues raised.

## Lighthouse Testing

The lighthouse test results are ok but the performance results on most tests are lower than I'd like. After doing some research, I found that the main performance dips were caused by the deployment site and the installed libraries. I did take some steps to increase the scores, such as image resizing, but this only made a small difference. However, my main goal was to make sure the accessibility score was high. Making sure the website is working well for screen readers.

I also came across an error while running my lighthouse test. This came as a surprise, as the day before I was running the lighthouse tests and I was receiving a SEO score of 100, as is visible in a few of my updated screenshots. However,  when I continued the next day with the tests, it appeared I was receiving an error about a **robots.txt file**. At this stage of the course, this hasn't been part of the learning material. This unfortunately bumped the rest of my scores back down. After speaking to the staff of the course, I was advised that this was not only happening to myself and that it is beyond the scope of this particular project. For this reason, I have decided to leave the scores as they are.
  
### Index Page
  
![Index Desktop](/documentation/testing/lighthouse-desktop-index.png)
![Index Mobile](/documentation/testing/lighthouse-mobile-index.png)

### Updated Index Page

![Updated Index Desktop](/documentation/testing/updated-lighthouse-desktop-index.png)
![Updated Index Mobile](/documentation/testing/updated-lighthouse-mobile-index.png)

### Loaction Detail Page

![Location Detail Desktop](/documentation/testing/lighthouse-desktop-location-detail.png)
![Location Detail Mobile](/documentation/testing/lighthouse-mobile-location-detail.png)

### Updated Loaction Detail Page

![Updated Loaction Detail Desktop](/documentation/testing/updated-lighthouse-desktop-location-detail.png)

The location detail mobile lighthouse test had not changed from the original test; for this reason, I have not supplied a screenshot.

### About Page
  
![About Desktop](/documentation/testing/lighthouse-desktop-about.png)
![About Mobile](/documentation/testing/lighthouse-mobile-about.png)

The About pages lighthouse tests had not changed from the original tests; for this reason, I have not supplied any screenshots.

### Contact Page

![Contact Desktop](/documentation/testing/lighthouse-desktop-contact.png)
![Contact Mobile](/documentation/testing/lighthouse-mobile-contact.png)

### Updated Contact Page

![Updated Contact Desktop](/documentation/testing/updated-lighthouse-desktop-contact.png)
![Updated Contact Mobile](/documentation/testing/updated-lighthouse-mobile-contact.png)

### Webinar Page

![Webinar Desktop](/documentation/testing/lighthouse-desktop-webinar.png)
![Webinar Mobile](/documentation/testing/lighthouse-mobile-webinar.png)

### Updated Webinar Page

![Updated Webinar Desktop](/documentation/testing/updated-lighthouse-desktop-webinar.png)
![Updated Webinar Mobile](/documentation/testing/updated-lighthouse-mobile-webinar.png)

### Webinar Detail Page

![Webinar Detail Desktop](/documentation/testing/lighthouse-desktop-webinar-detail.png)
![Webinar Detail Mobile](/documentation/testing/lighthouse-mobile-webinar-detail.png)

### Updated Webinar Detail Page

![Updated Webinar Detail Desktop](/documentation/testing/updated-lighthouse-desktop-webinar-detail.png)
![Updated Webinar Detail Mobile](/documentation/testing/updated-lighthouse-mobile-webinar-detail.png)

### Booking Page

![Booking Desktop](/documentation/testing/lighthouse-desktop-bookings.png)
![Booking Mobile](/documentation/testing/lighthouse-mobile-bookings.png)

### Updated Booking Page

![Updated Booking Desktop](/documentation/testing/updated-lighthouse-desktop-booking.png)
![Updated Booking Mobile](/documentation/testing/updated-lighthouse-mobile-booking.png)

## Bugs

### Resolved Bugs

Hamburger menu - While setting up my navigation bar using bootstrap, I was unable to get my 'hamburger icon' to perform the drop down menu. To fix this, I was required to download a different version of Bootstrap. I had followed one of the walkthrough videos through Code Institute, and the particular nav bar I was using wouldn't work with the version of Bootstrap I had installed.

Static folder - Although this bug was completely created by myself, I thought it was important to mention and keep on record as it required me to troubleshoot. I believe that while using my laptop trackpad, I managed to move the static folder to my gems app folder without realising it. Because these folders are close to each other within the folder structure in the workspace, this wasn't the easiest problem to see right away. Initially, when my CSS wasn't working, I noticed the static folder was missing. At this stage, the CSS was minimal due to using bootstrap, so I created a new static folder. This did not fix the problem I was having. After this, I went through my file structure carefully, found the correct static folder in the gems app, and moved it back to its original location. I then deleted the duplicated CSS folder. This fixed the problem, and I was able to expand on the original CSS I had written.

Contact form - While testing my contact form, I noticed that the message area was not rendering the placeholder text but also not registering as required. After troubleshooting through the contact form HTML, I noticed that the code had been automatically formatted and the text area indentation was incorrect. After formatting the code correctly, the message placeholder text is working, and the form cannot be submitted without writing a message.

Comments section - Everything within the comments section was working fine. However, if the user was not signed in and there were no comments registered for that particular post, the bottom of the page would be completely empty, and the user would not know if they could comment on that particular post. To fix this, I used Django templating to display different text in response to the user's authentication.

Like icon on mobiles while signed in - The like icon on mobile browsers not signed in is lined up with the like count number. However, if the user was to sign in the like button would move across the page while the number count remained in place. To fix this, I noticed the developer tools on Chrome were saying that the icon had a padding of 6px. I changed this within my CSS 'like button' with a value of zero, and now the icon stays in line with the count number.

### Known Bugs

Lighthouse tests - While testing my website using the lighthouse test tool in Chrome Dev Tools, I came across an error regarding a robot.txt file. The test was informing me, "Lighthouse was unable to download the robots.txt file". I had run many lighthouse tests prior to this and did not have the same error. After reaching out to the staff of the course, I was informed this wasn't just happening to myself, and "robots.txt" was beyond the scope of this particular project. For this reason, I left the error within lighthouse and after some research, I acknowledged that this error would not impact my website.

Return to [Readme](README.md)
