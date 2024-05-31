pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Use Maven to build the project
                sh 'mvn clean package'
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
                sh 'mvn test'
            }
            post {
                always {
                    // Publish test results
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Example: Docker deployment
                sh 'docker build -t myapp:latest .'
                sh 'docker run -d -p 8080:8080 myapp:latest'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
                // Push Docker image to a registry
                sh 'docker tag myapp:latest myregistry/myapp:latest'
                sh 'docker push myregistry/myapp:latest'
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
