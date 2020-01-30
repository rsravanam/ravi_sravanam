#!/usr/bin/env groovy

// get current build user
def getBuildUser() {
    return currentBuild.rawBuild.getCause(Cause.UserIdCause).getUserId()
}

// build duration
def getBuildDuration() {
    return Util.getTimeSpanString(System.currentTimeMillis() - currentBuild.startTimeInMillis)
}

def call(Map stageParams) {
    
    def channel = stageParams.channel
    //def alertessage = stageParams.msg
    def status = stageParams.status
    def environment = stageParams.environment
    def buildResult = "${currentBuild.currentResult}"
    def BUILD_USER = getBuildUser()
    alertMessage = "*--- ${status} ---* \n *ENV: * `${environment}`\n *JOB: * `${env.JOB_NAME}`\n *TRIGGERED BY: * `${BUILD_USER}` \n *BUILD NUMBER: * `${env.BUILD_NUMBER}`\n *BUILD URL: * (<${env.BUILD_URL}|Open>)"    
    
    if (buildResult == "SUCCESS") {
        color = "good" 
    } else if (buildResult == "FAILURE") {
        color = "danger" 
    } else if (buildResult == "ABORTED") {
        color = "warning" 
    } else {
        color = "warning"
    }

    slackSend (
        channel: "${channel}",
        color: "${color}",
        message: "${alertMessage}"
    )
}