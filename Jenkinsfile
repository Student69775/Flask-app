pipeline {
    agent any

    environment {
        PYTHON = "C:\\Python312"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Student69775/Flask-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                if not exist %VENV_DIR% (
                    %PYTHON% -m venv %VENV_DIR%
                )
                call %VENV_DIR%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                python -m unittest discover tests || exit /b 1
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                start /B python app.py
                '''
            }
        }
    }
}
