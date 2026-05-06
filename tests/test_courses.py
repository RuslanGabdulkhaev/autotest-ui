from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле Email
        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('user.name@gmail.com')

        # Заполняем поле Username
        user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
        user_name_input.fill('username')

        # Заполняем поле Password
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill('password')

        # Нажимаем на кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        # Открываем браузер с контекстом из прошлого теста
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        check_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(check_courses).to_have_text("Courses")

        check_no_results = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(check_no_results).to_have_text("There is no results")

        check_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(check_icon).to_be_visible()

        check_under_no_results = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(check_under_no_results).to_have_text("Results from the load test pipeline will be displayed here")
