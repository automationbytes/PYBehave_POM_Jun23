import os

from behave import __main__ as runner
import sys

if __name__ == '__main__':
    sys.stdout.flush()

    FeatureFilePath = "FeaturesFiles"
    AllureReportPath = " -f allure_behave.formatter:AllureFormatter -o Reports"
    BehaveOptions = " --summary --color --verbose --format=json --outfile=report.json --junit --junit-directory=junit_reports"
    run = FeatureFilePath+AllureReportPath+BehaveOptions
    runner.main(run)
    #
    # reportdir = os.getcwd() + "/Reports"
    # os.system('cmd /c "allure serve "'+reportdir)