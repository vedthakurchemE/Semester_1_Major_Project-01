import streamlit as st
import importlib
import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import contextlib

def run():
    st.title("👨‍💻 Programming for Problem Solving – Project Suite")
    st.markdown("📘 Semester 1 | Python + Streamlit | **10 Interactive Modules**")
    st.markdown("Select any tool from the sidebar to explore programming logic & applications.")
    st.markdown("---")

    # Technical name -> User-friendly label mapping
    modules_dict = {
        "bmi_calculator": "BMI Calculator (Body Mass Index)",
        "loan_emi_calculator": "Loan EMI Calculator",
        "leap_year_checker": "Leap Year Checker",
        "age_classifier": "Age Group Classifier",
        "prime_visualizer": "Prime Number Visualizer",
        "palindrome_checker": "Palindrome Checker",
        "fibonacci_plotter": "Fibonacci Sequence Plotter",
        "sorting_visualizer": "Sorting Algorithm Visualizer",
        "binary_search_visualizer": "Binary Search Visualizer",
        "temperature_converter": "Temperature Converter"
    }

    # Sidebar selection with user-friendly names
    selected_friendly = st.sidebar.selectbox(
        "Select a Lab Module to Run",
        list(modules_dict.values()),
        key="programming_selectbox"
    )
    selected_module = [k for k, v in modules_dict.items() if v == selected_friendly][0]

    # Initialize storage for inputs & results
    if "module_data" not in st.session_state:
        st.session_state.module_data = {}

    try:
        # Dynamically import the selected module from the modules folder
        module = importlib.import_module(f"programming_suite.modules.{selected_module}")

        # Capture printed output from the module
        output_buffer = io.StringIO()
        with contextlib.redirect_stdout(output_buffer):
            if hasattr(module, "run"):
                result_data = module.run()  # Expect module.run() to return dict with inputs/results
            else:
                st.error(f"Module '{selected_friendly}' does not have a run() function.")
                result_data = None

        printed_output = output_buffer.getvalue().strip()
        if printed_output:
            if not result_data:
                result_data = {}
            result_data["Output"] = printed_output

        if result_data:
            st.session_state.module_data[selected_module] = result_data

    except ModuleNotFoundError:
        st.error(f"Module '{selected_module}' not found in the modules folder.")
    except Exception as e:
        st.error(f"Error running module '{selected_friendly}': {e}")

    # --------------------------
    # Save results buttons
    # --------------------------
    if st.session_state.module_data:
        st.markdown("---")
        st.subheader("💾 Export Module Data")

        # CSV Export
        if st.button("Save All Results as CSV", key="save_csv_button"):
            all_data = []
            for mod, data in st.session_state.module_data.items():
                for key, value in data.items():
                    all_data.append({"Module": modules_dict.get(mod, mod), "Parameter": key, "Value": value})
            df = pd.DataFrame(all_data)
            csv_bytes = df.to_csv(index=False).encode()
            st.download_button("Download CSV", data=csv_bytes, file_name="module_results.csv", mime="text/csv")

        # PDF Export
        if st.button("Save All Results as PDF", key="save_pdf_button"):
            pdf_buffer = BytesIO()
            c = canvas.Canvas(pdf_buffer, pagesize=letter)
            width, height = letter
            y = height - 40
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y, "Module Results")
            c.setFont("Helvetica", 12)
            y -= 30
            for mod, data in st.session_state.module_data.items():
                c.drawString(50, y, f"Module: {modules_dict.get(mod, mod)}")
                y -= 20
                for key, value in data.items():
                    c.drawString(70, y, f"{key}: {value}")
                    y -= 15
                y -= 10
                if y < 50:
                    c.showPage()
                    y = height - 40
            c.save()
            pdf_buffer.seek(0)
            st.download_button("Download PDF", data=pdf_buffer, file_name="module_results.pdf", mime="application/pdf")
