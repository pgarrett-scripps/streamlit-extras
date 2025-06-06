# extras/streamlit_notify/__init__.py

import streamlit_notify as stn
import streamlit as st
from .. import extra

mdlit = extra(stn)

def example():
    import streamlit_notify as stn
    import streamlit as st

    # Display all queued notifications at the beginning of your app. This will also clear the list.
    stn.notify_all()

    # Add a notification that will be displayed on the next rerun
    if st.button("Show Toast"):
        stn.toast("This is a toast message", icon="✅")
        st.rerun()

    if st.button("Show Balloons"):
        stn.balloons()
        st.rerun()

    if st.button("Show Success Message"):
        stn.success("Operation successful!")
        st.rerun()
    ...

__title__ = "Streamlit Notify"
__desc__ = "A Streamlit component that provides status elements that persist across reruns." 
__icon__ = "🔭"
__examples__ = [example] 
__author__ = "Patrick Garrett"
__pypi_name__ = "streamlit-notify"
__package_name__ = "streamlit_notify"
__github_repo__ = "https://github.com/pgarrett-scripps/Streamlit_Notify"
__streamlit_cloud_url__ = "https://st-notify.streamlit.app/"
__experimental_playground__ = False
__is_namespace__ = True