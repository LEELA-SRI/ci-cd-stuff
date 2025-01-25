
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

4. Browse to http://localhost:8080 and provide the password
   Password can be retreived from ```Docker logs <container_name>``` or
   ```docker exec -it <container_name> cat /var/jenkins_home/secrets/initialAdminPassword```
