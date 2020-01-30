def call(){
    node {
        // Execute different stages depending on the job
        if(env.JOB_NAME.contains("deploy")){
            packageArtifact()
        } else if(env.JOB_NAME.contains("test")) {
            buildAndTest()
        }
    }
}

def packageArtifact(){
    stage("Package artifact") {
        sh "echo artifacts && sleep 10"
    }
}

def buildAndTest(){
    stage("Backend tests"){
        sh "echo test && sleep 10"
    }
}