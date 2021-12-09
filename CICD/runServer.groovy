pipeline{

  agent{
    node {
      label "master"
    }
  }
  
  stages{

    stage('clean'){
      deleteDir()
    }

    stage('Run Server'){
      steps{
        cd ${env.WORKSPACE}
        println("Inside WORKSPACE: ${env.WORKSPACE}")
        cd relationalDBManagementSystem/CICD/
        sudo chmod 777 runserver.sh
        sh runserver.sh
      }
    }
  }

}
