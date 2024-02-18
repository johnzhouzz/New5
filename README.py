# New5
import time

def focus_clock(minutes):
    start_time = time.time()
    end_time = start_time + minutes * 60
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        print(time_str, end="\r")
        time.sleep(1)
    
    print("Time's up!")

# 设置专注时长为25分钟
focus_clock(25)
