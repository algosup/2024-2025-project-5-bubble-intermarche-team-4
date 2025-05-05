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
      - [Assumptions](#assumptions)
      - [Constraints](#constraints)
  - [Audience \& Use Cases](#audience--use-cases)
    - [Target Audience](#target-audience)
    - [User Personas](#user-personas)
  - [UI/UX](#uiux)
    - [Mockups](#mockups)
  - [Functional Requirements](#functional-requirements)
  - [Non-Functional Requirements](#non-functional-requirements)
  - [Recommended Minimum Hardware Requirements](#recommended-minimum-hardware-requirements)
  - [Future Improvements](#future-improvements)
  - [Legal \& Compliance](#legal--compliance)
  - [Conclusion](#conclusion)

</details>

---

## Introduction

This document outlines the **functional specifications** for the development of a mobile application for [Intermarché](https://www.intermarche.com/?srsltid=AfmBOop3uKBkrZ9x8Szj8EtpgHOqzuk_bHP3x1af4_9TrFf_640On9RY).
Its purpose is to clearly define the project's requirements, scope, and objectives, ensuring that all stakeholders share a unified understanding of what is being developed.

### Project Overview

The goal of this project is to deliver a user-friendly **mobile application** for Intermarché customers, providing personalized assistance when choosing wine and/or cheese upon entering the store.
The app will suggest the most suitable wine or cheese based on the user's dish, taste preferences, or filters. It aims to simplify the selection process and enhance customer satisfaction by offering tailored recommendations.

---

### Project Definition

#### Vision

Our vision is to develop an **open-source mobile application** as a proof of concept for Intermarché, designed to:

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

A similar recommendation system already exists on Intermarché’s official website: [Wine Selection Tool](https://www.intermarche.com/recherche/vin). However, after evaluating its current features, we have identified several areas where our mobile application can offer significant improvements and differentiation:

- **No Account Required** – Users can access recommendations without the need to create an account, lowering the barrier to entry.
- **Enhanced User Experience** – A more intuitive and streamlined interface optimized for mobile devices.
- **Multilingual Support** – The application will be accessible in multiple languages, ensuring usability for a wider audience, including tourists and non-native speakers.
- **Personalized Recommendations** – Tailored suggestions based on individual preferences, tastes, and user input.
- **Value-Added Features** – Additional options such as pairing suggestions, local producer highlights, and dish-based recommendations that go beyond the existing tool.
- **Bar-code scanner** - Bar-code reader that sends the user to the product page.

These improvements aim to create a unique, user-focused experience that not only enhances customer satisfaction but also strengthens Intermarché’s digital ecosystem.

#### Scope

This project focuses on developing a **mobile application** for Intermarché that enhances the customer shopping experience by helping users select the most appropriate wine and/or cheese based on their dish, preferences, or filters. The application will serve as a **proof of concept** and prioritize ease of use, personalization, and support for local products.

**In Scope:**

- Development of a **mobile-first application** for Android and iOS
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

| Entities                           | Representative                                                   |
| ---------------------------------- | ---------------------------------------------------------------- |
| Intermarché's Representative       | Célia Moustier                                                   |
| Intern Aisle Responsible           | Chrys Cadeau                                                     |
| [ALGOSUP](https://www.algosup.com) | Franck Jeannin                                                   |
| Team 4                             | [Clementine Curel](https://www.linkedin.com/in/clementinecurel/) |

#### Team & Roles

| Full Name        | Role              | Role Description                                                         | Contact                                                           |
| ---------------- | ----------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Clementine Curel | Project Manager   | Responsible for project planning, coordination, and communication        | [LinkedIn](https://www.linkedin.com/in/clementinecurel/)          |
| Thibaud Marlier  | Program Manager   | Ensures project meets expectations; oversees design and functional specs | [LinkedIn](https://www.linkedin.com/in/thibaudmarlier/)           |
| Jason Grosso     | Technical Lead    | Oversees technical aspects, including architecture and implementation    | [LinkedIn](https://www.linkedin.com/in/jason-grosso-847b39251/)   |
| Elone Delille    | Quality Assurance | Ensures quality of deliverables and adherence to requirements            | [LinkedIn](https://www.linkedin.com/in/elonedelille/)             |
| Emilien Chinsy   | Software Engineer | Develops the mobile application and the algorithm                        | [LinkedIn](https://www.linkedin.com/in/emilien-chinsy-5a794632b/) |
| Robin Goumy      | Technical Writer  | Responsible for the User Manual and UX                                   | [LinkedIn](https://www.linkedin.com/in/robin-goumy-66452832a/)    |

#### Stakeholders

| Stakeholders           | Interest                                                |
| ---------------------- | ------------------------------------------------------- |
| Intermarché's customer | Primary beneficiary                                      |
| Intermarché            | Project initiator and secondary beneficiary              |
| ALGOSUP                | Technology provider, second project initiator           |
| ALGOSUP's students     | Project contributors, developers, testers, designers... |

#### Resources

_To be defined – include tools, platforms, data sources, and other technical or human resources._

#### Assumptions

_To be defined – list any assumed conditions necessary for project success._

#### Constraints

_To be defined – include limitations such as time, budget, technology, or regulations._

---

## Audience & Use Cases

### Target Audience

_To be defined – describe the main user groups (e.g., wine lovers, casual shoppers, tourists)._

### User Personas

_To be defined – include fictional examples of users to illustrate needs and behaviors._

---

## UI/UX

### Mockups

_To be defined – include visual prototypes or wireframes illustrating the app's layout and interaction flow._

---

## Functional Requirements

_To be defined – list features the app must support (e.g., product filtering, recommendation engine)._

---

## Non-Functional Requirements

_To be defined – include performance, scalability, reliability, accessibility, etc._

---

## Recommended Minimum Hardware Requirements

_To be defined – specify device compatibility (e.g., iOS/Android, minimum OS versions)._

---

## Future Improvements

_To be defined – outline features planned for future iterations (e.g., integration with loyalty cards, recipe suggestions)._

---

## Legal & Compliance

_To be defined – ensure GDPR, accessibility, and other legal standards are considered._

---

## Conclusion

_To be defined – summarize the document and next steps._

---
