##Building Docker image:  
```docker build . -t <image_name> ```  
##Run Docker container:  
```docker run -p 5000:5000 <image_name>```  
##Run Docker container in detached mode:  
```docker run -d -p 5000:5000 <image_name>```  
##Run Docker container an interactive mode:  
```docker run -d -p 5000:5000 <image_name>```   
```docker run -it <container id>```   
##Show all containers:  
```docker ps -a ```  
##Stop the container:  
```docker stop <container id>```   
##Remove the container:  
```docker rm <container id> ```  
##Show container logs:  
```docker logs <container id> ```  
##Attach to running container:  
```docker attach <conainer id> ```  
##Build docker-compose image:  
```docker-compose build ```  
##Run docker-compose image:  
```docker-compose up```  
