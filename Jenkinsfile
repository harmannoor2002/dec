pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPO_BACKEND = '203783636897.dkr.ecr.us-east-1.amazonaws.com/my-backend-repo'
        ECR_REPO_FRONTEND = '203783636897.dkr.ecr.us-east-1.amazonaws.com/my-frontend-repo'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/harmannoor2002/dec.git'
            }
        }

        stage('AWS ECR Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws-creds-id', 
                                                usernameVariable: 'AWS_ACCESS_KEY_ID', 
                                                passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh """
                        aws ecr get-login-password --region $AWS_REGION | \
                        docker login --username AWS --password-stdin $ECR_REPO_BACKEND
                    """
                    sh """
                        aws ecr get-login-password --region $AWS_REGION | \
                        docker login --username AWS --password-stdin $ECR_REPO_FRONTEND
                    """
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t my-backend:latest backend/'
                sh 'docker build -t my-frontend:latest frontend/'
            }
        }

        stage('Tag & Push to ECR') {
            steps {
                sh "docker tag my-backend:latest $ECR_REPO_BACKEND:latest"
                sh "docker tag my-frontend:latest $ECR_REPO_FRONTEND:latest"

                sh "docker push $ECR_REPO_BACKEND:latest"
                sh "docker push $ECR_REPO_FRONTEND:latest"
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-ssh-key-id']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no harmannoor2002@<EC2_PUBLIC_IP> '
                            cd /home/harmannoor2002/dec && \
                            docker-compose down && \
                            docker-compose pull && \
                            docker-compose up -d
                        '
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed. Check console logs.'
        }
    }
}
