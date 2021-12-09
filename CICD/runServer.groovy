pipeline{

  agent any

  stages{

    stage('clean'){
      steps{
        sh "cd /var/lib/jenkins/workspace/"
        checkout scm
      }
    }

    stage('Run Server'){
      steps{
        sh "cd ${env.WORKSPACE}/CICD;pwd"
        println("Inside WORKSPACE: ${env.WORKSPACE}/CICD")
        sh "ls -lrt;sudo chmod 777 runServer.sh"
        sh "sh runServer.sh ${env.WORKSPACE}"
      }
    }
  }
}
