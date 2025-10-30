pipeline {
     agent any
     stages {
        stage('checkout code') {
            steps {
                checkout scm
            }
        }
        stage('extract data') {
            steps {
                bat "python extract.py"
            }
        }
     }


}