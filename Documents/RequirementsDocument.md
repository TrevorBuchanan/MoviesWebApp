# Software Requirements Specification

## MovieRatings
--------
Prepared by:

* `Trevor Buchanan`,` Team Quartet`
* `Matei Vitalaru Moruz`,` Team Quartet`
* `Brian`,` Team Quartet`
---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [MovieRatings](#MovieRatings)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2023-10-10 |Initial draft | 1.0        |
|Revision 2 |2023-13-10 |Filling information| 1.1   |
|Revision 3 |2023-16-10 |Cleaning material  | 1.2   |

----
# 1. Introduction

This application is meant to give movie watchers the ability to access ratings for any movie. Registered users can give ratings and reviews for any movie. The platform allows movie watchers to network with others and fulfill all their needs outside of watching movies.


## 1.1 Document Purpose
The MovieRatings Software Requirement Specification (SRS) document serves as a guide outlining the functional and non-functional requirements for the development of the MovieRatings web application. This document is intended to provide a clear and detailed understanding of the software's scope, features, and objectives to the various stakeholders involved in the development and use of the application. This document is crafted for developers, database administrators, UI/UX designers, testers, project managers, and investors.<br /><br />
With this document, we provide a roadmap for the development team to create a user-friendly and feature-rich platform that aligns with the needs and expectations of casual browsers, serious movie buffs, and the stakeholders involved in the MovieRatings project.

## 1.2 Product Scope
#### Purpose of the Software:
The MovieRatings software is designed to be a centralized hub for movie and TV show enthusiasts, addressing the needs of two distinct user personas: casual browsers and serious movie buffs. The software aims to:
*	Empower casual browsers to make informed decisions about what to watch based on community ratings and reviews.
*	Provide serious movie buffs with a platform to actively contribute, share opinions, and engage in discussions within other film fans.
#### Objectives and Goals:
*	Engagement: Foster a vibrant and active community through user participation in ratings, reviews, and discussions.
*	Content Discovery: Facilitate easy content discovery for casual browsers by presenting top-rated and trending movies prominently.
*	User Empowerment: Enable serious movie buffs to express their opinions, build a personal watchlist, and connect with like-minded individuals.
*	Traffic Generation: Benefit website owners by attracting a diverse user base, increasing overall website traffic and potentially generating revenue.
#### Benefits:
*	User-Centric Experience: Deliver a personalized and user-centric experience tailored to the preferences of both casual browsers and serious movie buffs.
*	Informed Decision-Making: Facilitate informed decisions for casual browsers based on community ratings and reviews.
*	Community Building: Foster a sense of community among serious movie buffs, encouraging connection and interaction.
*	Traffic and Revenue: Increase website traffic and potential revenue for website owners through enhanced user engagement and Premium subscriptions.

## 1.3 Document Overview


The content below explains the requirements of the MovieRatings project. The topics covered will be the technical requirements, users, customers, and streakholders. The use cases of this project will also be covered. These include user groups, logging in and registering, rating movies, searching and filtering, and user profile.

----
# 2. Requirements Specification

This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

The software product at hand is a movie rating site with specific user login requirements and backed up data for each user which interacts with the site. The site will have regular and premium users, login/registration operations, rating aspects, filtering aspect, and profile management aspects. In order for the software to satisfy requirements, it must include modules and routes prohibiting site editing unless logged in. There will be classes of user groups (premium and regular) which will have each their own levels of site access. Users will be able to view others ratings and add their own in real time to the site. Users will also be able to search and filter movie ratings which will be implemented via sorting features. Profiles will have personalized lists of movies and friends they want to see which will be edited by the users themselves and logged into the db file. The project will have the constraint of running on flasks local https links and will need to update the db file after each user. The site will also adhere to display resolutions (i.e. 1920 x 1080) and will format to the users device resolution. The overall problem to be solved with the software we implement will be the creation of an interactive movie rating site with personalized aspects for the users

## 2.1 Customer, Users, and Stakeholders

Users:
Our app will have two different kinds of users: the serious movie buff and the casual browser. The casual browser refers to anyone who somewhat regularly visits the site to determine what to watch. Most of these people will visit the site because it is in the top search results. Then there is the serious movie buff user, they like watching movies and like sharing their opinions about the movie. This sort of user will have an account not just to view ratings, but to leave their own too.

Stake Holders:
The stake holders are the owners of the website owners and people who love movies. The operators of the website benefit from the traffic it can bring, while movie lovers gain a place to share reviews of movies.

Customer:
The customer for our software would be anyone who wanted to run a movie/TV show review site


----
## 2.2 Use Cases


| Use case # 1      | User Groups  |
| ------------------ |--|
| Name              | "User Groups"  |
| Users             | "Premium and Regular users"  |
| Rationale         | "Adding a premium user aspect to the software will allow for a limited and sought after aspect of having "friends" on the site. This will add registration incentive as well as a unique dynamic of having different user types"  |
| Triggers          | "Every registered user will be regular, to become a premium user, the user will select the "Become premium user" option"  |
| Preconditions     | "To become a regular user, site must be loaded and select "register" the precondition to becoming premium user is must be registered"  |
| Actions           | -Site will prompt user registration if making ratings or reviews is desired by the user  |
|                   | -User will register with email, username, password  |
|                   | -If user desires friends and personalized movie lists, premium registration is prompted  |
|                   | -User will register as a premium user via subscription   |
|                   | -User will have access to friends and personalized movie data lists"  |
| Alternative paths | -User is not required to register as a premium user, yet privilages will be more limited  |
|                   | -User also is not required to register to view movie ratings on the site  |
| Postconditions    | "User will end up as unregistered, regular user, or premium user based on user actions and desires"  |
| Acceptance tests  | "When registering an account, user email must be unique, username must be unique, password must be at least 8 characters. Premium users must submit full subscription prior to becoming premium"  |
| Iteration         | "tbd"  |



| Use case # 2      | Log in/Register  |
| ------------------ |--|
| Name              | "Log in-out / Register"  |
| Users             | "All users"  |
| Rationale         | "All site visitors are able access movie ratings, in order for one to submit their own rating, they must set up an account via register. This will grant the user access to login and logout functions via username, email, and an 8 character password. Registered users have greater access to site options which users may seek"  |
| Triggers          | "The user will select "Register" to register account, afterwards, they will be able to select "login" to login or "logout" to logout of their account"  |
| Preconditions     | "For register, site must be loaded, for login, user must be registered, for logout, user must be logged in"  |
| Actions           | -User will select "register" option
|                   | -User will create an account via email, username, and 8 character password  |
|                   | -Software will register an account into the database  |
|                   | -User will log in via username and password  |
|                   | -User will log out via logout button  |
| Alternative paths | "Users are not obligated to cerate accounts, they may choose to view movie ratings without registering an account, but will have limited site access"  |
| Postconditions    | "User will either end up registered or not, user then will either close the site logged in or out depending on if they select to log out before closing the browser (applies only to registered)"  |
| Acceptance tests  | "Usernames cannot be duplicates in database, emails cannot be duplicates as well, password must have 8 characters. When submitting login request, user information must be checked and correct"  |
| Iteration         | "tbd"  |


| Use case # 3      | Movie Rating  |
| ------------------ |--|
| Name              | "Movie Rating"  |
| Users             | "All registered users"  |
| Rationale         | "Although all movie ratings will be publicly available to view (meaning user does not have to be logged in to site) only registered/logged in users will be able to post their own ratings of movies in the database. This is an incentive of access for the users so people create accounts for the movie rating site itself. This allows for users to publicly state their opinions on the movies they love or hate"  |
| Triggers          | "user select "rate" and select most fitting option to their preferences"  |
| Preconditions     | "User must be logged in, movie must be in the database"  |
| Actions           | -User will select the rate button   |
|                   | -User will select rating based on preferences   |
|                   | -User will submit rating and software will apply rating to movie database  |
| Alternative paths | "User could cancel their rating by exiting the page before submitting, user ratings will also be able to change via profile"  |
| Postconditions    | "User will have submitted a rating to the database and the movie rating will change, personal profile database will be updated"  |
| Acceptance tests  | "Accepting only valid ratings (most likely will be click to rate, so no checks necessary)"  |
| Iteration         | "tbd"  |


| Use case # 4      | Search/Filter  |
| ------------------ |--|
| Name              | "Search/Filter"  |
| Users             | "All users"  |
| Rationale         | "In order to make a site that can be easily accessed by all users, a sort/filter feature needs to be implemented. This feature will allow all users (logged in or not) to break down their search into categories like ratings, mive characteristics, genre, reviews, etc. This will make the site easier to use and allow users to find the information they seek faster"  |
| Triggers          | "User will select "sort by" drop down menu and select desired field to sort by"  |
| Preconditions     | "Site must be loaded and movies/ratings in database"  |
| Actions           | -User will select the drop down menu for sort  |
|                   | -User will select sort field  |
|                   | -Software will display all abiding posts in the parameters of the sort selected  |
| Alternative paths | "User may select multiple sort fields to narrow search (tbd)"  |
| Postconditions    | "Site page will refresh and show movie ratings within the bounds of user search/filter"  |
| Acceptance tests  | "Movies shown after a sort selection has been made must abide by characteristics of the filtering selected"  |
| Iteration         | "tbd"  |


 | Use case # 5      | Profile  |
| ------------------ |--|
| Name              | "Profile"  |
| Users             | "All registered users"  |
| Rationale         | "With the incentive to create an account (register) users will be given their own profile page which will display their perosnal movie ratings. Premium users will have additional fields where friends lists will be displayed, only premium users can be friends with each other. This profile aspect will add individuality to the user which makes the movie rating site have a social aspect as well "  |
| Triggers          | "User will select "profile" option"  |
| Preconditions     | "User must be logged in"  |
| Actions           | -User will select "profile" option
|                   | -Software will load all user data  |
|                   | -User will have access to all profile information |
| Alternative paths | "Some users may not be premium users, these users will have less information in their profile page (no friends list)"  |
| Postconditions    | "User profile will be displayed"  |
| Acceptance tests  | "Make sure correct user information is shown and friends list is only shown for premium users, personal movie ratings should be displayed for all registered users"  |
| Iteration         | "tbd"  | 


----
## 2.3 Non-Functional Requirements

1. User privacy: Other users account information will not be disclosed publicly.

2. Performance: The platform must allow multiple user to access the site at once.

3. Consistency: The platform must show all users (according to account) the same results.

4. Compatibility: Users will be able to access the platform from different browers.

----
# 3. User Interface

![Alt text](<UserInterface.png>)

----
# 4. Product Backlog

Link to your GitHub repo issues page: 
https://github.com/WSU-CptS-322-Fall-2023/termproject-teamquartet/issues.


----
# 4. References


----