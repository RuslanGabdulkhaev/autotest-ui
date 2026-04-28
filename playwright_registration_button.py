from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()


    # Открытие страницы регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверка, что кнопка регистрации задизейблена
    registration_button_check = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button_check).to_be_disabled()

    # Ввод в поле email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    # Ввод в поле username
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    # Ввод в поле password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    # Проверка, что кнопка регистрации не задизейблена
    registration_button_check = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button_check).not_to_be_disabled()
