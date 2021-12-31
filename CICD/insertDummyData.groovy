pipeline{

  agent any

  stages{

    stage('clean'){
      steps{
        sh "cd /var/lib/jenkins/workspace/"
        checkout scm
      }
    }

    stage('Insert Dummy Data'){
      steps{
        sh "cd ${env.WORKSPACE}/DummyDataGenerate/;pwd"
        println("Inside Folder: ${env.WORKSPACE}/DummyDataGenerate/")
        sh "ls -lrt;sudo chmod 777 ${env.WORKSPACE}/DummyDataGenerate/DummyDataGeneration.py"
        sh "python3 DummyDataGeneration.py"
      }
    }
  }
}
