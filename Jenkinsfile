pipeline {
    agent any

    tools {
        maven 'Maven' // This should match the name given in the Global Tool Configuration
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                dir('path/to/your/project') {  // Update this path if your pom.xml is in a subdirectory
                    bat 'mvn clean package'
                }
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
                dir('path/to/your/project') {  // Update this path if your pom.xml is in a subdirectory
                    bat 'mvn test'
                }
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
                dir('path/to/your/project') {  // Update this path if your pom.xml is in a subdirectory
                    bat 'docker build -t myapp:latest .'
                    bat 'docker run -d -p 8080:8080 myapp:latest'
                }
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
                dir('path/to/your/project') {  // Update this path if your pom.xml is in a subdirectory
                    bat 'docker tag myapp:latest myregistry/myapp:latest'
                    bat 'docker push myregistry/myapp:latest'
                }
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
