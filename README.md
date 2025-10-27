# Playwright Todo App Tests with Allure

This project contains automated tests for the **TodoMVC** application using **Playwright**, **Pytest**, and **Allure Reports**.  
It covers basic functionality, edge cases, and extended scenarios, ensuring the app behaves correctly under various conditions.

---

## 🧪 Test Coverage

### Basic Tests
- Add a task
- Complete and clear a task

### Edge Cases
- Adding empty tasks (should not be allowed)
- Preventing duplicate tasks
- Adding very long task text

### Extended Tests
- Adding tasks with special characters
- Deleting a specific task
- Handling multiple duplicate tasks (when allowed)
- Combined scenarios of empty, duplicate, and long tasks

---

## ⚡ How to Run Tests

### Install Requirements
```bash
pip install -r Requirements.txt
Run All Tests with Allure Reporting
pytest --alluredir=allure-results
View Allure Report
allure serve allure-results


