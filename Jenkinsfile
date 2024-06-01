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
                    bat 'pip install -r requirements.txt'

                    // Run automated tests and capture output
                    bat 'python -m unittest discover -s tests -p "*.py" > results.xml'

                    // Archive test results
                    junit 'results.xml'
                }
            }
        }


          stage('Deploy') {
            steps {
                script {
                    // Pull the latest image (if applicable)
                    bat 'docker-compose pull'

                    // Deploy the application using Docker Compose
                    bat 'docker-compose up -d --build'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up workspace
                cleanWs()
            }
        }
        success {
            script {
                // Notify success (e.g., via email or Slack)
                echo 'Pipeline succeeded'
            }
        }
        unstable {
            script {
                // Notify unstable build
                echo 'Pipeline finished with some issues'
            }
        }
        failure {
            script {
                // Notify failure (e.g., via email or Slack)
                echo 'Pipeline failed'
            }
        }
    }
}

