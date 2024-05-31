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
       
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                bat 'docker build -t myapp:latest .'
                bat 'docker run -d -p 8080:8080 myapp:latest'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
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

