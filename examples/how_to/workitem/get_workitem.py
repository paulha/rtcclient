from rtcclient.client import RTCClient
from rtcclient.utils import setup_basic_logging


if __name__ == "__main__":
    # you can remove this if you don't need logging
    # default logging for console output
    setup_basic_logging()

    # -- Had to make many modifications to the below url...
    url = "https://rtc.intel.com/ccm0014001/web/projects/SSG-OTC%20Product%20Management%20-%20RTC"
    username = "sys_pm"
    password = "<,dUt<x3{T^C}RREuxa)s&~2=t8%F$JY"
    myclient = RTCClient(url, username, password)

    # get all workitems
    # If both projectarea_id and projectarea_name are None, all the workitems
    # in all ProjectAreas will be returned
    # Note: Gets to here and blows up now...
    workitems_list = myclient.getWorkitems(projectarea_id=None,
                                           projectarea_name=None)

    # get a workitem with its id
    workitem_id = 240687
    wk = myclient.getWorkitem(workitem_id)
