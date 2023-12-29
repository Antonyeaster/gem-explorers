
# Gem Exploreres

As a keen explorer myself, I believe Gem Explorers is the ideal site to visit if you're looking for a new location to visit that has a little something extra about it, something not everyone knows...

Gem Exploreres is not about revealing secrets or disrupting the local areas; its purpose is to point any other keen explorers in the right direction to discover the natural beauty of our world!

![Am I Responsive](/documentation/features/am-i-responsive.png)

[Gem Explorers Live Project](https://gem-explorers-7dfdfea9b382.herokuapp.com/)

## Contents

* [User Experience UX](#user-experience-ux)
* [Planning](#planning)
  * [Scope](#scope)
  * [Agile](#agile)
* [User Stories](#user-stories)
* [Design](#design)
  * [Wireframes](#wireframes)
  * [Relationship Diagrams](#relationship-diagrams)
  * [Colour Theme](#colour-theme)
  * [Typography](#typography)
* [Technologies Used](#technologies-used)
* [Features](#features)
  * [Landing Page](#landing-page)
  * [About Page](#about-page)
  * [Contact Page](#contact-page)
  * [Webinar Page](#webinar-page)
  * [Booking Page](#booking-page)
  * [Sign in](#sign-in)
  * [Sign up](#sign-up)
  * [Sign out](#sign-out)
  * [Error 404](#error-404)
  * [Error 500](#error-500)
* [Future Implementations](#future-implementations)
* [Accessibility](#accessibility)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
  * [Media and Content](#media-and-content)
    * [Media](#media)
    * [Content](#content)
  * [Code inspiration and help](#code-inspiration-and-help)
    * [General references](#general-references)
  * [Acknowledgement](#acknowledgement)

## User Experience UX

Users of this website can expect:

* A user friendly experience for explorers looking to find information in one place.
* An area to get extensive information in the form of a webinar.
* Using an intuitive booking section to arrange the webinars.
* A place to communicate with other explorers by using comments and liking posts.
* The chance to send their own ideas as suggestions for another post.

This website can help the user achieve these goals by:

* Having clear and intuitive navigation
* Giving the admin the ability to keep posts up to date and add new ones.
* Displaying other users comments and allowing users to continue the conversations with more comments.
* Offering a wide range of available webinar times and dates to suit most lifestyles.
* A list of current bookings to allow the user to double check when they have booked.
* Ability to update and delete bookings if things change.

This website:

* Gives the user a wide range of information all in one place.
* A mixture of buttons and menus to make navigation easy.
* Gives the user the opportunity to express their feelings by liking and commenting.
* Gives the user a straight forward experience for changing or deleting their bookings.
* Gives the user a chance to attend a webinar to receive expert advice on different locations.

## Planning

#### Site Aims

It's a big decision to decide where to go on your adventures, and it can also be quite a difficult one. Discovering the world is such a huge experience and something I would call a must.

This site aims to give you the hand you might need to get on the road. This is done by giving you multiple posts to look through with extensive information regarding a particular location. More so, you can engage with other users in the comments to build a community of eager explorers. On top of that, you can visit our webinar page and get booked in for a webinar that might just get you to take that next step.

### Scope

#### Must Have

* Sign Up
* Sign in/Out
* Admin posting with CRUD (Create, Read, Update and Delete)
* Navigation
* Extend post for more information
* User booking with CRUD (Create, Read, Update and Delete)
* Admin approve bookings

#### Should Have

* View post list
* Site purpose (Landing page)
* Like/Unlike posts
* Comment on posts
* Approve comments
* About page
* Creating webinar
* Webinar viewing

#### Could Have

* Confirmation pop up notifications
* Create draft post
* Contact/Idea form
* See comment total from post list view

#### Won't Have

* Add image upload to contact form

## Agile

I Used Agile to create and track my User Stories. I also used issues and milestones to track progress through the project, you can view Agile process is a separate file called [AGILE.md](AGILE.md)

## User Stories

* As an Admin I can...
  * As a site admin I can create. read, update and delete posts so that I can fully manage my blog content
  * As a site admin I can create a draft post so that I can finish creating the post later
  * As a site admin I can choose which comments to approve so that I can check they are appropriate for the blog
  * As a site admin I can approve bookings so that The my bookings page will update the user with there booking
  * As a Site admin I can create a webinar so that users can view which webinar they'd like to attend

* As a User I can...
  * As a site user I can read the homepage so that I understand the site purpose from the first page
  * As a site user I can use the navigation bar so that I can navigate to different pages on the site
  * As a site user I can register an account so that I can make bookings, comment on blog posts and like/unlike blog posts
  * As a site user I can sign in to my account so that I can proceed with making bookings, commenting and liking/unlike blog posts
  * As a site user I can see pop ups so that I know if the request has been successful
  * As a site user/admin I can like/unlike a blog post so that I can see what posts are popular to decide what one to read/get a understanding at what type of posts get the most attention
  * As a site user I can comment on a post so that I can be involved with the community and conversations with others
  * As a site user I can open a blog post so that I can read all the information provided
  * As a site user I can create a booking so that I can receive expert advise on a destination
  * As a site user I can update the amount of viewers attending the webinar on a single device so that I can make changes if anyone cant make it.
  * As a site user I can delete my booking so that my booking time can be used for someone else
  * As a site user I can view and read my booking so that I can check all the information is correct
  * As a site user I can use the contact/ideas form so that I can express any ideas for hidden gem location or give feedback to the site
  * As a site user I can view the post list so that so I can pick one I'd like to read
  * As a site user I can view the about page so that I can get a good understanding of the business behind the site
  * As a Site user I can see comments from the post list view so that I can quickly see where the conversations are happening
  * As a Site User I can view which webinars are being held and when so that I can book to attend

### User Stories not included as part of the agile process

* As a Site user I can upload images on the contact form so that I can share my experience with images as well as text

## Design

### Wireframes

![Desktop Wireframes](/documentation/wireframes/desktop-wireframes.png)
![Medium Screen Wireframes](/documentation/wireframes/medium-wireframes.png)
![Small Screen Wireframes](/documentation/wireframes/small-wireframes.png)
![Modal wireframes](/documentation/wireframes/modal-wireframes.png)
![Navbar Wireframe](/documentation/wireframes/navbar-wireframe.png)

### Relationship Diagrams

To be able to add all the functionality the site needs to run, I added 5 models to my models.py file. I have split the diagrams into two to make understanding the relationship between them easier to understand. I also added a "user" and "like" diagram; these do not correspond with my models.py file. However, they give a logical understanding of how Django manages users within its system.

The Post relationship diagram displays the relationship between the post, comments, likes, and users.

* The User and Post have a "one to many" relationship. Meaning the user can be linked to multiple posts, but each post is only linked to one user. At this stage of the site, it is the admin (author).
* Comments and Post have a "one to many" relationship. All the posts can have multiple comments within them, but each comment is only linked to that post.
* User and Likes use a "many to many" relationship. Meaning all users can like multiple posts, and the like is linked to that user within that post.

![Post Relationship Diagram](/documentation/relationship-diagrams/post-diagram.png)

The webinar relationship diagram displays the relationship between the webinar, timestamp, booking and user.

The unique constraints within the timestamp and booking model are to ensure there are no duplications with bookings at the same times and dates.

* The webinar and timestamp have a "one to many" relationship. Meaning one webinar can have multiple timestamps that users can book.
* Booking and user have a "many to one" relationship. Meaning one user can make multiple bookings, but all bookings are related to that user.
* Timestamp and booking have a "one to many" relationship. Each timestamp can have multiple bookings, but each booking is only linked to that one timestamp.
![Webinar relationship Diagram](/documentation/relationship-diagrams/webinar-diagram.png)

### Colour Theme

I decided to keep the colours neutral. The idea behind the theme was "The Sky Is The Limit" meaning there are so many places one can visit, that there really is no limit to what the world has to offer.

![Colours](/documentation/screenshots/colours.png)

I used [Eight Shapes Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23000000%2C%20Black%0D%0A%230233d3%0D%0A%2370eb8c%0D%0A%23DC3545%0D%0A%2369c4f8&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) to make sure the contrast was working well and the text was readable. Here is a list of the colour codes below.

* White #ffffff
* Black #000000
* Blue #0233d3
* Green #70eb8c
* Red #DC3545
* Sky Blue #69c4f8

### Typography

I decided to only use one font, I chose Quicksand font as I felt it had a good amount of style while keeping the readability high. The font within the Post blogs or webinar bookings are open to the admins discression. This is part of summernote, which I used as my text editor within Posts and Webinars

![Quicksand Font](/documentation/screenshots/quicksand-font.png)
![Summernote editor](/documentation/screenshots/summernote-editor.png)

## Technologies Used

### Languages Used

* HTML5
* CSS3
* Javascript
* Python

### Frameworks, Libraries & Programs Used

* [Balsamic](https://balsamiq.com/wireframes/) - Used to create wireframes.
* Git - For version control.
* Github/Codeanywhere - To save and store the code files for the website.
* [Google Fonts](https://fonts.google.com/) - To choose and import my desired font (Quicksand).
* [Font Awesome](https://fontawesome.com/) - For icon in the title and social media icons.
* [iloveimg](https://www.iloveimg.com/resize-image) - for resizing images.
* [Eight Shapes Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23000000%2C%20Black%0D%0A%230233d3%0D%0A%2370eb8c%0D%0A%23DC3545%0D%0A%2369c4f8&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) - To check colour contrast.
* [Convertio](https://convertio.co/jpg-webp/) - To change images to webp.
* [Am I Responsive?](https://ui.dev/amiresponsive) - To show the website on a range of different sized devices.
* [Wave Accessibility checker](https://wave.webaim.org/) - To check the site is contrast ready and accessible to visually impaired individuals.
* Google Dev Tools - To help with responsive design and troubleshooting.
* [Lucid](https://lucid.app/documents#/documents?folder_id=recent) - was used to create the relationship diagrams.
* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - was used for building a responsive website quickly.
* [Django](https://www.djangoproject.com/) - was used to build the application.
* Django allauth was used for user authentication.
* Django crispy forms was used to render forms.
* [EmailJS](https://www.emailjs.com/) - was used to conect the contact form to an email address.
* [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gad_source=1&gclid=CjwKCAiAhJWsBhAaEiwAmrNyqyQ_Ci5KK1n7K-1IzUHKBQBrgo9HYF2VgMGTCPRslAY7pWyZAI96_BoCc0UQAvD_BwE) - was used a to store static files.
* Summernote for WYSIWYG (What You See Is What You Get), this was used for the content section and description section of Posts and Webinars.
* [Heroku](https://id.heroku.com/login) - Was used to deploy the site.
* [TinyPNG](https://tinypng.com/) - Was used to reduce image size
* WordPad was used for manual testing logging.

## Features

### Landing Page

#### **Hero image and text**

The hero image was the perfect place to grab the user's attention with a beautiful image, referencing the astonishing nature we have. The vibrant colours within the image have been used to help draw the user in.

The text gives the image a boost by explaining the purpose of the sight and pushing the user to head further into the website.

![Hero image and text](/documentation/features/hero-image.png)

#### **Navbar**

I used a navigation bar to give the user a simplistic way to navigate the website. All pages within the website have a navigation bar at the top.

**All users will have access too:**

* The Gem Explorers logo - This is exactly the same as the home link below; however, this comes in more useful when you are on smaller devices with the "hamburger icon".
* Home - This link simply returns the user back to the landing page, where the blog posts are.
* About - Takes the user to the About Us page, where they can get more information about the purpose of the page.
* Contact - This link takes the user to a contact form, which can be filled out and sent to the admin.
* Webinar - Takes the users to the webinar page, which will display a list of available locations to get more information.
* Sign in - For users who have already created an account and want to make comments, like posts, and book webinars.
* Sign up - For new users that want to make the most of the website's functionality.

 ![Navigation bar (Not signed in)](/documentation/features/navbar-not-signed-in.png)

 **Signed in users have access too:**

 Excluding the sign in and sign up from above the signed in users will have access to all the above and additional navigation.

* Bookings - The bookings link will take the user to their approved bookings.
* Sign out - The sign out link will open a warning box, this is just for sign out confirmation.
* A displayed username - This gives the user indication they are signed into the correct account.

 ![Navigation bar (Signed in)](/documentation/features/navbar-signed-in.png)

#### **Admin**

 Admin has access to all the above links with an additional one.

* Admin - This gives the admin for the page a shortcut to the Django administration page, where they can manage all posts, comments, webinar post, webinar times, and bookings.

 ![Navigation bar (Admin)](/documentation/features/navbar-admin.png)

#### **Responsive Navigation (Hamburger menu)**

 The icon on the right hand side gives the users on smaller screens a similar experience to the users on larger screens by making all the links accessible within the icon.

![Menu icon](/documentation/features/hamburger-menu.png)

#### **Location Posts**

The Location Posts section gives the user an area where they can browse through the current location posts and choose which one they'd like to read more about. The location post section holds six posts per page, displaying a next or prev button as shown in the images.

![Next page](/documentation/features/pagination.png)
![Prev page](/documentation/features/pagination-prev.png)

![Locations Posts](/documentation/features/location-post-section.png)

#### **Location Detail**

When the user clicks on one of the location posts, they will be taken to the location detail page, which displays the post title, post image, post content, likes, and comments section. This allows the user to read the full content of that post.

![Location Detail](/documentation/features/location-detail.png)

#### **Like and comment icons**

If the user is signed in, they will unlock the like and comment features. This is exclusive to registered users and increases as each user likes and comments on a post.

![Like and Comment](/documentation/features/like-commented-icons.png)

#### **Comments**

If the user is not signed in but there are comments on the post, they will be able to read the comments but not make a comment.

![Commented not signed in](/documentation/features/commented-signed-out.png)

If the user is not signed in and there aren't any comments, there is text to inform the user to sign in to be the first to make a comment with a link to the sign in page.

![Not commented not signed in](/documentation/features/not-commented-not-signed-in.png)

If the user is signed in, they will have the ability to read the comments and make new ones. The comment box appears next to the comment list.

![Commented Signed in](/documentation/features/commented-signed-in.png)

If the user is signed in but there aren't any comments, there is text to inform the user that there are no comments and they could be the first to sign in.

![Not commented signed in](/documentation/features/not-commented-signed-in.png)

If the admin is signed in, they have the ability to delete comments on the frontend of the website. Although comments need to be approved, I wanted to add this feature as a safety net for the admin, just in case somebody manages to find a way around waiting for comment approval. This way, the admin can delete the comments quickly if they contain inappropriate text.

![Admin commented delete](/documentation/features/admin-commented.png)
![Admin comment delete modal](/documentation/features/admin-delete-comment.png)

If the user is signed in and submits a comment, they will be shown two success messages, one at the top to say thank you for your comment, which will disappear after 4 seconds. The other message remains where the comment box was, this just gives the user complete confirmation that the comment was successfully sent and is awaiting approval.

![Comment successful](/documentation/features/comment-message-top.png)
![Comment awaiting approval](/documentation/features/comment-awaiting-approval.png)

Within the Django admin panel, the admin can choose to approve multiple comments or approve comments individually. There are tick boxes next to each comment, once the tick box is clicked, you can use the drop down menu to select approve comments.

![Approve multiple comments](/documentation/features/approve-multiple-comments.png)
![Approve individual comments](/documentation/features/approve-individual-comment.png)

The admin user can delete comments or edit comments in the Django admin panel.To delete the comment you can click the tick box and use the drop down menu to select "Delete comment".
To edit the post, you can click on the name used to make the comment. This will take you into the comment where you can make adjustments or delete from inside the comment.

![Delete comment](/documentation/features/delete-comment.png)
![Edit comment](/documentation/features/edit-comments.png)

#### **Footer**

The footer consists of three links to LinkedIn, YouTube, and Github. All three links open in a new tab. The Youtube link is in reference to the fact that if the site held the webinars and you missed them, you could watch them back on a Youtube channel.

![Footer](/documentation/features/footer.png)

### About Page

The about page has two sections, our story and our mission. Our story gives a background to the reasons behind creating the website, expressing the passion behind it. While our mission seeks to get the reader involved with the website and, in time, find hidden gems.
The about page is meant to inspire, so at the bottom of the page lies a link to the sign up form as I believe at this point the user is most likely to sign up.

![About Our Story](/documentation/features/about-our-story.png)
![About Our Mission](/documentation/features/about-our-mission.png)

### Contact Page

The contact page includes a form for the user to fill out if they want to. The form consists of four fields: name, email, location, and message. The location field is optional, while all other fields are required. The email address has to be submitted in the correct format (using the @ symbol). The contact is for multiple purposes:

* The user is reaching out with a general question.
* Problems making a booking for a webinar
* General issues
* An idea for a location to post about
* Site feedback

![Contact Form](/documentation/features/contact-form.png)

The contact form will display a success message with a green background if the form is sent successfully or an error message if the form is unable to be sent.
The form will prompt the user for the required fields if they are missed by using a label inside the field.

![Message sent successfully](/documentation/features/submitted-form.png)
![Required Field](/documentation/features/required-field.png)

The contact returns an email to the admin, which includes all the information the user has typed in. This way, admin can reply to the user directly, following on from their enquire.

![Email received](/documentation/features/email-from-contact-from.png)

### Webinar Page

On the webinar page, there are 6 webinars per page with the same pagination as the location posts. From the outside of the posts, the user is informed of who the speaker is, along with the title and a small description of the webinar. This is then followed by the "See times" button, which will take the user into the webinar detail page.

![Webinar posts](/documentation/features/webinar-list.png)

### Webinar Detail Page

On the webinar detail page, the user will see the location image on the left and a list of booking cards on the right. Under the location image is the webinar description. Under the description is information regarding all webinars and how they work. This includes a direct link to the contact form for any users with questions.

![Webinar Detail](/documentation/features/webinar-detail.png)

#### **Booking Card**

The webinar booking card displays the location the booking is for, the date and time for the booking, a dropdown menu for the number of viewers, and a book button.

![Booking card](/documentation/features/booking-card.png)

#### **Not authenticated booking**

If the user is not signed in when they try to make a booking, they will be redirected to the sign in page. This will also trigger an error message that will appear at the top of the page with a red background.

![Not signed in booking](/documentation/features/not-signed-in-booking.png)

#### **No Bookings**

If the user goes to the booking page but has no approved booking, they will see a small message to confirm this.

![No Bookings](/documentation/features/no-bookings.png)

#### **Booking confirmation**

If the user creates a new booking, they will be greeted with a thank you message explaining that their booking is awaiting approval. The page also includes a link to the booking page.

![Booking confirmation](/documentation/features/thank-you-for-booking.png)

#### **Already booked**

If the user tries to book a webinar they have already booked, they will be prompted that they have already booked this webinar. This message includes a link to the booking page.

![Already booked](/documentation/features/already-booked-webinar.png)

#### **Approve Webinar Booking**

The admin can approve webinar bookings. This can be done by going to the bookings tab within the Django admin panel. Once the tick boxes next to booking names are selected, the admin can use the drop down menu to approved the bookings.

![Approve multiple bookings](/documentation/features/approve-multiple-bookings.png)

The admin can also approve bookings individually by selecting the name linked to the booking, selecting the approve tick box, and then saving in the bottom right corner.

![Approve individual booking](/documentation/features/approve-individual-booking.png)

#### **Delete Booking Admin**

The admin can delete the user's bookings. This can be done inside the bookings tab in the Django admin panel. Select the tick box next to the name of the user, go to the drop down menu, and select delete.

![Delete booking multiple](/documentation/features/delete-webinar-booking.png)

The admin can select a particular booking and delete it individually, this can be done by selecting the delete button in the bottom left corner.

![Delete Individual booking](/documentation/features/delete-individual-booking.png)
![Delete confirmation](/documentation/features/confirm-delete-booking.png)

#### **Edit Bookings Admin**

Editing a booking can be done within the Django admin panel. In the booking section, select the name of the user who has booked. Once the booking has opened, you can change the user, the webinar, the number of viewers, and the approved status.

![Edit booking](/documentation/features/edit-booking.png)

#### **Create Webinar**

The admin of the page has the ability to create webinars in the Django Admin panel. To create a webinar, the admin can press the "add webinar" button on the right of the panel. Once the post opens, the admin will be required to enter a unique title, which generates a slug automatically, a speaker name, a description of the webinar, an image to be on the booking, and a status drop down.

![Create Webinar](/documentation/features/create-webinar.png)

#### **Edit Webinar**

The admin has the ability to edit the webinar post. This is done by clicking the webinar name within the Django admin panel. Once the post is open, all the fields will be prefilled with the original post. The admin can adjust what they want and click the save button in the bottom right. This route can also be used to delete the post in the bottom left corner.

![Edit Webinar](/documentation/features/edit-delete-webinar.png)

#### **Delete Webinar**

The admin also has the ability to delete the webinar posts. This can be done by selecting the tick boxes next to the webinars. Once the admin has the webinars selcted they can use the drop down menu to delete the webinar. Multiple webinar post can be delete at the same time.

![Delete Webinar](/documentation/features/delete-webinars.png)

### Timestamps

#### **Create Timestamp**

To create a timestamp, admin must be in the Django admin panel and in the timestamp section. From there, click "Add timestamp" in the top right corner. This will load the same page as the image below. Select a webinar to relate to the timestamp, then select a data and time to hold the webinar.

![Create Timestamp](/documentation/features/create-timestamp.png)

#### **Delete Timestamp**

To delete a timestamp, the admin must be in the admin panel. Go to the timestamp section and select a timestamp to delete. Select multiple timestamp tick boxes to delete more than one at a time.

![Delete multiple timestamps](/documentation/features/delete-multiple-timestamps.png)

The admin can delete the timestamp individually by selecting the particular timestamp and pressing the delete button in the bottom left corner.

![Delete individual timestamps](/documentation/features/admin edit-delete-timestamp.png)
![Confirm Delete](/documentation/features/delete-timestamp.png)

### Booking Page

The booking page is where all the approved bookings show up. Each booking is clearly separated from the others. Bookings will only show up here once they have been approved. The approved booking card displays the location the webinar is about, the date the booking is for, the number of viewers booked, and the update and delete button.

![Booked Webinars](/documentation/features/approved-bookings.png)

#### **Update Booking User**

To update the booking, the user can select the update button on the approved booking card, and a modal pop up will appear, giving the user the option to update the number of viewers. Once the number of viewers has been updated, the page will refresh and show the new number of viewers.

![Update booking user](/documentation/features/update-booking.png)

#### **Delete Booking User**

To delete the booking, the user can select the delete button on the approved booking card, and a modal pop up will appear, giving the user the option to delete or cancel. This is a safety net for users to not delete bookings by accident.

![Delete booking user](/documentation/features/delete-booking.png)

### Sign in

The sign in form consists of a welcome back message and a form which includes a required username and password. At the bottom is a link to the sign up page incase a new user clicked the wrong link.

![Sign in](/documentation/features/sign-in.png)

Once the user has successfully signed in, a success message will appear at the top of the screen for 4 seconds, telling the user they have signed in and displaying their username.

![Signed in successfully](/documentation/features/successfully-signed-in.png)

### Sign up

The sign up form consists of a welcome message and an explanation of why an email address is required for sign up. The form includes a required username, email address, and password entered twice. Also at the bottom of the page is a link to the sign in page, in case the user is already registered.

![Sign up](/documentation/features/sign-up.png)

### Sign out

The sign out button at the top right hand side of the page opens a modal. This is to make the process quicker without having to load a new page. It also gives the user a chance to confirm sign out, just in case it was a mistake.

![Sign out](/documentation/features/sign-out-modal.png)

Once the user has signed out, a success message will be displayed at the top of the page for 4 seconds. telling the user they have signed out successfully.

![Signed out successfully](/documentation/features/successfully-signed-out.png)

### Error 404

If the user encounters a **Page Not Found** error page they will have the option to return home.

![Error 404](/documentation/screenshots/error-404.png)

### Error 500

If the user encounters a **Server Error** error page, they will have the option to return home. Or they have the option to go to the sign up page or sign in page. In case they were trying to access features only registered users can use.

![Error 500](/documentation/screenshots/error-500.png)

## Future Implementations

In the future, I would like to add the following features:

* Adding images to the contact form would then allow the admin to use the image sent for the post.
* Posts created by users would require admin approval. I believe this will attract a lot more users to the website.
* Create a reply button in the comments that would directly reply to a particular comment.
* Add videos to the location post.
* Enhance the like button to not refresh the page when liked or unliked.

## Accessibility

It's vital to make websites as accessible and easy to follow as possible. This has been achieved by:

* Using semantic HTML
* Using descriptive alt attributes on images
* Using aria labels for links, including naming the footer social media icons
* Using a colour contrast that is easy to see

I also used [Wave - Web accessibility evaluation tools](https://wave.webaim.org/) to make sure I had no errors regarding colour contrast and aria labels.

## Testing

I have included testing information in a separate file called [Testing.md](TESTING.md)

## Deployment

### How to fork

1. Go to [Gem Explorers](https://github.com/Antonyeaster/gem-explorers)Repository.
2. Click on the fork button in the top right hand corner of the page between **Watch** and **Star**.

### How To Clone

1. Go to [Gem Explorers](https://github.com/Antonyeaster/gem-explorers)Repository.
2. Locate the Green code button on the right hand side of the screen, click the drop down.
3. Choose the **Local** tab and you will see 3 choces (HTTPS, SSH, Github CLI). Use HTTPS tab and copy the URL below.
4. Navigate to your own workspace where you would like the cloned directory to be.
5. Open a terminal and use the **git clone** command and then paste the URL you've just copied.
6. Use the enter key to confirm the clone.

### Deployment to Heroku using Github

The Gem EXplorers Website has been deployed using Heroku. The Code Institute Django Cheatsheet was used for deployment [CI Django Cheatsheet](/documentation/deployment/django-deployment-instructions.pdf)

#### **Your Workspace part 1**

1. Create a new repository on Github, copy the URL and paste into your chosen workspace.
2. Open a new terminal and install:
    * **pip3 install 'django(<)4 gunicorn'** Remove the brackets from around the less-than symbol.
    * **pip3 install dj_database_url==0.5.0 psycopg2**
    * **pip3 install dj3-cloudinary-storage**
    * **pip3 install urllib3==1.26.15**
3. Create a requirements file using the command **pip3 freeze --local > requirements.txt** in the terminal.
4. Create a project name using command **django-admin startproject ______ .** (Your project name remembering to put a '.' at the end)
5. Create an App using command **python3 manage.py startapp _______** (Your app name after start app)
6. Open **settings.py** add your app name to the bottom of 'INSTALLED APPS'
7. Migrate Changes in terminal with **python3 manage.py migrate**
8. Run server to test with command **python3 manage.py runserver**
9. When the error screen loads cope the HOST NAME and paste it into the ALLOWED HOSTS in settings.py file

#### **ElephantSQL (Database)**

1. Create or sign in to ElephantSQL
2. Click **Create new instance**
3. Set up your plan
4. Return to the dashboard and click on the database instance name you just created
5. Copy your ElephantSQL database URL

#### **Heroku part 1**

1. Go to [Heroku](https://www.heroku.com/) and create an account if you haven't already.
2. Click **New** the **Create app**
3. Open settings tab and click **Reveal Config Vars**
4. Add a Config Var called **DATABASE_URL** the value should be the URL you copied from ElephantSQL in a previous step

#### **Your Workspace part 2**

Go back to the workspace you created at the begining of deployment.

1. Create a new file called **env.py**
2. Open env.py and at the top type **import os**
3. Below the import set your environment variables using:
    * os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
    * os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"

#### **Heroku part 2**

Go back to heroku and add **SECRET_KEY** to the config vars, you can create your own or use [Django Secret Key Generator](https://django-secret-key-generator.netlify.app/)

#### **Your Workspace part 3**

1. In the **settings.py** file use code
    * ![Deployment Instructions](/documentation/deployment/deplyment-instructions.png)
  
2. In the **settings.py** remove the original secret key and replace with **SECRET_KEY = os.environ.get('SECRET_KEY')** This will use your secret key from Heroku
3. Comment out old Database section and add new **See image for the code**
    * ![Old database and new database](/documentation/deployment/deployment-database-code.png)
4. Once saved, in the terminal you need to make migrations using command **python3 manage.py migrate**

#### **Cloudinary**

1. Go to [Cloudinary](https://cloudinary.com/) and sign in or create account
2. Copy your **CLOUDINARY_URL e.g. API Environment Variable** located in the dashboard

#### **Your Workspace part 4**

Go to your **env.py** file and paste in your cloudinary URL being sure to remember to make sure the link starts like the example **os.environ["CLOUDINARY_URL"] = "cloudinary://************************"

#### **Heroku part 3**

1. Add Cloudinary URL to config vars e.g **CLOUDINARY_URL with the value of your cloudinary url "cloudinary://************************"
2. Add DISABLE_COLLECTSTATIC to config vars with the value of 1. This is a temporary config var, will be removed before final deployment

#### **Your Workspace part 5**

1. In **settings.py** file add Cloudinary libraries to **INSTALLED_APPS** see image below for ordering of apps as it's important.
    * ![Cloudinary instructions](/documentation/deployment/deployment-cloudinary.png)

2. Set up static files to use Cloudinary and link templates. See screenshot below
    * ![Cloudinary setup in settings.py](/documentation/deployment/deployment-cloudinary-static.png)

3. Add Heroku Hostname to **ALLOWED_HOSTS** ALLOWED_HOSTS =["_______.herokuapp.com", "YOUR_HOSTNAME"] Your project name goes in the blank space and replace "Your hostname" with the actual host link.
4. Create 3 new folders **media** **static** **templates**
5. The create a **Procfile** being sure to use a capital 'P'
6. In the Procfile add web: **gunicorn ______.wsgi** Your project name goes in the blank space.
7. Add, Commit and Push your code to Github using **git add .** **git commit -m "Deployment Commit"** **git push**

#### **Heroku part 4**

1. Add config var called PORT with the value 8000
2. Go to the deploy tab and select **GitHub** as the deployment method.
3. Connect your GitHub account along with your repository
4. Scroll down to deploy manually, select **Deploy Branch**
5. Once the deployment has complete, you should receive a message saying 'Your app was successfully deployed' select View and check the app runs.

### Final Deployment

#### **Your Workspace**

1. In settings.py file change **DEBUG** from True to False
2. In settings.py set **X_FRAME_OPTIONS = SAMEORIGIN**
3. Make sure that the requirements.txt file up-to-date: **pip3 freeze --local > requirements.txt**

#### **Heroku**

1. Delete the **DISABLE_COLLECTSTATIC** form the Config Vars
2. Go to the deploy tab and scroll to the bottom as click **Deploy Branch**

## Credits

### Media and Content

#### Media

Images have been taken from multiple location listed below:

* [Canadian rockies image](https://www.travelweekly-asia.com/Destination-Travel/World-top-10-hidden-gems-to-travel-to)
* [Rainbow Mountains image](https://www.forbes.com/sites/trevornace/2016/03/02/rainbow-mountains-china-earths-paint-palette/)
* [Lake Tekapo image](https://www.viator.com/en-GB/Christchurch-attractions/Lake-Tekapo/d400-a16452)
* [Valensole Plateau image](https://www.viator.com/en-GB/Aix-en-Provence-attractions/Valensole-Plateau/overview/d5228-a20516)
* [The Lofoten Islands image](https://www.muchbetteradventures.com/magazine/the-lofoten-islands-a-photo-guide-to-visiting-the-archipelago-in-norway/)
* [Vatnajökull ice cave image](https://glaciertrips.is/vatnajokull-ice-cave-tour-with-glacier-hike-faq-in-2023/)
* [Three Shires Head](https://dualadventures.com/three-shires-head-peak-district-uk/)
* [Hero image](https://www.pexels.com/)
* Placeholder image (If post images in not added or a problem with original image) [Placeholder image](https://www.exploreyourworlds.com/2021/01/23/hidden-places/)

#### Content

Content and inspiration used from multiple locations list below:

* [The Lofoten Islands](https://visitlofoten.com/en/topic/see-and-do/)
* [Canadian rockies](https://www.discovercanadatours.com/blog/7-amazing-facts-about-the-canadian-rockies/)
* [Valensole Plateau](https://www.saltinourhair.com/france/valensole/)
* [Three shires head](https://www.peakdistrict.org/three-shires-head-walk-waterfall/)
* [Rainbow Mountains](https://www.forbes.com/sites/trevornace/2016/03/02/rainbow-mountains-china-earths-paint-palette/)
* [Vatnajökull ice cave](https://guidetoiceland.is/book-holiday-trips/glacier-caving-in-vatnajokull)
* Lake Tekapo was written by myself Antony Easter as it's a location I have explored myself.

### Code inspiration and help

The below links are websites and youtube videos I used for inspiration and help with my code. Links have also been referenced within the code comments.

* The walk through project provided in the Code Institutes course **I Think Therefore I Blog** was used closely to help with the project.
* [Django Tutorial](https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5)
* [Django Documentation](https://docs.djangoproject.com/en/5.0/)
* [Django Templates](https://www.geeksforgeeks.org/django-templates/)
* I used Bootstrap components from [Bootstrap Documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Frontend Delete Button](https://www.youtube.com/watch?v=CIR2QhX5mqA)
* [Ordering In Views](https://stackoverflow.com/questions/47899265/order-by-time-of-a-datetime-field-in-django)
* [Max Length Username](https://stackoverflow.com/questions/50548685/how-to-add-max-length-to-allauth-username)
* [Emailjs](https://www.emailjs.com/docs/tutorial/overview/)
* [Model Constraints](https://www.laac.dev/blog/database-constraints-in-django/)
* [Admin Button](https://forum.djangoproject.com/t/creating-a-button-for-the-admin-page/15147)
* [Linking a HTML Page](https://stackoverflow.com/questions/46860710/django-linking-a-html-page-to-a-view)
* [Number Of Viewers Dropdown Menu](https://blog.hubspot.com/website/html-dropdown)
* [JSHint Warning Fix](https://stackoverflow.com/questions/27441803/why-does-jshint-throw-a-warning-if-i-am-using-const)
  
#### General references

* [Stack Overflow](https://stackoverflow.com/)
* [W3C Schools](https://www.w3schools.com/)
* [Slack Community](https://slack.com/intl/en-gb/help/articles/212681477-Sign-in-to-Slack)
* [Geeks For Geeks](https://www.geeksforgeeks.org/)

### Acknowledgement

I would like to acknowledge the following people/communities for their help with completing my first milestone project:

* The Slack Community.
* My family and friends for taking the time to check the responsiveness on their personal devices.
* My family for their understanding of the lack of time spent with them over the Chistmas period
* My mentor David Bowers, for the incredible amount of support and encouragement he brings to our meetings.

### Disclaimer

This website has been made for educational purposes.

[Back to the top](https://github.com/Antonyeaster/gem-explorers/blob/main/README.md#gem-exploreres)
