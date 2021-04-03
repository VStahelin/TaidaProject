# Configure firewall in raspberry host
sudo netstat -lptu
Command: ufw  
Tutorials:
> https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04-pt  


# Clone Project
```git clone https://github.com/VStahelin/TaidaProject.git /TaidaProject ```

# Virtual env
(Inside project dir)  
Install venv: ```pip install virtualenv```  
Create project venv: ```virtualenv taida_venv```  
Enter in venv: ```source taida_venv/bin/activate```  

# Database
Docker images:  
    - MariaDB: https://hub.docker.com/r/linuxserver/mariadb  (linuxserver/mariadb)  
    - MySql: https://hub.docker.com/r/linuxserver/mysql (linuxserver/mysql)  

Mariadb password = ```HXt5A8QnGkNbpLEr34HpWkeaws753j9u4Aw3FsUX```  
Database name: ```taidaproject```  
Database user: ```taidauser```  
User Password: ```ZAJFBuamEtuVTzWj2598WMy```  

Docker container: ```sudo docker run --restart always -d --name mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=HXt5A8QnGkNbpLEr34HpWkeaws753j9u4Aw3FsUX linuxserver/mariadb```  
Enter in MariaDB container: ```docker exec -it mariadb bash```  
> mysql -uroot -p  
CREATE database taidaproject;  
CREATE USER taidauser@'%' IDENTIFIED BY 'ZAJFBuamEtuVTzWj2598WMy';  
GRANT ALL PRIVILEGES ON taidaproject.* TO taidauser@'%';  
FLUSH PRIVILEGES;  
