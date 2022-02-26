pipeline {
    agent any

    stages {
        stage ('(1) Git checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shay79il/DevOpsProject.git'
            }
        }
        stage ('(2) Build image') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage ('(3) Run image') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('(4) Run test') {
            steps {
                sh 'python3 e2e.py'
            }
        }
    }

    post {
        success {
            echo "${env.BUILD_URL}"
            echo "======= SUCCESS =======\n======= SUCCESS =======\n======= SUCCESS =======\n"
            echo "Terminate container... and upload image to Docker Hub"
            sh 'docker-compose down'
            sh 'docker-compose push'
        }
        failure {
            echo "${env.BUILD_URL}"
            echo "======= FAIL !!! =======\n======= FAIL !!! =======\n======= FAIL !!! =======\n"
            echo "Terminate container..."
            sh 'docker-compose down'
        }
    }
}