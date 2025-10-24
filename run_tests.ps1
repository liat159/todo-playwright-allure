# Clean old results
if (Test-Path "C:\Users\PC\PycharmProjects\todoMVCProject\allure-results") {
    Remove-Item "C:\Users\PC\PycharmProjects\todoMVCProject\allure-results" -Recurse -Force
}

# Run pytest with Allure
pytest

# Serve Allure report (open in browser)
allure serve C:\Users\PC\PycharmProjects\todoMVCProject\allure-results
