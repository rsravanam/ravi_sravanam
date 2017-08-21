#docker pull ubuntu:14.04
#docker pull ubuntu:16.04
#docker image ls
#docker tag ccc7a11d65b1 sravanam1242/private_docker:ubuntu-16.04
#docker push sravanam1242/private_docker:ubuntu-16.04

#		DOCKER ARGUMETNS
$IMAGE_REPO = "sravanam1242/private_docker"
$IMAGE_TAG = "Apache-Mesos-POC-ubuntu-14.04"
$DOCKER_FILE_LOCATION = "."
$DOCKER_IMAGE_ID = docker images -q $IMAGE_REPO':'$IMAGE_TAG

$MESSAGE = "**********CURRENT DOCKER IMAGE DETAILS**********"

Write-Output $MESSAGE
Write-Output ""
Write-Output "IMAGE_REPO is $IMAGE_REPO"
Write-Output "IMAGE_TAG is $IMAGE_TAG"
Write-Output "DOCKER_FILE_LOCATION is $DOCKER_FILE_LOCATION"
Write-Output "DOCKER_IMAGE_ID is $DOCKER_IMAGE_ID"
Write-Output ""
Write-Output "****************************************"

#Apache Mesos Master Installation step (build with docker file)
docker build -t $IMAGE_REPO':'$IMAGE_TAG $DOCKER_FILE_LOCATION
docker commit $DOCKER_IMAGE_ID $IMAGE_REPO':'$IMAGE_TAG
docker push $IMAGE_REPO':'$IMAGE_TAG

$MESSAGE = "**********LATEST DOCKER IMAGE DETAILS**********"
Write-Output $MESSAGE
Write-Output ""
Write-Output "IMAGE_REPO is $IMAGE_REPO"
Write-Output "IMAGE_TAG is $IMAGE_TAG"
Write-Output "DOCKER_FILE_LOCATION is $DOCKER_FILE_LOCATION"
Write-Output "DOCKER_IMAGE_ID is $DOCKER_IMAGE_ID"
Write-Output ""
Write-Output "*********************************************"