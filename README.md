# HiStory Book Store
(Developer: Kamil Wojciechowski)

![Mockup image](docs/responsive.png)

[LIVE WEBPAGE](https://hi-story-book-store-5899052efb65.herokuapp.com/)

## About 

HiStory Book Store - 5th Portfolio Project for Diploma in Full Stack Software Development with Code Institute. E-commerce history book store website built using Django.
Store specialized selling history books where passionates & proffessionals can find their next HiStory to read. 

## Table of Contents

- [HiStory Book Store](#history-book-store)
  - [About](#about)
  - [Table of Contents](#table-of-contents)
  - [Business Model](#business-model)
    - [Purpose of the Application](#purpose-of-the-application)
    - [Core Business Intents](#core-business-intents)
    - [Marketing Strategies](#marketing-strategies)
  - [Marketing Techniques](#marketing-techniques)
    - [Social Media Platform](#social-media-platform)
    - [Newsletter Signup Form](#newsletter-signup-form)
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Business Owner Goals](#business-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
      - [Users](#users)
      - [Site Admin](#site-admin)
    - [Agile Methodologies](#agile-methodologies)
  - [Design](#design)
    - [Design Choices](#design-choices)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
  - [Models Diagrams](#models-diagrams)
  - [Amazon Web Services](#amazon-web-services)
  - [Messages and Interaction with Users](#messages-and-interaction-with-users)
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries \& Frameworks](#libraries--frameworks)
    - [Django Packages](#django-packages)
  - [Features](#features)
  - [Search Engine Optimization](#search-engine-optimization)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [PEP8 Validation](#pep8-validation)
  - [Accessibility](#accessibility)
  - [Performance](#performance)
  - [Device Testing](#device-testing)
  - [Browser compatibility](#browser-compatibility)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Media](#media)
  - [Further Developments](#further-developments)
  - [Acknowledgements](#acknowledgements)

## Business Model

### Purpose of the Application

The business is a B2C e-commerce platform with the main goal of selling tangible product: books listed online on the website.
The store is dedicated to sell history books so the primary customer the business targets are people interested in history, 
but also people who would like to start reading history books or maybe buy them as a gift for someone. 
The business aims at customers who expect high quality of the offered positions, matching the store's theme.
The payment type employed is: SINGLE PAYMENT
The transaction is finished & delivery order is created once a single payment is made. 
The available payment option is payment by card, implemented using <a href="https://stripe.com/ie">Stripe</a>

### Core Business Intents

[Back to Table Of Contents](#table-of-contents)

### Marketing Strategies

The main marketing strategy is a mix of both online & offline marketing. 

The online marketing strategy campaign includes regular short posting on social media platform: Facebook, but also to be carried using the contact emails received via the newsletter form thanks to which regular newsletters can be sent to the subscribes informing them about important events, e.g. sales.

The offline marketing strategy is to engage with the users outside the web via the HiStory Book Club, a non-profit organization working to promote history as a hobby.

The strategy was chosen taking into account the store is a new business with limited budget so it must be done at a relatively low cost. Online marketing via Facebook is to be carried out by a staff member who is responsible for the Facebook page activities. 

Offline marketing is based on a non-profit activities that aim to make the brand present during subject-related events and visible for people who could potentially be looking to buy history books. During the events, the participants will be able to support the activities of the HiStory Club by contributing in a voluntary crowd-funding action to organize future events gathering history enthusiasts.

[Back to Table Of Contents](#table-of-contents)

## Marketing Techniques

### Social Media Platform

HiStory Book Store has its own page on Facebook. 
The content of posts is to address the memory of important history events or figures, often to be related to pieces of culture & pop-culture e.g. movies in historical theme. The goal is to encourage the followers to confront the content of those pieces of culture which picture a history event or figure with the knowledge that can be found in the literature. Sharing links to the blog posts posted on the websites blog. Interacting with the followers in the comments sections under the Facebook posts which would be aimed to drive constructive discussion feeding the algorithm to increase the popularity of the page amongst Facebook users.

<a href="https://www.facebook.com/profile.php?id=61550506871142">Facebook</a>

![social-media-platform](docs/social/page.png)
![social-media-platform](docs/social/post.png)

[Back to Table Of Contents](#table-of-contents)

### Newsletter Signup Form

HiStory Book Store uses Mailchimp to collect email addresses from users who would like to subscribe for store's newsletter. 
It is on purpose very simple, just enough that a user enters email address & click on the subscribe button. 
The newsletter content is to inform about sales or new books added to the store available on website.

![Features](docs/features/newsletter-form.png)

[Back to Table Of Contents](#table-of-contents)

## Project Goals

### User Goals

- Purchase books(related user stories: 3, 4, 5, 8, 9, 10, 11)
- Find books offered for sale (related user stories: 3, 5, 6, 7)
- Get to known the details of books offered for sale (related user stories: 3, 4)
- Find information about the store (related user stories: 14)
- Use own account (related user stories: 1, 2)
- Easily navigate through the website (related user stories: 5, 6, 7, 12)
- Communicate with the website's administration (related user stories: 13)

### Business Owner Goals

- Keep the books offer up to date (related user stories: 15, 16, 17)
- Retain users on the website increasing the chance for sales(related user stories: 18, 20)
- Keep the users engaged to build customers relationship(related user stories: 17)

[Back to Table Of Contents](#table-of-contents)

## User Experience

### Target Audience

- people who are looking to buy history books
- people whose hobby is history
- people who would like to expand their knowledge of history
  
[Back to Table Of Contents](#table-of-contents)

### User Requirements and Expectations

- Accessible and responsive website.
- Intuitive website with a layout allowing to easily navigate through it.
- Easy access to Create, Read, Update & Delete functionalities.
- Links and features that function in accordance with their intended purpose.
- Connection with the community on the social media platforms.
- A contact form to contact the website owner.
- Adding to shopping cart.
- Updating shopping cart.
- Option to register and save delivery details.
- Secure checkout.

[Back to Table Of Contents](#table-of-contents)

### User Stories

- [User Stories on Github Issues](https://github.com/WojtekKamilowski/CI_PP5_HSBS/issues)

#### Users

As a User I want to:

1. Sign up so that I can login with my own account.
2. Login so that I can access my account profile.
3. View books list so that I can see what books the store sales.
4. View book details so that I can check if the book is one that I am looking for.
5. Search for a book so that I can find book I am looking for without checking the entire list.
6. Access categorized catalogue of books so that only books from a required category are displayed.
7. Sort books so that I see books sorted in a required order.
8. Add books to shopping cart so that I can have all books I wish to buy listed together.
9. Update the list of items in my shopping cart so that the correct list is ready for checkout.
10. Remove items from the shopping cart so that the shopping cart matches my final purchase decission.
11. Check-out so that I can finalize the purchase of my items.
12. See the list of all books offered paginated so that I can easier review the offer.
13. Contact site admins so that I can communicate feedback/complaints/suggestions.
14. Read about the website so that I know who offers me the products for sale.

[Back to Table Of Contents](#table-of-contents)

#### Site Admin

As an Admin I want to:

15. Add books to the store offer so that the store can sell online the new books available in the store.
16. Edit book details so that user can see books offered by the store with up to date details.
17. Delete books from the store's offer so that users cannot see books that are no longer available for sale.
18. Set up a custom 404 page so that users can be easily redirected to the books list from a non-existing page, increasing their offer viewing time and the likely-hood of buying a book.
19. Invite users to related non-profit group to engage outside the web so that it helps to build brand and supports the growth of regular customers base.
20. Offer users looking for more content a blog section so that they can access more engaging content related to the potential users' hobbies sot that they can be possibly retained longer on the website increasing the chance of making some extra purchase than originally intended by a user.
21. Collect email addresses from users who want to subscribe for newsletter so that I can use them for informing the subscribers about sales etc

[Back to Table Of Contents](#table-of-contents)

### Agile Methodologies

<a href="https://github.com/users/WojtekKamilowski/projects/4/views/1">Github Project</a>

<a href="https://github.com/WojtekKamilowski/CI_PP5_HSBS/issues">User Stories</a>

<a href="https://github.com/WojtekKamilowski/CI_PP5_HSBS/milestones?state=closed">Epics</a>

![Kanban](docs/agile/epics.png)

<details>
    <summary>Kanban</summary>
    
![Kanban](docs/agile/kanban-1.png)
![Kanban](docs/agile/kanban-2.png)
![Kanban](docs/agile/kanban-3.png)
![Kanban](docs/agile/kanban-4.png)
![Kanban](docs/agile/kanban-5.png)
![Kanban](docs/agile/kanban-6.png)
![Kanban](docs/agile/kanban-7.png)
![Kanban](docs/agile/kanban-8.png)
![Kanban](docs/agile/kanban-9.png)
![Kanban](docs/agile/kanban-10.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Design

### Design Choices

The main design choice was to create an open space feeling website with a contemporary approach towards the users.
The name HiStory was chosen to represent openness, welcoming them to shop on our website by simpy saying 'hi'. The store is dedicated for sales of books store which is why the standard category names were replaced by historical era times.

### Colors

The main chosen color theme is white & purple (#505 & #FAFAFA). Purple color is often considered as a simbol of royalty as historically it used to be very scarce & expensive so only wealthy people of high status could afford it. Roles of kings & emperors are often associated with a general history so the main color pallete aimed to match the store's theme.

- #505 & #FAFAFA from <a href="https://favicon.io/favicon-generator/">Favicon</a>.
<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-1.png)

</details>

- #EEEEFF from <a href="https://www.eggradients.com/shades-of-white">Eggradients</a>.

<details>
    <summary>Contrast</summary>

![Colors](docs/colors/contrast-2.png)

</details>

- #30d5c from <a href="https://www.color-meanings.com/colors-that-go-with-purple/">Color Meanings</a>.

- #FFF642 from <a href="https://coolors.co/contrast-checker/fff642-550055">Coolors</a>.

<details>
    <summary>Contrast</summary>

![Colors](docs/colors/contrast-3.png)

</details>

- #0F3860 <a href="https://coolors.co/contrast-checker/0f3860-ffffff">Coolors</a>.

<details>
    <summary>Contrast</summary>

![Colors](docs/colors/contrast-4.png)

</details>

- #294A08 <a hred="https://coolors.co/contrast-checker/294a08-ffffff">Coolors</a>.

<details>
    <summary>Contrast</summary>

![Colors](docs/colors/contrast-5.png)

</details>

[Back to Table Of Contents](#table-of-contents)

### Fonts

'Lato' - main font with sans-serif as its fallback font.

'Playfair Display' - h1 - h5 font with serif for fallback.

'Lato' font from <a href="https://fonts.google.com/specimen/Lato">Google Fonts</a>
'Playfair Display' font from <a href="https://fonts.google.com/specimen/Playfair+Display?query=playfair">Google Fonts</a>


[Back to Table Of Contents](#table-of-contents)


### Structure

The website consists of seven django applications:

1. home
2. books
3. cart
4. checkout
5. profiles
6. contact
7. blog

The logo is the name of the website placed on the top left corner(desktop only), 
In the central part of the header there is a search input so users can easily start shopping, knowing more/less what they are looking for.
For users who are more interested to view the offer first and see what is available for sale there is a number of ways to view the full, sorted or categorized books list. Such structure is aimed to bring the users as quickly as possible to the offered products increasing the chance of making the purchase. 
User can categorize books list by:
1. Price - lowest or highest. In certain situations it is expected users may want to buy cheaper or more expensive books.
2. Rating - as default they appear from the higher rating as it is expected that users would be less likely to by books with lower ratings.
3. Oldest Times & Newest Times - it is expected that some users may be more interest to buy history books describing newer or older period of history.

[Back to Table Of Contents](#table-of-contents)

### Wireframes

<details>
    <summary>Facebook Page</summary> 

![Wireframes](docs/wireframes/facebook.png)

</details>

<details>
    <summary>Desktop</summary> 

![Wireframes](docs/wireframes/1.a-home-notloggedin-desktop.png)
![Wireframes](docs/wireframes/2.b-home-loggedin-desktop.png)
![Wireframes](docs/wireframes/3.c-home-signup-desktop.png)
![Wireframes](docs/wireframes/4.d-home-email-confirm-desktop.png)
![Wireframes](docs/wireframes/5.e-home-email-confirmed-desktop.png)
![Wireframes](docs/wireframes/6.f-home-signin-desktop.png)
![Wireframes](docs/wireframes/7.g-home-about-desktop.png)
![Wireframes](docs/wireframes/8.h-home-club-desktop.png)
![Wireframes](docs/wireframes/9.i-home-privacy-desktop.png)
![Wireframes](docs/wireframes/10.j-home-delivery-desktop.png)
![Wireframes](docs/wireframes/11.k-books-all-desktop.png)
![Wireframes](docs/wireframes/12.l-books-sorted-desktop.png)
![Wireframes](docs/wireframes/13.m-books-era-desktop.png)
![Wireframes](docs/wireframes/14.n-books-search-desktop.png)
![Wireframes](docs/wireframes/15.o-books-details-desktop.png)
![Wireframes](docs/wireframes/16.p-books-add-desktop.png)
![Wireframes](docs/wireframes/17.r-cart-desktop.png)
![Wireframes](docs/wireframes/18.s-checkout-desktop.png)
![Wireframes](docs/wireframes/19.t-order-desktop.png)
![Wireframes](docs/wireframes/20.u-profile-desktop.png)
![Wireframes](docs/wireframes/21.v-contact-desktop.png)
![Wireframes](docs/wireframes/22.w-blog-desktop.png)
![Wireframes](docs/wireframes/23.x-post-desktop.png)

</details>

[Back to Table Of Contents](#table-of-contents)

<details>
    <summary>Tablet</summary> 

![Wireframes](docs/wireframes/24.y-home-notloggedin-tablet.png)
![Wireframes](docs/wireframes/25.z-home-loggedin-tablet.png)
![Wireframes](docs/wireframes/26.aa-home-signup-tablet.png)
![Wireframes](docs/wireframes/27.bb-home-email-confirm-tablet.png)
![Wireframes](docs/wireframes/28.cc-home-email-confirmed-tablet.png)
![Wireframes](docs/wireframes/29.dd-home-signin-tablet.png)
![Wireframes](docs/wireframes/30.ee-home-about-tablet.png)
![Wireframes](docs/wireframes/31.ff-home-club-tablet.png)
![Wireframes](docs/wireframes/32.gg-home-privacy-tablet.png)
![Wireframes](docs/wireframes/33.hh-home-delivery-tablet.png)
![Wireframes](docs/wireframes/34.ii-books-all-tablet.png)
![Wireframes](docs/wireframes/35.jj-books-sorted-tablet.png)
![Wireframes](docs/wireframes/36.kk-books-era-tablet.png)
![Wireframes](docs/wireframes/37.ll-books-search-tablet.png)
![Wireframes](docs/wireframes/38.mm-books-details-tablet.png)
![Wireframes](docs/wireframes/39.nn-books-add-tablet.png)
![Wireframes](docs/wireframes/40.oo-cart-tablet.png)
![Wireframes](docs/wireframes/41.pp-checkout-tablet.png)
![Wireframes](docs/wireframes/42.rr-order-tablet.png)
![Wireframes](docs/wireframes/43.ss-profile-tablet.png)
![Wireframes](docs/wireframes/44.tt-contact-tablet.png)
![Wireframes](docs/wireframes/45.uu-blog-tablet.png)
![Wireframes](docs/wireframes/46.vv-post-tablet.png)

</details>

[Back to Table Of Contents](#table-of-contents)

<details>
    <summary>Mobile</summary> 

![Wireframes](docs/wireframes/47.ww-home-notloggedin-mobile.png)
![Wireframes](docs/wireframes/48.xx-home-loggedin-mobile.png)
![Wireframes](docs/wireframes/49.yy-home-signup-mobile.png)
![Wireframes](docs/wireframes/50.zz-home-email-confirm-mobile.png)
![Wireframes](docs/wireframes/51.aaa-home-email-confirmed-mobile.png)
![Wireframes](docs/wireframes/52.bbb-home-signin-mobile.png)
![Wireframes](docs/wireframes/53.ccc-home-about-mobile.png)
![Wireframes](docs/wireframes/54.ddd-home-club-mobile.png)
![Wireframes](docs/wireframes/55.eee-home-privacy-mobile.png)
![Wireframes](docs/wireframes/56.ffff-home-delivery-mobile.png)
![Wireframes](docs/wireframes/57.ggg-books-all-mobile.png)
![Wireframes](docs/wireframes/58.hhh-books-sorted-mobile.png)
![Wireframes](docs/wireframes/59.iii-books-era-mobile.png)
![Wireframes](docs/wireframes/60.jjj-books-search-mobile.png)
![Wireframes](docs/wireframes/61.kkk-books-details-mobile.png)
![Wireframes](docs/wireframes/62.lll-books-add-mobile.png)
![Wireframes](docs/wireframes/63.mmm-cart-mobile.png)
![Wireframes](docs/wireframes/64.nnn-checkout-mobile.png)
![Wireframes](docs/wireframes/65.ooo-order-mobile.png)
![Wireframes](docs/wireframes/66.ppp-profile-mobile.png)
![Wireframes](docs/wireframes/67.rrr-contact-mobile.png)
![Wireframes](docs/wireframes/68.sss-blog-mobile.png)
![Wireframes](docs/wireframes/69.ttt-post-mobile.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Models Diagrams

<details>
    <summary>Books</summary> 

Diagram:
![Diagrams](docs/models/books-models-diagram.png)

Implemented models as per diagram:
![Diagrams](docs/models/books-models.png)

</details>

<details>
    <summary>Checkout</summary>

Diagram:
![Diagrams](docs/models/checkout-models-diagram.png)

Implemented models as per diagram:
![Diagrams](docs/models/checkout-models-1.png)
![Diagrams](docs/models/checkout-models-2.png)

</details>

<details>
    <summary>Profiles</summary>

Diagram:
![Diagrams](docs/models/profiles-models-diagram.png)

Implemented models as per diagram:
![Diagrams](docs/models/profiles-models.png)

</details>

<details>
    <summary>Contact</summary>

Diagram:
![Diagrams](docs/models/contact-models-diagram.png)

Implemented models as per diagram:
![Diagrams](docs/models/contact-models.png)

</details>

<details>
    <summary>Blog</summary>

Diagram:
![Diagrams](docs/models/blog-models-diagram.png)

Implemented models as per diagram:
![Diagrams](docs/models/blog-models-1.png)
![Diagrams](docs/models/blog-models-2.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Amazon Web Services

AWS in use for hosting media & static files in a S3 Bucket created for this project.

![Amazon](docs/aws.png)

[Back to Table Of Contents](#table-of-contents)

## Messages and Interaction with Users

Implemented using toast, for success toast there is data-delay="30000" attribute set for a considerable time for the user to have enough time to read the message especially when it is in relation to adding books to the shopping cart.

<details>
    <summary>Messages updating the user on interactions status.</summary> 

- Sign up: confirmation e-mail sent
![Messages and Interaction With Users](docs/messages/confirmation-sent.png)

- Sign up: e-mail confirmed
![Messages and Interaction With Users](docs/messages/email-confirmed.png)

- Sign in
![Messages and Interaction With Users](docs/messages/signin.png)

- Sign Out
![Messages and Interaction With Users](docs/messages/signout.png)

- Newsletter
![Messages and Interaction With Users](docs/messages/newsletter.png)

- Add a book to the shopping cart
![Messages and Interaction With Users](docs/messages/book-added.png)

- Standard user attempting to access books management options
![Messages and Interaction With Users](docs/messages/restricted.png)

- Add a a new book to the offer
![Messages and Interaction With Users](docs/messages/new-book.png)

- Commence editting book details
![Messages and Interaction With Users](docs/messages/edit-book.png)

- Update book details
![Messages and Interaction With Users](docs/messages/update-book.png)

- Delete book from the offer
![Messages and Interaction With Users](docs/messages/delete-book.png)

- Update the shopping cart
![Messages and Interaction With Users](docs/messages/book-update.png)

- Remove a book from the shopping cart
![Messages and Interaction With Users](docs/messages/book-removed.png)

- Order processed successfully
![Messages and Interaction With Users](docs/messages/order.png)

- Previous order confirmation from profile's order history
![Messages and Interaction With Users](docs/messages/previous-order.png)

- Profil updated
![Messages and Interaction With Users](docs/messages/profile-update.png)

- Contact form submitted
![Messages and Interaction With Users](docs/messages/contact.png)

- Comment a blog post
![Messages and Interaction With Users](docs/messages/comment.png)

- Post like
![Messages and Interaction With Users](docs/messages/like.png)

- Post unlike
![Messages and Interaction With Users](docs/messages/unlike.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Admin Panel/Superuser

Django administration in use.

![Admin Panel/Superuser](docs/admin.png)

[Back to Table Of Contents](#table-of-contents)

## Technologies Used

- [GitHub](https://github.com/)
- [Codeanywhere](https://app.codeanywhere.com/)
- [Heroku](https://id.heroku.com/)
- [Lucidchart](https://lucid.app/)
- [Favicon](https://favicon.io/favicon-generator/)
- [Fontawesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/?fbclid=IwAR0M5mybiiO6URy8GMzAKIYHRdX_lQHlJhwcmI6h-bNFuL90-osnCNZaC8Q)
- [Balsamiq](https://balsamiq.com/)
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [TinyPNG](https://tinypng.com/)
- [jQuery](https://jquery.com/)
- [WAVE](https://wave.webaim.org/)
- [TechSini](https://techsini.com/multi-mockup/index.php)
- [Ignore X-Frame headers](https://chrome.google.com/webstore/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe/related)
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/download.php?lang=en&token=jIR86oYCsiIVTzYSP6sF8FlsimURJVCo#)
- [Stripe](https://stripe.com/ie)
- [ElephantSQL](https://customer.elephantsql.com/)
- [XML-Sitemaps](https://www.xml-sitemaps.com/)

[Back to Table Of Contents](#table-of-contents)

### Languages

- HTML5
- CSS3
- JavaScript
- Python

[Back to Table Of Contents](#table-of-contents)

### Libraries & Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

[Back to Table Of Contents](#table-of-contents)

### Django Packages

- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Summernote](https://summernote.org/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [django-storages](https://django-storages.readthedocs.io/en/latest/)
- [django-countries](https://pypi.org/project/django-countries/)
- [django-phonenumber-field](https://django-phonenumber-field.readthedocs.io/en/latest/)*
  *Used for updating phone_number model in checkout.models.py, migrations made & migrated during tests & changed back to CharField to better suit the project needs.


[Back to Table Of Contents](#table-of-contents)

## Features

<details>

<summary>Header</summary>

It is included on all pages. Contains: website name that is clickable link to Home page which is a common feature on many websites so users expect it.
There is search queries form, navigation bar, user profile & shopping cart icons.
Header is responsive: For medium & smaller screens navigation items are displayed from a drop-down burger menu where a Home link also appears to assist users navigating to the home page in a more ergonomic way than only using the link from the logo, a useful addition when browsing the website on tablet or mobile screens.
The extra home link from the is especially helpful for mobile screen users as the search queries form dropdowns from the search icon for medium & smaller than devices, on mobile screens the website logo is covered when the form is droppedown from the icon.

Search queries form is displayed after clicking the magnifying glass icon & the Authentication icon has shorter under-description.
User stories covered: 1, 2, 3, 5, 6, 7.

![Features](docs/features/header.png)

</details>


<details>

<summary>Footer</summary>

It is included on all pages. It is divided in sections: About Us, Check Our Profiles on, Explore Our Website & Contact.
About Us included links to Who We Are & HiStory Club pages.
Check Our Profiles on with links to Pinterest, YouTube & Facebook.
Explore Our Website links to Books & Blog.
Contact with contact details and link to the contact page.
Footer is responsive: the sections are displayed verticaly for mobile screens.
User stories covered: 13, 14, 19, 20.

![Features](docs/features/footer.png)

</details>

<details>

<summary>Newsletter Signup Form</summary>

It is included on the home page.
Collects email addresses from users who want to subscribe for Newsletter.
It is responsive.
User stories covered: 21. 

![Features](docs/features/newsletter-form.png)
![Features](docs/features/subscribed.png)

</details>


<details>

<summary>Authentication</summary>

From Allauth.
Includes customised signup, signin, email confirmation & password reset pages that display on dektop, laptop, tablet & mobile screens as intended. 
User stories covered: 1, 2, 15.

![Features](docs/features/signup.png)
![Features](docs/features/signin.png)
![Features](docs/features/email.png)
![Features](docs/features/password.png)

</details>

<details>

<summary>About</summary>

Included on the about.html
Describes the history of the founding of the store, convincing users why to shop from the store & includes a link to HiStory Club.
Displays on dektop, laptop, tablet & mobile screens as intended.
User stories covered: 14.

![Features](docs/features/about.png)

</details>

<details>

<summary>HiStory Club</summary>

Included on the club page. 
Describes the non-profit organization managed by the store owners & inviting users to join it by expressing their interest via the contact page.
Displays on dektop, laptop, tablet & mobile screens as intended.
User stories covered: 19.

![Features](docs/features/club.png)

</details>

<details>

<summary>Books</summary>

Implemented in the books application.
Displays a paginated All Books list. Allows users to search, sort & categorize by era the list of books.
Includes page with book details for each offered position. 
Site admins access books management section to add, delete & update the offered books on the store.
Feature is responsive & displays on dektop, laptop, tablet & mobile screens.
User stories covered: 3, 4, 5, 6, 7, 8, 12, 16, 17.

![Features](docs/features/all-books.png)
![Features](docs/features/book-details.png)
![Features](docs/features/cat-books.png)
![Features](docs/features/sort-books.png)
![Features](docs/features/search-books.png)
![Features](docs/features/books-add.png)
![Features](docs/features/books-edit.png)
![Features](docs/features/books-delete.png)

</details>

<details>

<summary>Cart</summary>

Implemented in the cart application.
Shows list of items added to the shopping cart with all details to be reviews before checkout(price, quanitity etc.).
Feature is responsive & displays on dektop, laptop, tablet & mobile screens. on mobile screens the books image is hidden.
User stories covered: 8, 9, 10.

![Features](docs/features/cart.png)

</details>

<details>

<summary>Checkout</summary>

Part of the checkout application.
Includes a form to collect delivery details and payment section built using <a href="https://stripe.com/ie">Stripe</a>.
There are <a href="https://stripe.com/docs/webhooks">Stripe Webhooks</a> in place. Order confirmation email are sent to the user after completing the checkout process.
Feature is responsive & displays on dektop, laptop, tablet & mobile screens. 
User stories covered: 11.

![Features](docs/features/checkout.png)
![Features](docs/features/order.png)
![Features](docs/features/order-email.png)
![Features](docs/features/webhook.png)

</details>

<details>

<summary>Profile</summary>

Implemented in the profiles application.
Includes a form to collect default delivery details and a table with order history.
Feature is responsive & displays on dektop, laptop, tablet & mobile screens. 
User stories covered: 2.

![Features](docs/features/profile.png)

</details>

<details>

<summary>Contact</summary>

Implemented in the contact application.
Includes a form to collect name, email & contact message from the contacting user.
Feature is responsive & displays on dektop, laptop, tablet & mobile screens. 
User stories covered: 13.

![Features](docs/features/contact.png)
![Features](docs/features/contact-sent.png)
![Features](docs/features/contact-received.png)

</details>

<details>

<summary>Blog</summary>

Implemented in the blog application.
Contains a list of blog posts published by the site admins, where users can add comments & likes.
Users are informed that cannot edit or delete comments without contactig the admins: please see [Further Developments](#further-development)
Feature is responsive & displays on dektop, laptop, tablet & mobile screens. 
User stories covered: 20.

![Features](docs/features/blog.png)
![Features](docs/features/post.png)

</details>

<details>

<summary>Customised 404 page</summary>

Code on the 404.html page
Contains error message displayed on a yellow colour background instantly informing user something is not right.
To maximise possibility of sales there is FIND YOUR BOOK NOW button linking to all books list
Feature is responsive & displays on dektop, laptop, tablet & mobile screens. 
User stories covered: 18.

![Features](docs/features/404.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Search Engine Optimization

All pages on the site can be reached by a link from another findable page.
Meta tags included for SEO:
![SEO](docs/meta.png)
Site title:
![SEO](docs/title.png)
Links relationships defined:
![SEO](docs/nofollow.png)

To allow search engine bot crawling there is sitemap.xml included & robots.txt file to control search engine bot crawling.
robots.txt dissallow to crawl /accounts/, /profile/, /cart/ & /checkout/ urls. As per <a href="https://tillison.co.uk/blog/robots-txt-for-ecommerce/#:~:text=Furthermore%2C%20eCommerce%20websites%20may%20have,helping%20to%20protect%20customer%20information.">Tillison Consulting</a> these are some of the most popular directives for eCommerce websites. These URLs may contain sensitive information that should not be publicly accessible.

## Validation

### HTML Validation

To validate HTML of the website<a href="https://validator.w3.org/?fbclid=IwAR37NqVmxg37_tfuFOF4BJoyH8h_H-2n-Ed-64KJpoP1nEgLduNPO227mvE">the W3C Markup Validation Service</a> was used.

<details>
    <summary>Home</summary>

![HTML Validation](docs/validation/html/home.png)
![HTML Validation](docs/validation/html/html-about.png)
![HTML Validation](docs/validation/html/html-club.png)
![HTML Validation](docs/validation/html/html-delivery.png)

Example of warnings removed:
*2 warnings removed as per Rocketvalidator regardning type attribute on mailchimp scripts:
![HTML Validation](docs/validation/html/type-warning.png)
*Dedicated h1 logo for medium screens was removed & small logo h1 was replaced by one mobile h1 logo for both small & medium screens to remove below h1 warning:
![HTML Validation](docs/validation/html/h1-warning.png)

</details>

<details>
    <summary>Books</summary>

![HTML Validation](docs/validation/html/html-books.png)
![HTML Validation](docs/validation/html/html-sort.png)
![HTML Validation](docs/validation/html/html-search.png)
![HTML Validation](docs/validation/html/html-category.png)
![HTML Validation](docs/validation/html/html-details.png)
![HTML Validation](docs/validation/html/html-add.png)
![HTML Validation](docs/validation/html/html-edit.png)
![HTML Validation](docs/validation/html/html-delete.png)

</details>

<details>
    <summary>Cart</summary>

![HTML Validation](docs/validation/html/html-cart.png)

</details>

<details>
    <summary>Checkout</summary>

![HTML Validation](docs/validation/html/html-checkout.png)
![HTML Validation](docs/validation/html/html-order.png)

</details>

<details>
    <summary>Profiles</summary>

![HTML Validation](docs/validation/html/html-profile.png)
![HTML Validation](docs/validation/html/signup.png)
![HTML Validation](docs/validation/html/login.png)

</details>

<details>
    <summary>Blog</summary>

![HTML Validation](docs/validation/html/html-blog.png)
![HTML Validation](docs/validation/html/html-blog-2.png)
![HTML Validation](docs/validation/html/html-post.png)

</details>

<details>
    <summary>Contact</summary>
    
![HTML Validation](docs/validation/html/html-contact.png)

</details>

[Back to Table Of Contents](#table-of-contents)

### CSS Validation

To validate style.css <a href="https://jigsaw.w3.org/css-validator/?fbclid=IwAR2zBUIZHTXAGa9KEvR__gsTkB05ZifTcd-us-pR0Kud0bLVaIPET-V-Hi4#validate_by_upload">the W3C Jigsaw CSS Validation Service</a> was used.

<details>
    <summary>CSS Validation</summary>

![CSS Validation](docs/validation/css/base.png)

</details>

[Back to Table Of Contents](#table-of-contents)

### JavaScript Validation

<a href="https://jshint.com/">JSHint</a> JS Validation Serviced was used to validate the Javascript code for the website.

<details>
    <summary>cart_script</summary>

One undefined variable message appears for jQuery $ sign:
![JavaScript Validation](docs/validation/js/cart-script.png)

</details>

<details>
    <summary>Mailchimp script</summary>

The array literal notation [] is preferable two warnings. Three undefined variables & one unused variable messages.
![JavaScript Validation](docs/validation/js/mailchimp-script.png)
Warnings removed:
![JavaScript Validation](docs/validation/js/mailchimp-script-fixed.png)

</details>

<details>
    <summary>Back to Top</summary>

One undefined variable message appears for jQuery $ sign:
![JavaScript Validation](docs/validation/js/top-script.png)

</details>

<details>
    <summary>quantity_input_script</summary>

One undefined variable message appears for jQuery $ sign:
![JavaScript Validation](docs/validation/js/quantity-script.png)

</details>

<details>
    <summary>stripe_elements</summary>

![JavaScript Validation](docs/validation/js/stripe.png)

</details>

### PEP8 Validation

<a href="https://pep8ci.herokuapp.com">CI Python Linter</a> was used to perform the PEP8 requirements validation:

<details>
    <summary>HSBS</summary>

- asgi.py
![PEP8 Validation](docs/validation/pep8/hsbs-asgi.png)
- settings.py
![PEP8 Validation](docs/validation/pep8/hsbs-settings.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/hsbs-urls.png)
- wsgi.py
![PEP8 Validation](docs/validation/pep8/hsbs-wsgi.png)

</details>

<details>
    <summary>Home</summary>

- apps.py
![PEP8 Validation](docs/validation/pep8/home-apps.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/home-urls.png)
- views.py
![PEP8 Validation](docs/validation/pep8/home-views.png)

</details>

<details>
    <summary>Books</summary>

- admin.py
![PEP8 Validation](docs/validation/pep8/books-admin.png)
 forms.py
![PEP8 Validation](docs/validation/pep8/books-forms.png)
- apps.py
![PEP8 Validation](docs/validation/pep8/books-apps.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/books-urls.png)
- views.py
![PEP8 Validation](docs/validation/pep8/books-views.png)
- models.py
![PEP8 Validation](docs/validation/pep8/books-models.png)

</details>

<details>
    <summary>Cart</summary>

- cart_tools.py
![PEP8 Validation](docs/validation/pep8/cart-tools.png)
- apps.py
![PEP8 Validation](docs/validation/pep8/cart-apps.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/cart-urls.png)
- views.py
![PEP8 Validation](docs/validation/pep8/cart-views.png)
- contexts.py
![PEP8 Validation](docs/validation/pep8/cart-contexts.png)

</details>

<details>
    <summary>Checkout</summary>

- apps.py
![PEP8 Validation](docs/validation/pep8/checkout-apps.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/checkout-urls.png)
- views.py
![PEP8 Validation](docs/validation/pep8/checkout-views.png)
- admin.py
![PEP8 Validation](docs/validation/pep8/checkout-admin.png)
- forms.py
![PEP8 Validation](docs/validation/pep8/checkout-forms.png)
- models.py
![PEP8 Validation](docs/validation/pep8/checkout-models.png)
- signals.py
![PEP8 Validation](docs/validation/pep8/checkout-signals.png)
- views.py
![PEP8 Validation](docs/validation/pep8/checkout-views.png)
- webhook_handler.py
![PEP8 Validation](docs/validation/pep8/checkout-handler.png)
- webhooks.py
![PEP8 Validation](docs/validation/pep8/checkout-webhooks.png)

</details>

<details>
    <summary>Profiles</summary>

- apps.py
![PEP8 Validation](docs/validation/pep8/profiles-apps.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/profiles-urls.png)
- views.py
![PEP8 Validation](docs/validation/pep8/profiles-views.png)
- forms.py
![PEP8 Validation](docs/validation/pep8/profiles-forms.png)
- models.py
![PEP8 Validation](docs/validation/pep8/profiles-models.png)

</details>

<details>
    <summary>Contact</summary>

- apps.py
![PEP8 Validation](docs/validation/pep8/contact-apps.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/contact-urls.png)
- views.py
![PEP8 Validation](docs/validation/pep8/contact-views.png)
- admin.py
![PEP8 Validation](docs/validation/pep8/contact-admin.png)
- forms.py
![PEP8 Validation](docs/validation/pep8/contact-forms.png)
- models.py
![PEP8 Validation](docs/validation/pep8/contact-models.png)

</details>

<details>
    <summary>Blog</summary>

- apps.py
![PEP8 Validation](docs/validation/pep8/blog-apps.png)
- urls.py
![PEP8 Validation](docs/validation/pep8/blog-urls.png)
- views.py
![PEP8 Validation](docs/validation/pep8/blog-views.png)
- admin.py
![PEP8 Validation](docs/validation/pep8/blog-admin.png)
- forms.py
![PEP8 Validation](docs/validation/pep8/blog-admin.png)
- models.py
![PEP8 Validation](docs/validation/pep8/blog-models.png)

</details>

<details>
    <summary>root</summary>

- custom_storages.py
![PEP8 Validation](docs/validation/pep8/custom-storages.png)
- manage.py
![PEP8 Validation](docs/validation/pep8/manage.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Accessibility

<details>
    <summary>WAVE</summary> 

![Accessibility](docs/accessibility/wave-home.png)
![Accessibility](docs/accessibility/wave-login.png)
![Accessibility](docs/accessibility/wave-signup.png)
![Accessibility](docs/accessibility/wave-about.png)
![Accessibility](docs/accessibility/wave-club.png)
![Accessibility](docs/accessibility/wave-post.png)
![Accessibility](docs/accessibility/wave-contact.png)
![Accessibility](docs/accessibility/wave-privacy.png)
![Accessibility](docs/accessibility/wave-delivery.png)
![Accessibility](docs/accessibility/wave-reset.png)
![Accessibility](docs/accessibility/wave-profile.png)
![Accessibility](docs/accessibility/wave-order.png)
![Accessibility](docs/accessibility/wave-message.png)
![Accessibility](docs/accessibility/wave-new-book.png)
![Accessibility](docs/accessibility/wave-edit.png)
Alerts on the above relate to underlines of links which is design choice for this project.
![Accessibility](docs/accessibility/wave-all-books.png)
![Accessibility](docs/accessibility/wave-all-books-alert.png)
Alerts on the above relate to:
1. Reduntant links for page navigation buttons, design choice to help navigate when there is more pages.
2. Possible heading for the price paragraphs, design choice to highlight important for users information. It alignes with the business strategy as the store wants to highlight the value as an indicator of the quality. 
![Accessibility](docs/accessibility/wave-books-category.png)
![Accessibility](docs/accessibility/wave-books-search.png)
![Accessibility](docs/accessibility/wave-book-details.png)
Alerts on the above relate to underlines of links & possible heading for the price paragraphs, design choice.
![Accessibility](docs/accessibility/wave-cart.png)
![Accessibility](docs/accessibility/wave-blog.png)
Alerts on the above relate to underlines of links & skipped heading level, which are part of the chosen design.
![Accessibility](docs/accessibility/wave-checkout.png)
Alerts on the above relate to:
1. Underlines of links which is a part of the chosen design.
2. Form control does not have a lable, aria-labels added in forms.py

</details>

[Back to Table Of Contents](#table-of-contents)

## Performance

<details>
    <summary>Desktop</summary> 

- home
![Performance](docs/performance/home-desktop.png)
- about
![Performance](docs/performance/about-desktop.png)
- club
![Performance](docs/performance/club-desktop.png)
- books
![Performance](docs/performance/books-desktop.png)
- book details
![Performance](docs/performance/details-desktop.png)
- cart
There is no 100 score for the SEO as it detects update-link as no crawlable, it is only an a tag to update the cart not a link to a different page.
Cart pages are disallowed for crawling in robots.txt
![Performance](docs/performance/cart-desktop.png)
![Performance](docs/performance/cart-seo.png)
- checkout
![Performance](docs/performance/checkout-desktop.png)
- profiles
![Performance](docs/performance/profiles-desktop.png)
- contact
![Performance](docs/performance/contact-desktop.png)
- blog
![Performance](docs/performance/blog-desktop.png)
- post
![Performance](docs/performance/post-desktop.png)
![Performance](docs/performance/post-seo.png)
There is no 100 score for the SEO as it detects the arrow-up as no crawlable, it is only an a tag to for back to the top, not a link to a different page.

</details>

<details>
    <summary>Mobile</summary> 

- home
![Performance](docs/performance/home-mobile.png)
- about
![Performance](docs/performance/about-mobile.png)
- club
![Performance](docs/performance/club-mobile.png)
- books
![Performance](docs/performance/books-mobile.png)
- book details
![Performance](docs/performance/details-mobile.png)
- cart
There is no 100 score for the SEO as it detects update-link as no crawlable, it is only an a tag to update the cart not a link to a different page.
Cart pages are disallowed for crawling in robots.txt
![Performance](docs/performance/cart-mobile.png)
![Performance](docs/performance/cart-seo.png)
- checkout
![Performance](docs/performance/checkout-mobile.png)
- profiles
![Performance](docs/performance/profiles-mobile.png)
- contact
![Performance](docs/performance/contact-mobile.png)
- blog
![Performance](docs/performance/blog-mobile.png)
- post
![Performance](docs/performance/post-mobile.png)
![Performance](docs/performance/post-seo.png)
There is no 100 score for the SEO as it detects the arrow-up as no crawlable, it is only an a tag to for back to the top, not a link to a different page.

</details>

## Device Testing

List of devices used to test the website:

- HP Pavilion 14
- Acer Nitro 5 without and with an external monitor (HP V22)
- Sony Xperia L2
- Motorola Moto G20

The website was also tested using Google Chrome Developer Tools, Toggle Device Toolbar simulating view from a few different listed devices, including popular amongst users iPad and iPhone 5.

[Back to Table Of Contents](#table-of-contents)

## Browser compatibility

Following browsers were used to test the website:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge

[Back to Table Of Contents](#table-of-contents)

## Testing

### Manual Testing

<details>

<summary>Manual Testing</summary>

---------------------------------------------------------------

Testing user stories:

1. As a User I want to sign up so that I can login with my own account.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Header | Click on Authentication icon, select Register option from the drop-down menu  | The sign up page is loaded | Works as expected |
| Authentication | Fill up the sign up form, click the sign up button, go to your e-mail inbox, click on the link from the email message, click on the confirm button | Success message is displayed: You have confirmed emailaddress@email.com & the sign in page is loaded | Works as expected |

![Manual Testing](docs/testing/manual/1.png)

2. As a User I want to login so that I can access my account profile.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Header | Click on Authentication icon, select Login option from the drop-down menu  | The sign in page is loaded | Works as expected |
| Authentication | Fill up the sign in form, click the sign in button | Success message is displayed: Successfully signed in as username, the home page is loaded, there is 'My Profile' under the authenitcation icon & Logged-in as: username info displayed  | Works as expected |

![Manual Testing](docs/testing/manual/2.png)

3. As a User I want to view books list so that I can see what books the store sales.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Header | Click on All Books link, select All Books option from the drop-down menu | The books page is loaded | Works as expected |
| Books | Scroll through the page | Books List is displayed | Works as expected |

![Manual Testing](docs/testing/manual/3.png)

4. As a User I want to view book details so that I can check if the book is one that I am looking for.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Books | From Books page click on book's the name/author&publication date paragraph or book's image | Book details page is loaded and full details including book's description displayed | Works as expected |

![Manual Testing](docs/testing/manual/4.png)

5. As a User I want to search for a book so that I can find book I am looking for without checking the entire list

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Header | Fill out the search our site input with desired search query related to the book the user is looking for, click on the magnifying glass icon | Books page is loaded with found results | Works as expected  |
| Books | Scroll through the search results if any found or continue search using other words | User informed how many books found for the search query & list of related books is displayed if any found | Works as expected |

![Manual Testing](docs/testing/manual/5-a.png)
![Manual Testing](docs/testing/manual/5-b.png)

6. As a User I want to access categorized catalogue of books so that only books from a required category are displayed.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Header | Click on any of the eras' links as desired | Era page is loaded | Works as expected |
| Books | View books from to the selected era | Era name is displayed & the list of books match it | Works as expected  |

![Manual Testing](docs/testing/manual/6.png)

7. As a User I want to sort books so that I see books sorted in a required order.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Header | Click on All Books link, select one of the options, excluding All Books from the drop-down menu | The books page is loaded | Works as expected |
| Books | Scroll through the page | Books List is displayed in an order corresponding to the selected option | Works as expected |

Oldest to newest times example:
![Manual Testing](docs/testing/manual/7.png)

8. As a User I want to add books to shopping cart so that I can have all books I wish to buy listed together.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Books | On a book details page adjust quantity as desired & click on the ADD TO SHOPPING CART button | Success message appears: 'Added book.name to your shopping cart' & a summary of the shopping cart items is displayed with a link to the shopping cart underneath | Works as expected |
| Cart | Load the cart page, for example using the trolley icon button or link from the success message items summary | Page is loaded with a list of items & their details added to the shopping cart & Shopping Cart summary  | Works as expected |

![Manual Testing](docs/testing/manual/8-a.png)
![Manual Testing](docs/testing/manual/8-b.png)

9. As a User I want to update the list of items in my shopping cart so that the correct list is ready for checkout.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Cart | Review & adjust items quantities using the minus or plus or quantity input then click 'Update' | A success message appears with updated summary | Works as expected |

![Manual Testing](docs/testing/manual/9.png)

10. As a User I want to remove items from the shopping cart so that the shopping cart matches my final purchase decission.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Cart | Review & adjust items quantities using the quantity input set to 0 or click 'Remove' | A success message appears with updated summary | Works as expected |

![Manual Testing](docs/testing/manual/10.png)

11. As a User I want to check-out so that I can finalize the purchase of my items.
    
| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Checkout | Open the checkout page by clicking 'SECURE CHECKOUT' button, fill up the form, review order summary, click on the Complete Order button | Loading spinner is displayed when the action is being processed, checkout success page is loaded with the order summary, user receives email with the confirmation email as informed | Works as expected |

![Manual Testing](docs/testing/manual/11-a.png)
![Manual Testing](docs/testing/manual/11-b.png)

12. As a User I want to see the list of all books offered paginated so that I can easier review the offer

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Books | Open Home All Books page scroll to the very bottom navigate through different pages | Chosen pages are loaded after clicking, page number is correctly displayed | Works as expected |

![Manual Testing](docs/testing/manual/12-a.png)
![Manual Testing](docs/testing/manual/12-b.png)

13. As a User I want to contact site admins so that I can communicate feedback/complaints/suggestions.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Footer | From the Contact section in the footer click on the link: 'Contact us using our form' | Contact page with a contact form is loaded, if user is logged in, fields: Name & Email are pre-populated | Works as expected |
| Contact | fill up the form & click on the submit your message button | Page with confirmation is loaded, success message is displayed | Works as expected |

![Manual Testing](docs/testing/manual/13.png)

14. As a User I want to read about the website so that I know who offers me the products for sale.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Footer | From the About Us section in the footer click on the link: 'Who We Are' | the about page is loaded | Works as expected |
| About | Read the information if the user wants to know some extra information about other activity related to the business click on the 'more here' link to navigate to HiStory Club page | User can read the text, the link to HiStory Club page works | Works as expected |

![Manual Testing](docs/testing/manual/14.png)

15. As an Admin I want to add books to the store offer so that the store can sell online the new books available in the store.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Authentication | Using a superuser account sign up via the sign up page. Click on the My Profile icon and choose 'Add New Book' option from the dropdown menu, fill up and submit the form | A new book with the details from the submitted form is added, its book details page loads & a success message is displayed | Works as expected |

![Manual Testing](docs/testing/manual/15.png)

16. As an Admin I want to edit book details so that user can see books offered by the store with up to date details.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Books | Logged in as a superuser from the books or book details page click on the Edit link, apply changes to the form as required & click 'Update Book Details' | Book details are updated as editted, the book details page is loaded with the new details & a success message appears | Works as expected |

![Manual Testing](docs/testing/manual/16-a.png)
![Manual Testing](docs/testing/manual/16.png)

17. As an Admin I want to delete books from the store's offer so that users cannot see books that are no longer available for sale.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Books | From the books or book details page click Delete & confirm deleting by clicking on 'Confirm & Return to Books List' button | The chosen book is deleted from the store's offer & a success message informs that the book has been deleted | Works as expected |


![Manual Testing](docs/testing/manual/17.png)

18. As an Admin I want to set up a custom 404 page so that users can be easily redirected to the books list from a non-existing page, increasing their offer viewing time and the likely-hood of buying a book.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Customised 404 page | After the website urls add anything that is not a findable page e.g. '/aaa' | 404 error is informed to the user, explaining that the page was not found. FIND YOUR BOOK NOW button is displayed that links to All Books page | Works as expected |

![Manual Testing](docs/testing/manual/18.png)

19. As an Admin I want to invite users to related non-profit group to engage outside the web so that it helps to build brand and supports the growth of regular customers base.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Footer | From the About Us section in the footer click on the link: 'HiStory Club' | the club page is loaded | Works as expected |
| HiStory Club | Read the content, if a user decides that would like to join the voluneer organization may click on 'our contact form' link | Information are displayed, the link to the contact page works | Works as expected |

![Manual Testing](docs/testing/manual/19.png)

20. As an Admin I want to offer users looking for more content a blog section so that they can access more engaging content related to the potential users' hobbies sot that they can be possibly retained longer on the website increasing the chance of making some extra purchase than originally intended by a user.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Footer | From the Explore Our Website section in the footer click on the link: 'Blog' | the blog page is loaded | Works as expected |
| Blog | Click on one of the blog posts, read the content, add a like if user wants or undo if changed user's mind. Add a comment if user wants | the post detail page is loaded, conten is readible, like is added on the first click & removed on the following click with corresponding success messages. Comment is added to the blog post & a success message appears | Works as expected |

![Manual Testing](docs/testing/manual/20-a.png)
![Manual Testing](docs/testing/manual/20-b.png)
![Manual Testing](docs/testing/manual/20-c.png)
![Manual Testing](docs/testing/manual/20-d.png)
![Manual Testing](docs/testing/manual/20-e.png)

21. As an Admin I want to collect email addresses from users who want to subscribe for newsletter so that I can use them for informing the subscribers about sales etc

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Newsletter Signup Form | On the home page add email address to the input of the Subscribe for Newsletter form & click on the subscribe button |
Mailchinmp's Thank you for subscribing! response appears & the email address is added to Mailchimp's all contacts audience list | Works as expected |

![Manual Testing](docs/testing/manual/21-a.png)
![Manual Testing](docs/testing/manual/21-b.png)
![Manual Testing](docs/testing/manual/21-c.png)


Python & JavaScript tested manually.

1. Add New Book Form:
![Manual Testing](docs/testing/manual/books-form.png)
2. Back to the Top Arrow:
![Manual Testing](docs/testing/manual/arrow.png)
*clicked
![Manual Testing](docs/testing/manual/arrow-up.png)
3. Quantity Input from Book Details & Cart
*'-' sign diabled for qty < 1
![Manual Testing](docs/testing/manual/input-1.png)
![Manual Testing](docs/testing/manual/input-1-a.png)
*qty > 1 and < 99
![Manual Testing](docs/testing/manual/input-2.png)
![Manual Testing](docs/testing/manual/input-2-a.png)
*qty => 99
![Manual Testing](docs/testing/manual/input-3.png)
![Manual Testing](docs/testing/manual/input-3-a.png)
4. Qty & Update Cart Options:
*From Shopping Cart set qty to < 1 & click update
![Manual Testing](docs/testing/manual/input-4.png)
![Manual Testing](docs/testing/manual/input-4-a.png)
5. Cart Icon:
![Manual Testing](docs/testing/manual/cart-icon-mt.png)
*Book added, cart with added delivery
![Manual Testing](docs/testing/manual/cart-icon.png)
*Cart with free delivery, matches total for books
![Manual Testing](docs/testing/manual/cart-free.png)

6. Cart Remove Option:
![Manual Testing](docs/testing/manual/cart-remove.png)
7. Checkout Form
![Manual Testing](docs/testing/manual/checkout-name.png)
![Manual Testing](docs/testing/manual/checkout-email.png)
![Manual Testing](docs/testing/manual/checkout-phone.png)
![Manual Testing](docs/testing/manual/checkout-city.png)
![Manual Testing](docs/testing/manual/checkout-county.png)
![Manual Testing](docs/testing/manual/checkout-passed.png)
![Manual Testing](docs/testing/manual/checkout-order.png)

No errors or warnings logged to the console:
![Manual Testing](docs/testing/manual/console.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Bugs

| Bug  | Fix  |
| ------- | ------- |
| Books Images uploaded to the root directory | Add MEDIA_URL = '/media/' & MEDIA_ROOT = os.path.join(BASE_DIR, 'media') to settings.py |
| Webhook HTTP status code 500 for payment_intent.succeeded | review the code for typos & add import stripe |
| Item quantity form on the cart page does not responding as expected  | Review the code and add missig input attributes |
| Books Pagination not working for search queries, on era tabs & when sorting books list | update variables & remove pagination for search queries, on era tabs & when sorting books list as 'Page' object has no related attributes |
| 404 Custom Page not displayed 500 Error instead | delete views & url for the 404 error, keep 404.html |
| Post likes cannot be added, Extending the user model: SimpleLazyObject error | use the profile when you check/add/remove likes |
| IntegrityError when trying to post a comment | add  userprofile to request.user in comment_form.instance.username = request.user |
| Post likes are not removed on click after user added a like | Review the if statement & update to 'if request.user.userprofile in post.likes.all():' |
| The array literal notation [] is preferrable jshint warning on Mailchimp script | Replace new Array() with [] |

[Back to Table Of Contents](#table-of-contents)

## Deployment

<details>

<summary>This site was deployed using Heroku in following steps:</summary>

Pre deployment steps for AWS & Stripe:

1. To Set up an AWS S3 Bucket sign in to <a href="https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Feu-north-1.console.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26region%3Deu-north-1%26state%3DhashArgsFromTB_eu-north-1_c0ccf0eb8e5a9f52&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=1QLf1BdX-tBkIzNlTlRMe7a281HIMkbkoiBG1o2KBho&code_challenge_method=SHA-256">Amazon Web Services</a>
![Deployment](docs/deployment/amazon.png)

2. Search & open the S3 Service, click on the Create bucket button.
![Deployment](docs/deployment/bucket.png)
3. Create a unique bucket name - project name is advised & the location region.
4. Configure as needed, set up permissions, e.g. ACLs ENABLED, set settings, property tab: index.html & error.html - > save, CORS.
5. Generate & copy policy to Bucket Policy Editor.
6. Create policy & attach policy to group.
7. Retrieve AWS access keys
8. From the workspace console: pip3 install boto3 & pip3 install django-storages  pip3 freeze > requirements.txt
9. Add AWS keys remove COLLECT_STATICFILES from Heroku 
![Deployment](docs/deployment/keys.png)
10. Add custom_storages.py 
![Deployment](docs/deployment/storages.png)   
11.  Add cache control
![Deployment](docs/deployment/cache.png)   
12.   Create a media folder & upload images to the bucket.
![Deployment](docs/deployment/upload.png)
13.   Add Stripe Endpoint:
    1.  Login to <a href="https://dashboard.stripe.com/dashboard">Stripe</a>
    2.  Retrieve the publishable & secret keys
    3.  ![Deployment](docs/deployment/stripe-keys.png)
    4.  Create STRIPE_PUBLIC_KEY & STRIPE_SECRET_KEY environmental variables to local env & on Heroku.
    5.  Go to Webhooks tab from Stripe Developers section & add endpoint with the website URL
    6.  ![Deployment](docs/deployment/webhooks.png)
    7.  Save the key generated & create with it STRIPE_WH_SECRET environment variable.

Before Heroku deployment remember to:

1. Install Django and gunicorn: pip3 install 'django<4' gunicorn
2. Install supporting libraries: pip3 install dj_database_url==0.5.0 psycopg2
3. Migrate Changes: python3 manage.py migrate
4. Create a new external database:
   1. Log in to <a href="https://customer.elephantsql.com/">ElephantSQL</a>
   2. Create New Instance.
   3. ![Deployment](docs/deployment/instance.png)
   4. Set up your plan: Name (usually the name of the project) with the Tiny Turtle (Free) plan.
   5. Select Region: Select a data center near you.
   6. Review & Create instance.
   7. Click on the database instance name.
   8. Copy ElephantSQL database URL

5. Create a Procfile with: web: gunicorn hi_story_book_store.wsgi:application
6.  set DEBUG = False
7.  Ensure requirements.txt is updated using terminal command: pip3 freeze --local requirements.txt

![Deployment](docs/deployment/debug.png)
![Deployment](docs/deployment/requirements.png)

1. Log in to Heroku or create an account
2. ![Deployment](docs/deployment/heroku-login.png)
3. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create new app
4. ![Deployment](docs/deployment/new.png)
5. You must enter a unique app name
6. Next select your region
7. Click on the Create App button
![Deployment](docs/deployment/create.png)
8. Go to the Settings tab
9. Click Reveal Config Vars and add:
![Deployment](docs/deployment/vars.png)
    *PORT = 8000
10.  Below Config Vars in Buildpacks make sure python is selected
![Deployment](docs/deployment/buildpack.png)
11.  Go to the Deploy Tab
12.  Choose Deployment method GitHub and click Save Changes
13.  Confirm you want to connect to GitHub
14.  Search for the repository name and click the connect button
15.  Scroll to the bottom of the deploy page and select the preferred deployment type ( Automatic deploys or Manual deploy)
![Deployment](docs/deployment/auto-manual.png)
16.    Choose a branch to deploy: main
17.   Click on Deploy Branch button & wait until the app is successfully deployed/ address log errors
18. ![Deployment](docs/deployment/manual.png)
![Deployment](docs/deployment/deployed.png)
19.    For Automatic deploys click on Enable Automatic Deploys button
![Deployment](docs/deployment/auto.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Credits

- E-commerce store functionalities inspired by <a href="https://github.com/Code-Institute-Solutions/boutique_ado_v1">Code Institue's "Boutique Ado" Walkthrough Project</a>

- Parts of code based on <a href="https://github.com/Code-Institute-Solutions/boutique_ado_v1">Code Institue's "Boutique Ado" Walkthrough Project</a>

- JavaScript code to Ensure proper enabling/disabling of all inputs on page load, check enable/disable every time the input is changed on quantity_input_script & move the screen back to the top of the books list from <a href="https://github.com/Code-Institute-Solutions/boutique_ado_v1">Code Institue's "Boutique Ado" Walkthrough Project</a>

- Disable +/- buttons outside 1-99 range, increment quantity & decrement quantity on quantity_input_script based on <a href="https://github.com/Code-Institute-Solutions/boutique_ado_v1">Code Institue's "Boutique Ado" Walkthrough Project</a>

- .overlay, .text-black, #payment-form, .form-control & #card-element & .loading-spinner CSS from <a href="https://github.com/Code-Institute-Solutions/boutique_ado_v1">Code Institue's "Boutique Ado" Walkthrough Project</a>

- Some elements of the checkout app from <a href="https://github.com/Code-Institute-Solutions/boutique_ado_v1">Code Institue's "Boutique Ado" Walkthrough Project</a>
  
- webhooks.py based on: <a href="https://stripe.com/docs/webhooks">Stripe</a>, <a href="https://github.com/Code-Institute-Solutions/boutique_ado_v1">Code Institue's "Boutique Ado" Walkthrough Project</a> & <a href="https://github.com/ArronBeale/CI_PP5_tee_time/blob/main/checkout/webhooks.py">Teetime</a>

- aria_labels in profiles.forms.py based on <a href="https://github.com/ArronBeale/CI_PP5_tee_time/blob/main/profiles/forms.py">Teetime</a>

- checkout.froms.py widgets in OrderForm based on <a href="https://docs.djangoproject.com/en/4.2/ref/forms/widgets/">Django</a> & <a href="https://stackoverflow.com/questions/48822759/override-in-the-widget-attributes-the-max-length-set-on-the-model">Stackoverflow</a>, additionally part of code also from <a href="https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters">Stackoverflow</a>

- Books List pagination from YouTube by <a href="https://www.youtube.com/watch?v=N-PB-HMFmdo">Codemy.com</a>

- Parts of the code inspired by the knowledge from my Project Portfolio 4:<a href="https://github.com/WojtekKamilowski/CI_PP4_MPN">My Pantry Note</a>

- base.html inspired by <a href="https://github.com/Alan-Bushell/razor-sharp">'Razor Sharp'</a>

- Parts of blog app inspired by <a href="https://github.com/Alan-Bushell/razor-sharp/tree/main/blog">'Razor Sharp'</a> 
  
- object-fit for book images from <a href="https://stackoverflow.com/questions/61530120/how-to-make-the-images-same-fit-or-same-size">Stackoverflow</a>
  
- Dropright main-nav submenu for sorting by lowest & highest price based on <a href="https://getbootstrap.com/docs/4.6/components/dropdowns/">Bootstrap</a>

- Post likes bug fix from <a href="https://stackoverflow.com/questions/44458764/extending-the-user-model-simplelazyobject-error-when-using-user-is-authenticate">Stackoverflow</a>

- Adding comments bug fix from <a href="https://stackoverflow.com/questions/71892594/integrityerror-exception-value-with-db-relations-in-django-on-form-submission">Stackoverflow</a>

- Update timezone from <a href="https://stackoverflow.com/questions/29311354/how-to-set-the-timezone-in-django">Stackoverflow</a>

- Fix remove likes on clicking the like icon after adding a like <a href="https://stackoverflow.com/questions/65557334/like-button-is-working-but-not-changing-to-unlike-in-django">Stackoverflow</a>

- Remove html validation warnings regarding script type attribute <a href="https://rocketvalidator.com/html-validation/the-type-attribute-is-unnecessary-for-javascript-resources">Rocketvalidator</a>

- The array literal notation [] is preferrable JavaScript validation error fix for the mailchimp script <a href="http://linterrors.com/js/the-array-literal-notation-is-preferrable">Linterrors</a>

- The most popular robots.txt Disallow directives for eCommerce websites from <a href="https://tillison.co.uk/blog/robots-txt-for-ecommerce/#:~:text=Furthermore%2C%20eCommerce%20websites%20may%20have,helping%20to%20protect%20customer%20information.">Tillison Consulting</a>

### Media

- Favicon from <a href="https://favicon.io/favicon-generator/">Favicon</a>.
- Homepage background image from <a href="https://www.freepik.com/free-vector/background-with-sand-hourglass-glass-timer_22753059.htm#query=time%20glass&position=8&from_view=search&track=ais">Freepik</a>.
- Fonts pair found on <a href="https://www.fontpair.co/pairings/playfair-display-lato">Fontpair</a>
- 'Lato' font from <a href="https://fonts.google.com/specimen/Lato">Google Fonts</a>
- 'Playfair Display' font from <a href="https://fonts.google.com/specimen/Playfair+Display?query=playfair">Google Fonts</a>
- Ancient Europe book cover image from <a href="https://www.freepik.com/free-vector/vintage-roman-empire-poster-with-inscription-julius-caesar-coins-buildings-ancient-rome-civilization_9397964.htm#query=rome%20book%20cover&position=7&from_view=search&track=ais">Freepik</a>.
- Ancient ROW book cover image from <a href="https://www.freepik.com/free-vector/archaeology-cartoon-composition-with-set-digging-tool-icons-ancient-findings-grunge-board-with-text-illustration_21253335.htm#query=mezopotamy%20history%20book%20cover&position=26&from_view=search&track=ais">Freepik</a>.
- Medieval Europe book cover image from <a href="https://www.pexels.com/photo/black-steel-helmet-near-black-and-gray-handle-sword-161936/">Pexels</a>
- Medieval ROW book cover image from <a href="https://www.pexels.com/photo/young-mongolian-man-with-eagle-riding-horse-5275516/">Pexels</a>
- Reneissance Europe book cover image from <a href="https://www.pexels.com/photo/vitruvian-man-drawing-in-close-up-shot-12414385/">Pexels</a>
- Reneissance ROW book cover image from <a href="https://www.pexels.com/photo/great-wall-of-china-2412603/">Pexels</a>
- Early Industrial Revolution & Modern Era Europe book cover image from <a href="https://www.freeimages.com/photo/cotton-manufacturing-2424360">Freeimages</a> 
- Early Industrial Revolution & Modern Era ROW book cover image from <a href="https://www.pexels.com/photo/paper-map-of-australia-placed-on-wall-6564832/">Pexels</a>  
- XX Century Europe book cover image from <a href="https://pixabay.com/illustrations/microsoft-windows-window-to-dye-257885/">Pixabay</a>
- XX Century ROW book cover image from
- Early XXI Century Europe book cover image from <a href="https://www.freeimages.com/download/eu-polish-flags-636220">Freeimages</a>
- Early XXI Century ROW book cover image from <a href="https://pixabay.com/illustrations/bad-business-collage-crisis-19907/">Pixabay</a>
- Image for egyptian blog post <a href="https://www.pexels.com/photo/egyptian-symbols-3199399/">Pexels</a>
- Facebook cover photo <a href="https://www.pexels.com/photo/closeup-photography-of-book-page-folding-forming-heart-1083633/">Pexels</a>
- Image for US blog post <a href="https://www.pexels.com/photo/the-statue-of-liberty-69205/">Pexels</a>
- Image for Roman blog post <a href="https://www.pexels.com/photo/administration-ancient-arches-architecture-356966/">Pexels</a>
- Image for China blog post <a href="https://www.pexels.com/photo/gazebo-near-trees-during-day-3018977/">Pexels</a>
- Image for Ramzes II book <a href="https://www.pexels.com/photo/gold-tutankhamun-statue-33571/">Pexels</a>
- Image for Napoleon book <a href="https://www.pexels.com/photo/man-people-festival-music-16721221/">Pexels</a>


[Back to Table Of Contents](#table-of-contents)

## Further Developments

- Add pagination feature for search queries, on era tabs & when sorting books list. Possibly by starting with fixing error: 'Page' object has no attribute 'ordered'
initial solutions research started on <a href="https://stackoverflow.com/questions/22426502/page-object-has-no-attribute-ordered-exception">Stackoverflow</a>

- Add functionalities to add,update & delete blog posts from the website without using django admin by superusers.
  
- Add functionalities to add,update & delete all users'post comments from the website without using django admin by superusers.
  
- Add functionalities to add,update & delete user's own post comments.
  
- Add additional product app where the items listed for sale would be related to the book store(complementary sales), however with different details than books usually have, for example bookmarks or reading torches, HiStory t-shirts and other gadgets etc.
  
- Expand books app to include books in a digital form such audio-books & e-books.

- Add more payment options, e.g. Paypal.

- Add books rating system available for users with admins confirmation.
  
- Visualize rating with proportionally filling stars.

- Add settings option for users profile.

[Back to Table Of Contents](#table-of-contents)

## Acknowledgements
I would like to thank those who were a great support and inspiration during writing this project:
- My wife, who supported me during the process of creating this project.
- My mentor Mo Shami.
- Code Institute for preparing the materials and providing a wide range of available means of learning for the students.
