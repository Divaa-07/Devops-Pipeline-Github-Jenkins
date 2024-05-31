pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Use PowerShell to build the project
                powershell 'mvn clean package'
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
                // Run tests using PowerShell
                powershell 'mvn test'
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
                powershell 'docker build -t myapp:latest .'
                powershell 'docker run -d -p 8080:8080 myapp:latest'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
                // Push Docker image to a registry using PowerShell
                powershell 'docker tag myapp:latest myregistry/myapp:latest'
                powershell 'docker push myregistry/myapp:latest'
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
