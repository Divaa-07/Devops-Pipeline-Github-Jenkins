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
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'

                    // Install test dependencies
                    sh 'pip install -r requirements.txt'

                    // Run automated tests
                    sh 'python -m unittest discover -s tests'

                    // Archive test results
                    junit '**/test-results/*.xml'
                }
            }
        }
    }
}
