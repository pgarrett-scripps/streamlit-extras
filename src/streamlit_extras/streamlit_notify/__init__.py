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
    get_notifications,
    get_notification_queue,
    create_notification,
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
get_notifications = extra(get_notifications)
get_notification_queue = extra(get_notification_queue)
create_notification = extra(create_notification)


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
        toast_stn(
            "🔔 Reminder: Meeting at 3 PM",
            priority=5,
            data={"meeting_time": "3 PM", "location": "Zoom"},
        )
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
    from streamlit_notify.extras import snow_stn, notify

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
        except ValueError as e:
            exception_stn(e)
            st.rerun()

    if st.button("⚡ Timeout Error"):
        try:
            raise TimeoutError("API request timed out after 30 seconds")
        except TimeoutError as e:
            exception_stn(
                e, priority=8, data={"endpoint": "/api/data", "timeout": "30s"}
            )
            st.rerun()


def example_notify():
    import streamlit as st
    from streamlit_notify.extras import notify, toast_stn, success_stn

    notify(element="toast")  # Display only toast notifications

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


def example_get_notification_queue():
    import streamlit as st
    from streamlit_notify.extras import get_notification_queue, notify

    # Get the notification queue for 'toast' notifications directly
    toast_notification_queue = get_notification_queue("toast")

    """
    The notification queue supports standard list operations:

        append(item) - Add notification to queue
        extend(items) - Add multiple notifications
        pop(index) - Remove and return notification at index
        get(index) - Get notification without removing it
        remove(item) - Remove specific notification
        clear() - Remove all notifications
        has_items() - Check if queue has notifications
        is_empty() - Check if queue is empty
        contains(item) - Check if notification exists in queue
        get_all() - Get all notifications
        size() - Get number of notifications

    """

    # Display the current size of the queue
    st.write(
        f"Current Toast Notification Queue Size: {toast_notification_queue.size()}"
    )

    if st.button("Add Toast Notification"):
        notify(element="toast", message="🔔 New Toast Notification", priority=3)
        st.rerun()


def example_get_notifications():
    import streamlit as st
    from streamlit_notify.extras import get_notifications, toast_stn, success_stn

    toast_notifications = get_notifications("toast")

    for notification in toast_notifications:

        """
        Notification objects:

            Attributes:

                base_widget: Callable[..., Any]
                args: OrderedDict[str, Any]
                priority: int = 0
                data: Any = None

            Properties:
                name: str - Name of the notification type (e.g., 'toast')

            Methods:
                notify: Display the notification
        """

        notification.notify()  # Display each toast notification individually

    print(len(toast_notifications))  # Print number of toast notifications in queue

    if st.button("Queue Notifications"):
        toast_stn("🔔 Toast Notification", priority=3)
        success_stn("✅ Success Notification", priority=5)
        st.rerun()


def example_create_notification():
    import streamlit as st
    from streamlit_notify.extras import create_notification, get_notifications, notify

    # notifications are automatically created when you use a stn function like toast_stn()
    # but you can also create custom notifications directly with create_notification()
    notify()

    if st.button("Create Custom Notification"):
        notification = create_notification(
            notification_type="toast",
            message="🌟 Custom Toast Notification",
            priority=4,
            icon="⭐",
        )

        get_notifications("toast").append(notification)  # Manually add to toast queue


__title__ = "Streamlit Notify"
__desc__ = (
    "A Streamlit component that provides status elements that persist across reruns."
)
__icon__ = "🔭"
__examples__ = {  # type: ignore
    example_notify_toast: [toast_stn],
    example_balloons: [balloons_stn],
    example_snow: [snow_stn],
    example_success: [success_stn],
    example_info: [info_stn],
    example_error: [error_stn],
    example_warning: [warning_stn],
    example_exception: [exception_stn],
    example_notify: [notify],
    example_get_notification_queue: [get_notification_queue],
    example_get_notifications: [get_notifications],
    example_create_notification: [create_notification],
}
__author__ = "Patrick Garrett"
__pypi_name__ = "streamlit-notify"
__package_name__ = "streamlit_notify"
__github_repo__ = "https://github.com/pgarrett-scripps/Streamlit_Notify"
__streamlit_cloud_url__ = "https://st-notify.streamlit.app/"
__experimental_playground__ = False
