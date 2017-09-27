pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'whoami'
                sh 'docker build -t titomiguelcosta/tupperware .'
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub-titomiguelcosta', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
                    sh 'echo uname=$USERNAME'
                    sh 'docker login --username=$USERNAME --password=$PASSWORD'
                    sh 'docker push titomiguelcosta/tupperware:latest'
                    sh 'docker rmi -f titomiguelcosta/tupperware'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}
