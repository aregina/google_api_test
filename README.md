Here you can find the way to test that the distance between given pairs of points does not
change from the base accepted values.

Python3 is required to run the tests

You can find all needed requirements in requirements.txt  


**How to run tests**

`GOOGLE_API_KEY=<YOUR_KEY> pytest your_path/calendar42_tests`

Each test run adds new row with tests results to test_report.csv

To run tests every 10 minutes automatically just add the following command to crontab

`*/10 * * * * GOOGLE_API_KEY=<YOUR_KEY> pytest your_path/calendar42_tests`