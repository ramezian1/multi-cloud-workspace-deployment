# AWS WorkSpaces Setup (Template)

## Prerequisites
- AWS account with permissions for WorkSpaces, IAM, VPC, Directory Service, S3, CloudWatch.
- Existing VPC with private subnets and appropriate routing/NACLs.
- AD Connector or AWS Managed Microsoft AD (for SSO).

## Steps (High-level)
1. **Directory Integration**
   - Set up AWS Managed Microsoft AD *or* AD Connector to on‑prem/EC2 AD.
   - Verify user sync and test a pilot WorkSpace user.

2. **Networking**
   - Choose two private subnets in different AZs for WorkSpaces.
   - Ensure Security Groups allow WorkSpaces traffic per AWS docs.

3. **Bundles & Images**
   - Select standard Windows/Linux bundles (or create a custom image).
   - Add required software via image builder where needed.

4. **Provisioning**
   - Create WorkSpaces for pilot users; validate profile persistence and MFA.
   - Roll out to additional users via bulk import.

5. **Storage**
   - Use S3 buckets for shared artifacts; apply `s3_lifecycle_policy.json` as needed.
   - Enable bucket versioning and default encryption (SSE-S3 or SSE-KMS).

6. **Monitoring**
   - Configure CloudWatch metrics/alarms for WorkSpaces health and capacity.
   - Stream logs to CloudWatch Logs for troubleshooting.

## Security Considerations
- Enforce MFA and conditional access policies.
- Restrict access by VPC endpoints and Security Groups.
- Apply least-privilege IAM roles for automation.

> Replace placeholders with your environment details before using in production.
