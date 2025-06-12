# extras/streamlit_notify/__init__.py

from streamlit_notify.extras import (
    toast_stn,
    balloons_stn,
    snow_stn,
    success_stn,
    info_stn,
    error_stn,
    warning_stn,
    exception_stn,
    notify,
    has_notifications,
    clear_notifications,
    get_notifications,
)

from .. import extra

toast_stn = extra(toast_stn)
balloons_stn = extra(balloons_stn)
snow_stn = extra(snow_stn)
success_stn = extra(success_stn)
info_stn = extra(info_stn)
error_stn = extra(error_stn)
warning_stn = extra(warning_stn)
exception_stn = extra(exception_stn)
notify = extra(notify)
has_notifications = extra(has_notifications)
clear_notifications = extra(clear_notifications)
get_notifications = extra(get_notifications)

def example_notify_toast():
    import streamlit as st
    from streamlit_notify.extras import toast_stn, notify

    notify()

    # Display toast notifications with different priorities and icons
    if st.button("Show High Priority Toast"):
        toast_stn("🎉 Welcome back!", icon="👋")
        st.rerun()

    # can also set priority and data
    if st.button("Show Medium Priority Toast"):
        toast_stn("🔔 Reminder: Meeting at 3 PM", priority=5,
                 data={"meeting_time": "3 PM", "location": "Zoom"})
        st.rerun()
    

def example_balloons():
    import streamlit as st
    from streamlit_notify.extras import balloons_stn, notify
    
    notify()

    # Display balloons with celebration context
    if st.button("🎊 Celebrate Achievement"):
        balloons_stn()
        st.rerun()
        

def example_snow():
    import streamlit as st
    from streamlit_notify.extras import snow_stnm, notify

    notify()
    
    # Display snow with seasonal context
    if st.button("❄️ Winter Theme"):
        snow_stn()
        st.rerun()

def example_success():
    import streamlit as st
    from streamlit_notify.extras import success_stn, notify

    notify()
    
    # Display success messages for different operations
    if st.button("💾 Save Data"):
        success_stn("Data saved successfully!")
        st.rerun()
        

def example_info():
    import streamlit as st
    from streamlit_notify.extras import info_stn, notify

    notify()
    
    # Display info messages with helpful context
    if st.button("📊 Data Update"):
        info_stn("New data available for analysis")
        st.rerun()
        

def example_error():
    import streamlit as st
    from streamlit_notify.extras import error_stn
    
    # Display error messages with troubleshooting info
    if st.button("❌ Data Load Error"):
        error_stn("Failed to load data from source")
        st.rerun()
        
def example_warning():
    import streamlit as st
    from streamlit_notify.extras import warning_stn, notify
    
    notify()

    # Display warnings with actionable information
    if st.button("⚠️ Storage Warning"):
        warning_stn("Storage space running low (85% full)")
        st.rerun()
        

def example_exception():
    import streamlit as st
    from streamlit_notify.extras import exception_stn, notify
    
    notify()
    
    # Display exception notifications with debug info
    if st.button("🐛 Processing Error"):
        try:
            raise ValueError("Invalid input: expected number, got string")
        except Exception as e:
            exception_stn(e)
            st.rerun()
            
    if st.button("⚡ Timeout Error"):
        try:
            raise TimeoutError("API request timed out after 30 seconds")
        except Exception as e:
            exception_stn(e, priority=8,
                         data={"endpoint": "/api/data", "timeout": "30s"})
            st.rerun()

def example_notify():
    import streamlit as st
    from streamlit_notify.extras import notify, toast_stn, success_stn

    notify(filter='toast') # Display only toast notifications
    
    # Queue multiple notifications then display them
    if st.button("Show Toast Notifications"):
        toast_stn("🔔 Notification 1", priority=3)
        toast_stn("🔔 Notification 2", priority=5)
        success_stn("✅ Success Notification", priority=7)
        st.rerun()

    # will not be displayed because we filtered for 'toast'
    if st.button("Show Success Notifications"):
        success_stn("🎉 Success Notification 1", priority=2)
        success_stn("🎉 Success Notification 2", priority=4)
        st.rerun()



def example_has_notifications():
    import streamlit as st
    from streamlit_notify.extras import has_notifications
    
    # has any notifications been queued?
    if has_notifications():
        st.write("🔔 Notifications are queued!")

    # check specifuic notification types
    if has_notifications(filter='toast'):
        st.write("🔔 Toast notifications are queued!")

def example_clear_notifications():
    import streamlit as st
    from streamlit_notify.extras import clear_notifications

    # Clear all notifications
    if st.button("Clear All Notifications"):
        clear_notifications()
        st.write("✅ All notifications cleared!")

    # Clear specific notification types
    if st.button("Clear Toast Notifications"):
        clear_notifications(filter='toast')
        st.write("✅ Toast notifications cleared!")

def example_get_notifications():
    import streamlit as st    
    from streamlit_notify.extras import get_notifications, toast_stn

    for notification_type, notifications in get_notifications(filter='toast').items():
        st.write(f"🔔 {notification_type.capitalize()} Notifications:")
        for notification in notifications:

            base_widget = notification.base_widget
            widget_args = notification.args
            priority = notification.priority
            data = notification.data

            st.write(f"Base Widget: {base_widget}")
            st.write(f"Args: {widget_args}")
            st.write(f"Data: {data}")
            st.write(f"Priority: {priority}")

            if notification.data == 'Hello World':
                notification.notify()  # Display each notification

    # Display toast notifications with different priorities and icons
    if st.button("Show High Priority Toast"):
        toast_stn("🎉 Welcome back!", icon="👋", priority=20, data='Hello World')
        st.rerun()

__title__ = "Streamlit Notify"
__desc__ = "A Streamlit component that provides status elements that persist across reruns." 
__icon__ = "🔭"
__examples__ = {
    example_notify_toast: [toast_stn],
    example_balloons: [balloons_stn],
    example_snow: [snow_stn],
    example_success: [success_stn],
    example_info: [info_stn],
    example_error: [error_stn],
    example_warning: [warning_stn],
    example_exception: [exception_stn],
    example_notify: [notify],
    example_has_notifications: [has_notifications],
    example_clear_notifications: [clear_notifications],
    example_get_notifications: [get_notifications],
}
__author__ = "Patrick Garrett"
__pypi_name__ = "streamlit-notify"
__package_name__ = "streamlit_notify"
__github_repo__ = "https://github.com/pgarrett-scripps/Streamlit_Notify"
__streamlit_cloud_url__ = "https://st-notify.streamlit.app/"
__experimental_playground__ = False

