# vulnerable-labs

This is a collection of source code with docker images to build vulnerable web applications made for exploitation. These "challenges" are made for beginners and showcase popular web attack vectors.

Each lab has its own folder. To install these locally, you can first clone the repository :
![1](https://github.com/user-attachments/assets/49c356b9-380d-45ef-8c35-d669c0d7be7f)

Then, move into the directory of the lab you want to do. Execute the setup shell script :
![2](https://github.com/user-attachments/assets/0ea70edd-43d3-4fc4-89b2-02a04554d3b4)

The shell script automatically imports the source code and builds the docker image. It then runs the container. The web application running on the docker container is mapped to a port on our localhost. You can then access this challenge through this port :
![3](https://github.com/user-attachments/assets/eb706cb3-07a0-4058-b4ce-48268299af22)

Once done, you can exit out of the container and stop its execution :
![4](https://github.com/user-attachments/assets/e1998a94-0ace-4bb8-add9-32699db0256a)

The --rm flag instanly removes it from the docker container list.
All of the CSS and most of the HTML are AI-generated. 
