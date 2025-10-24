import pytest
import allure
from pages.todo_page import TodoPage


@pytest.mark.usefixtures("browser")
class TestTodoAppEdgeCases:

    @allure.title("Verify empty task cannot be added")
    @allure.severity(allure.severity_level.MINOR)
    def test_empty_task_not_added(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        with allure.step("Try to add an empty task"):
            page.add_task("")

        tasks = page.get_tasks()
        with allure.step("Verify no new task was added"):
            assert all(task.text.strip() != "" for task in tasks)

    @allure.title("Verify duplicate tasks are not added")
    @allure.severity(allure.severity_level.NORMAL)
    def test_duplicate_task_not_added(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        with allure.step("Add a task first time"):
            page.add_task("Read a book")
        with allure.step("Try to add the same task again"):
            page.add_task("Read a book")

        tasks = page.get_tasks()
        with allure.step("Verify only one instance of the task exists"):
            task_texts = [t.text.strip() for t in tasks]
            assert task_texts.count("Read a book") == 1

    @allure.title("Verify long text task can be added")
    @allure.severity(allure.severity_level.MINOR)
    def test_long_text_task_added(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        long_text = "This is a very long task description " * 5
        with allure.step("Add long text task"):
            page.add_task(long_text)

        tasks = page.get_tasks()
        with allure.step("Verify the long text task was added"):
            assert any(long_text.strip() in t.text for t in tasks)

    @allure.title("Verify combination of empty, duplicate, and long text")
    @allure.severity(allure.severity_level.NORMAL)
    def test_combined_edge_cases(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        with allure.step("Try adding empty task"):
            page.add_task("")

        long_text = "Another very long task " * 4
        with allure.step("Add a long text task"):
            page.add_task(long_text)

        with allure.step("Try adding duplicate of long text task"):
            page.add_task(long_text)

        tasks = page.get_tasks()
        task_texts = [t.text.strip() for t in tasks]

        with allure.step("Verify empty task was not added"):
            assert all(t != "" for t in task_texts)
        with allure.step("Verify duplicate task was not added"):
            assert task_texts.count(long_text.strip()) == 1
