pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('meca-dockerhub')
    }
    
    stages {
        stage('Checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins-github', url: 'https://github.com/chineduanunobi/python-api.git']])
            }
        }
        
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python -m pytest test_api.py'
            }       
        }
        
        stage('Docker Build and Push') {
            steps {
      	        sh 'docker build -t mecat/python_api .'
      	        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push mecat/python_api'
            }
        }
    }
        post {
            always {
                sh 'docker logout'
            }
        }
}