from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time

class TodoPage:
    """Page Object for the TodoMVC application"""

    def __init__(self, driver):
        self.driver = driver
        self.new_todo_input = (By.CLASS_NAME, "new-todo")
        self.todo_items = (By.CSS_SELECTOR, ".todo-list li")
        self.clear_completed_btn = (By.CLASS_NAME, "clear-completed")

    @allure.step("Load TodoMVC page")
    def load(self, url):
        self.driver.get(url)
        time.sleep(1)  # optional wait for full page load

    @allure.step("Add task: {task_text}")
    def add_task(self, task_text, allow_duplicates=False):
        """Add a new todo task, handle empty, duplicates, long text"""
        if not task_text:
            allure.attach("Attempted to add empty task, skipping",
                          name="Empty task",
                          attachment_type=allure.attachment_type.TEXT)
            return

        existing_tasks = [t.text.strip() for t in self.get_tasks()]
        if not allow_duplicates and task_text.strip() in existing_tasks:
            allure.attach(f"Task '{task_text}' already exists, skipping duplicate",
                          name="Duplicate task",
                          attachment_type=allure.attachment_type.TEXT)
            return

        input_field = self.driver.find_element(*self.new_todo_input)
        input_field.send_keys(task_text + Keys.RETURN)
        time.sleep(0.5)

    @allure.step("Get all tasks")
    def get_tasks(self):
        return self.driver.find_elements(*self.todo_items)

    @allure.step("Complete task at index {index}")
    def complete_task(self, index):
        tasks = self.get_tasks()
        if index < len(tasks):
            checkbox = tasks[index].find_element(By.CSS_SELECTOR, "input.toggle")
            checkbox.click()
            time.sleep(0.2)

    @allure.step("Clear completed tasks")
    def clear_completed(self):
        clear_btns = self.driver.find_elements(*self.clear_completed_btn)
        if clear_btns:
            clear_btns[0].click()
            time.sleep(0.5)

    @allure.step("Delete task by name: {task_name}")
    def delete_task_by_name(self, task_name):
        tasks = self.get_tasks()
        for task in tasks:
            if task.text.strip() == task_name:
                delete_btn = task.find_element(By.CSS_SELECTOR, "button.destroy")
                self.driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(0.3)
                break
