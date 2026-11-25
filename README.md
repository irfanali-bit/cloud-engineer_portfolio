# Cloud Engineering Portfolio

Hi! I'm an aspiring Cloud Engineer building practical skills through hands-on projects.

## About Me

I am learning AWS Cloud Engineering through practical labs and projects. My goal is to understand cloud infrastructure, deployment, storage, networking, and troubleshooting.

## Technical Skills

- AWS EC2
- Amazon EBS
- Amazon Machine Images (AMI)
- Application Load Balancer (ALB)
- Target Groups and Health Checks
- Linux (Ubuntu)
- Nginx Web Server
- Basic Networking

## Hands-on Projects

### 1. EC2 Web Server with Nginx
- Launched an EC2 instance using Ubuntu.
- Installed and configured Nginx.
- Hosted a custom web page.
- Practiced Security Group rules and HTTP access.

### 2. EBS Backup and Recovery
- Created and attached an EBS volume.
- Created a file on the volume.
- Created an EBS snapshot.
- Created a new volume from the snapshot.
- Verified data recovery.

### 3. Application Load Balancer
- Configured two EC2 instances with Nginx.
- Created a Target Group and registered both instances.
- Configured an Application Load Balancer.
- Tested the website through the load balancer DNS.
- Observed responses from both web servers.

## Learning Goals

- Improve AWS troubleshooting skills.
- Learn cloud security best practices.
- Build more hands-on cloud projects.
- Prepare for a Cloud Engineering internship or entry-level role.

## Note

These are personal hands-on learning projects, not professional work experience.    
## Three-Tier Web Architecture on AWS

Built and verified a Three-Tier Architecture in `ap-south-1` (Mumbai):

- **Networking:** Custom VPC (`three-tier-vpc`) with Public and Private Subnets (`ap-south-1a`, `ap-south-1b`), Internet Gateway, and Route Tables.
- **Security Groups:** `alb-sg` (HTTP 80 from `0.0.0.0/0`), `web-sg` (HTTP 80 from `alb-sg`), and `db-sg` (MySQL 3306 from `web-sg`).
- **Web & ALB Tier:** EC2 instance running Nginx behind an Application Load Balancer (`three-tier-alb`) and Target Group (`web-tg`).
- **Database Tier:** Amazon RDS MySQL (`three-tier-db`) in Private Subnets (`Public access: No`).
- **Proof & Cleanup:** Screenshots added in the [`images/`](./images) folder. All AWS resources were deleted after testing to avoid extra cost.
