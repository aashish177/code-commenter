pipeline {
    agent any // Runs on any available Jenkins node

    environment {
        OPENAI_API_KEY = credentials('OPENAI_API_KEY') // Load OpenAI API key from Jenkins secrets
    }

    stages {
        stage('Clone Repository') {
            steps {
            git credentialsId: 'github-credentials', branch: 'main', url: 'https://github.com/aashish177/code-commenter.git'
            }
        }

        stage('Set Up Python') {
            steps {
                sh 'python3 -m venv venv' // Create a virtual environment
                sh 'source venv/bin/activate && pip install -r requirements.txt' // Install dependencies 
            }
        }

        stage('Run AI Code Commenter') {
            steps {
                sh 'source venv/bin/activate && python3 commenter/cli.py sample.py test_script.py'
            }
        }


        stage('Commit and Push Changes') {
            steps {
                sh '''
                    git config --global user.name "jenkins-bot"
                    git config --global user.email "jenkins@ci.com"
                    git add .
                    git commit -m "Auto-generate AI  docstrings" || echo " No changes detected"
                    git push origin HEAD:{GIT_BRANCH}
                '''
            }
        }
    }
}