pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Example: Use Maven to build a Java project
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
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Deploy the application (example: Docker container)
                sh 'docker build -t myapp:latest .'
                sh 'docker run -d -p 8080:8080 myapp:latest'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
                // Push Docker image to a Docker registry
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
