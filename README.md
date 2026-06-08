# Mental Health Analytics Dashboard

An interactive Streamlit dashboard for analyzing mental health survey data with 300K+ records.

## Features

- **Interactive Filtering**: Filter data by gender, country, occupation, mental health risk level, and age range
- **KPI Metrics**: View key metrics like total records, average stress, anxiety, and depression scores
- **Data Visualizations**:
  - Gender distribution pie chart
  - Age distribution histogram
  - Mental health risk bar chart
  - Stress trends over time
  - Anxiety vs Depression scatter plot
  - Stress score box plot
  - Correlation heatmap
  - Sleep hours trends
  - Occupation frequency analysis
  - Stress distribution by risk level

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dashboard_project1
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirnments.txt
```

## Running Locally

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

## Project Structure

```
dashboard_project1/
├── app.py                          # Main Streamlit app
├── charts.py                       # Chart components
├── filters.py                      # Filter components
├── requirnments.txt               # Python dependencies
├── data/
│   └── mental_health_survey_dataset_300k.csv
└── README.md
```

## Deployment

### Option 1: Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Click "New app" and select your repository
4. Deploy!

### Option 2: Heroku

1. Create a `Procfile` with: `web: streamlit run app.py`
2. Push to Heroku: `git push heroku main`

### Option 3: Other Platforms
- Railway
- Render
- AWS/Azure/Google Cloud

## Data

The dashboard uses the `mental_health_survey_dataset_300k.csv` file located in the `data/` folder.

## License

MIT License
