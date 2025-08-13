"""Email alert monitor (template)
Monitors disk usage and error keywords, then emails a notification.
Replace placeholders and secure credentials (e.g., use AWS Secrets Manager / Azure Key Vault).
"""

import os, smtplib, shutil, time
from email.mime.text import MIMEText

THRESHOLD_PCT = int(os.getenv("DISK_THRESHOLD", "85"))
ALERT_TO = os.getenv("ALERT_TO", "admin@example.com")
ALERT_FROM = os.getenv("ALERT_FROM", "monitor@example.com")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_USER = os.getenv("SMTP_USER", "user")
SMTP_PASS = os.getenv("SMTP_PASS", "pass")

LOG_PATHS = os.getenv("LOG_PATHS", "/var/log/syslog").split(",")
ERROR_KEYWORDS = [k.strip() for k in os.getenv("ERROR_KEYWORDS", "ERROR,CRITICAL,FAILED").split(",")]

def disk_pct(path="/"):
    total, used, free = shutil.disk_usage(path)
    return int(used * 100 / total)

def scan_logs():
    hits = []
    for p in LOG_PATHS:
        if os.path.exists(p):
            with open(p, errors='ignore') as f:
                for line in f:
                    if any(k in line for k in ERROR_KEYWORDS):
                        hits.append(line.strip())
    return hits[:50]

def send_email(subject, body):
    msg = MIMEText(body)
    msg['From'] = ALERT_FROM
    msg['To'] = ALERT_TO
    msg['Subject'] = subject
    with smtplib.SMTP(SMTP_SERVER) as s:
        try:
            s.starttls()
        except Exception:
            pass
        if SMTP_USER and SMTP_PASS:
            try:
                s.login(SMTP_USER, SMTP_PASS)
            except Exception:
                pass
        s.sendmail(ALERT_FROM, [ALERT_TO], msg.as_string())

def main():
    alerts = []
    pct = disk_pct("/")
    if pct >= THRESHOLD_PCT:
        alerts.append(f"Disk usage high: {pct}%")
    log_hits = scan_logs()
    if log_hits:
        alerts.append("Recent errors:\n" + "\n".join(log_hits))
    if alerts:
        send_email("Infra Alert", "\n\n".join(alerts))

if __name__ == "__main__":
    # Run once; in production, wrap with a scheduler/systemd/cron
    main()
