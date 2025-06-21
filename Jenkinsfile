pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Deepandeeps29/CICD_V4.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run UI Tests') {
            steps {
                sh 'pytest --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportName: 'Test Report',
                    reportDir: '.',
                    reportFiles: 'report.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ])
            }
        }

        stage('CD: Deploy to Server') {
            steps {
                // Send files to server and restart Apache/Nginx
                sh '''
                    scp -o StrictHostKeyChecking=no -r * user@192.168.1.10:/var/www/html/
                    ssh user@192.168.1.10 "sudo systemctl restart apache2"
                '''
            }
        }
    }
}
