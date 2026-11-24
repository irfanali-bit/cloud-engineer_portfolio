# AWS Three-Tier Architecture Project

## Overview
Designing and deploying a Three-Tier Architecture on AWS using a custom VPC, public and private subnets, Application Load Balancer (ALB), Auto Scaling Group (ASG), and Amazon RDS.

## Architecture Tiers & Components
1. **Networking (VPC):**
   - Custom VPC with Public and Private Subnets across Availability Zones
   - Internet Gateway (IGW) for public subnet internet access
   - NAT Gateway for private subnet outbound access (updates/patches)
   - Route Tables, Security Groups, and Network ACLs

2. **Web / Application Tier:**
   - Application Load Balancer (ALB) to distribute incoming traffic
   - EC2 instances with Auto Scaling Group (ASG) for high availability and scalability

3. **Database Tier:**
   - Amazon RDS placed in private subnets
   - Access restricted to application/web tier via Security Groups

## Why This Design?
- **Security:** Database and internal workloads stay isolated in private subnets.
- **High Availability & Scalability:** ALB and ASG handle traffic spikes and instance failures automatically.
- **Maintainability:** Managed RDS reduces manual database administration overhead.
