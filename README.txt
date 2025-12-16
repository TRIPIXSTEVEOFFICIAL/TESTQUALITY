Hello! Welcome to my README.txt and my final deliverables for TESTQUALITY
This is the OrangeHRM website we used and tried to automate but
i mainly focused on the sign up and login page.

On what i have right now in my code:

Pytest - running the commands (later)
Comments - to help it understand easily on what it is
Asserts - for the messages and assumes on what to run
Wedriver - to functional its website and must needed one
Teardown - have its own functionally as well. yield cause after opening the website driver.quit() it will automatically closes the website
Fixtures - automatic teardown, clean code, reusability
Xpath, By.NAME, send_keys, .click - these are the elements of selenium

After seeing the code i used these comamnds to run Pytest

Pytest
Pytest -v
Pytest --html=report.html
Pytest -s
Pytest -m