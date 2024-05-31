pipeline {
    agent any

    tools {
        maven 'Maven' // This should match the name given in the Global Tool Configuration
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Use Maven to build the project
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
                echo 'Testing...'
                // Run tests using Maven
                bat 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Example: Docker deployment using PowerShell
                bat 'docker build -t myapp:latest .'
                bat 'docker run -d -p 8080:8080 myapp:latest'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
                // Push Docker image to a registry using PowerShell
                bat 'docker tag myapp:latest myregistry/myapp:latest'
                bat 'docker push myregistry/myapp:latest'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

