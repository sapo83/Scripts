# Docker commands

Build image - uses Dockerfile in current directory

`docker build -t my_image .`

Run container

`docker run my_image`

Run container - allow for interactive shell

`docker run -t my_image /bin/bash/`

Remove all stopped containers

`docker container prune`

Remove all docker images - **WILL REMOVE EVERYTHING!**

`docker rmi $(docker images -q)`
