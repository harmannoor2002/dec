pipeline {
  agent any

  environment {
    AWS_REGION = 'us-east-1'  
    AWS_REGION = 'us-east-1'  //AWS info
    AWS_REGION = 'us-east-1'  
    AWS_ACCOUNT = '203783636897'

    BACKEND_REPO = 'my-backend-repo'  //local Docker image
    FRONTEND_REPO = 'my-frontend-repo'
////Docker image URLs in AWS 
   ECR_BACKEND = "${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${BACKEND_REPO}"  
ECR_FRONTEND = "${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${FRONTEND_REPO}"


//Docker image URLs in AWS ECR
    AWS_CRED = 'aws-creds-id'     // REPLACE in Jenkins
    EC2_SSH_KEY = 'ec2-ssh-key-id' // REPLACE in Jenkins
    EC2_USER = 'harmannoor2002'
    EC2_HOST = '54.90.166.7'

    GIT_REPO = 'GIT_REPO_URLhttps://github.com/harmannoor2002/dec.git' 
  }
//Pulls the latest code from the Git repository configured in Jenkins.

//scm refers to the repository of the Jenkins job itself.
//Logs into AWS ECR (Elastic Container Registry) so Docker can push images.

//withCredentials safely provides AWS credentials stored in Jenkins.

//docker login command authenticates Docker with AWS.
  stages {

    stage('Checkout') { //checkout code
      steps { checkout scm } // pulls code from git repo
    }
//Logs into AWS ECR (Elastic Container Registry) so Docker can push images.
    stage('Login to ECR') { //aws ecr login
      steps {
        withCredentials([usernamePassword(    
          credentialsId: "${AWS_CRED}",
          usernameVariable: 'AWS_ACCESS_KEY_ID',
          passwordVariable: 'AWS_SECRET_ACCESS_KEY' //  REPLACE in Jenkins
        )]) {
          // Sets AWS credentials in the environment and logs into ECR
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


//Gets the short Git commit SHA (git rev-parse --short=8 HEAD) to tag images.

//Builds Docker image for backend using backend/Dockerfile.

//Tags the image with:

//Specific commit (:sha)

//latest

//Pushes both tags to ECR.
    stage('Build & Push Backend') {
    steps {
    script { //build backend image
      //Gets the current Git commit ID (short version, 8 characters) and stores it in sha.

//This is used to tag the Docker image for versioning.
// gets the current Git commit hash
          def sha = sh(script: "git rev-parse --short=8 HEAD", returnStdout: true).trim()
          sh """
            docker build -t ${BACKEND_REPO}:${sha} -f backend/Dockerfile backend
            docker tag ${BACKEND_REPO}:${sha} ${ECR_BACKEND}:${sha} // Tags the image with the ECR repository URL and the commit SHA.
            docker tag ${BACKEND_REPO}:${sha} ${ECR_BACKEND}:latest
            docker push ${ECR_BACKEND}:${sha} //Pushes both images (SHA-tagged and latest) to AWS ECR.
            docker push ${ECR_BACKEND}:latest 
          """
          //This is a shell step in Jenkins.

//Whatever commands are inside """ will run in the shell.
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
        //Deploys the updated application to the EC2 instance.
        sshagent (credentials: ["${EC2_SSH_KEY}"]) {
          sh """
          //Connects to your EC2 instance via SSH using Jenkins credentials.
            ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} << 'EOF' 
              set -e //stop on error
              rm -rf ~/app || true //remove old app folder
              git clone ${GIT_REPO} ~/app //clone latest code
              cd ~/app //  navigate to app directory

              aws ecr get-login-password --region ${AWS_REGION} \      // login to AWS ECR
                | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com // authenticate Docker with ECR

              docker-compose pull // pull new images
              docker-compose up -d --remove-orphans // start containers in detached mode
              docker image prune -f // remove unused Docker images
            EOF // end ssh session
          """
        }
      }
    }
  }
}
//Connects to your EC2 instance via SSH using Jenkins credentials.

//Steps executed on the EC2 server:

//Remove old app folder (rm -rf ~/app)

//Clone latest code from Git

//Log in to AWS ECR

//Pull new Docker images via docker-compose pull

//Start containers in detached mode (docker-compose up -d)

//Remove unused Docker images (docker image prune -f)
