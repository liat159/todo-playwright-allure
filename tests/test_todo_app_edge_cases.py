import pytest
import allure
from pages.todo_page import TodoPage


@pytest.mark.usefixtures("browser")
@allure.feature("Todo App - Edge Cases")
class TestTodoAppEdgeCases:

    @allure.story("Complete Non-existent Task")
    @allure.title("Verify completing a task when list is empty does nothing")
    @allure.severity(allure.severity_level.MINOR)
    def test_complete_non_existent_task(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        with allure.step("Attempt to complete task at index 0 when list is empty"):
            try:
                page.complete_task(0)
            except IndexError:
                pass  # expected

        with allure.step("Verify task list is still empty"):
            tasks = page.get_tasks()
            assert len(tasks) == 0, "No tasks should exist"

    @allure.story("Uncomplete Task")
    @allure.title("Verify a completed task can be marked as incomplete")
    @allure.severity(allure.severity_level.NORMAL)
    def test_uncomplete_task(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        page.add_task("Read book")
        page.complete_task(0)

        with allure.step("Mark the same task as incomplete again"):
            page.uncomplete_task(0)  # נצטרך להוסיף פונקציה למחלקה

        with allure.step("Verify task is back to active state"):
            # נניח שיש class בשם 'completed' שמוסר כאשר המשימה פעילה שוב
            tasks = page.get_tasks()
            assert not any("completed" in t.get_attribute("class") for t in tasks), "Task should be active"

    @allure.story("Clear with Empty List")
    @allure.title("Verify clearing when list is empty causes no error")
    @allure.severity(allure.severity_level.MINOR)
    def test_clear_empty_list(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        with allure.step("Try to clear completed tasks when list is empty"):
            page.clear_completed()

        with allure.step("Verify still no tasks exist"):
            tasks = page.get_tasks()
            assert len(tasks) == 0

    @allure.story("Clear When No Completed Tasks")
    @allure.title("Verify clear completed does not remove active tasks")
    @allure.severity(allure.severity_level.NORMAL)
    def test_clear_no_completed_tasks(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        page.add_task("Task 1")
        page.add_task("Task 2")

        with allure.step("Clear completed tasks (none completed)"):
            page.clear_completed()

        with allure.step("Verify both tasks remain"):
            tasks = page.get_tasks()
            assert len(tasks) == 2, "Active tasks should remain untouched"

    @allure.story("Complete And Uncomplete Multiple Tasks")
    @allure.title("Verify toggling completion state on multiple tasks")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_toggle_multiple_tasks(self, browser, config):
        page = TodoPage(browser)
        page.load(config["base_url"])

        task_names = ["Run", "Walk", "Swim"]
        for t in task_names:
            page.add_task(t)

        with allure.step("Complete all tasks"):
            for i in range(len(task_names)):
                page.complete_task(i)

        with allure.step("Uncomplete the middle task"):
            page.uncomplete_task(1)

        with allure.step("Verify the middle task is active, others completed"):
            tasks = page.get_tasks()
            classes = [t.get_attribute("class") for t in tasks]
            assert "completed" not in classes[1], "Middle task should be active"
            assert all("completed" in c for i, c in enumerate(classes) if i != 1), "Other tasks should remain completed"
