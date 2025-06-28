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


def example_notify_toast():
    import streamlit as st
    from streamlit_notify.extras import toast_stn, notify

    # Will display all queued notifications
    notify()

    # Show a basic toast notification
    if st.button("Show High Priority Toast"):
        toast_stn("🎉 Welcome back!", icon="👋")
        st.rerun()

    # Show a toast with priority and extra data
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

    # Display balloons
    if st.button("🎊 Celebrate Achievement"):
        balloons_stn()
        st.rerun()


def example_snow():
    import streamlit as st
    from streamlit_notify.extras import snow_stn, notify

    notify()

    # Display snow
    if st.button("❄️ Winter Theme"):
        snow_stn()
        st.rerun()


def example_success():
    import streamlit as st
    from streamlit_notify.extras import success_stn, notify

    notify()

    # Display success messages
    if st.button("💾 Save Data"):
        success_stn("Data saved successfully!")
        st.rerun()


def example_info():
    import streamlit as st
    from streamlit_notify.extras import info_stn, notify

    notify()

    # Display info messages
    if st.button("📊 Data Update"):
        info_stn("New data available for analysis")
        st.rerun()


def example_error():
    import streamlit as st
    from streamlit_notify.extras import error_stn, notify

    notify()

    # Display error messages
    if st.button("❌ Data Load Error"):
        error_stn("Failed to load data from source")
        st.rerun()


def example_warning():
    import streamlit as st
    from streamlit_notify.extras import warning_stn, notify

    notify()

    # Display warnings
    if st.button("⚠️ Storage Warning"):
        warning_stn("Storage space running low")
        st.rerun()


def example_exception():
    import streamlit as st
    from streamlit_notify.extras import exception_stn, notify

    notify()

    # Display exception notifications
    if st.button("🐛 Processing Error"):
        try:
            raise ValueError("Invalid input")
        except ValueError as e:
            exception_stn(e)
            st.rerun()


def example_notify():
    import streamlit as st
    from streamlit_notify.extras import notify, toast_stn, success_stn

    # Show only toast notifications
    notify(element="toast")

    # Queue toast and success notifications
    if st.button("Show Toast Notifications"):
        toast_stn("🔔 Notification 1", priority=3)
        toast_stn("🔔 Notification 2", priority=5)
        success_stn("✅ Success Notification", priority=7)
        st.rerun()

    # These will not show because only 'toast' notifications are displayed
    if st.button("Show Success Notifications"):
        success_stn("🎉 Success Notification 1", priority=2)
        success_stn("🎉 Success Notification 2", priority=4)
        st.rerun()


def example_get_notification_queue():
    import streamlit as st
    from streamlit_notify.extras import get_notification_queue, notify

    # Get the toast notification queue
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
    st.write(f"Queue Size: {len(toast_notification_queue)}")

    if st.button("Add Toast Notification"):
        notify(element="toast", message="🔔 New Toast Notification", priority=3)
        st.rerun()


def example_get_notifications():
    import streamlit as st
    from streamlit_notify.extras import get_notifications, toast_stn, success_stn

    # Get all toast notifications
    toast_notifications = get_notifications("toast")

    toast_and_success_notifications = get_notifications(["toast", "success"])

    # Get all notifications of all types
    all_notifications = get_notifications()

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

    # Notifications are automatically created when you use an stn function like toast_stn(),
    # but you can also create custom notifications directly with create_notification()
    notify()

    if st.button("Create Custom Notification"):
        notification = create_notification(
            notification_type="toast",
            message="🌟 Custom Toast Notification",
            priority=4,
            icon="⭐",
        )

        # Manually add a custom notification to the queue
        get_notifications("toast").append(notification)


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

__title__ = "Streamlit Notify"
__desc__ = (
    "Queue and display Streamlit Status Elements like toasts, balloons, and snowflakes."
)
__icon__ = "🔔"
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