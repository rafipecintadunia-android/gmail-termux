#!/usr/bin/env python3
import json, subprocess
from datetime import datetime

LOG_FILE = "indrive_orders.log"

def get_notifications():
    try:
        result = subprocess.getoutput("termux-notification-list")
        return json.loads(result)
    except:
        return []

notifs = get_notifications()
found = 0
print(f"Cek jam {datetime.now().strftime('%H:%M:%S')} - Total notif: {len(notifs)}")

for n in notifs:
    pkg = n.get("packageName","")
    if "inDriver" in pkg or "indriver" in pkg.lower():
        found += 1
        title = n.get("title","")
        content = n.get("content","")
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{waktu}] {title} | {content}\n"
        print(f"ORDER KETEMU: {log_line}")
        with open(LOG_FILE, "a") as f:
            f.write(log_line)

if found == 0:
    print("Belum ada notif inDrive aktif - normal kalau lagi sepi")
    print("Buka inDrive, biar ada notif di atas")
else:
    print(f"Berhasil catat {found} order")
