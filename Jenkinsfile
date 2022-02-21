pipeline {
    agent any

    stages {
        stage ('(1) Git checkout') {
            git 'https://github.com/shay79il/DevOpsProject.git'
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
                sh 'python e2e.py'
            }
        }
    }

    post {
        success {
            echo "${env.BUILD_URL} has result success"
            sh 'docker-compose down'
            sh 'docker-compose push'
        }
        failure {
            echo "${env.BUILD_URL} has result fail, terminate container..."
            sh 'docker-compose down'
        }
    }
}