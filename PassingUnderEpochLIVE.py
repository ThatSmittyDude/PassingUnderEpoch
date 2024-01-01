#PassingUnderEpochLive
#Author: Austin Smith
#Email: ThatSmittyDude@outlook.com
#Unix Timestamp: 1704078801

while True:
    import time
    from datetime import datetime
    
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    
    unix_time_r = round(unix_timestamp)
    
    
    print(" ")
    print("Unix Timestamp:", unix_time_r)
    print(" ")
    time.sleep(1)
    