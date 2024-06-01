pipeline {
    agent any

    tools {
        maven 'Maven 3.8.4'  // This should match the name given in the Maven configuration
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
                    bat 'pip install -r requirements.txt'

                    // Run automated tests and capture output
                    bat 'python -m unittest discover -s tests -p "*.py" > results.xml'

                    // Archive test results
                    junit 'results.xml'
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
        success {
            // Notify success (e.g., via email or Slack)
            echo 'Pipeline succeeded'
        }
        failure {
            // Notify failure (e.g., via email or Slack)
            echo 'Pipeline failed'
        }
    }
}

