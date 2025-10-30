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
                bat "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python314\\python.exe extract.py"
            }
        }
     }


}