# Project 2: AWS Application Load Balancer

## 1. Project Goal
I configured an Application Load Balancer to distribute traffic between two EC2 web servers.

Hindi: Maine do EC2 web servers ke beech traffic distribute karne ke liye Load Balancer configure kiya.

## 2. AWS Services Used
- EC2: Runs virtual servers.
- Nginx: Serves website content.
- Target Group: Contains registered web servers.
- Application Load Balancer: Distributes incoming requests.
- Security Groups: Control network access.

## 3. What I Did
1. Launched two EC2 instances.
2. Installed Nginx on both servers.
3. Created different web pages for Server A and Server B.
4. Created a Target Group.
5. Registered both EC2 instances.
6. Checked that both targets were healthy.
7. Created an Application Load Balancer.
8. Opened both server websites and tested their responses.

## 4. What I Learned
- A Load Balancer distributes incoming traffic between healthy targets.
- A Target Group identifies the servers that can receive requests.
- Health checks help identify unhealthy servers.
- Nginx serves the website on each EC2 instance.

## 5. Project Status
Completed as a hands-on learning project.
