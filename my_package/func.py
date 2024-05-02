import datetime
from dateutil import tz
#なんか[dateutil]は　$python3 -m pip install python-dateutil　じゃないとinstallできなかった
def convert_date_format(date_string):
    date_obj = datetime.datetime.fromisoformat(date_string.replace('Z', '+00:00'))
    utc_time = date_obj.replace(tzinfo=tz.gettz('UTC'))
    local_time = utc_time.astimezone(tz.gettz('Asia/Tokyo'))
    formatted_date = local_time.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_date
