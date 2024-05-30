<img id="overview" src="readme-assets/escoot-logo.png"
     alt="Am I responsive"
     width="800px" style="max-width: 100%;"/>

<h2><a href="" target="_blank">Live App here</a></h2>


E-scoot
---

E-scoot is a Django application designed as an ecommerce website.Tailored specifically for the market of electric scooters, it delivers a seamless and personalized shopping experience for users looking to build their ideal e-scooter. It also allows the site owner to efficiently manage their orders.

## Table of Contents

1. [Overview](https://github.com/luciotorelli/escoot#overview)
2. [Business Model](https://github.com/luciotorelli/escoot#business-model)
3. [Epics - User Stories](https://github.com/luciotorelli/escoot#epics-user-stories)
4. [Wireframes](https://github.com/luciotorelli/escoot#wireframes)
5. [Project Management and Planning](https://github.com/luciotorelli/escoot#project-management-and-planning)
6. [UX](https://github.com/luciotorelli/escoot#ux)
7. [Features](https://github.com/luciotorelli/escoot#features)
8. [Technologies Used](https://github.com/luciotorelli/escoot#technologies-used)
9. [Testing](https://github.com/luciotorelli/escoot#testing)
10. [Deployment](https://github.com/luciotorelli/escoot#deployment)
11. [Credits](https://github.com/luciotorelli/escoot#credits)

---

# Business Model

## Core Business Intents

### Customized E-Scooter Sales

- **Easy Interface:** A user-friendly interface lets customers build their scooters by choosing specific parts and upgrades.
- **Lots of Options:** We offer a wide variety of customization choices to meet different needs and preferences.
- **B2C Focus:** We love connecting directly with our customers. This approach lets us understand their needs better, offer personalized solutions, and ensure they have a great shopping experience while helping scaling sustainably.

### Official Parts Inventory

- **Wide Inventory:** We keep a large stock of official parts to help with customization and maintenance.
- **Quality Assurance:** By offering official parts, we ensure high quality and reliability.
- **Convenience:** Easy access to replacement parts and accessories encourages repeat purchases.

### Keeping Customers Happy

- **Loyalty Rewards:** We introduce programs that reward repeat customers with discounts, exclusive offers, and early access to new products.
- **Stay in Touch:** We use email marketing to keep customers updated on new arrivals, promotions, and personalized recommendations.
- **Great Service:** We provide excellent customer service to build trust and encourage long-term relationships.

### Going Green

- **Eco-Friendly:** We emphasize the eco-friendly nature of electric scooters as a sustainable transportation option.
- **Partnerships:** We partner with environmental organizations to promote sustainability initiatives and enhance our brand image.

## Marketing Strategies

### Working with Influencers

- **Collaborations:** We work with influencers and content creators who love electric scooters and green transportation.
- **Generate Buzz:** Influencers help create excitement by sharing reviews, unboxings, and tutorials, which attract new customers.

### Social Media and Engaging Content

- **Focus on Facebook:** We post engaging content on Facebook, including how customers customize their scooters and their personal stories.
- **Targeted Ads:** We run ad campaigns on Facebook aimed at people interested in sustainable transportation and tech gadgets.

### Keeping in Touch through Emails

- **Stay Updated:** We have a strong email marketing strategy to keep our subscribers informed about new products, special offers, and company news.
- **Personal Touch:** We send personalized emails recommending products based on what customers like and have bought before.

### Getting Found Online

- **Optimize Website:** We make sure our website is easy to find through search engines, increasing our visibility and attracting organic traffic.
- **SEO Tips:** We use relevant keywords, create high-quality content, and build backlinks to improve our search rankings and bring more visitors to the site.

### Making Our Website User-Friendly

- **Mobile-Friendly:** We ensure our website is easy to use on mobile devices, fast, and simple to navigate, offering a smooth shopping experience.
- **Easy Navigation:** We use intuitive design elements to guide users through the customization and purchasing process effortlessly.


By focusing on these strategies and keeping our business intents customer-centric, E-scoot aims to become a leading brand in the electric scooter market, driving sales and building long-term customer loyalty.

<img id="facebook-mockup" src="readme-assets/facebook-mockup.png"
     alt="Facebook Business Page Mockup"
     width="800px" style="max-width: 100%;"/>

A business page is valuable in my ecommerce website because it serves as a platform to reach a broad audience, engage with potential customers, and build a community around my brand.

---

# Epics - User Stories


In the initial phase of developing the E-scoot E-commerce Platform, user stories were created to capture the specific needs and expectations of both buyers and the site owner. Following this, the user stories were organized and grouped into coherent themes and prioritized following the MoSCow method, resulting in the identification of key epics. This separation into epics streamlined the development process by categorizing related functionalities, ensuring a more organized and efficient approach to building the comprehensive features outlined in the user stories below.

## Buyer Epics:

| **Epic** | **User Story** | **MoSCoW Priority** |
|----------|-----------------|---------------------|
| **1. Product Purchase and Customization:** | - As a Buyer, I want to purchase an e-scooter by selecting only the parts and upgrades I require for my unique case so that I can customize my purchase to meet my specific needs.<br>- As a Buyer who already owns an e-scooter, I want to purchase parts separately from the main product so that I can replace or upgrade specific components without buying a new scooter.<br>- As a first-time site visitor, I want to quickly understand the purpose of the site and what I can accomplish on it so that I can easily navigate and find relevant information. | Must-Have |
| **2. User Account Management:** | - As a Buyer, I want to see my addresses, edit them, or delete them as required so that I can manage my shipping information efficiently.<br>- As a Buyer, I want to see the status of my order and view past orders so that I can track my purchases and review my order history.<br>- As a Buyer, I want to sign up for a mailing list to stay up to date on offers so that I can receive updates and promotions.<br>- As a Buyer, I want to log in and log out of my profile or create a profile when checking out for the first time so that I can access personalized features and track my orders. | Must-Have |
| **3. Shopping Cart and Checkout:** | - As a Buyer, I want to add products to my cart, view the subtotal, edit quantities, or remove products as required so that I can easily manage my shopping experience.<br>- As a Buyer, I want to pay for my order on a secure checkout page so that I can complete transactions with confidence. | Must-Have |
| **4. Communication and Support:** | - As a Buyer, I want to contact the company either through a chat option or an email form so that I can seek assistance or get answers to my queries. | Should-Have |

## Site Owner Epics:

| **Epic** | **User Story** | **MoSCoW Priority** |
|----------|-----------------|---------------------|
| **1. Website Management:** | - As the Site Owner, I want a modern and simple-to-navigate website to sell my products so that I can provide a positive user experience for potential buyers.<br>- As the Site Owner, I want to add or remove products so that I can keep my product offerings up to date.<br>- As the Site Owner, I want to edit the products so that I can make necessary updates or modifications to product information. | Must-Have |
| **2. Order and Customer Management:** | - As the Site Owner, I want to view the orders placed so that I can efficiently process and ship the products to the buyer.<br>- As the Site Owner, I want to receive emails from buyers when they submit a form or chat on the site so that I can promptly respond to inquiries and provide support.<br>- As the Site Owner, I want to control the stock of the products and make products unavailable/unlisted so that I can manage inventory effectively. | Must-Have |
| **3. Marketing and Outreach:** | - As the Site Owner, I want to have a Business Facebook page to increase my product/brand reach so that I can leverage social media for marketing and visibility. | Should-Have |
| **4. Security and Data Protection:** | - As the Site Owner, I want to ensure the security and privacy of user information by implementing authentication and data protection measures to safeguard sensitive data so that users can trust the platform. | Must-Have |
| **5. Chat bot to answer queries and check orders statuses** | Implement a chat bot feature that can assist users by answering queries and providing order status updates. | Could-Have |
| **6. Reviews on product page** | Integrate a review system on product pages to allow buyers to share their experiences and opinions about the products. | Could-Have |



# Wireframes

<img src="readme-assets/wireframes/mobile-homepage.png" alt="Wireframe for mobile home page" width="800px" />

## All pages:

<details>
   <summary>Mobile</summary>
      
-  <details>
         <summary>Homepage</summary>
            <img src="readme-assets/wireframes/mobile-homepage.png" width="800px" />
      </details>

-  <details>
         <summary>Login Page</summary>
            <img src="readme-assets/wireframes/mobile-login.png" width="800px" />
      </details>

-  <details>
         <summary>Change Password</summary>
            <img src="readme-assets/wireframes/mobile-change-password.png" width="800px" />
      </details>

-  <details>
         <summary>Cart</summary>
            <img src="readme-assets/wireframes/mobile-cart.png" width="800px" />
      </details>

-  <details>
         <summary>Checkout</summary>
            <img src="readme-assets/wireframes/mobile-checkout.png" width="800px" />
      </details>

-  <details>
         <summary>Contact Us</summary>
            <img src="readme-assets/wireframes/mobile-contact-us.png" width="800px" />
      </details>

-  <details>
         <summary>Menu</summary>
            <img src="readme-assets/wireframes/mobile-menu.png" width="800px" />
      </details>

-  <details>
         <summary>Orders</summary>
            <img src="readme-assets/wireframes/mobile-orders.png" width="800px" />
      </details>

-  <details>
         <summary>Profile</summary>
            <img src="readme-assets/wireframes/mobile-profile.png" width="800px" />
      </details>

-  <details>
         <summary>Search</summary>
            <img src="readme-assets/wireframes/mobile-search.png" width="800px" />
      </details>

-  <details>
         <summary>Stock</summary>
            <img src="readme-assets/wireframes/mobile-stock.png" width="800px" />
      </details>

</details>

<details>
   <summary>Desktop</summary>
   
-  <details>
         <summary>Homepage</summary>
            <img src="readme-assets/wireframes/desktop-homepage.png" width="800px" />
      </details>

-  <details>
         <summary>Login</summary>
            <img src="readme-assets/wireframes/desktop-login.png" width="800px" />
      </details>

-  <details>
         <summary>Change Password</summary>
            <img src="readme-assets/wireframes/desktop-change-password.png" width="800px" />
      </details>

-  <details>
         <summary>Cart</summary>
            <img src="readme-assets/wireframes/desktop-cart.png" width="800px" />
      </details>      

-  <details>
         <summary>Checkout</summary>
            <img src="readme-assets/wireframes/desktop-checkout.png" width="800px" />
      </details>  

-  <details>
         <summary>Contact Us</summary>
            <img src="readme-assets/wireframes/desktop-contact-us.png" width="800px" />
      </details>

-  <details>
         <summary>Orders</summary>
            <img src="readme-assets/wireframes/desktop-orders.png" width="800px" />
      </details>

-  <details>
         <summary>Popup</summary>
            <img src="readme-assets/wireframes/desktop-popup.png" width="800px" />
      </details>

-  <details>
         <summary>Popup</summary>
            <img src="readme-assets/wireframes/desktop-profile.png" width="800px" />
      </details>

-  <details>
         <summary>Search</summary>
            <img src="readme-assets/wireframes/desktop-search.png" width="800px" />
      </details>

-  <details>
         <summary>Stock</summary>
            <img src="readme-assets/wireframes/desktop-stock.png" width="800px" />
      </details>

</details>

## Project Management and Planning


### Agile Methodology

This project was idealized following the Agile methodology where the epics were ordered into sprints based on the importance, timeframe and logic flow. The sprints were them used to create the tasks found within Github built-in project management tool.  


| Sprint | Description                                     |
|--------|-------------------------------------------------|
| Sprint 1 | Project ideation, README, and planning                            |
| Sprint 2 | Admin dashboard and Products                     |
| Sprint 3 | Shopping Experience                     |
| Sprint 4 | Communication and Support                       |
| Sprint 5 | Site Owner Management                            |
| Sprint 6 | Marketing and Security Enhancements              |
| Sprint 7 | Additional Features                              |


### MVC Architecture
This project utilizes the MVC architecture to create a full-stack application. During each sprint those steps were reiterated as required.

## Data Model

### Data Model

<img src="readme-assets/relational-database-schema.png" alt="Relational Database Schema" />

### User Table

| Key Type   | Attribute           | Type       | Unique | Relationship |
|------------|----------------------|------------|--------|--------------|
| Primary Key | user_id             | Integer    | Yes    | -            |
| -          | full_name            | CharField  | No     | -            |
| -          | username             | CharField  | Yes    | -            |
| -          | email                | EmailField | Yes    | -            |
| -          | password             | CharField  | No     | -            |
| -          | address              | TextField  | No     | -            |
| -          | phone_number         | CharField  | No     | -            |
| -          | role                 | CharField  | No     | -            |


### Product Table

| Key Type   | Attribute            | Type         | Unique | Relationship |
|------------|----------------------|--------------|--------|--------------|
| Primary Key | product_id          | Integer      | Yes    | -            |
| -          | product_name         | CharField    | No     | -            |
| -          | description          | TextField    | No     | -            |
| -          | price                | DecimalField | No     | -            |
| -          | stock_quantity       | Integer      | No     | -            |
| -          | image                | ImageField   | No     | -            |
| -          | status               | CharField    | No     | -            |
| -          | product_category     | CharField    | No     | -            |


### Order Table

| Key Type     | Attribute         | Type            | Unique | Relationship |
|--------------|-------------------|-----------------|--------|--------------|
| Primary Key  | order_id          | Integer         | Yes    | -            |
| Foreign Key  | user_profile_id   | ForeignKey      | No     | UserProfile  |
| -            | full_name         | CharField       | No     | -            |
| -            | email             | EmailField      | No     | -            |
| -            | phone_number      | CharField       | No     | -            |
| -            | country           | CountryField    | No     | -            |
| -            | postcode          | CharField       | No     | -            |
| -            | town_or_city      | CharField       | No     | -            |
| -            | street_address1   | CharField       | No     | -            |
| -            | street_address2   | CharField       | No     | -            |
| -            | county            | CharField       | No     | -            |
| -            | date              | DateTimeField   | No     | -            |
| -            | delivery_cost     | DecimalField    | No     | -            |
| -            | order_total       | DecimalField    | No     | -            |
| -            | grand_total       | DecimalField    | No     | -            |
| -            | original_cart     | TextField       | No     | -            |
| -            | stripe_pid        | CharField       | No     | -            |
| -            | discount_amount   | DecimalField    | No     | -            |
| -            | discount_code     | CharField       | No     | -            |

### Order Item Table

| Key Type     | Attribute         | Type          | Unique | Relationship |
|--------------|-------------------|---------------|--------|--------------|
| Primary Key  | order_item_id     | Integer       | Yes    | -            |
| Foreign Key  | order_id          | ForeignKey    | No     | Order        |
| Foreign Key  | product_id        | ForeignKey    | No     | Product      |
| -            | quantity          | Integer       | No     | -            |
| -            | lineitem_total    | DecimalField  | No     | -            |

### Contact Message Table

| Key Type     | Attribute         | Type          | Unique | Relationship |
|--------------|-------------------|---------------|--------|--------------|
| Primary Key  | contact_message_id | Integer       | Yes    | -            |
| -            | name              | CharField     | No     | -            |
| -            | email             | EmailField    | No     | -            |
| -            | message           | TextField     | No     | -            |
| Foreign Key  | order_id          | ForeignKey    | No     | Order        |
| -            | date_submitted    | DateTimeField | No     | -            |

### Discount Code Table

| Key Type     | Attribute         | Type          | Unique | Relationship |
|--------------|-------------------|---------------|--------|--------------|
| Primary Key  | discount_code_id  | Integer       | Yes    | -            |
| -            | code              | CharField     | Yes    | -            |
| -            | discount          | DecimalField  | No     | -            |
| -            | active            | BooleanField  | No     | -            |

### Applied Discount Table

| Key Type     | Attribute         | Type          | Unique | Relationship |
|--------------|-------------------|---------------|--------|--------------|
| Primary Key  | applied_discount_id | Integer      | Yes    | -            |
| OneToOne     | order_id          | OneToOneField | No     | Order        |
| Foreign Key  | discount_code_id  | ForeignKey    | No     | DiscountCode |
| -            | discount_amount   | DecimalField  | No     | -            |

### UserProfile Table

| Key Type     | Attribute         | Type          | Unique | Relationship |
|--------------|-------------------|---------------|--------|--------------|
| Primary Key  | user_profile_id   | Integer       | Yes    | -            |
| OneToOne     | user_id           | OneToOneField | Yes    | User         |
| -            | default_phone_number | CharField   | No     | -            |
| -            | default_street_address1 | CharField | No     | -            |
| -            | default_street_address2 | CharField | No     | -            |
| -            | default_town_or_city | CharField    | No     | -            |
| -            | default_county    | CharField     | No     | -            |
| -            | default_postcode  | CharField     | No     | -            |
| -            | default_country   | CountryField  | No     | -            |

### Wishlist Table

| Key Type     | Attribute         | Type          | Unique | Relationship |
|--------------|-------------------|---------------|--------|--------------|
| Primary Key  | wishlist_id       | Integer       | Yes    | -            |
| OneToOne     | user_id           | OneToOneField | Yes    | User         |
| ManyToMany   | products          | ManyToManyField | No   | Product      |
| -            | created_at        | DateTimeField | No     | -            |



## UX

### Wireframes


### Color palette

<img src="readme-assets/color-palette.png" alt="Color Palette for the app/site" width="800px" />

### Font



## Features

### Future Features
#### Some features were considered for implementation of this project. However, due to the time constrains and importance those were added to future features instead.

---

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main template contents.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the styling, design and layout.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for responsiveness and pre-built components.
- [JavaScript](https://www.javascript.com) used to dynamically display searches on the front-end, to save information to Session Storage, and to replace HTML content on the DOM.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Python is a high-level, general-purpose language, used to code Django files.
- [Gitpod](https://www.gitpod.io/about) - Gitpod is an open-source developer platform automating the provisioning of ready-to-code developer environments. Used to create the tests due to the limitation of local development.
- [Heroku](https://dashboard.heroku.com/) - Heroku is a cloud platform as a service supporting several programming languages, used to host the live application.
- [Github and Git](https://docs.github.com/en/get-started/using-git/about-git) - Used to host the development of the project and version control using Git.
- [Django](https://www.djangoproject.com) - used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) - used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) - used as the database host.
- [Cloudinary](https://cloudinary.com) - used for hosting and serving static files.
- [Stripe](https://stripe.com) - used to handle online payments and transactions.


---

## Testing

### Test Cases



### Browser Compatibility

The app was manually tested on the following browsers. All forms, buttons, views, templates, scripts, and functions worked as expected. Database updates are consistent for all browsers.

| Browser        | Compatible | Notes                                                      |
|----------------|------------|------------------------------------------------------------|
| Chrome Desktop | Yes        | N/A                                                        |
| Firefox Desktop| Yes        | N/A                                                        |
| Safari Desktop | Yes        | N/A                                                        |
| Edge Desktop   | Yes        | N/A                                                        |
| Arc Desktop    | Yes        | N/A                                                        |
| Brave Desktop  | Partially, see notes        | Brave shields may block some of the JS, AJAX or Form handling. Turning it off fixes it.|
| Chrome Mobile  | Yes        | Scroll bar may be displayed differently       |
| Safari Mobile  | Yes        | Scroll bar may be displayed differently       |
| Brave Mobile   | Partially, see notes        | Brave shields may block some of the JS, AJAX or Form handling. Turning it off fixes it. |



### Automated Testing



### Issues

Issues were logged using GitHub native issue tracking system. All logged issues can be [viewed here.](https://github.com/luciotorelli/escoot/issues)
They were tagged as either bug, enhancement, documentation or user stories accordingly. 

<img src="readme-assets/bugs.jpg" width="1000px" />


### Feedback



### CRUD (Create, Read, Update, Delete)

#### During automated and manual tests, the following data manipulation operations through the front-end (not including admin) were confirmed to be working as expected.

| Create           | Read             | Update           | Delete           |
|:----------------:|:----------------:|:----------------:|:----------------:|
| Product          | Product          | Product          | Product          |
| Order            | Order            | Order            | Order            |
| Order Item       | Order Item       | Order Item       | Order Item       |
| User Profile     | User Profile     | User Profile     | X                |
| Wishlist         | Wishlist         | X                | Wishlist         |
| Contact Message  | Contact Message  | X                | X                |
| Discount Code    | Discount Code    | Discount Code    | Discount Code    |
| Applied Discount | Applied Discount | X                | Applied Discount |



### Validation


### Lighthouse

<br>

### Deployment


---

## Credits

### Special Thanks!


### Resources use


### Imported templates/libraries

---