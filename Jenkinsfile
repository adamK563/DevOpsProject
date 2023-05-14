pipeline {
    agent any
    stages {
        stage('Build image') {
            steps {
                sh 'uptime'
            }
        }
    }
    post {
        always {
            echo 'This will always run on (success/failure/unstable/changed)'
        }
        success {
            echo 'This will run only if the build succeeds'
        }
        failure {
            echo 'This will run only if the build fails'
        }
        unstable {
            echo 'This will run only if the build is unstable'
        }
        changed {
            echo 'This will run only if the build status has changed'
        }
    }
}
