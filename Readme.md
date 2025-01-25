
# Installing Jenkins via Docker

1. **Build a Jenkins Image with blue-ocean plugin:**
    ```
    FROM jenkins/jenkins:2.494-jdk21
    USER root
    RUN apt-get update && apt-get install -y lsb-release python3-pip
    RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
    https://download.docker.com/linux/debian/gpg
    RUN echo "deb [arch=$(dpkg --print-architecture) \
    signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
    https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
    RUN apt-get update && apt-get install -y docker-ce-cli
    USER jenkins
    RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
    ```

2. **Build the docker image:**
    ```
    docker build -t <imagename>:<tag> .
    ```
3. **Run the container:**
    ```
    docker run --name <container_name> --restart=on-failure --detach `
    --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
    --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
    --volume jenkins-data:/var/jenkins_home `
    --volume jenkins-docker-certs:/certs/client:ro `
    --publish 8080:8080 --publish 50000:50000 <imagename>:<tag>
    ```

4. Browse to http://localhost:8080 and provide the password.
   Password can be retreived from<br> ```Docker logs <container_name>``` <br>or<br>
   ```docker exec -it <container_name> cat /var/jenkins_home/secrets/initialAdminPassword```


# Configuring jenkins

**Plugins**
1. Navigate to Dashboard> Manage Jenkins > System Config > plugins.
2. Search for the Docker plugin, install the update, and reload Jenkins.

**Jenkins Agents**   

1. Navigate to Dashboard> Manage Jenkins > System Config > Clouds
2. Create a new cloud with the type set to Docker.
3. In the **Docker Cloud** details, configure the following:<br>
       **Docker Host URI** (Example: tcp://<ip>:<port>) - Run the following commands to expose Docker over TCP:<br><br>
       ``` docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock


       docker inspect <container_id>
       ``` 
       <br>
       Find the **HostPort** under NetworkSettings > Ports and the **IpAddress** under NetworkSettings > Networks > jenkins.
5. Test the connection and save the configuration.
6. Go to **Docker Agent Template** > Add **docker template** and configure the following<br>
       **Name:** Name of the cloud agent.<br>
       **Label:** Same as the name.<br>
        Check the **"Enabled"** box.<br>
       **Docker Image:** Provide an image from the registry.<br>
       **Instance Capacity:** Set to 2 (or as desired).<br>
       **Remote File System Root:** /home/jenkins.<br>
7. Save the changes.


       
   
