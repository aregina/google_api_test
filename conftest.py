import csv
import datetime
import os
import pathlib

import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call':
        datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_for_report = [datetime_str, rep.nodeid, rep.duration, rep.outcome]
        if rep.outcome == 'failed':
            data_for_report.append(rep.longreprtext)
        file_path = pathlib.Path(os.path.abspath(__file__))
        report_path = file_path.parent / "test_report.csv"
        with open(report_path, "a") as report:
            report_writer = csv.writer(report)
            report_writer.writerow(data_for_report)
