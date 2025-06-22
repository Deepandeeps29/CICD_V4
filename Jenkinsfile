pipeline {
    agent any

    environment {
        DEPLOY_SERVER = '192.168.1.10'
        DEPLOY_USER = 'user'
        DEPLOY_PATH = '/var/www/html'
    }

    stages {

        stage('Install Requirements') {
            steps {
                echo '📦 Installing Python dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run UI Tests') {
            steps {
                echo '🧪 Running Selenium Pytest UI tests...'
                bat 'pytest --html=report.html'
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

                timeout(time: 2, unit: 'MINUTES') {
                    sshagent(credentials: ['deploy-key']) {
                        bat """
                            echo Transferring HTML report to server...
                            scp -o StrictHostKeyChecking=no report.html %DEPLOY_USER%@%DEPLOY_SERVER%:%DEPLOY_PATH%

                            echo Restarting Apache server remotely...
                            ssh -o StrictHostKeyChecking=no %DEPLOY_USER%@%DEPLOY_SERVER% "sudo systemctl restart apache2"
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD pipeline completed successfully!'

            // 📧 Send email with test report
            emailext (
                subject: "✅ UI Test Report - Build #${env.BUILD_NUMBER}",
                body: """
                    Hello Team,<br><br>
                    The UI automation test pipeline has completed successfully.<br>
                    <b>Project:</b> ${env.JOB_NAME}<br>
                    <b>Build Number:</b> ${env.BUILD_NUMBER}<br>
                    <b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a><br><br>
                    Please find the attached report for more details.<br><br>
                    Regards,<br>CI/CD Bot
                """,
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'deepanvinayagam1411@gmail.com',
                attachLog: false,
                attachmentsPattern: 'report.html',
                mimeType: 'text/html'
            )
        }
        failure {
            echo '❌ CI/CD pipeline failed. Check logs above.'
        }
    }
}
