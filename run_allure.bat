@echo off
cd /d %~dp0

REM Remove old allure-results
if exist allure-results rmdir /s /q allure-results

REM Run pytest using python -m to ensure interpreter is used
python -m pytest --alluredir=allure-results

REM Serve Allure report
"C:\Users\PC\scoop\apps\allure\current\bin\allure.bat" serve allure-results
