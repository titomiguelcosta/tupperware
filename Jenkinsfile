pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t titomiguelcosta/tupperware .'
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
