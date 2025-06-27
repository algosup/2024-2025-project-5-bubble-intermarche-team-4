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