pipeline {
  agent any

  environment {
    AWS_REGION = 'us-east-1'
    AWS_ACCOUNT = '203783636897'

    BACKEND_REPO = 'my-backend-repo'
    FRONTEND_REPO = 'my-frontend-repo'

    ECR_BACKEND = "${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${BACKEND_REPO}"
    ECR_FRONTEND = "${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${FRONTEND_REPO}"

    AWS_CRED = 'aws-creds-id'     // REPLACE in Jenkins
    EC2_SSH_KEY = 'ec2-ssh-key-id' // REPLACE in Jenkins
    EC2_USER = 'harmannoor2002'
    EC2_HOST = '54.90.166.7'

    GIT_REPO = 'GIT_REPO_URL' // replace
  }

  stages {

    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Login to ECR') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: "${AWS_CRED}",
          usernameVariable: 'AWS_ACCESS_KEY_ID',
          passwordVariable: 'AWS_SECRET_ACCESS_KEY'
        )]) {
          sh '''
            aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
            aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
            aws configure set region ${AWS_REGION}
            aws ecr get-login-password --region ${AWS_REGION} \
             | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com
          '''
        }
      }
    }

    stage('Build & Push Backend') {
      steps {
        script {
          def sha = sh(script: "git rev-parse --short=8 HEAD", returnStdout: true).trim()
          sh """
            docker build -t ${BACKEND_REPO}:${sha} -f backend/Dockerfile backend
            docker tag ${BACKEND_REPO}:${sha} ${ECR_BACKEND}:${sha}
            docker tag ${BACKEND_REPO}:${sha} ${ECR_BACKEND}:latest
            docker push ${ECR_BACKEND}:${sha}
            docker push ${ECR_BACKEND}:latest
          """
        }
      }
    }

    stage('Build & Push Frontend') {
      steps {
        script {
          def sha = sh(script: "git rev-parse --short=8 HEAD", returnStdout: true).trim()
          sh """
            docker build -t ${FRONTEND_REPO}:${sha} -f frontend/Dockerfile frontend
            docker tag ${FRONTEND_REPO}:${sha} ${ECR_FRONTEND}:${sha}
            docker tag ${FRONTEND_REPO}:${sha} ${ECR_FRONTEND}:latest
            docker push ${ECR_FRONTEND}:${sha}
            docker push ${ECR_FRONTEND}:latest
          """
        }
      }
    }

    stage('Deploy to EC2') {
      steps {
        sshagent (credentials: ["${EC2_SSH_KEY}"]) {
          sh """
            ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} << 'EOF'
              set -e
              rm -rf ~/app || true
              git clone ${GIT_REPO} ~/app
              cd ~/app

              aws ecr get-login-password --region ${AWS_REGION} \
                | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com

              docker-compose pull
              docker-compose up -d --remove-orphans
              docker image prune -f
            EOF
          """
        }
      }
    }
  }
}
