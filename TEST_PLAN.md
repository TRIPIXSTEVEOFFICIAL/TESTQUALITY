# Test Plan: OrangeHRM Login Functionality

## 1. Objective

To verify that the login functionality of the OrangeHRM application works correctly for both valid and invalid credential combinations using automated testing.

---

## 2. Test Environment

* Operating System: Windows
* Browser: Google Chrome
* Automation Tool: Selenium WebDriver
* Test Framework: PyTest
* Programming Language: Python

---

## 3. Test Scope

### In Scope

* Login page validation
* Username and password field handling
* Login button functionality
* Dashboard redirection for valid credentials
* Prevention of access for invalid credentials

### Out of Scope

* UI/UX design validation
* Performance testing
* Advanced security testing

---

## 4. Test Data

| Username  | Password  | Description                 |
| --------- | --------- | --------------------------- |
| Admin     | admin123  | Valid credentials           |
| Admin     | wrongpass | Invalid password            |
| wronguser | admin123  | Invalid username            |
| wronguser | wrongpass | Invalid username & password |
| (empty)   | (empty)   | Empty fields                |
| (empty)   | admin123  | Empty username              |
| Admin     | (empty)   | Empty password              |

---

## 5. Test Cases

### TC01: Valid Login

* **Steps:** Enter valid username and password, click Login
* **Expected Result:** User is redirected to the dashboard page

### TC02: Dashboard Redirect Validation

* **Steps:** Login using valid credentials
* **Expected Result:** Dashboard page loads successfully

### TC03–TC08: Invalid Login Scenarios

* **Steps:** Enter invalid or empty credentials and click Login
* **Expected Result:** User is not redirected to the dashboard

---

## 6. Entry Criteria

* Application is accessible
* Test environment is ready
* Required tools and dependencies are installed

---

## 7. Exit Criteria

* All planned test cases executed
* Test results reviewed
* Defects identified if any

---

## 8. Risks and Assumptions

### Risks

* UI changes may affect element locators
* Network instability may impact test execution

### Assumptions

* Demo site credentials remain unchanged
* Chrome browser is available on the test machine

---

## 9. Approval

This test plan is created for academic and learning purposes.