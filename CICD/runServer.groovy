pipeline{

  agent{
    node {
      label "master"
    }
  }

  stages{

    stage('clean'){
      steps{
        deleteDir()
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
