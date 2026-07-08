import speedtest
from datetime import datetime

print("===== INTERNET SPEED TESTER =====\n")

try:
    st = speedtest.Speedtest()

    print("Finding Best Server...")
    st.get_best_server()

    print("Testing Download Speed...")
    download_speed = st.download() / 1_000_000

    print("Testing Upload Speed...")
    upload_speed = st.upload() / 1_000_000

    ping = st.results.ping

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    report = f"""
========== INTERNET SPEED REPORT ==========

Date & Time      : {current_time}

Download Speed   : {download_speed:.2f} Mbps
Upload Speed     : {upload_speed:.2f} Mbps
Ping             : {ping:.2f} ms

===========================================
"""

    print(report)

    with open("speed_history.txt", "a") as file:
        file.write(report)
        file.write("\n")

    print("✅ Result Saved in speed_history.txt")

except Exception as e:
    print("❌ Error:", e)
