pipeline:
  agent:
    any

  environment:
    PYCHARM_PROJECT_PATH: "C:/Users/Vigne/PycharmProjects/PyBehave_May_2023"
    VENV_PATH: "${PYCHARM_PROJECT_PATH}/venv"
    ALLURE_REPORTS_PATH: "${PYCHARM_PROJECT_PATH}/reports"

  stages:
    - stage: Setup Virtual Environment
      steps:
        - dir: ${PYCHARM_PROJECT_PATH}
          bat: |
            xcopy /s /i /y . ${WORKSPACE}
            python -m venv "${VENV_PATH}"
            call "${VENV_PATH}\\Scripts\\activate.bat"
            # pip install -r requirements.txt

    - stage: Run Script
      steps:
        - dir: ${PYCHARM_PROJECT_PATH}
          bat: |
            call "${VENV_PATH}\\Scripts\\activate.bat" && python runner.py

    - stage: Download and Extract Allure
      steps:
        - bat: |
            cd ${WORKSPACE}
            curl -o allure-2.14.0.zip -Ls https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.zip
            powershell -Command "Expand-Archive -Path allure-2.14.0.zip -DestinationPath . -Force"

  post:
    success:
      steps:
        - allure:
            includeProperties: false
            jdk: ''
            properties: []
            reportBuildPolicy: 'ALWAYS'
            results:
              - path: 'Reports'
        - archiveArtifacts:
            artifacts: 'Reports/**'
