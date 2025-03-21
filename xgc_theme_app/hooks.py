app_name = "xgc_theme_app"
app_title = "Xgc Theme App"
app_publisher = "XGC Software Inc"
app_description = "XGC One UI Theme"
app_email = "support@xgccorp.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
 add_to_apps_screen = [
 	{
 		"name": "xgc_theme_app",
 		"logo": "/assets/xgc_theme_app/images/logo/xgclogo.png",
 		"title": "Xgc Theme App",
 		"route": "/xgc_theme_app",
 		"has_permission": "xgc_theme_app.api.permission.has_app_permission"
 	}
 ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/xgc_theme_app/css/oneui.css"
app_include_js = "/assets/xgc_theme_app/js/oneui.app.min.js"
app_include_js = "/assets/xgc_theme_app/js/setTheme.js"

# include js, css files in header of web template
web_include_css = "/assets/xgc_theme_app/css/oneui.css"
web_include_js = "/assets/xgc_theme_app/js/oneui.app.min.js"
web_include_js = "/assets/xgc_theme_app/js/setTheme.js"

# include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "xgc_theme_app/public/scss/main.scss"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "xgc_theme_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "xgc_theme_app.utils.jinja_methods",
# 	"filters": "xgc_theme_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "xgc_theme_app.install.before_install"
# after_install = "xgc_theme_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "xgc_theme_app.uninstall.before_uninstall"
# after_uninstall = "xgc_theme_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "xgc_theme_app.utils.before_app_install"
 after_app_install = "xgc_theme_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

 before_app_uninstall = "xgc_theme_app.utils.before_app_uninstall"
# after_app_uninstall = "xgc_theme_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

 notification_config = "xgc_theme_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
 }
#
 has_permission = {
 	"Event": "frappe.desk.doctype.event.event.has_permission",
 }

# DocType Class
# ---------------
# Override standard doctype classes

 override_doctype_class = {
 	"ToDo": "custom_app.overrides.CustomToDo"
 }

# Document Events
# ---------------
# Hook on document methods and events

 doc_events = {
 	"*": {
 		"on_update": "method",
 		"on_cancel": "method",
 		"on_trash": "method"
 	}
 }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"xgc_theme_app.tasks.all"
# 	],
# 	"daily": [
# 		"xgc_theme_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"xgc_theme_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"xgc_theme_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"xgc_theme_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "xgc_theme_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "xgc_theme_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "xgc_theme_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["xgc_theme_app.utils.before_request"]
# after_request = ["xgc_theme_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["xgc_theme_app.utils.before_job"]
# after_job = ["xgc_theme_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"xgc_theme_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

