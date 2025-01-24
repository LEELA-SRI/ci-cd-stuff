pipeline {
    agent { 
        node {
            label 'docker-python-agent'
            }
      }
      triggers{
          pollSCM 'H/5 * * * *'
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                python3 -m venv venv
                . venv/bin/activate && cd myapp && pip install -r requirements.txt 
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                . venv/bin/activate && cd myapp && python3 hello.py && python3 hello.py --name=Maze && cd .. && python3 helloworld.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}