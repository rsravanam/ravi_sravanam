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
    def alertMessage = stageParams.msg
    def buildResult = "${currentBuild.currentResult}"
    def BUILD_USER = getBuildUser()
    
    
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