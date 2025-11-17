import streamlit as st
import importlib
import traceback
import sys, os
import pandas as pd
import sqlite3
import io
import contextlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import matplotlib.pyplot as plt
import time
import inspect

# ---- Streamlit App Config ----
st.set_page_config(
    page_title="📘 Semester 1 – Engineering Project Suite",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- LOADING SCREEN ----
if "loaded" not in st.session_state:
    st.title("📁 Project is loading...")
    st.caption("Loading main project, please wait...")

    with st.spinner("🔄 Initializing Dashboard..."):
        progress_bar = st.progress(0)
        loading_text = st.empty()
        for percent_complete in range(100):
            progress_bar.progress(percent_complete + 1)
            loading_text.text(f"Loading... {percent_complete + 1}%")
            time.sleep(0.02)

    loading_text.empty()
    st.success("✅ Project Loaded!")
    st.session_state["loaded"] = True
    st.rerun()

# ---- DESCRIPTION SCREEN ----
if "description_done" not in st.session_state:
    st.session_state["description_done"] = False

if not st.session_state["description_done"]:
    st.markdown("""
    # 🧑‍🏭 Semester 1 Major Project Suite

    Welcome to the **Smart Manufacturing Analytics Platform** – an innovative dashboard engineered from core Semester 1 subjects, tailored for both engineering students and professionals!
    ### 🌟 Features
    - 📊 **Graph Generation:** Instantly create and explore engineering graphs from core subjects, using cutting-edge Python plotting libraries.
    - 🧮 **Data Analysis:** Analyze process, lab, and field data for research, assignments, or real-world insights.
    - 🛠️ **Toolkits for Accuracy:** Get robust calculators and simulators trusted for precise measurements and predictions.
    - 👨‍🎓 **Student-Friendly:** Designed for rapid learning, hands-on practice, and understanding complex topics visually.
    - 👩‍💼 **Professional Grade:** Utility tools and analytics models ready for faculty, research, or industrial use.
    ---
    Crafted with modern Python technologies, this suite bridges classroom learning and industrial practice – bringing hands-on analytics, visualization, and automation to every major engineering discipline.
    """)
    if st.button("Next"):
        st.session_state["description_done"] = True
        st.video("coverpage.mp4")
        st.rerun()
    st.stop()

# ---- Main Title and Caption ----
st.title("📘 Semester 1 – Engineering Project Suite")
st.caption("🔁 Centralized Dashboard for All 12 Labs & Project Suites")

# ---- Project root path config ----
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# ---- Database Setup ----
DB_FILE = os.path.join(PROJECT_ROOT, "project_results.db")
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project TEXT,
            parameter TEXT,
            value TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_results_to_db(project, results: dict, input_data: dict = None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    for param, value in results.items():
        c.execute("INSERT INTO results (project, parameter, value) VALUES (?, ?, ?)",
                  (project, str(param), str(value)))
    if input_data:
        for param, value in input_data.items():
            c.execute("INSERT INTO results (project, parameter, value) VALUES (?, ?, ?)",
                      (project, str(param), str(value)))
    conn.commit()
    conn.close()

def load_results_from_db(project=None):
    conn = sqlite3.connect(DB_FILE)
    if project:
        df = pd.read_sql_query("SELECT parameter, value FROM results WHERE project = ?", conn, params=(project,))
    else:
        df = pd.read_sql_query("SELECT project, parameter, value FROM results", conn)
    conn.close()
    return df

init_db()

# ---- Project suite mapping ----
PROJECT_SUITES = {
    "🧱 Basic Civil Lab": "basic_civil_lab.modules.civil_lab_main",
    "🌍 Basic Civil Tools": "basic_civil_suite.modules.civil_tools_main",
    "🏗️ Electronics Tools": "basic_electronics.modules.basic_electronics_main",
    "🧮 Calculus Tools": "CalculusBridgeAI.modules.calculus_main",
    "🤖 Design Thinking Lab": "design_thinking_lab.modules.design_thinking_main",
    "📡 Electronics Lab": "electronics_workshop.modules.electronics_main",
    "📊 Engineering Graphics Lab": "eng_graphics_lab.modules.eng_graphics_lab_main",
    "📐 Engineering Graphics": "EngGraphViz_Suite.modules.eng_graphics_main",
    "⚙️ Physics AI Tools": "optics_ai_suite.modules.physics_ai_main",
    "⚛️ Physics AI Lab": "optics_modern_lab.modules.physics_lab_main",
    "🖥️ Programming Lab": "programming_lab.modules.problem_solving_main",
    "🌡️ Programming Tools": "programming_suite.modules.programming_main",
}

# ---- Sidebar navigation ----
st.sidebar.title("📂 Project Navigation")
choice = st.sidebar.selectbox("Select a Project Suite", list(PROJECT_SUITES.keys()))
run_all = st.sidebar.button("▶️ Run All Project Suites")

if st.sidebar.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()
st.sidebar.markdown("---")

# ---- File Upload/Download ----
st.sidebar.header("📤 Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV, Excel, or Image", type=["csv", "xlsx", "png", "jpg", "jpeg"])

uploaded_data = None
if uploaded_file:
    file_type = uploaded_file.type
    try:
        if file_type == "text/csv":
            uploaded_data = pd.read_csv(uploaded_file)
            st.sidebar.write(uploaded_data.head())
        elif "excel" in file_type or ".xlsx" in uploaded_file.name:
            uploaded_data = pd.read_excel(uploaded_file)
            st.sidebar.write(uploaded_data.head())
        elif "image" in file_type:
            uploaded_data = Image.open(uploaded_file)
            st.sidebar.image(uploaded_data)
    except Exception as e:
        st.sidebar.error(f"Error loading file: {e}")

# ---- Safe runner function ----
def run_project(display_name, module_path):
    with st.expander(f"📌 {display_name}", expanded=True):
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, "run") and callable(module.run):
                st.markdown(f"### ✅ Running {display_name}")
                with st.spinner(f"🔄 Loading {display_name}..."):
                    output_buffer = io.StringIO()
                    with contextlib.redirect_stdout(output_buffer):
                        run_params = inspect.signature(module.run).parameters
                        if "uploaded_data" in run_params:
                            result_data = module.run(uploaded_data=uploaded_data)
                        else:
                            result_data = module.run()
                    printed_output = output_buffer.getvalue().strip()
                    input_data, results, graphs = {}, {}, []

                    if isinstance(result_data, tuple):
                        if len(result_data) == 2:
                            input_data, results = result_data
                        elif len(result_data) == 3:
                            input_data, results, graphs = result_data
                    elif isinstance(result_data, dict):
                        results = result_data

                    if printed_output:
                        results["Output"] = printed_output

                    if results:
                        if "all_results" not in st.session_state:
                            st.session_state["all_results"] = {}
                        st.session_state["all_results"][display_name] = results
                        save_results_to_db(display_name, results, input_data=input_data)
                        for key, value in results.items():
                            st.markdown(f"- **{key}:** {value}")

                    if graphs:
                        for g in graphs:
                            if isinstance(g, plt.Figure):
                                st.pyplot(g)
                            elif isinstance(g, Image.Image):
                                st.image(g)

                    # ---- DOWNLOAD BUTTONS ----
                    st.markdown("---")
                    if results:
                        df = pd.DataFrame(list(results.items()), columns=["Parameter", "Value"])
                        csv_bytes = df.to_csv(index=False).encode()
                        st.download_button("Download Results as CSV", data=csv_bytes, file_name=f"{display_name}_results.csv", mime="text/csv")

                        # PDF Download
                        pdf_buffer = io.BytesIO()
                        c = canvas.Canvas(pdf_buffer, pagesize=letter)
                        width, height = letter
                        y = height - 40
                        c.setFont("Helvetica-Bold", 14)
                        c.drawString(50, y, f"Results for {display_name}")
                        c.setFont("Helvetica", 12)
                        y -= 30
                        for key, value in results.items():
                            c.drawString(50, y, f"{key}: {value}")
                            y -= 15
                            if y < 50:
                                c.showPage()
                                y = height - 40
                        c.save()
                        pdf_buffer.seek(0)
                        st.download_button("Download Results as PDF", data=pdf_buffer, file_name=f"{display_name}_results.pdf", mime="application/pdf")
            else:
                st.warning(f"⚠ The project `{display_name}` has no `run()` function.")
        except ModuleNotFoundError:
            st.error(f"❌ Could not find **{module_path}**.")
        except Exception as e:
            st.error(f"❌ Unexpected error in `{display_name}`")
            with st.expander("Show Error Details"):
                st.code(traceback.format_exc(), language="python")
        st.markdown("---")

# ---- Execute selected / all ----
if run_all:
    st.subheader("▶️ Running All Project Suites")
    for display_name, module_path in PROJECT_SUITES.items():
        run_project(display_name, module_path)
else:
    run_project(choice, PROJECT_SUITES[choice])

# ---- Database Viewer ----
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Database Viewer")
if st.sidebar.checkbox("Show Saved Database"):
    df_db = load_results_from_db()
    st.sidebar.dataframe(df_db)

import datetime

st.markdown("---")
st.subheader("💬 Feedback for this Tool")
feedback = st.text_area("Share your thoughts or suggestions:", key=f"feedback_{st.session_state.get('tool_name', '')}")
if st.button("Submit Feedback", key=f"submit_{st.session_state.get('tool_name', '')}"):
    if "feedback_tool_list" not in st.session_state:
        st.session_state["feedback_tool_list"] = []
    st.session_state["feedback_tool_list"].append({
        "tool": st.session_state.get('tool_name', 'Unknown Tool'),
        "text": feedback,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    st.success("Thank you for your valuable feedback!")

# ---- Footer ----
st.markdown(
    "<hr><p style='text-align:center;font-size:12px;color:gray'>"
    "Developed by Ved Thakur • Semester 1 • IPS Academy Indore</p>",
    unsafe_allow_html=True,
)
