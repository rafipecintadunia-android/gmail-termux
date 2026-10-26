cd ~/gmail-termux
cat > indrive_logger.py << 'PYEOF'
#!/usr/bin/env python3
import json, subprocess, time, os
from datetime import datetime

LOG_FILE = "indrive_orders.log"
JSON_FILE = "indrive_orders.json"

def get_notifications():
    try:
        result = subprocess.getoutput("termux-notification-list")
        # kadang keluarannya bukan json murni
        if not result.strip().startswith("["):
            return []
        return json.loads(result)
    except Exception as e:
        print(f"Error baca notif: {e}")
        return []

def git_push_cepat():
    try:
        os.system("git add indrive_orders.log indrive_orders.json > /dev/null 2>&1")
        os.system('git commit -m "order baru inDrive" > /dev/null 2>&1')
        os.system("git push > /dev/null 2>&1")
        print(">> AUTO PUSH KE GITHUB, EMAIL