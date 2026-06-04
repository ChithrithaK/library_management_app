pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/library-repo.git'
            }
        }
        stage('Build and Push') {
            steps {
                sh 'docker build -t your-dockerhub-username/library-app:latest .'
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    sh 'docker push your-dockerhub-username/library-app:latest'
                }
            }
        }
    }
}