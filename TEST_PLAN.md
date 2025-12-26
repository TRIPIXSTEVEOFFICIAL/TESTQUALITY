Test Plan: OrangeHRM Login Functionality
1. Objective

The purpose of this test plan is to validate that the login feature of OrangeHRM works correctly.
This includes verifying both valid and invalid username/password combinations using automated tests.

2. Test Environment

Operating System: Windows
Browser: Google Chrome
Automation Tool: Selenium WebDriver
Testing Framework: PyTest
Programming Language: Python

3. Test Scope
In Scope

Login page behavior
Username and password field validation
Login button functionality
Dashboard redirection for valid users
Blocking access for invalid credentials

Out of Scope

UI/UX design validation
Performance/load testing
Advanced security testing

4. Test Data
Username	Password	Description
Admin	admin123	Valid credentials
Admin	wrongpass	Invalid password
wronguser	admin123	Invalid username
wronguser	wrongpass	Invalid username and password
(empty)	(empty)	Both fields empty
(empty)	admin123	Empty username
Admin	(empty)	Empty password

5. Test Cases
TC01: Valid Login

Steps: Enter valid username and password, click login.

Expected Result: User is redirected to the dashboard page.

TC02: Dashboard Redirect Check

Steps: Login using valid credentials.
Expected Result: Dashboard page loads successfully.

TC03–TC08: Invalid Login Attempts

Steps: Enter invalid or empty login credentials and click login.
Expected Result: User is not redirected to the dashboard.

6. Entry Criteria

Testing can begin when:
The OrangeHRM demo site is accessible
Test environment is properly set up
Required tools and dependencies are installed

7. Exit Criteria

Testing is complete when:
All planned test cases are executed
Test results are reviewed
Any defects are noted

8. Risks and Assumptions
Risks

UI changes may break element locators
Slow or unstable internet may impact test execution

Assumptions

Demo credentials remain unchanged
Google Chrome is installed and available

9. Approval

This test plan is created for academic and learning purposes only.