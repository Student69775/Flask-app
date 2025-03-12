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
                if not exist venv (
                    python -m venv venv
                )
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python -m unittest discover || exit /b 1
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python app.py
                '''
            }
        }
    }
}
