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
                echo 'Running JUnit tests...'
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
                script {
                    // Pull the latest Docker image
                    sh 'docker pull myregistry/myapp:latest'

                    // Stop and remove any existing container
                    sh '''
                        if [ "$(docker ps -q -f name=myapp)" ]; then
                            docker stop myapp
                            docker rm myapp
                        fi
                    '''

                    // Run the new container
                    sh 'docker run -d --name myapp -p 8080:8080 myregistry/myapp:latest'
                }
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
                sh 'docker tag myapp:latest myregistry/myapp:latest'
                sh 'docker push myregistry/myapp:latest'
            }
        }
        stage('Monitoring and Alerting') {
            steps {
                echo 'Setting up monitoring and alerting...'
                script {
                    def response = httpRequest(
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        url: 'https://api.datadoghq.com/api/v1/monitor',
                        customHeaders: [
                            [name: 'DD-API-KEY', value: env.DATADOG_API_KEY],
                            [name: 'DD-APPLICATION-KEY', value: env.DATADOG_APP_KEY]
                        ],
                        requestBody: """{
                            "name": "${env.DATADOG_MONITOR_NAME}",
                            "type": "metric alert",
                            "query": "${env.DATADOG_MONITOR_QUERY}",
                            "message": "Alert: MyApp production environment has issues.",
                            "tags": ["env:production"],
                            "options": {
                                "notify_audit": true,
                                "locked": false,
                                "timeout_h": 0,
                                "include_tags": true,
                                "thresholds": {
                                    "critical": 1
                                }
                            }
                        }"""
                    )
                    echo "Datadog monitor setup response: ${response.content}"
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
