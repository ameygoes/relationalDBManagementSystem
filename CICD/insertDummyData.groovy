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
        sh "cd /var/lib/jenkins/workspace/runServer/backEnd/DummyDataGenerate;ls -lrt"
        println("Inside Folder: /var/lib/jenkins/workspace/runServer/backEnd/DummyDataGenerate")
        sh "ls -lrt;sudo chmod 777 /var/lib/jenkins/workspace/runServer/backEnd/DummyDataGenerate/DummyDataGeneration.py"
        sh "python3 DummyDataGeneration.py"
      }
    }
  }
}
