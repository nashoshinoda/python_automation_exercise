# Python Automation Exercise

### Summary
This is a little project to test the login section of website https://the-internet.herokuapp.com/ generating html, logs, xml files as reports and screenshots as well using the following tools:
* Python
* PyTest
* Selenium
* Allure-pytest

### How to use it
* Download the test code from the [repository](https://github.com/nashoshinoda/python_automation_exercise) 
* Install required modules using this command line:
    ```sh
    pip install -r requirements.txt
    ```
* Install developed modules with this command line:
    ```sh
    pip install -e .
    ```
* Run command **pytest** to execute all the tests available or **pytest /tests/PATH_OF_THE_TEST.py** to execute once in particular.
* Run command **allure serve ./reports/html** to generate the HTML report once the test execution finished:
    ```sh
    allure serve reports/html
    Generating report to temp directory...
    Report successfully generated to C:\Users\IVELDE~1\AppData\Local\Temp\16445734970921447855\allure-report
    Starting web server...
    2021-06-19 14:06:09.114:INFO::main: Logging initialized @1697ms to org.eclipse.jetty.util.log.StdErrLog
    Server started at <http://ip:port/>. Press <Ctrl+C> to exit
    ```
    A new window will be automatically opened showing the results of the tests.
