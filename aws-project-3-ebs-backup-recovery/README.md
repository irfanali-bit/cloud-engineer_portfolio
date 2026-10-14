# Project 3: AWS EBS Backup and Recovery

## 1. Project Goal
I practiced backing up data with an Amazon EBS snapshot and restoring it to a new EBS volume.

## 2. AWS Services and Tools
- Amazon EC2
- Amazon EBS
- EBS Snapshots
- Ubuntu/Linux commands

## 3. What I Did
1. Attached an EBS volume to my EC2 instance.
2. Created a file named `important.txt` on the mounted volume.
3. Created an EBS snapshot and waited until its status became Completed.
4. Created a new EBS volume from the snapshot.
5. Attached and mounted the restored volume.
6. Checked the restored file to verify that the data was recovered.

## 4. What I Learned
- EBS provides storage for EC2 instances.
- Snapshots help back up EBS volume data.
- A new volume can be created from a snapshot.
- A volume must be attached and mounted before accessing its files.
- Linux commands like `lsblk -f` and `cat` help verify disks and files.

## 5. Project Status
Completed as a hands-on learning project.

## 6. Cleanup
After testing, I cleaned up the temporary AWS resources I no longer needed.
