import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    page.wait_for_timeout(2000)