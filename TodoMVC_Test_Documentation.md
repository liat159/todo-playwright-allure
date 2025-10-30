
# TodoMVC Automation Test Documentation

## 1. Test Plan

**Purpose:** Test the TodoMVC application functionality using Playwright + Allure.

**Environment:**  
- OS: Windows  
- Browser: Chrome

**Scope:**  
- Create, update, delete tasks  
- Filter tasks (All / Active / Completed)  
- Mark tasks as Completed / Active  
- Clear completed tasks  
- UI basic checks  
- Allure report integration

**Types of tests:** Functional / Smoke / Regression

---

## 2. Test Cases

| # | Test Case | Steps | Expected Result | Priority |
|---|-----------|-------|----------------|----------|
| 1 | Add new task | 1. Open app<br>2. Enter task name<br>3. Press Enter | Task appears in list | High |
| 2 | Mark task as completed | 1. Create task<br>2. Click checkbox | Task shows as completed | High |
| 3 | Delete task | 1. Create task<br>2. Click delete button | Task disappears from list | High |
| 4 | Filter Active tasks | 1. Create multiple tasks (some completed)<br>2. Click 'Active' | Only active tasks displayed | Medium |
| 5 | Filter Completed tasks | 1. Create multiple tasks (some completed)<br>2. Click 'Completed' | Only completed tasks displayed | Medium |
| 6 | Clear completed tasks | 1. Complete one or more tasks<br>2. Click 'Clear Completed' | Completed tasks removed from list | Medium |
| 7 | Task persists after reload | 1. Create task<br>2. Reload page | Task still in list | High |

---

## 3. Acceptance Criteria

- Each added task appears in the list  
- Task can be marked as Completed and status persists after reload  
- Tasks can be deleted immediately  
- Filters show only matching tasks  
- Clear Completed removes all completed tasks  
- Allure reports show all test statuses

---

## 4. Test Coverage

- ✅ Add / Delete / Update task  
- ✅ Complete / Active toggle  
- ✅ Filtering (All / Active / Completed)  
- ✅ Clear Completed  
- ✅ Persistence after reload  
- ✅ Integration with Allure
