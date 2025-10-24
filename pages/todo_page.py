import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TodoPage:
    """Page Object for the TodoMVC application"""

    def __init__(self, driver):
        self.driver = driver
        self.new_todo_input = (By.CLASS_NAME, "new-todo")
        self.todo_items = (By.CSS_SELECTOR, ".todo-list li")
        self.clear_completed_btn = (By.CLASS_NAME, "clear-completed")

    @allure.step("Load Todo app at URL: {url}")
    def load(self, url):
        self.driver.get(url)

    @allure.step("Add task: {task_name}")
    def add_task(self, task_text):
        """Add a new todo task"""
        input_field = self.driver.find_element(*self.new_todo_input)
        input_field.send_keys(task_text + Keys.RETURN)

    @allure.step("Get all tasks")
    def get_tasks(self):
        """Return all task elements"""
        return self.driver.find_elements(*self.todo_items)

    @allure.step("Complete task at index: {index}")
    def complete_task(self, index=0):
        """Mark task as completed"""
        tasks = self.get_tasks()
        toggle = tasks[index].find_element(By.CLASS_NAME, "toggle")
        toggle.click()

    @allure.step("Clear all completed tasks")
    def clear_completed(self):
        """Click the 'Clear completed' button"""
        self.driver.find_element(*self.clear_completed_btn).click()

    @allure.step("Delete task with name: {task_name}")
    def delete_task_by_name(self, task_name):
        tasks = self.driver.find_elements(*self.todo_items)
        for task in tasks:
            if task.text.strip() == task_name:
                # a cursor on delete
                delete_btn = task.find_element(By.CLASS_NAME, "destroy")
                self.driver.execute_script("arguments[0].click();", delete_btn)
                break

    @allure.step("Uncomplete task at index: {index}")
    def uncomplete_task(self, index):
        tasks = self.get_tasks()
        checkbox = tasks[index].find_element(By.CLASS_NAME, "toggle")
        checkbox.click()
