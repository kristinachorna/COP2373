# Kristina Chorna
# Programming Exercise 13
# The objective of this code is to create a population table by obtaining data from a function that simulates growth
# using matplotlib. It then prompts the user to enter one of the cities and displays the population growth for it.

import sqlite3
import random
import matplotlib.pyplot as plt


# Create a function to create the database and table
def create_database():
    # Connect to SQLite database in case the database doesn't exist
    conn = sqlite3.connect('population_KC.db')
    cursor = conn.cursor()

    # Create a table called population
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')

    # Commit and close connection
    conn.commit()
    conn.close()


# Create function to insert city populations for 2023 and simulate population growth for 20 years
def insert_population_data():
    # Make a list of cities in Florida
    cities = ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'St. Petersburg',
              'Tallahassee', 'Fort Lauderdale', 'Cape Coral', 'Gainesville', 'Naples']

    # Initial population estimates for 2023
    initial_populations = {
        'Miami': 467963,
        'Orlando': 309154,
        'Tampa': 399700,
        'Jacksonville': 911507,
        'St. Petersburg': 265358,
        'Tallahassee': 194500,
        'Fort Lauderdale': 189000,
        'Cape Coral': 204000,
        'Gainesville': 133857,
        'Naples': 216000
    }

    # Connect to SQLite database
    conn = sqlite3.connect('population_KC.db')
    cursor = conn.cursor()

    # Insert initial data for 2023
    for city in cities:
        cursor.execute('''
            INSERT INTO population (city, year, population) 
            VALUES (?, ?, ?)
        ''', (city, 2023, initial_populations[city]))

    # Simulate population growth for the next 20 years
    for city in cities:
        current_population = initial_populations[city]
        for year in range(2024, 2044):
            # Simulate growth
            growth_rate = random.uniform(0.005, 0.02)
            new_population = int(current_population * (1 + growth_rate))
            cursor.execute('''
                INSERT INTO population (city, year, population) 
                VALUES (?, ?, ?)
            ''', (city, year, new_population))
            current_population = new_population

    # Commit and close connection
    conn.commit()
    conn.close()


# Create a function to visualize population growth for a specific city
def plot_population_growth():
    # Connect to SQLite database
    conn = sqlite3.connect('population_KC.db')
    cursor = conn.cursor()

    # Get the list of available cities in the database
    cursor.execute('SELECT DISTINCT city FROM population')
    cities = [row[0] for row in cursor.fetchall()]

    # Prompt the user to enter a city
    print("Choose a city to see its population growth (from the following list):")
    for city in cities:
        print(city)

    chosen_city = input("Enter the name of the city: ")

    # Fetch population data for the chosen city
    cursor.execute('''
        SELECT year, population FROM population 
        WHERE city = ? 
        ORDER BY year
    ''', (chosen_city,))
    data = cursor.fetchall()

    # Check if the city exists
    if not data:
        print(f"City '{chosen_city}' not found in the database.")
        return

    # Prepare data for plotting
    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    # Plot the population growth using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker='o', color='b', linestyle='-', markersize=5)
    plt.title(f"Population Growth of {chosen_city} (2023-2043)", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)
    plt.grid(True)
    plt.xticks(range(2023, 2044, 1), rotation=45)
    plt.tight_layout()
    plt.show()

    # Close the connection
    conn.close()


# Main function to run the complete program
def main():
    # Create database and table
    create_database()
    # Insert data and simulate growth
    insert_population_data()
    # Display population growth
    plot_population_growth()


# Run the main function
if __name__ == "__main__":
    main()
