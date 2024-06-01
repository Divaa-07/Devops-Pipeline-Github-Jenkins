pipeline {
    agent any

    tools {
        maven 'Maven'  // This should match the name given in the Maven configuration
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Checkout code from Git repository
                    checkout scm

                    // Debug: List directory contents to verify files
                    bat 'dir'

                    // Build the Java project using Maven
                    bat 'mvn clean install'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Set up virtual environment for Python tests
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate.bat'

                    // Ensure __init__.py exists in the tests directory
                    bat 'if not exist tests\\__init__.py ( echo.> tests\\__init__.py )'

                    // Debug: List directory contents to verify files
                    bat 'dir tests'

                    // Install test dependencies
                    bat 'pip insta
