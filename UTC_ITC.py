from datetime import datetime, timedelta

def convert_utc_to_ist(utc_time_str):
    # Parse the UTC time string to a datetime object
    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%d %H:%M:%S')
    
    # Add the time difference to get IST time
    ist_time = utc_time + timedelta(hours=5, minutes=30)
    
    return ist_time

# Example usage:

utc_time_str = '2024-05-23 06:25:55'  # This should be in 'YYYY-MM-DD HH:MM:SS' format
ist_time = convert_utc_to_ist(utc_time_str)
print('IST Time:', ist_time)
