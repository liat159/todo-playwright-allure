import pytest
import allure
from pages.todo_page import TodoPage

@pytest.mark.usefixtures("browser")
@allure.feature("Todo App")
class TestTodoApp:

    @allure.story("Add Task")
    @allure.title("Verify a task can be added")
    @allure.description("This test adds a task to the todo list and verifies it appears in the list")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_task(self, browser, config):
        page = TodoPage(browser)
        with allure.step("Load the Todo app"):
            page.load(config['base_url'])

        with allure.step("Add task: 'Buy milk'"):
            page.add_task("Buy milk")

        with allure.step("Get all tasks"):
            tasks = page.get_tasks()

        with allure.step("Verify 'Buy milk' is in the task list"):
            assert any("Buy milk" in t.text for t in tasks)

    @allure.story("Complete and Clear Task")
    @allure.title("Verify completing and clearing a task works")
    @allure.description("This test marks a task as completed and then clears it from the list")
    @allure.severity(allure.severity_level.NORMAL)
    def test_complete_and_clear_task(self, browser, config):
        page = TodoPage(browser)
        with allure.step("Load the Todo app"):
            page.load(config['base_url'])

        with allure.step("Add task: 'Go running'"):
            page.add_task("Go running")

        with allure.step("Complete the first task"):
            page.complete_task(0)

        with allure.step("Clear completed tasks"):
            page.clear_completed()

        with allure.step("Get all tasks and verify the list is empty"):
            tasks = page.get_tasks()
            assert len(tasks) == 0
