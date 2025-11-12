# weather_data_analyzer.py
# 🌤 Weather Data Analyzer (Streamlit Version with CSV Export)

import streamlit as st
import pandas as pd

def run():
    st.title("🌤 Weather Data Analyzer")

    # Session state for storing data
    if "weather_data" not in st.session_state or not isinstance(st.session_state.weather_data, dict):
        st.session_state.weather_data = {}

    # Input form for new location data
    with st.form("weather_form"):
        location = st.text_input("Enter location name")
        days = st.number_input("Number of days to record temperature", min_value=1, max_value=365, step=1)

        temps = []
        if location and days:
            st.markdown("### Enter temperatures")
            for i in range(int(days)):
                temp = st.number_input(f"Day {i + 1} temperature (°C)", format="%.2f", key=f"{location}_day_{i}")
                temps.append(temp)

        submitted = st.form_submit_button("Add Location Data")
        if submitted:
            if location and all(isinstance(t, (int, float)) for t in temps):
                st.session_state.weather_data[location] = temps
                st.success(f"✅ Data for '{location}' added successfully!")
            else:
                st.error("❌ Please enter a valid location and temperatures for all days.")

    # Display weather data
    if st.session_state.weather_data:
        st.subheader("📊 Recorded Weather Data")

        # Convert data to DataFrame
        max_days = max(len(v) for v in st.session_state.weather_data.values())
        df = pd.DataFrame.from_dict(st.session_state.weather_data, orient='index').T
        df.index = [f"Day {i + 1}" for i in range(max_days)]
        st.dataframe(df, use_container_width=True)

        # Weather analysis section
        st.subheader("📈 Weather Analysis")
        analysis_list = []
        for location, temps in st.session_state.weather_data.items():
            avg_temp = sum(temps) / len(temps)
            max_temp = max(temps)
            min_temp = min(temps)
            temp_range = max_temp - min_temp

            analysis_list.append({
                "Location": location,
                "Average Temp (°C)": round(avg_temp, 2),
                "Highest Temp (°C)": round(max_temp, 2),
                "Lowest Temp (°C)": round(min_temp, 2),
                "Range (°C)": round(temp_range, 2)
            })

            with st.expander(f"📍 {location}"):
                st.metric("Average Temp (°C)", f"{avg_temp:.2f}")
                st.metric("Highest Temp (°C)", f"{max_temp:.2f}")
                st.metric("Lowest Temp (°C)", f"{min_temp:.2f}")
                st.metric("Range (°C)", f"{temp_range:.2f}")

        # Create analysis DataFrame
        analysis_df = pd.DataFrame(analysis_list)

        st.subheader("📑 Weather Summary Table")
        st.table(analysis_df)

        # Download CSV buttons
        col1, col2 = st.columns(2)
        with col1:
            csv_data = df.to_csv().encode("utf-8")
            st.download_button(
                label="⬇ Download Raw Weather Data (CSV)",
                data=csv_data,
                file_name="weather_data.csv",
                mime="text/csv"
            )
        with col2:
            csv_analysis = analysis_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇ Download Weather Analysis (CSV)",
                data=csv_analysis,
                file_name="weather_analysis.csv",
                mime="text/csv"
            )
    else:
        st.info("📌 No weather data recorded yet. Please add a location above.")
