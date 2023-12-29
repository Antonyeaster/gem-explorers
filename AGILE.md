# Agile

- [Agile](#agile)
  - [Sprint Notes](#sprint-notes)
    - [Sprint 1](#sprint-1)
    - [Sprint 2](#sprint-2)
    - [Sprint 3](#sprint-3)
    - [Sprint 4](#sprint-4)
    - [Sprint 5](#sprint-5)
    - [Sprint 6](#sprint-6)
    - [Sprint 7](#sprint-7)
    - [Sprint 8](#sprint-8)
    - [Sprint 9](#sprint-9)
    - [Sprint 10](#sprint-10)
    - [Sprint Conclusion](#sprint-conclusion)

Github issues were used to create user stories, these issues were then grouped into sprints. I used sprints to keep my development on track and under control. The issues were managed through a Kanban board.
The issues were also used in a slightly different way. I decided sprints were the best way to keep on track, and for this reason, I decided to track all my tasks using the "Todo Kanban System." These have been clearly named (User Story, Development, and Todo Task).

You can view the Kanban board [here](https://github.com/users/Antonyeaster/projects/6)

## Sprint Notes

### Sprint 1

The first sprint was all about Django project development.

I set myself the task of finishing this sprint by the next day, November 13, 2023.

I encountered one issue while attempting to push my code to GitHub: "Updates were rejected because the tip of your current branch is behind its remote counterpart." After fixing a typo in my Procfile and performing the "git pull" request, I was able to get my code pushing to GitHub again.

The sprint was finished in time with all tasks completed.

![Sprint 1](/documentation/screenshots/sprint-one.png)

### Sprint 2

During Sprint 2, I made the decision to slightly adjust my booking system. This was after going through my plan with my partner and deciding the better approach would be a webinar booking. This way, I felt the information could reach more people and expand the community.

The main goal with this sprint was to get the admin panel up and running with the basic information in place.

I finished this sprint a day early and plan on incorporating the remaining tasks into a later sprint involving the booking system.

![Sprint 2](/documentation/screenshots/sprint-two.png)

### Sprint 3

This sprint's primary goal was to set up my workspace with the majority of templates I need to run the full site.

During this sprint, I had to keep reminding myself to only do the tasks I had set out in the sprint and not get carried away with styling just yet, as the main focus at this point is to have a functional site. The whole milestone process is a huge help for not feeling overwhelmed with what to do next; however, I believe I still have a lot to learn to make the process smoother, which should come more naturally as I do more sprints.

I hadn't set a completion date for this sprint as there was some planned maintenance on the codeanywhere workspace over the weekend; however, I managed to finish the sprint before the weekend started.

![Sprint 3](/documentation/screenshots/sprint-three.png)

### Sprint 4

For this sprint, I wanted to get my blog posts to open with basic HTML and Bootstrap CSS, which I will expand on in a future sprint. Also, to get my 'allauth' installed and wire up the built in templates allauth comes with.

This sprint was done very quickly due to the very nice features of the built in allauth templates for (Login, Logout, and Sign Up).

So far in all my sprints, I have managed to finish them much quicker than I anticipated. Due to this, I plan on incorporating more issues per sprint moving forward.

![Sprint 4](/documentation/screenshots/sprint-four.png)

### Sprint 5

As mentioned in my last sprint, I wanted to make this sprint larger by incorporating more issues. I found I had only just managed to complete this within the timeframe I gave myself. This being said, I did encounter a few more problems than I had in my previous sprints.

Problems I encountered:

- While setting up my navigation, I noticed that the "burger menu" for smaller screens would not work when clicked. To correct this, I ended up using a newer version of Bootstrap, as I had previously set up Bootstrap using the Code Institute walk through video.

- At some stage between setting up my static/css and sprint 5, I managed to move the folder by accident into my gems app, causing the path to be incorrect. At first, I thought it had been deleted, so I created a new one in the correct place. However, this still didn't work until I found the original one, so when I moved it to the correct location, I deleted the duplicated one.

- While setting up my contact form, I had trouble connecting my form to emailjs. After going back over my notes and through the walkthrough, I managed to understand the process better and got everything wired up properly.

While it was frustrating to come across these problems as small as they were, it felt like a good achievement to troubleshoot myself and work out the problems.

![Sprint 5](/documentation/screenshots/sprint-five.png)

### Sprint 6

This was the largest spint I have done so far, purely because each part of the sprint was quite a task with plenty to go wrong.

I did encounter a problem during this sprint, which made me rethink the update booking process:
I made a slight change to the update booking process. This was originally going to be so the user could update their booking from one booking to a completely different booking. However, due to the nature of the course, time restraints are a big part, and after giving this a go, I kept returning with an empty dropdown menu where the available webinars should have been listed. Also, it occurred to me that changing a booking could be a loophole to getting around the "approved bookings" part of the booking system. So I would have needed to add the "approved" waiting to the update button, which I believe is no different from deleting the current booking and booking another one and waiting for approval.

I mostly used bootstrap templates for components during this sprint. This helped me get the pages set up and running. However, I do plan on customising these templates in a later sprint once I have all the must-have features running and the site is working as intended. Expanding on this, I found that having a modal for the delete booking button was a much smoother process for the user, as this means the page doesn't have to load twice while deleting the booking and then again to confirm this is what the user intended to do. So, I plan on incorporating more of these modals into other buttons, such as the sign out button.

I finished this sprint within the timeframe I had set for myself.

![Sprint 6](/documentation/screenshots/sprint-six.png)

### Sprint 7

This sprint was mostly about making certain parts of the site smoother and clearer. Up until now, most of the site has been set up using the bootstrap component templates, which has allowed me to work on functionality as much as possible.

As mentioned in the user story notes, I decided to make the contact form its own page for better navigation and less page clutter for the user. This has been done during this sprint and will possibly be expanded on with style in the upcoming sprints, depending on time due to the deadline.

As per the previous sprint, I added a modal for the sign out button, this makes the user's sign out experience much quicker.

This milestone was quite a small one in comparison to the previous one but included some important details, which are now starting to bring the site together.

![Sprint 7](/documentation/screenshots/sprint-seven.png)

### Sprint 8

I decided it was necessary to retrieve the user's email address during the sign up process. This is because, with the webinars, the speaker will need to send the invitation email out to all that have booked. While making changes to the sign up form, I also restricted usernames to 20 characters only. This is to keep the site cleaner and responsive while working efficiently.

I also created a heading and a small paragraph to help separate the hero image from the location posts.

While styling the location detail pages, I came across bugs when there were no comments or the user was not logged in. I also made it clear to the user that if there were no comments, they could be the first to make one. The message displays differently depending on whether they are logged in or not.

All footer icons are now open to the correct locations and open in a new tab.

This sprint went to plan, with a few small changes along the way.

![Sprint 8](/documentation/screenshots/sprint-eight.png)

### Sprint 9

This sprint was mostly getting all lorem text removed and writing in the official content, as well as a few styling changes to the content pages.

The about page layout was changed slightly because once the official text was on the page, it didn't flow the way I had imagined it would.

A few minor changes to the webinar post list and detail pages,giving the user information regarding the webinar calls

Adding in all the location details, along with images to match.

![Sprint 9](/documentation/screenshots/sprint-nine.png)

### Sprint 10

Sprint 10 was the final sprint and a small one in comparison to the others. I used the sprint as a final deployment with some testing. This sprint went completely according to plan, and the final deployment worked the first time. Also, the database is updated according to the website.

![Sprint 10](/documentation/screenshots/sprint-ten.png)

### Sprint Conclusion

I found the Sprint process very useful for keeping myself on track and always going forward instead of going in circles. I still have a lot to learn regarding the process and feel future projects will be better managed with sprints. However, this being my first one, I am very happy with the way it went.

Return to [Readme](README.md)
