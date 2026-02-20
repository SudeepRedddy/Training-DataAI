import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Setup directories for output
os.makedirs('plots', exist_ok=True)
os.makedirs('output', exist_ok=True)

DATASET_FILE = 'netflix_titles.csv'

def section_header(title):
    print(f"\n{'='*10} {title} {'='*10}")

def run_numpy_tasks():
    section_header("NumPy Tasks (1-6)")

    # 1. Create a NumPy array with 10 elements
    arr = np.arange(10)
    print(f"1. Array: {arr}")
    print(f"   Shape: {arr.shape}, Size: {arr.size}, Data Type: {arr.dtype}")

    # 2. Arithmetic operations
    print(f"2. Addition (+5): {arr + 5}")
    print(f"   Subtraction (-2): {arr - 2}")
    print(f"   Multiplication (*2): {arr * 2}")
    # Avoid division by zero for the first element
    with np.errstate(divide='ignore', invalid='ignore'):
        print(f"   Division (/2): {arr / 2}")

    # 3. 2D Array and Indexing
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"3. 2D Array:\n{arr_2d}")
    print(f"   Element at [1, 2] (Row 1, Col 2): {arr_2d[1, 2]}")

    # 4. Slicing
    print(f"4. Sliced (First 2 rows, first 2 cols):\n{arr_2d[:2, :2]}")

    # 5. Reshape
    reshaped = arr.reshape(2, 5)
    print(f"5. Reshaped (2x5):\n{reshaped}")

    # 6. Broadcasting
    # Adding a 1D array to a 2D array
    broadcast_add = arr_2d + np.array([10, 20, 30])
    print(f"6. Broadcasting (Adding [10, 20, 30] to rows):\n{broadcast_add}")

def run_pandas_tasks():
    section_header("Pandas Tasks (7-22)")

    # 7. Load Dataset
    if not os.path.exists(DATASET_FILE):
        print(f"Error: {DATASET_FILE} not found. Please download it from Kaggle.")
        return None
    
    df = pd.read_csv(DATASET_FILE)
    print("7. Dataset Loaded Successfully.")

    # 8. Display rows
    print(f"8. First 5 rows:\n{df.head(5)}")
    print(f"   Last 5 rows:\n{df.tail(5)}")

    # 9. Info and Columns
    print("9. Dataset Info:")
    df.info()
    print(f"   Columns: {df.columns.tolist()}")

    # 10. Handle Missing Values
    print(f"10. Missing values before:\n{df.isnull().sum()}")
    # Strategy: Fill 'country' with 'Unknown', drop rows with missing 'date_added' or 'rating'
    df['country'] = df['country'].fillna('Unknown')
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df.dropna(subset=['date_added', 'rating'], inplace=True)
    print("    Missing values handled.")

    # 11. Select specific columns
    subset = df[['title', 'type', 'release_year']]
    print(f"11. Selected columns sample:\n{subset.head(3)}")

    # 12. Filter rows (Movies released after 2020)
    recent_movies = df[(df['type'] == 'Movie') & (df['release_year'] > 2020)]
    print(f"12. Movies released after 2020: {len(recent_movies)}")

    # 13. Add new column (Content Age)
    current_year = 2024
    df['content_age'] = current_year - df['release_year']
    print(f"13. Added 'content_age' column. Max age: {df['content_age'].max()}")

    # 14. Remove a column (Removing 'show_id' as it's just an ID)
    df.drop(columns=['show_id'], inplace=True)
    print("14. Removed 'show_id' column.")

    # 15. Rename a column
    df.rename(columns={'listed_in': 'categories'}, inplace=True)
    print("15. Renamed 'listed_in' to 'categories'.")

    # 16. Sort data
    df.sort_values(by='release_year', ascending=False, inplace=True)
    print("16. Sorted by release_year (descending).")

    # 17. Indexing and Slicing (iloc)
    print(f"17. Extracting rows 5 to 10 using iloc:\n{df.iloc[5:10][['title', 'release_year']]}")

    # 18. GroupBy Analysis
    type_counts = df.groupby('type')['title'].count()
    print(f"18. GroupBy Type:\n{type_counts}")

    # 19. Pivot Table
    # Count of content by Type and Rating
    pivot = df.pivot_table(index='rating', columns='type', values='title', aggfunc='count', fill_value=0)
    print(f"19. Pivot Table (Rating vs Type):\n{pivot.head()}")

    # 20. Shift()
    # Calculate year difference between consecutive rows (since it's sorted by year)
    df['year_diff'] = df['release_year'].diff()
    print(f"20. Shift/Diff example (Year difference between rows):\n{df[['release_year', 'year_diff']].head()}")

    # 21. Rank()
    # Rank movies by duration (Need to parse duration first)
    # Extract numeric part of duration for Movies
    movies_df = df[df['type'] == 'Movie'].copy()
    movies_df['duration_min'] = movies_df['duration'].str.replace(' min', '').astype(float)
    movies_df['duration_rank'] = movies_df['duration_min'].rank(ascending=False)
    print(f"21. Rank example (Top 3 longest movies):\n{movies_df.sort_values('duration_rank').head(3)[['title', 'duration']]}")

    # 22. Rolling()
    # Calculate moving average of content count per year
    year_counts = df['release_year'].value_counts().sort_index()
    rolling_avg = year_counts.rolling(window=5).mean()
    print(f"22. Rolling Mean (5-year window) of content production:\n{rolling_avg.tail()}")

    return df

def run_visualization_tasks(df):
    if df is None: return
    section_header("Matplotlib Tasks (23-28)")

    # 23. Bar Chart (Content Type Distribution)
    plt.figure(figsize=(6, 4))
    type_counts = df['type'].value_counts()
    plt.bar(type_counts.index, type_counts.values, color=['red', 'black'])
    plt.title('Distribution of Movies vs TV Shows')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.savefig('plots/23_bar_chart.png')
    print("23. Saved Bar Chart to plots/23_bar_chart.png")
    plt.close()

    # 24. Pie Chart (Top 5 Ratings)
    plt.figure(figsize=(8, 8))
    rating_counts = df['rating'].value_counts().head(5)
    plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Top 5 Content Ratings')
    plt.savefig('plots/24_pie_chart.png')
    print("24. Saved Pie Chart to plots/24_pie_chart.png")
    plt.close()

    # 25. Histogram (Release Year Distribution)
    plt.figure(figsize=(10, 6))
    plt.hist(df['release_year'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Release Years')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.savefig('plots/25_histogram.png')
    print("25. Saved Histogram to plots/25_histogram.png")
    plt.close()

    # 26. Subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Subplot 1: Top 10 Countries
    top_countries = df['country'].value_counts().head(10)
    ax1.barh(top_countries.index, top_countries.values, color='green')
    ax1.set_title('Top 10 Countries by Content')
    ax1.invert_yaxis() # Highest on top

    # Subplot 2: Content added over years (extracted from date_added)
    df['date_added'] = pd.to_datetime(df['date_added'])
    df['year_added'] = df['date_added'].dt.year
    added_counts = df['year_added'].value_counts().sort_index()
    ax2.plot(added_counts.index, added_counts.values, marker='o', linestyle='-')
    ax2.set_title('Content Added Over Time')
    ax2.set_xlabel('Year Added')
    
    # 27. Add titles/labels (Done above)
    plt.tight_layout()
    
    # 28. Save plots
    plt.savefig('plots/26_subplots.png')
    print("26-28. Saved Subplots to plots/26_subplots.png")
    plt.close()

def run_analysis_tasks(df):
    if df is None: return
    section_header("Analysis & Reporting (29-38)")

    report_lines = []
    report_lines.append("# Netflix Dataset Analysis Report\n")

    # 29. Count Movies and TV Shows
    type_counts = df['type'].value_counts()
    res_29 = f"Movies: {type_counts.get('Movie', 0)}, TV Shows: {type_counts.get('TV Show', 0)}"
    print(f"29. {res_29}")
    report_lines.append(f"## Content Distribution\n{res_29}\n")

    # 30. Most common release year
    common_year = df['release_year'].mode()[0]
    res_30 = f"Most common release year: {common_year}"
    print(f"30. {res_30}")
    report_lines.append(f"## Release Trends\n{res_30}\n")

    # 31. Analyze trends (Content added per year)
    trend = df.groupby('year_added').size()
    peak_year = trend.idxmax()
    res_31 = f"Peak year for adding content to Netflix was {int(peak_year)} with {trend.max()} titles."
    print(f"31. {res_31}")
    report_lines.append(f"## Growth Trends\n{res_31}\n")

    # 32. Identify patterns (Duration)
    # Average duration of movies
    movies = df[df['type'] == 'Movie'].copy()
    movies['duration_min'] = movies['duration'].str.replace(' min', '').astype(float)
    avg_duration = movies['duration_min'].mean()
    res_32 = f"Average Movie Duration: {avg_duration:.2f} minutes."
    print(f"32. {res_32}")
    report_lines.append(f"## Content Patterns\n{res_32}\n")

    # 33. Conclusions
    conclusions = """
    ### Conclusions
    1. Netflix has significantly more Movies than TV Shows.
    2. The platform saw exponential growth in content addition leading up to the peak year.
    3. The United States is the leading producer of content in this dataset.
    """
    print("33. Conclusions generated.")
    report_lines.append(conclusions)

    # 34. NumPy and Pandas together
    # Calculate Z-score of movie durations to find outliers
    durations = movies['duration_min'].dropna().values
    mean_d = np.mean(durations)
    std_d = np.std(durations)
    z_scores = (durations - mean_d) / std_d
    outliers = np.sum(np.abs(z_scores) > 3)
    res_34 = f"Found {outliers} movies with duration outliers (Z-score > 3)."
    print(f"34. {res_34}")
    report_lines.append(f"\n## Statistical Analysis\n{res_34}\n")

    # 35. Statistical Analysis
    desc_stats = movies['duration_min'].describe().to_string()
    print(f"35. Statistical Summary of Movie Durations:\n{desc_stats}")
    report_lines.append(f"### Duration Statistics\n```\n{desc_stats}\n```\n")

    # 36. Multiple Visualizations (Already done in run_visualization_tasks, adding reference)
    report_lines.append("## Visualizations\nRefer to the `plots/` directory for generated charts.\n")

    # 37. Save analysis results to CSV
    # Saving the cleaned and processed dataset
    output_csv = 'output/processed_netflix_data.csv'
    df.to_csv(output_csv, index=False)
    print(f"37. Saved processed data to {output_csv}")

    # 38. Create complete analysis report
    report_file = 'output/analysis_report.md'
    with open(report_file, 'w') as f:
        f.writelines(report_lines)
    print(f"38. Complete analysis report saved to {report_file}")

if __name__ == "__main__":
    run_numpy_tasks()
    df_processed = run_pandas_tasks()
    if df_processed is not None:
        run_visualization_tasks(df_processed)
        run_analysis_tasks(df_processed)
        print("\n=== Project Completed Successfully ===")