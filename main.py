import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the data from the CSV file
data = pd.read_csv('Cleaned_data.csv')

@app.route('/')
def index():
    # Get unique locations and sort them
    locations = sorted(data['location'].unique())
    # Render the index.html template with the locations data
    return render_template('index.html', locations = locations)

if __name__ == "__main__":
    # Run the Flask app on port 3000 with debug mode enabled
     app.run(debug=True, port=5001)
