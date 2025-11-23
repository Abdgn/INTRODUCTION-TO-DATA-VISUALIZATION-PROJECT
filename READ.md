First of all, I prepared my data using the KAGGLE website. The dataset contains earthquakes that occurred in Turkiye and its surrounding areas. This dataset only includes earthquakes with a magnitude greater than 3.5 that occurred between 1915 and February 2024. The columns are Date, time, latitude, longitude, depth, MD/ML/Mw/Ms/Mb magnitudes, location, etc.

1️⃣ Earthquake Numbers by Year (Time Series – Advanced)

Question: How did the number of earthquakes change between 1915 and 2024?
Variables: Date (year)
Interactivity: Slider (year filtering), zoom, hover
Purpose: To show long-term trends in earthquake frequency

2️⃣ Distribution by Magnitude Type (Violin Plot – Advanced)

Question: In which range do the magnitudes MD, ML, and Mw occur?
Variables: MD, ML, Mw
Interactivity: Dropdown (magnitude type selection), hover
Purpose: To compare the distribution of different magnitude measurements

3️⃣ Depth Histogram by Magnitude Range

Question: Do earthquakes occur shallower or deeper at certain magnitudes?
Variables: xM (maximum magnitude), depth
Interactivity: Slider (magnitude range), hover
Purpose: To see the magnitude-depth relationship

🛠 Technologies Used
Python
Streamlit
Plotly Express
Pandas
Numpy

👤 Member Responsibilities
This section was developed entirely by Member 1:
- Data preprocessing
- 3 chart designs
- Slider & dropdown interactivity
- Time series and distribution analysis

▶ Run (terminal)
streamlit run app1.py



