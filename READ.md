# QA Automation Testing Framework

## Project Overview
A modular and scalable QA Automation Testing Framework developed using Python, Selenium, and PyTest.

This framework automates web application testing workflows including:
- UI Login Validation
- Data-Driven Testing
- Broken Link Validation
- HTML Report Generation
- Screenshot Capture
- Execution Logging

The project follows industry-level automation concepts such as:
- Page Object Model (POM)
- Modular Framework Design
- External Test Data Handling
- Automated Reporting

---

# Technologies Used

- Python
- Selenium
- PyTest
- PyTest HTML Reports
- Pandas
- OpenPyXL
- Requests
- WebDriver Manager

---

# Key Features

## 1. UI Automation Testing
Automated login validation for:
- Valid Login
- Invalid Login
- Empty Username
- Empty Password

---

## 2. Page Object Model (POM)
Implemented scalable POM architecture for:
- reusable locators
- maintainable automation
- cleaner test structure

---

## 3. Data-Driven Testing
Implemented Excel-based test execution using:
- Pandas
- parameterized testing

---

## 4. Broken Link Validation
Automatically validates website links and detects broken URLs using HTTP status codes.

---

## 5. HTML Reporting
Generates professional execution reports using pytest-html.

---

## 6. Screenshot Capture
Automatically captures timestamped screenshots during test failures.

---

## 7. Logging System
Maintains execution logs for:
- debugging
- monitoring
- execution tracking

---

# Project Structure

```plaintext
QA_Automation_Framework/
│
├── logs/
├── pages/
├── project_screenshots/
├── reports/
├── screenshots/
├── tests/
├── utils/
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Tests

```bash
pytest tests/test_login.py -v
```

---

# Generate HTML Report

```bash
pytest tests/test_login.py --html=reports/report.html --self-contained-html
```

---

# Sample Features Demonstrated

- Selenium UI Automation
- PyTest Framework Integration
- Data-Driven Testing
- Logging
- Screenshot Handling
- Broken Link Validation
- POM Architecture

---

# Future Improvements

- API Automation Testing
- Parallel Test Execution
- CI/CD Integration
- Docker Support
- Cloud Browser Execution