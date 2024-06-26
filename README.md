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

---

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main template contents.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the styling, design, and layout.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for responsiveness and pre-built components.
- [JavaScript](https://www.javascript.com) used to dynamically display searches on the front-end, save information to Session Storage, and replace HTML content on the DOM.
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
| Case | Page Link | Achieved |
| :---:   | :---: | :---: |
| As a Buyer, I want to purchase an e-scooter by selecting only the parts and upgrades I require for my unique case so that I can customize my purchase to meet my specific needs. | [Product Page](https://example.com/products) | Yes |
| As a Buyer who already owns an e-scooter, I want to purchase parts separately from the main product so that I can replace or upgrade specific components without buying a new scooter. | [Parts Page](https://example.com/parts) | Yes |
| As a Buyer, I want to see my addresses, edit them, or delete them as required so that I can manage my shipping information efficiently. | [Profile Page](https://example.com/profile) | Yes |
| As a Buyer, I want to see the status of my order and view past orders so that I can track my purchases and review my order history. | [Orders Page](https://example.com/orders) | Yes |
| As a Buyer, I want to add products to my cart, view the subtotal, edit quantities, or remove products as required so that I can easily manage my shopping experience. | [Cart Page](https://example.com/cart) | Yes |
| As the Site Owner, I want a modern and simple-to-navigate website to sell my products so that I can provide a positive user experience for potential buyers. | [Homepage](https://example.com) | Yes |
| As the Site Owner, I want to view the orders placed so that I can efficiently process and ship the products to the buyer. | [Admin Orders Page](https://example.com/admin/orders) | Yes |
| As the Site Owner, I want to ensure the security and privacy of user information by implementing authentication and data protection measures to safeguard sensitive data so that users can trust the platform. | [Admin Settings Page](https://example.com/admin/settings) | Yes |

### Browser Compatibility
The app was manually tested on the following browsers. All forms, buttons, views, templates, scripts, and functions worked as expected. Database updates are consistent for all browsers.

| Browser        | Compatible | Notes                                                      |
|----------------|------------|------------------------------------------------------------|
| Chrome Desktop | Yes        | N/A                                                        |
| Firefox Desktop| Yes        | N/A                                                        |
| Safari Desktop | Yes        | N/A                                                        |
| Edge Desktop   | Yes        | N/A                                                        |
| Arc Desktop    | Yes        | N/A                                                        |
| Brave Desktop  | Partially  | Brave shields may block some of the JS, AJAX, or form handling. Turning it off fixes it.|
| Chrome Mobile  | Yes        | Scroll bar may be displayed differently                    |
| Safari Mobile  | Yes        | Scroll bar may be displayed differently                    |
| Brave Mobile   | Partially  | Brave shields may block some of the JS, AJAX, or form handling. Turning it off fixes it. |

### Issues

# Fixed Issues and Bugs

This document lists the issues and bugs that have been fixed in the project.

| Number | Commit Link | Commit Title | Issue Explanation | Fixed Summary |
| --- | --- | --- | --- | --- |
| 1 | [Commit Link](https://github.com/luciotorelli/escoot/commit/50593ce) | Fix success page text breaks | The success page text breaks on certain screen sizes or resolutions. | Adjusted the CSS styling to ensure proper word wrapping and alignment within the container elements. |
| 2 | [Commit Link](https://github.com/luciotorelli/escoot/commit/cbc01b0) | Fix incorrect wrapping of discount value on mobile screens | The discount value wraps incorrectly on mobile screens, causing layout issues. | Modified the CSS to use media queries that optimize the layout for smaller screen sizes, ensuring the discount value is displayed correctly without breaking the layout. |
| 3 | [Commit Link](https://github.com/luciotorelli/escoot/commit/32c796d) | Improve page 404 | The 404 error page lacks user-friendly text and styling. | Enhanced the 404 page by adding more user-friendly text, improved styling, and a link to guide users back to the homepage. |
| 4 | [Commit Link](https://github.com/luciotorelli/escoot/commit/9a9f071) | Fix centering of email confirmation template | The email confirmation template is not properly centered across different email clients. | Adjusted the HTML structure and CSS styles to ensure the content is properly centered across different email clients. |
| 5 | [Commit Link](https://github.com/luciotorelli/escoot/commit/c42bc32) | Fix orders being created with discounts when they should be blank | Orders are being created with discounts when they should not have any discounts applied. | Added validation checks in the order creation logic to ensure discounts are only applied when appropriate, preventing the creation of orders with unintended discount values. |
| 6 | [Commit Link](https://github.com/luciotorelli/escoot/commit/93b3708) | Fix product Id error on Stripe | Product ID error occurs during Stripe transactions, causing payment failures. | Corrected the product ID references in the payment processing code, ensuring that the correct IDs are used during transactions. |
| 7 | [Commit Link](https://github.com/luciotorelli/escoot/commit/50f4acb) | Fix error 404 from Stripe | 404 error is returned from Stripe during payment processing. | Updated the API endpoint URLs and ensured that all requests to Stripe are correctly formed and directed to the right endpoints. |
| 8 | [Commit Link](https://github.com/luciotorelli/escoot/commit/821149b) | Fix double orders being created due to discount codes | Double orders are being created when discount codes are applied. | Added additional checks in the order processing workflow to prevent multiple submissions or processing of the same order. |
| 9 | [Commit Link](https://github.com/luciotorelli/escoot/commit/ce8c392) | Fix webhook error "Cannot resolve keyword 'id' into field" | Webhook returns an error 'Cannot resolve keyword 'id' into field' due to incorrect keyword references. | Ensured that the webhook handler correctly references existing fields and models in the database schema, avoiding incorrect keyword references. |
| 10 | [Commit Link](https://github.com/luciotorelli/escoot/commit/50593ce) | Fix success page text breaks | Duplicate entry for the success page text breaks order summary. | Adjusted the CSS styling to ensure proper word wrapping and alignment within the container elements. |

### Feedback

| Feedback | Implemented/Fixed  | Notes |
| :---:   | :---: | :---: |
| Didn't get a confirmation message when I submitted a form | Yes  | Added toast notifications to confirm form submissions. |
| It's hard to tell if I'm logged in or not | Yes  | Added a welcome message for logged-in users and a toast notification upon login. |
| The button order on mobile was confusing, made me click "select another part" by mistake | Yes  | Reordered buttons based on mobile views to improve user experience. |
| Would like to add more than one part per product | No  | Added to future features |
| Separate models for products and services would be great | No  | Added to future features |
| Buttons looked inconsistent | Yes  | Standardized button styles across the app with consistent hover effects. |
| The desktop navbar is usually placed at the top or left | Yes  | Adjusted the navbar for mobile at the bottom and for desktop to the left. |
| Display all orders in one single page | Yes  | Divided the order page into sections to display all orders of the current logged-in user. |

### Validation

- The code for all Python files (aside from settings.py) was tested against [provided CI Python Linter](https://pep8ci.herokuapp.com).
- The code for all HTML files was tested against [W3C Markup validation service](https://validator.w3.org/).
- The code for the CSS file was tested against [W3C CSS validation service](https://jigsaw.w3.org/css-validator/).
- The code for the JavaScript file was tested against [JShint](https://jshint.com/).

No errors were displayed at final deployment.

### Lighthouse

Google Chrome built-in Lighthouse was used to test all pages, which returned an acceptable average score of 92 for all categories.

---

### Deployment

1. **Database Setup**: Begin by configuring the database. If you're using PostgreSQL, you can set up a PostgreSQL database using [ElephantSQL](https://www.elephantsql.com). Follow these steps:
   - Sign up for an account on ElephantSQL.
   - Create a new instance with a unique name, like your project name.
   - Choose the Tiny Turtle (Free) plan.
   - Select the region and data center closest to you.
   - Once created, note down the database URL and password.

2. **Cloudinary API Integration**: To store media assets online, integrate the [Cloudinary API](https://cloudinary.com) into your application:
   - Create a Cloudinary account.
   - On your Cloudinary Dashboard, obtain your API Environment Variable.
   - Copy the API key, removing `CLOUDINARY_URL=` to leave only the key.
   - Add to your environment variable "DATABASE_URL"

3. **Deploying on Heroku**:
   - Sign up for a Heroku account if you haven't already.
   - Create a new app from your Heroku Dashboard.
   - Access your app's settings and set up environment variables:
      - `DATABASE_URL`: Your PostgreSQL database URL.
      - `SECRET_KEY`: Your chosen secret key.
      - `CLOUDINARY_URL`: Your Cloudinary API key.
      - `DEBUG_VALUE`: True or False.
      - `STRIPE_PUBLIC_KEY`: Your Stripe public key.
      - `STRIPE_SECRET_KEY`: Your Stripe secret key.
      - `STRIPE_WH_SECRET`: Your Stripe webhook secret.
      - `MAILCHIMP_API_KEY`: Your Mailchimp API key.
      - `MAILCHIMP_LIST_ID`: Your Mailchimp list ID.
   - Ensure you have the following files in your project:
      - `requirements.txt`: List your project's requirements.
      - `Procfile`: Create this file with the content `web: gunicorn app_name.wsgi`.
   - Connect your GitHub repository to your Heroku app.
   - Choose automatic deployment from Heroku or manually push your code.

4. **Local Deployment for Testing**:
   - Clone or fork the project repository to your local machine.
   - Install project requirements using `pip3 install -r requirements.txt`.
   - Create an `env.py` file at the root level, adding the following environment variables for local testing:

     ```python
     import os

     os.environ["DATABASE_URL"] = "your_database_url"
     os.environ["SECRET_KEY"] = "your_secret_key"
     os.environ["CLOUDINARY_URL"] = "your_cloudinary_url"
     os.environ["DEBUG_VALUE"] = "True"
     os.environ["STRIPE_PUBLIC_KEY"] = "your_stripe_public_key"
     os.environ["STRIPE_SECRET_KEY"] = "your_stripe_secret_key"
     os.environ["STRIPE_WH_SECRET"] = "your_stripe_wh_secret"
     os.environ["MAILCHIMP_API_KEY"] = "your_mailchimp_api_key"
     os.environ["MAILCHIMP_LIST_ID"] = "your_mailchimp_list_id"
     ```

   - Run the Django app: `python3 manage.py runserver`.
   - Perform migrations: `python3 manage.py makemigrations`, then `python3 manage.py migrate`.
   - Create a superuser for local testing: `python3 manage.py createsuperuser`.

5. In case you would like to fork, click the "Fork" button at the top right of the repository's page. This creates a copy of the repository under your GitHub account and then you can follow the steps above for local or Heroku deployment.
