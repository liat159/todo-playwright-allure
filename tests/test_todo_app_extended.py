import pytest
import allure
from pages.todo_page import TodoPage


@pytest.mark.usefixtures("browser")
@allure.feature("Todo App - Extended Scenarios")
class TestTodoAppExtended:

    @allure.story("Empty Task")
    @allure.title("Verify empty task cannot be added")
    @allure.severity(allure.severity_level.MINOR)
    def test_empty_task_not_added(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        with allure.step("Try to add an empty task"):
            page.add_task("")

        with allure.step("Verify no task was added"):
            tasks = page.get_tasks()
            assert len(tasks) == 0, "Empty task should not be added"

    @allure.story("Duplicate Tasks")
    @allure.title("Verify adding duplicate tasks shows both")
    @allure.severity(allure.severity_level.NORMAL)
    def test_duplicate_tasks_added(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        with allure.step("Add the same task twice"):
            page.add_task("Go running")
            page.add_task("Go running")

        with allure.step("Verify two tasks appear in the list"):
            tasks = page.get_tasks()
            texts = [t.text for t in tasks]
            assert texts.count("Go running") == 2, "Expected 2 duplicate tasks"

    @allure.story("Long Task Name")
    @allure.title("Verify very long task name is handled properly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_long_task_name(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        long_text = "Buy " + "milk " * 50  # very long name
        page.add_task(long_text)

        tasks = page.get_tasks()
        assert any(long_text.strip() in t.text for t in tasks), "Long task name was not displayed correctly"

    @allure.story("Special Characters")
    @allure.title("Verify task with special characters is added")
    @allure.severity(allure.severity_level.NORMAL)
    def test_special_characters_task(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        special_task = "@!#$$%^&*()_+{}[]:;\"'<>,.?/🚀"
        page.add_task(special_task)

        tasks = page.get_tasks()
        assert any(special_task in t.text for t in tasks), "Special characters task was not added"

    @allure.story("Delete Specific Task")
    @allure.title("Verify a specific task can be deleted")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_specific_task(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        page.add_task("Task A")
        page.add_task("Task B")
        page.add_task("Task C")

        # נניח שיש כפתור מחיקה על כל משימה
        with allure.step("Delete 'Task B'"):
            page.delete_task_by_name("Task B")

        with allure.step("Verify 'Task B' was deleted"):
            tasks = [t.text for t in page.get_tasks()]
            assert "Task B" not in tasks, "'Task B' should be deleted"
