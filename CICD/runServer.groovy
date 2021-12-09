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
        sh "cd \"${env.WORKSPACE}\""
        println("Inside WORKSPACE: ${env.WORKSPACE}")
        sh "cd CICD"
        sh "sudo chmod 777 runserver.sh"
        sh "sh runserver.sh"
      }
    }
  }

}
