pipeline{

  agent any

  stages{

    stage('clean'){
      steps{
        deleteDir()
        checkout scm
      }
    }

    stage('Run Server'){
      steps{
        sh "cd \"${env.WORKSPACE}\"CICD"
        println("Inside WORKSPACE: ${env.WORKSPACE}")
        sh "sudo chmod 777 runServer.sh"
        sh "sh runServer.sh ${env.WORKSPACE}"
      }
    }
  }

}
