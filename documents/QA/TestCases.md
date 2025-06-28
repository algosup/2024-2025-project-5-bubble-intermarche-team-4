This test suite covers all key features and workflows based on the Functional Specifications and Test Plan.

⸻

## 1. Multilingual Support

### TC-001: Language Dropdown Behavior
	•	Precondition: App is opened.
	•	Steps:
	1.	Click on the language dropdown.
	2.	Select “English”.
	•	Expected Result: All UI elements are translated to English.

### TC-002: Language Persistence Across Pages
	•	Steps:
	1.	Change to “Spanish” on homepage.
	2.	Navigate to Product Page.
	•	Expected Result: Page content remains in Spanish.

⸻

## 2. Onboarding (Sign-Up Flow)

### TC-003: Country & Language Input Validation
	•	Steps:
	1.	Leave one dropdown empty.
	2.	Try to continue.
	•	Expected Result: Continue button remains disabled.

### TC-004: Successful Onboarding
	•	Steps:
	1.	Select “Italy” and “Italian”.
	2.	Click Continue.
	•	Expected Result: Redirected to QR scan flow or homepage.

⸻

## 3. QR Code Flows

### TC-005: QR Code - Entrance
	•	Steps:
	1.	Scan entrance QR.
	•	Expected Result: Redirects to Sign-Up Page.

### TC-006: QR Code - Wine Aisle
	•	Steps:
	1.	Scan wine aisle QR.
	•	Expected Result: Options shown: “Find a wine” / “Something to accompany my wine”

### TC-007: QR Code - Cheese Aisle
	•	Steps:
	1.	Scan cheese aisle QR.
	•	Expected Result: Options shown: “Find a cheese” / “Something to accompany my cheese”

⸻

## 4. Recommendation Flow

### TC-008: Recommendation Based on Dish
	•	Steps:
	1.	Search for “Boeuf Bourguignon”.
	2.	Click Recommend.
	•	Expected Result: Suggests red wine and hard/cow cheeses.

### TC-009: Season-Specific Suggestion
	•	Precondition: Current season = winter.
	•	Steps:
	1.	Enter country: France.
	2.	Select mid-price cheese.
	•	Expected Result: Suggests red wine suited for winter.

⸻

## 5. Barcode Scanning

### TC-010: Successful Barcode Match
	•	Steps:
	1.	Scan product barcode from Intermarché DB.
	•	Expected Result: Redirects to Product Page with correct data.

### TC-011: Invalid Barcode Handling
	•	Steps:
	1.	Scan unknown barcode.
	•	Expected Result: Displays “Product not found” with Retry button.

⸻

## 6. Product Filtering

### TC-012: Filter by Wine Type & Price
	•	Steps:
	1.	Go to Wines Discovery Page.
	2.	Apply filters: Type = Red, Price = 5–15€.
	•	Expected Result: List updates with red wines in range.

### TC-013: Cheese Filter by Milk Type
	•	Steps:
	1.	Go to Cheese Discovery.
	2.	Filter: Milk = Goat.
	•	Expected Result: Only goat milk cheeses are shown.

⸻

## 7. Product Tags

### TC-014: Tag Click Filter
	•	Steps:
	1.	Click on tag “Rosé” on a product.
	•	Expected Result: Redirects to filtered product list showing all Rosé wines.

⸻

## 8. Search Mechanic

### TC-015: Typo Tolerance
	•	Steps:
	1.	Enter “camember” in search.
	•	Expected Result: Suggests “Camembert”.

### TC-016: Search + Filter Combination
	•	Steps:
	1.	Search “Savoie”
	2.	Filter: Milk = Cow.
	•	Expected Result: Products match both criteria.

⸻

## 9. Mix & Match Feature

### TC-017: Fixed Combination Display
	•	Steps:
	1.	Open Mix & Match section.
	•	Expected Result: Displays 5 curated combos (e.g., Cod Brandade + Cinsault Rosé + Figou).

⸻

## 10. UI Responsiveness & Accessibility

### TC-018: Mobile Layout Scaling
	•	Steps:
	1.	Open on iPhone X and Pixel 4.
	•	Expected Result: Layout adapts, text is readable.

### TC-019: Language Button Contrast
	•	Steps:
	1.	Navigate to Home page.
	•	Expected Result: Language toggle has sufficient contrast (WCAG).

⸻

## 11. Performance

### TC-020: Load Time
	•	Steps:
	1.	Open homepage over 4G.
	•	Expected Result: Loads within 2 seconds.

### TC-021: Search Response Time
	•	Steps:
	1.	Type search term.
	•	Expected Result: Results update in <1 second.

⸻

## 12. Error States

### TC-022: Broken Image Handling
	•	Steps:
	1.	Open Product Page with missing image.
	•	Expected Result: Shows placeholder image.

### TC-023: API Timeout Simulation
	•	Steps:
	1.	Disconnect network during product fetch.
	•	Expected Result: Show error message and retry option.