import pytest
import allure
from pages.todo_page import TodoPage

@pytest.mark.usefixtures("browser")
class TestTodoAppExtended:

    @allure.title("Verify adding duplicate tasks")
    @allure.severity(allure.severity_level.NORMAL)
    def test_duplicate_tasks_added(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        task_name = "Duplicate task"
        with allure.step("Add first instance of the task"):
            page.add_task(task_name, allow_duplicates=True)
        with allure.step("Add second instance of the same task"):
            page.add_task(task_name, allow_duplicates=True)

        tasks = page.get_tasks()
        task_texts = [t.text.strip() for t in tasks]
        with allure.step("Verify both duplicates exist"):
            assert task_texts.count(task_name) == 2

    @allure.title("Verify tasks with special characters can be added")
    @allure.severity(allure.severity_level.MINOR)
    def test_special_characters_task(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        # Use only BMP characters to avoid ChromeDriver error
        special_text = "Task with !@#$%^&*()_+-=[]{};:,.<>?/~"
        with allure.step(f"Add task with special characters: {special_text}"):
            page.add_task(special_text)

        tasks = page.get_tasks()
        task_texts = [t.text.strip() for t in tasks]
        with allure.step("Verify the special character task was added"):
            assert special_text in task_texts

    @allure.title("Verify deleting a specific task by name")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_specific_task(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        task_to_delete = "Task to delete"
        with allure.step("Add a task to be deleted"):
            page.add_task(task_to_delete)
        with allure.step("Delete the specific task"):
            page.delete_task_by_name(task_to_delete)

        tasks = page.get_tasks()
        task_texts = [t.text.strip() for t in tasks]
        with allure.step("Verify the task was deleted"):
            assert task_to_delete not in task_texts

    @allure.title("Verify adding very long task text")
    @allure.severity(allure.severity_level.MINOR)
    def test_long_text_task_added(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        long_text = "This is a very long task description " * 5
        with allure.step("Add long text task"):
            page.add_task(long_text)

        tasks = page.get_tasks()
        task_texts = [t.text.strip() for t in tasks]
        with allure.step("Verify the long text task was added"):
            assert long_text.strip() in task_texts

