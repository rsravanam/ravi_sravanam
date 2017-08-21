#docker pull ubuntu:14.04
#docker pull ubuntu:16.04
#docker image ls
#docker tag ccc7a11d65b1 sravanam1242/private_docker:ubuntu-16.04
#docker push sravanam1242/private_docker:ubuntu-16.04

$image_repo = "sravanam1242/private_docker"
$image_tag = "Apache-Mesos-POC-ubuntu-14.04"
$docker_file_location = "."
$docker_image_id = docker images -q ${image_repo}:${image_tag}

Write-Output $image_repo
Write-Output $image_tag
Write-Output $docker_file_location
Write-Output $docker_image_id

#Apache Mesos Master Installation (build with docker file)
#docker build -t $image_repo:$image_tag $docker_file_location
#docker commit $docker_image_id $image_repo:$image_tag
#docker push $image_repo:$image_tag