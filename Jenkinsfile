pipeline {
    agent any

    stages {

        stage('Install Requirements') {
            steps {
                echo '📦 Installing Python dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run UI Tests') {
            steps {
                echo '🧪 Running Selenium Pytest UI tests...'
                sh 'pytest --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                echo '📤 Publishing HTML Test Report...'
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
                echo '🚀 Deploying to remote Apache server...'
                sh '''
                    scp -o StrictHostKeyChecking=no -r * user@192.168.1.10:/var/www/html
                    ssh user@192.168.1.10 "sudo systemctl restart apache2"
                '''
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD pipeline completed successfully!'
        }
        failure {
            echo '❌ CI/CD pipeline failed. Check logs above.'
        }
    }
}
