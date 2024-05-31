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
                script {
                    // Deploy the application using Docker Compose
                    sh 'docker-compose -f docker-compose.yml up -d --build'
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
