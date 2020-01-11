from time import time, ctime, struct_time, gmtime, localtime

# time_tuple = (
#     year, month, day, 
#     hour, minute, second, 
#     day, day_of_year, daylight_savings
#     )
# time_tuple = (2019,2,26,7,6,55,1,57,0)

def get_struct_time():
    time_tuple = (2019,2,26,7,6,55,1,57,0)
    return struct_time(time_tuple)

def get_day_of_year():
    return time_obj.tm_yday

def get_day_of_month():
    return time_obj.tm_mday

def get_current_time():
    return gmtime()

import calendar
def get_epoch_from_calendar():
    return calendar.timegm(get_current_time())

def get_localtime_from_epoch():
    epoch_secs = time()
    return localtime(epoch_secs)

def get_system_epoch():
    return gmtime(0)

def observes_daylight_savings():
    t = time()
    st = localtime(t)
    print(f"t: {st}")
    print(f"t.tm_isdst: {st.tm_isdst}")

def get_timezone():
    current_local = localtime()
    return current_local.tm_zone

if __name__ == "__main__":
    time_obj = get_struct_time()

    print(f"get_day_of_month: {get_day_of_month()}")
    print(f"get_day_of_year: {get_day_of_year()}")
    print(f"get_current_time: {get_current_time()}")
    print(f"get_epoch_from_calendar: {get_epoch_from_calendar()}")
    print(f"get_localtime_from_epoch: {get_localtime_from_epoch()}")
    print(f"get_system_epoch: {get_system_epoch()}")
    print(f"observes_daylight_savings: {observes_daylight_savings()}")
    print(f"get_timezone: {get_timezone()}")