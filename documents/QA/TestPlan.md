# Introduction

This Test Plan ensures that the Cheerish Bubble.io-based mobile web app is stable, functional, and aligned with all defined functional specifications before delivery. It formalizes testing activities, roles, and metrics for success, based on the complete scope of the Cheerish Functional Specifications.

# Objectives & Tasks

## Objectives

* Validate all user flows and functional features.
* Ensure multilingual functionality and personalized recommendation accuracy.
* Verify correct behavior of QR scanning and search mechanisms.
* Validate product filtering, tagging, and pairing logic.
* Confirm responsive design and browser/device compatibility.

## Tasks

1. Design test cases aligned with functional specification sections.
2. Execute manual test runs on each core page and feature.
3. Validate multilingual transitions and product data localization.
4. Test performance using Lighthouse (page load, responsiveness).
5. Simulate edge cases in recommendation algorithms.
6. Report defects and verify bug resolution.

# Test Items

* Bubble Application Front-End: Pages, workflows, recommendation logic.
* Backend: Product and tag database.
* Integrations: QR code redirection, barcode scanner, filters.

# Features to Be Tested

## In Scope

* QR code scanning & contextual redirection.
* Multilingual setup (FR, EN, ES, DE, IT, CN).
* All Discovery Pages and filtering logic.
* Barcode scanning functionality.
* Recommendation system (by context, origin, season, budget).
* Mix & Match predefined combinations.
* Responsive UI on mobile/tablet.

## Out of Scope

* External databases or e-commerce integration.
* Loyalty account features.
* In-store physical navigation guidance (planned for future).
* User reviews or dynamic ML recommendations.

# Test Approach

## Test Levels

* System Testing
* Acceptance Testing

## Test Types

* Functional
* Compatibility
* Performance/Load

## Techniques & Tools

* Manual exploratory testing.
* Structured test cases with boundary input coverage.
* Google Lighthouse (performance).
* Real device and emulator testing for compatibility.
* QR & barcode scan simulation using test labels.

# Pass/Fail Criteria

## Entry Criteria

* Complete implementation of functional requirements.
* Working deployment on a test Bubble environment.

## Exit Criteria

* > \= 95% of test cases passed.
* No "Critical" severity bugs.
* "High" severity issues resolved or mitigated.

# Test Environment

## Devices

* iPhone X and above
* Pixel 4 and above

## Browsers

* Chrome (Android/iOS)
* Safari (iOS)
* Firefox (Android/iOS)

## Network

* Simulated 4G and public LAN.

## Data

* Product database covering:

  * Meals (meal.json)
  * Wines (wines.json)
  * Cheeses (cheese.json)
* Test personas for origin/language configurations

# Roles & Responsibilities

| Role            | Responsibility                                        |
| --------------- | ----------------------------------------------------- |
| QA Engineer     | Create and execute test cases, manage defect tracking |
| Developer       | Implement fixes, provide builds, log support          |
| Project Manager | Ensure deadlines, approve releases                    |

# Risks & Contingencies

| Risk                          | Impact                 | Mitigation                              |
| ----------------------------- | ---------------------- | --------------------------------------- |
| QR/barcode not recognized     | Blocks major user flow | Validate using mock codes & logs        |
| Language not loading properly | Bad UX for tourists    | Use fallback strings, test all variants |
| Recommendation logic mismatch | Low result trust       | Retest rules, validate test use cases   |
| Limited manual QA capacity    | Slower progress        | Prioritize features by usage frequency  |

# Deliverables & Approvals

## Deliverables

* This Test Plan
* Test Case suite covering each functional requirement
* Execution logs and defect reports
* Final Test Summary Report

## Approvals

| Role         | Name             | Date   |
| ------------ | ---------------- | ------ |
| QA Engineer  | Elone Delille    | \[TBD] |
| Project Lead | Clémentine Curel | \[TBD] |
| Customer     | Célia Moustier   | \[TBD] |
