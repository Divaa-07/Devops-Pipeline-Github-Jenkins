pipeline {
    agent any

    tools {
        maven 'Maven' // This should match the name given in the Global Tool Configuration
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'mvn clean package'
            }
            post {
                success {
                    archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Set up virtual environment for Python tests
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate.bat'

                    // Install test dependencies
                    bat 'pip install -r requirements.txt'

                    // Run automated tests
                    bat 'python -m unittest discover -s tests'

                    // Archive test results
                    junit '**/test-results/*.xml'
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
}
