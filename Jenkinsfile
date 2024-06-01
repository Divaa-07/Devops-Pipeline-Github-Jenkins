pipeline {
    agent any

    environment {
        DATADOG_API_KEY = credentials('DATADOG_API_KEY')
    }

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


           stage('Monitor') {
            steps {
                script {
                    // Example of triggering a Datadog event
                    def response = httpRequest(
                        url: "https://api.datadoghq.com/api/v1/events",
                        httpMode: 'POST',
                        customHeaders: [
                            [name: 'Content-Type', value: 'application/json'],
                            [name: 'DD-API-KEY', value: env.DATADOG_API_KEY]
                        ],
                        requestBody: """{
                            "title": "Deployment completed",
                            "text": "Deployment of ${env.JOB_NAME} completed successfully",
                            "priority": "normal",
                            "tags": ["env:production", "app:${env.JOB_NAME}"]
                        }"""
                    )
                    echo "Datadog event response: ${response}"
                }
            }
        }
    }

    post {
        failure {
            script {
                // Example of triggering a Datadog event on failure
                def response = httpRequest(
                    url: "https://api.datadoghq.com/api/v1/events",
                    httpMode: 'POST',
                    customHeaders: [
                        [name: 'Content-Type', value: 'application/json'],
                        [name: 'DD-API-KEY', value: env.DATADOG_API_KEY]
                    ],
                    requestBody: """{
                        "title": "Deployment failed",
                        "text": "Deployment of ${env.JOB_NAME} failed",
                        "priority": "high",
                        "alert_type": "error",
                        "tags": ["env:production", "app:${env.JOB_NAME}"]
                    }"""
                )
                echo "Datadog event response: ${response}"
            }
        }
    }
}
