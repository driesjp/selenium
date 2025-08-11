# Selenium Python Automation Starter Kit

This project is a foundational example of a web automation script written in Python using the Selenium library. It demonstrates a clean, robust, and maintainable approach to UI testing, designed to be easily expanded and integrated into a larger framework.

# Key features & demonstrated skills

  - Modular and reusable code: The core logic is encapsulated in helper functions for common actions like finding elements, clicking, typing, and verifying text. This promotes code reuse and makes test scripts easy to read and maintain.
  - Robust error handling: The script includes try/except blocks to gracefully handle potential failures such as NoSuchElementException and TimeoutException, ensuring the test doesn't crash and provides useful debugging information.
  - Pseudo-intelligent retries: Functions like find_element, click, and type_text have built-in retry logic to overcome minor timing issues and make the tests more stable and reliable.
  - Basic formatted logging: All key actions, warnings, and errors are logged to both the console and a test_log.txt file, providing a clear history of the test run for debugging and analysis.
  - Self-contained environment: The project includes a simple index.html file for a fully reproducible test environment and a requirements.txt file for easy dependency management.

# Getting started

To run this project, you need Python installed on your system.

  Clone this repository to your local machine.
```
git clone https://github.com/driesjp/selenium
cd selenium
```
   
Install the required libraries using pip.
    
```
pip install -r requirements.txt
```

# How to run

Simply execute the main script from your terminal:
```
python test.py
```

The script will launch a browser, navigate to the local index.html file, perform a series of interactions, and then close the browser. Test results will be printed to the console and saved to test_log.txt.

# Ideas for expansion

This project serves as a starting point.
There are several ways to expand this into a more comprehensive framework by:
  - Adding a more structured testing framework (e.g., using Pytest).
  - Implementing data-driven testing with external data sources (e.g., CSV or JSON).
  - Integrating with a CI/CD pipeline for automated test runs.
  - Expanding the test scenarios to cover more complex web interactions.
