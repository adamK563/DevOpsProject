pipeline {
  agent any
  stages {
    stage('Build and push') {
      steps {
        sh 'docker build -t backend .'
        sh 'docker push backend'
      }
    }
  }
}
