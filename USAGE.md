# Usage Guide — Multi-Cloud Virtual Workspace Deployment

This repository is a **template and documentation project** for setting up a hybrid virtual workspace using AWS and Azure.  
It is designed for **portfolio demonstration** and **real-world IT support scenarios**.

---

## 1. Prerequisites
- AWS account with WorkSpaces, S3, IAM, CloudWatch permissions  
- Azure subscription with Virtual Machines, Blob Storage, Monitor access  
- Basic knowledge of networking, Active Directory, and cloud concepts  
- Python 3.x installed (for automation scripts)

---

## 2. Repository Structure
```
/aws
  workspace_setup.md         # AWS WorkSpaces setup guide
  s3_lifecycle_policy.json   # Example S3 lifecycle rules
/azure
  vm_setup.md                # Azure VM setup guide
  blob_lifecycle_policy.json # Example Blob Storage lifecycle rules
/scripts
  email_alert_monitor.py     # Disk/log alert email script
  log_parser.py              # Multi-log parser script
/docs
  architecture-diagram.png   # Project network diagram
README.md
USAGE.md
```

---

## 3. How to Use

### Step 1 — Review Architecture
Open `/docs/architecture-diagram.png` to see the high-level design.

### Step 2 — Set Up AWS
1. Follow `/aws/workspace_setup.md` to deploy AWS WorkSpaces and S3 storage.  
2. Apply lifecycle policies from `s3_lifecycle_policy.json`.

### Step 3 — Set Up Azure
1. Follow `/azure/vm_setup.md` to deploy Azure Virtual Machines and Blob storage.  
2. Apply lifecycle policies from `blob_lifecycle_policy.json`.

### Step 4 — Integrate Identity
- Connect AWS and Azure environments to your on-prem or Azure Active Directory for SSO.

### Step 5 — Monitor & Automate
1. Deploy `email_alert_monitor.py` on a monitoring host to receive disk/log alerts.  
2. Use `log_parser.py` to consolidate and review system logs.

---

## 4. Customization
- Replace placeholder values in `.md` and `.json` files with your environment details.  
- Swap `/docs/architecture-diagram.png` with your own diagram from draw.io or Canva.  

---

## 5. Disclaimer
> This project is for **educational and demonstration purposes**.  
> Do not deploy in a production environment without reviewing and hardening configurations.
