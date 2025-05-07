<div align="center">

# Functional Specifications – Team 4

</div>

## Table of Contents

<details>

- [Functional Specifications – Team 4](#functional-specifications--team-4)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Project Overview](#project-overview)
    - [Project Definition](#project-definition)
      - [Vision](#vision)
      - [Market Analysis](#market-analysis)
      - [Scope](#scope)
      - [Deliverables](#deliverables)
  - [Project Organization](#project-organization)
      - [Project Representatives](#project-representatives)
      - [Team \& Roles](#team--roles)
      - [Stakeholders](#stakeholders)
    - [Resources](#resources)
      - [Team](#team)
      - [Client](#client)
      - [Technology](#technology)
      - [Database](#database)
    - [Assumptions](#assumptions)
    - [Constraints](#constraints)
  - [Audience \& Use Cases](#audience--use-cases)
    - [Target Audience](#target-audience)
      - [Tourists](#tourists)
      - [Casual Shoppers](#casual-shoppers)
      - [Wine Lovers](#wine-lovers)
      - [Wine Newbies](#wine-newbies)
  - [UI/UX](#uiux)
    - [Graphic Charter](#graphic-charter)
    - [Logotype](#logotype)
      - [Base Logo](#base-logo)
      - [Intermarché Super Logo](#intermarché-super-logo)
      - [Round Intermarché Logo](#round-intermarché-logo)
    - [Logo Usage Guidelines](#logo-usage-guidelines)
    - [Logo Liability Disclaimer](#logo-liability-disclaimer)
    - [Color Palette](#color-palette)
    - [Mockups](#mockups)
      - [Sign-Up Page](#sign-up-page)
      - [Menu Page](#menu-page)
  - [Functional Requirements](#functional-requirements)
    - [Multilingual Support](#multilingual-support)
    - [QR Code Accessibility](#qr-code-accessibility)
      - [Example: Wine Aisle QR Code Flow](#example-wine-aisle-qr-code-flow)
      - [If the user chooses "Something to accompany my wine"](#if-the-user-chooses-something-to-accompany-my-wine)
      - [If the user chooses "Find a wine"](#if-the-user-chooses-find-a-wine)
    - [Search Mechanic](#search-mechanic)
    - [List Of Products](#list-of-products)
    - [Product Tags](#product-tags)
    - [Research Filters](#research-filters)
    - [Bar-Code Scanner](#bar-code-scanner)
    - [In-Shop Location of Products](#in-shop-location-of-products)
    - [Recommendation Algorithm](#recommendation-algorithm)
      - [Client's Origin](#clients-origin)
    - [Local Product Spotlight](#local-product-spotlight)
  - [Non-Functional Requirements](#non-functional-requirements)
    - [Performance](#performance)
    - [Scalability](#scalability)
    - [Reliability](#reliability)
    - [Accessibility](#accessibility)
  - [Recommended Minimum Hardware Requirements](#recommended-minimum-hardware-requirements)
  - [Future Improvements](#future-improvements)
    - [Product Opinion](#product-opinion)
  - [Legal \& Compliance](#legal--compliance)
    - [Data Protection and Privacy](#data-protection-and-privacy)
    - [Accessibility](#accessibility-1)
  - [Conclusion](#conclusion)

</details>

---

## Introduction

This document outlines the **functional specifications** for the development of a mobile web application for [Intermarché](https://www.intermarche.com/?srsltid=AfmBOop3uKBkrZ9x8Szj8EtpgHOqzuk_bHP3x1af4_9TrFf_640On9RY).
Its purpose is to clearly define the project's requirements, scope, and objectives, ensuring that all stakeholders share a unified understanding of what is being developed.

### Project Overview

The goal of this project is to deliver a user-friendly **mobile web application** for Intermarché customers, providing personalized assistance when choosing wine and/or cheese upon entering the store.
The app will suggest the most suitable wine or cheese based on the user's dish, taste preferences, or filters. It aims to simplify the selection process and enhance customer satisfaction by offering tailored recommendations.

---

### Project Definition

#### Vision

Our vision is to develop an **open-source mobile web application** as a proof of concept for Intermarché, designed to:

- Simplify the pairing of food with wine and cheese
- Highlight and promote **local producers**
- Encourage discovery of **regional specialties**
- Provide **personalized recommendations** based on user preferences and origin
- Be accessible to a **multilingual audience**
- Attract more customers and **increase in-store sales**
- Feature an **intuitive and inclusive interface** for all adult users
- No-need to **create an account**
- **No internet dependency** (if possible)

#### Market Analysis

A similar recommendation system already exists on Intermarché’s official website: [Wine Selection Tool](https://www.intermarche.com/recherche/vin). However, after evaluating its current features, we have identified several areas where our mobile web application can offer significant improvements and differentiation:

- **No Account Required** – Users can access recommendations without the need to create an account, lowering the barrier to entry.
- **Enhanced User Experience** – A more intuitive and streamlined interface optimized for mobile devices.
- **Multilingual Support** – The web application will be accessible in multiple languages, ensuring usability for a wider audience, including tourists and non-native speakers.
- **Personalized Recommendations** – Tailored suggestions based on individual preferences, tastes, and user input.
- **Value-Added Features** – Additional options such as pairing suggestions, local producer highlights, and dish-based recommendations that go beyond the existing tool.
- **Bar-code scanner** - Bar-code reader that sends the user to the product page.

These improvements aim to create a unique, user-focused experience that not only enhances customer satisfaction but also strengthens Intermarché’s digital ecosystem.

#### Scope

This project focuses on developing a **mobile web application** for Intermarché that enhances the customer shopping experience by helping users select the most appropriate wine and/or cheese based on their dish, preferences, or filters. The web application will serve as a **proof of concept** and prioritize ease of use, personalization, and support for local products.

**In Scope:**

- Development of a **mobile-first web application** for Android and iOS
- **Recommendation engine** for pairing wine and cheese with dishes
- **User preference filtering** (taste, region, type, etc.)
- **Multilingual support** (French, English, German, Spanish)
- **Highlighting local producers** and regional specialties
- Simple **onboarding without requiring an account**
- Basic **mockups and UI/UX design**
- Integration with a **test database** of wine, and cheese provided by Saint-Rémy de Florence Intermarché
- Delivery of an **open-source proof of concept**

**Out of Scope:**

- Full integration with Intermarché’s existing database or e-commerce system
- Loyalty program integration or account-based features
- Payment or ordering functionality
- Advanced AI or machine learning recommendation systems
- Offline mode or heavy caching for disconnected environments

This scope ensures a focused and achievable MVP (Minimum Viable Product), allowing Intermarché to evaluate the concept's value and gather user feedback for future development.

**Technology Used:**

The product is developed using the no-code tool Bubble.io.

#### Deliverables

| Deliverables             | Date       |
| ------------------------ | ---------- |
| Functional Specification | 16/05/2025 |
| Technical Specification  | 28/05/2025 |
| Test Plan                | 06/06/2025 |
| User Manual              | 16/06/2025 |
| Code                     | 16/06/2025 |

---

## Project Organization

#### Project Representatives

| Entities                           | Representative                                                                     |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| Intermarché's Representative       | [Célia Moustier](moustier09@hotmail.fr)                                            |
| Intern Aisle Responsible           | [Chrys Cadeau](chryscadeau13@gmail.com)                                            |
| [ALGOSUP](https://www.algosup.com) | [Franck Jeannin](franck.jeannin@algosup.com)                                       |
| Team 4                             | [Clementine Curel](https://www.linkedin.com/in/clementinecurel/) - Project Manager |

#### Team & Roles

| Full Name        | Role              | Role Description                                                         | Contact                                                           |
| ---------------- | ----------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Clementine Curel | Project Manager   | Responsible for project planning, coordination, and communication        | [LinkedIn](https://www.linkedin.com/in/clementinecurel/)          |
| Thibaud Marlier  | Program Manager   | Ensures project meets expectations; oversees design and functional specs | [LinkedIn](https://www.linkedin.com/in/thibaudmarlier/)           |
| Jason Grosso     | Technical Lead    | Oversees technical aspects, including architecture and implementation    | [LinkedIn](https://www.linkedin.com/in/jason-grosso-847b39251/)   |
| Elone Delille    | Quality Assurance | Ensures quality of deliverables and adherence to requirements            | [LinkedIn](https://www.linkedin.com/in/elonedelille/)             |
| Emilien Chinsy   | Software Engineer | Develops the mobile web application and the algorithm                    | [LinkedIn](https://www.linkedin.com/in/emilien-chinsy-5a794632b/) |
| Robin Goumy      | Technical Writer  | Responsible for the User Manual and UX                                   | [LinkedIn](https://www.linkedin.com/in/robin-goumy-66452832a/)    |

#### Stakeholders

| Stakeholders           | Interest                                                |
| ---------------------- | ------------------------------------------------------- |
| Intermarché's customer | Primary beneficiary                                     |
| Intermarché            | Project initiator and secondary beneficiary             |
| ALGOSUP                | Technology provider, second project initiator           |
| ALGOSUP's students     | Project contributors, developers, testers, designers... |

### Resources

#### Team

A team of 6 members, each with clearly defined roles and responsibilities.

- **Estimated Project Duration:** 110 hours
- **Estimated Total Workload:** 660 man-hours

#### Client

- Contact has been established with the **Intermarché store in Issoudun** to test the product on site.
- Communication is also in progress with the **department manager at Saint-Rémy-de-Provence** for further product validation.

#### Technology

- Supervised access to **Bubble.io** with support from an instructor for guidance and troubleshooting.

#### Database

You can find the database [here](../../data/Data%20-%20Wine%20and%20Cheese.xlsx)

- The client has provided an Excel database containing detailed information about wines and cheeses available in-store.

The database includes:

- Product barcodes in the following formats:

  - `ITM8`
  - `EAN PRIO`

- Product name
- Region of origin
- Country of origin
- Product type:

  - Cheese
  - Yogurt
  - Red Wine
  - White Wine
  - Rosé Wine
  - Sparkling Wine
  - Other dairy products

- Milk type (for cheese/dairy products)

---

### Assumptions

- The client will provide timely feedback during key development milestones.
- The database provided is accurate, up-to-date, and reflective of actual stock.
- Users will access the web application primarily on modern web browsers with internet connectivity.
- Bubble.io offers all the required features to build the desired functionalities without needing external integrations.
- The test environments provided by Intermarché (Issoudun and Saint-Rémy-de-Provence) will support functional validation of the prototype.
- Product classifications (e.g., wine types, milk types) are consistent across all entries in the database.

---

### Constraints

- The project must be developed using **Bubble.io**, as per the client’s technological preference.
- It must remain **open-source** to ensure transparency and encourage community contributions.
- All features must be aligned with the **client’s functional and aesthetic requirements**.
- The final product must adhere to **Intermarché’s brand values**, including quality, simplicity, and accessibility.

---

## Audience & Use Cases

### Target Audience

#### Tourists

**Age Range:** 25–60

**Persona Name:** _Anna, the Curious Traveler_

**Description:**
Anna is a tourist visiting France, eager to explore French culture through its gastronomy. She doesn’t speak fluent French and is unfamiliar with local wine or cheese. She often shops at Intermarché for convenience and wants help choosing authentic regional products.

**How They’ll Use the App:**
Anna opens the app in-store, sets her preferred language to English, and browses local wine and cheese pairings recommended for regional dishes. She filters by “local products” and gets insights into producers, allowing her to bring a taste of France home.

<div align="center">

<img src="./images/personas/anna.png" width=200px>

</div>

---

#### Casual Shoppers

**Age Range:** 30–55

**Persona Name:** _Marc, the Busy Parent_

**Description:**
Marc is a working parent who shops weekly at Intermarché. He’s not a wine connoisseur but wants to make nice meals for his family. Convenience and speed matter most to him.

**How They’ll Use the App:**
Marc uses the app to quickly match wine or cheese with meals he already plans to cook. He appreciates the simple interface, no-login access, and dish-based suggestions like “Which wine goes with lasagna?”

<div align="center">

<img src="./images/personas/marc.png" width=200px>

</div>

---

#### Wine Lovers

**Age Range:** 35–65

**Persona Name:** _Claire, the Wine Enthusiast_

**Description:**
Claire has a deep appreciation for wine and occasionally hosts tastings. She values quality, regional authenticity, and food pairing precision. She enjoys exploring lesser-known wines and artisanal cheeses.

**How They’ll Use the App:**
Claire uses advanced filters to explore pairing combinations, discover hidden gems from local producers, and save preferred pairings. She might share her recommendations with friends and even plan tasting menus with the help of the app.

<div align="center">

<img src="./images/personas/claire.png" width=200px>

</div>

---

#### Wine Newbies

**Age Range:** 18–30

**Persona Name:** _Lucas, the Curious Student_

**Description:**
Lucas is new to wine and cheese culture but wants to learn. He’s open to trying new things but often feels overwhelmed by the selection in-store.

**How They’ll Use the App:**
Lucas enters a few taste preferences (fruity, light, etc.) and selects a dish he plans to cook with friends. The app gives him easy, beginner-friendly pairings with short descriptions and explanations — helping him gain confidence with each use.

<div align="center">

<img src="./images/personas/lucas.png" width=200px>

</div>

---

## UI/UX

### Graphic Charter

This project follows the official Intermarché graphic charter to ensure visual consistency and brand recognition. The following elements reflect the branding guidelines.

---

### Logotype

The web application uses official Intermarché logos provided under the brand’s existing identity. Below are the logos available for use:

---

#### Base Logo

<div align="center">

<img src="./images/logo/LogoIntermarcheBase.jpg" alt="Intermarché Base Logo">

</div>

This is the main Intermarché logo, used primarily for branding, advertising, and digital web applications.

---

#### Intermarché Super Logo

<div align="center">

<img src="./images/logo/LogoIntermarcheSuper.png" alt="Intermarché Super Logo">

</div>

This logo represents **Intermarché Super**, supermarkets with a strong focus on fresh food products, tailored to local clientele.
It is the **primary logo** for this project, as the main client is **Intermarché Super in Saint-Rémy-de-Provence**.

---

#### Round Intermarché Logo

<div align="center">

<img src="./images/logo/LogoIntermarcheRound.jpg" alt="Round Intermarché Logo" width="300px">

</div>

This round version of the logo is ideal for **loading pages** or compact areas where a circular design is more fitting.

---

### Logo Usage Guidelines

According to Intermarché’s official branding policy:

- The logo must **not** be altered in shape, proportions, or color.
- A **minimum usage size of 25mm** is required for optimal readability.
- Logos must be displayed on a **white background** to maintain visual clarity.

---

### Logo Liability Disclaimer

> **Disclaimer:**
> All logos used in this project are the intellectual property of **Intermarché** and its affiliates.
> They are used **exclusively** for educational, prototyping, or demonstrative purposes, and **not for commercial redistribution**.
> Our team claims **no ownership** over these visual assets.

---

### Color Palette

The application’s color scheme aligns with Intermarché’s official brand colors to maintain consistency.

| Color     | RGBA Value         | Example                                       |
| --------- | ------------------ | --------------------------------------------- |
| **Red**   | 226, 0, 26, 100    | ![Red](./images/color/IntermarcheRed.png)     |
| **Black** | 26, 23, 26, 100    | ![Black](./images/color/IntermarcheBlack.png) |
| **Grey**  | 220, 220, 220, 100 | ![Grey](./images/color/IntermarcheGrey.png)   |

---

### Mockups

A visual prototype of the application has been designed using Figma. You can view the interactive mockup [here](https://www.figma.com/design/FiDisAv5pKKYsvQBODIIYx/BUBBLE-INTER?node-id=0-1&t=5USWv2xX2utpUy6t-1).

This mockup outlines the core user flows and primary pages of the application, with a focus on intuitive navigation and an engaging user experience.

---

#### Sign-Up Page

Although not a traditional user sign-up, this onboarding process helps tailor the experience by understanding the user’s background. The choices made here are essential for personalized recommendations — for instance, a user from the United Kingdom might receive different pairings than one from Germany. More details can be found in the [Recommendation Algorithm](#recommendation-algorithm) section.

**Information Collected:**

- The user's country of origin — used to refine recommendation logic
- The language spoken — used for full interface translation

<div align="center">

<img src="./images/pages/SignUpPage.png" width="200px" alt="Sign-Up Page Mockup">

</div>

**UI Elements:**

- Two dropdown fields: one for selecting the country, and one for the preferred language
- A "Continue" button that is **disabled** by default and becomes **active** only when both fields are filled

**Available Countries:**

- France
- United Kingdom
- Spain
- Germany
- Italy
- China
- Other

Supported languages can be found in the [Multilingual Support](#multilingual-support) section.

**Button Behavior:**

- **Disabled state:** Grey background, inactive

- **Enabled state:** Red background, active

<div align="center">

![alt](./images/pages/buttons/ButtonDisabled.png)

</div>

- **Enabled state:** Red background, active

<div align="center">

![alt](./images/pages/buttons/ButtonActive.png)

</div>


These button colors are defined in the [Color Palette](#color-palette) section.

**Button Values**

- Height: 30px
- Width: 195px
- Centered
- Padding: 15px

#### Menu Page

---

## Functional Requirements

### Multilingual Support

- **Functionality:**
  The mobile application must be available in multiple languages.

- **Details:**

  - The following languages must be supported:

    - French
    - English
    - Spanish
    - German
    - Italian
    - Chinese

  - Additional languages can be supported, but are not mandatory.
  - The entire application interface must be fully translated automatically when a language is selected.

---

### QR Code Accessibility

- **Functionality:**
  The application should be accessible by scanning a QR code.

- **Details:**

  - Three QR codes will be placed in the store:

    - At the store entrance
    - Near the wine aisle
    - Near the cheese aisle

  - Each QR code will redirect users to a **personalized interface** based on their location.

#### Example: Wine Aisle QR Code Flow

When the user scans the QR code near the **wine aisle**, the following screen appears:

<div align="center">

<img src="./images/pages/ScanQrCodeWelcomePage.png" width=200px>

</div>

The user is presented with two options:

1. **Find a wine** based on their preferences
2. **Something to accompany my wine** (such as food or cheese) for a wine they already have

---

#### If the user chooses "Something to accompany my wine"

- The user is prompted to input the **name of the wine** they have selected.
- After submission, they are redirected to the product page, which includes:

  - Suggested **dishes** that pair well with the wine
  - Recommended **cheeses** that complement both the wine and the chosen dish

> [!NOTE]
> More information about the recommendation system can be found in the [Recommendation Algorithm](#recommendation-algorithm) section.

---

#### If the user chooses "Find a wine"

- The user can apply filters to refine their search, including:

  - **Price range**
  - **Country of origin**
  - **Selected dish**
  - **Selected cheese**
  - **Additional preferences**

> [!NOTE]
> Details about filtering options can be found in the [Research Filters](#research-filters) section.

### Search Mechanic

### List Of Products

### Product Tags

### Research Filters

- **Functionality:**
  The mobile application must allow users to apply filters when searching for products

- **Details:**
  
  The Users can use the following filters to refine their search:

  - the type of product,
  - the price range,
  - the seasonality of the product,
  - the region or country of origin

  If the Users specified the type of of product they are looking for, they will have access to secific filters for that type of product:
  - for the **wine** type, the user unlock the following filters:
    - the color of the wine (red, white, rosé, sparkling),
    - the grape variety,
    - the sweetness level (dry, semi-dry, sweet),
    - the alcohol content
  - for the **cheese** type, the user unlock the following filters:
    - the milk type (cow, goat, sheep),
    - the texture (soft, hard, semi-soft),
    - the aging process (fresh, aged, blue-veined),
    - the flavor profile (mild, strong, spicy)
  - for the **meal** type, the user unlock the following filters:
    - the dieatary restrictions (vegetarian, vegan, gluten-free),
    - the region of origin (Provence, Bordeaux, ...)
  
### Bar-Code Scanner

### In-Shop Location of Products

### Recommendation Algorithm

#### Client's Origin

### Local Product Spotlight

---

## Non-Functional Requirements

### Performance

- The application must provide a smooth and responsive user experience across all supported devices.
- Page load times should not exceed **2 seconds** under normal network conditions.
- Recommendations and search results must be generated within **1 second** of user input.
- The backend must be capable of handling up to **100 concurrent users** without degradation in performance.

### Scalability

- The system must be scalable to support future growth, including:

  - An increasing number of users (up to 10,000+ active users).
  - Additional products (e.g., regional additions to wine and cheese).
  - Expansion into new countries or language support.

- The application architecture should support easy deployment to new shops or regions without structural changes.

### Reliability

- The system must achieve **99.5% uptime** on a monthly basis.
- All critical user data (e.g., preferences, search history, selections) should be saved reliably, even in case of crashes.
- A fallback mechanism must be in place to handle third-party service failures (e.g., translation, barcode scanning).

### Accessibility

- All functionalities should be usable by people with visual impairments, including support for:

  - Screen readers
  - High contrast modes
  - Keyboard navigation

- Texts should be legible across various screen sizes, and interactions must be intuitive and user-friendly.

---

## Recommended Minimum Hardware Requirements

_To be defined – specify device compatibility (e.g., iOS/Android, minimum OS versions)._

---

## Future Improvements

### Product Opinion

---

## Legal & Compliance

### Data Protection and Privacy

- Do not store any data related to the user.

### Accessibility

- The mobile application must comply with accessibility standards to accommodate all types of disabilities.

---

## Conclusion

_To be defined – summarize the document and next steps._

---
