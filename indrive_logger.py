#!/usr/bin/env python3
import json, subprocess, time, os
from datetime import datetime

LOG_FILE = "indrive_orders.log"
JSON_FILE = "indrive_orders.json"

def get_notifications():
    try:
        result = subprocess.getoutput("termux-notification-list")
        if not result.strip().startswith("["):
            return []
        return json.loads(result)
    except:
        return []

def git_push_cepat():
    try:
        os.system("git add indrive_orders.log indrive_orders.json > /dev/null 2>&1")
        os.system('git commit -m "order baru inDrive" > /dev/null 2>&1')
        os.system("git push > /dev/null 2>&1")
        print("AUTO PUSH KE GITHUB, EMAIL AKAN TERKIRIM!")
    except:
        pass

print("=== LOGGER INDRIVE KENCENG AKTIF ===")
last_content = set()

while True:
    notifs = get_notifications()
    jam = datetime.now().strftime('%H:%M:%S')
    found_now = 0
    for n in notifs:
        pkg = n.get("packageName","").lower()
        if "indriver" in pkg or "indrive" in pkg:
            title = n.get("title","") or ""
            content = n.get("content","") or n.get("text","")
            full = f"{title} {content}".strip()
            if len(full) < 5: continue
            if full in last_content: continue
            if "Rp" in full or "km" in full.lower() or "penumpang" in full.lower():
                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_line = f"[{waktu}] {title} | {content}\n"
                print(f"\nORDER BARU [{jam}]")
                print(log_line)
                with open(LOG_FILE, "a") as f:
                    f.write(log_line)
                with open(JSON_FILE, "w") as f:
                    json.dump({"waktu": waktu, "title": title, "content": content}, f)
                subprocess.getoutput("termux-vibrate -d 800")
                last_content.add(full)
                found_now += 1
                git_push_cepat()
    if found_now == 0:
        print(f"\rCek {jam} - standby...", end="")
    time.sleep(2)
