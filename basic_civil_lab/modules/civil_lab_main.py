import streamlit as st
import importlib
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os  # For environment variables

def send_feedback_email(feedback_text, tool_name):
    sender_email = "vedthakursa@gmail.com"
    sender_password = os.environ.get("EMAIL_PASSWORD")  # Store securely, e.g. export EMAIL_PASSWORD=your_app_password
    recipient_email = "vedthakursa@gmail.com"  # Locked

    msg = MIMEText(f"Tool: {tool_name}\nTime: {datetime.now()}\n\nFeedback:\n{feedback_text}")
    msg['Subject'] = f'New Feedback for {tool_name}'
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

def run():
    st.set_page_config(page_title="Civil Engineering Lab Suite", layout="centered")
    st.title("🧱 Civil Engineering Lab Suite")
    st.caption("10 Interactive Modules for Basic Civil Engineering")

    modules_dict = {
        "brick_compression_tool": "Brick Compression Strength Tester",
        "cement_consistency_tester": "Cement Consistency Assessment",
        "cement_fineness_analyzer": "Cement Fineness Analyzer",
        "cement_soundness_test": "Cement Soundness Evaluation",
        "fineness_modulus_calculator": "Fineness Modulus Calculator (Aggregate Grading)",
        "flow_table_test": "Cement Flow Table Test (Workability)",
        "sand_bulking_analyzer": "Sand Bulking Analyzer",
        "sieve_analysis_simulator": "Aggregate Sieve Analysis Simulator",
        "specific_gravity_calculator": "Specific Gravity Calculator (Materials)",
        "water_absorption_checker": "Water Absorption Checker (Brick/Material)",
        "constant_range_demo_1": "Constant Range Graph Demo"
    }

    selected_friendly = st.sidebar.selectbox("Select a Lab Module to Run", list(modules_dict.values()))
    selected_module = [key for key, value in modules_dict.items() if value == selected_friendly][0]

    try:
        module = importlib.import_module(f"basic_civil_lab.modules.{selected_module}")

        # Run the selected module
        if hasattr(module, "run"):
            module.run()
        else:
            st.error(f"Module '{selected_module}' does not have a run() function.")
    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_module}': {e}")

    # --- FEEDBACK SECTION ---
    st.markdown("---")
    st.subheader("Submit Feedback for this Tool")

    feedback_text = st.text_area("Enter your feedback (sent privately to the tool developer):")

    # Add a tip about App Passwords for Gmail
    st.info(
        "Tip: To enable feedback emailing, set your Gmail App Password as the environment variable 'EMAIL_PASSWORD'. "
        "Do not use your regular Gmail password if 2-Step Verification is enabled."
    )

    if st.button("Send Feedback"):
        if feedback_text.strip():
            try:
                send_feedback_email(feedback_text, selected_friendly)
                st.success(
                    "Thank you! Your feedback has been emailed directly to the developer and will help improve this tool."
                )
            except smtplib.SMTPAuthenticationError:
                st.error(
                    "Failed to send feedback: Email authentication error. "
                    "Make sure you're using an App Password for your Gmail account. "
                    "See https://support.google.com/mail/?p=BadCredentials"
                )
            except Exception as err:
                st.error(f"Failed to send feedback email: {err}")
        else:
            st.warning("Feedback field is empty.")
