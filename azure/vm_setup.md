# Azure VM Setup (Template)

## Prerequisites
- Azure subscription with access to Compute, Storage, Networking, Monitor.
- Resource Group, Virtual Network, and subnets in place.
- Azure AD / Entra ID integrated; optional AD DS or AAD DS for domain join.

## Steps (High-level)
1. **Networking & Security**
   - Create/choose VNet, subnets, and NSGs (ingress minimal; use Just-In-Time access).
   - Configure Azure Bastion or a jump host for admin access.

2. **Provision VMs**
   - Create Windows and/or Linux VMs for testing/staging.
   - Use VM Extensions for bootstrap (custom script extension) to install dependencies.

3. **Identity & Access**
   - Join to domain (if required) and configure SSO with Entra ID.
   - Use Managed Identities for app access to storage/secrets.

4. **Storage**
   - Use Azure Blob Storage for shared data.
   - Apply lifecycle policy similar to `blob_lifecycle_policy.json`.

5. **Monitoring**
   - Enable Azure Monitor and Log Analytics.
   - Create alerts for CPU, disk, and critical log patterns.

## Security Considerations
- Restrict RDP/SSH; use Bastion/Privileged Identity Management.
- Encrypt disks, enforce Defender for Cloud recommendations.
- Keep images and extensions patched.

> Replace placeholders with your environment details before using in production.
