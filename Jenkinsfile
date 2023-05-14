pipeline {
    agent any

    tools {
        // Define the Docker tool
        dockerTool 'docker'
    }

    stages {
        stage('Build image') {
            steps {
                // Build the Docker image
                sh 'docker build -t my-image .'
            }
        }

        stage('Run container') {
            steps {
                // Run the Docker container
                sh 'docker run -d -p 8080:8080 my-image'
            }
        }
    }
}
