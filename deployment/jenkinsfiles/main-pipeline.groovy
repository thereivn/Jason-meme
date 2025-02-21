pipeline{
    agent any

    stages{
        stage('Build and deploy'){
            steps{
                sh 'docker compose up --build -d'
            }
        }
        stage('Check'){
            steps{
                sh 'curl http://localhost/check'
                sh 'curl -I http://localhost/jason'
                sh 'brave http://localhost/jason'
            }
        }
    }
}