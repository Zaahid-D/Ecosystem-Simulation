import pandas as pd
import matplotlib.pyplot as plt
from population import initialize_population, update_population
from environment import determine_environmental_condition, apply_environmental_effects, adjust_rates_based_on_environment

def simulate_savanna_ecosystem(initial_population_size, average_birth_rate, average_mortality_rate, average_migration_rate, time_steps):
    population = initialize_population(initial_population_size)
    environmental_condition = "none"
    log = []

    for step in range(time_steps):
        try:
            environmental_condition = determine_environmental_condition(environmental_condition)
            adjusted_birth_rate, adjusted_mortality_rate = adjust_rates_based_on_environment(environmental_condition, average_birth_rate, average_mortality_rate)

            for i in range(len(population)):
                population[i] = apply_environmental_effects(population[i], environmental_condition)

            population = update_population(population, adjusted_birth_rate, adjusted_mortality_rate, average_migration_rate)

            log_entry = f"Population size after year {step + 1}: {len(population)}"
            log.append(log_entry)
            if environmental_condition != "none":
                log.append(f"{environmental_condition.capitalize()} occurred! Birth rate decreased and mortality rate increased.")
            
            print(log_entry)
        except Exception as e:
            print(f"Error occurred in step {step}: {e}")

    return population, log
    
def save_simulation_results(population, log, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Population Statistics:\n")
            total_population = len(population)
            f.write(f"Total Population: {total_population}\n\n")
            f.write("="*75 + "\n\n")

            # Write log: Population after each year/time step
            f.write("Simulation Log:\n")
            for entry in log:
                f.write(entry + "\n")
            f.write("\n" + "="*75 + "\n\n")
            
            # Convert population data to a DataFrame
            data = []
            for animal in population:
                data.append([animal['species'], animal['age'], round(animal['health_status'], 2), ""])
                for offspring in animal['offspring']:
                    data.append([f"↳ {offspring['species']}", offspring['age'], round(offspring['health_status'], 2), "Yes"])

            df = pd.DataFrame(data, columns=["Species", "Age", "Health Status", "Offspring"])

            # Generate statistics
            f.write("Population Count per Species:\n")
            species_counts = df[df['Offspring'] == '']['Species'].value_counts()
            f.write(species_counts.to_string() + '\n\n')
            f.write("="*75 + "\n\n")

            f.write("Average Age of Population:\n")
            f.write(f"Overall: {df[df['Offspring'] == '']['Age'].mean().round(2)}\n\n")
            f.write("="*75 + "\n\n")

            f.write("Average Age per Species:\n")
            average_age_per_species = df[df['Offspring'] == ''].groupby('Species')['Age'].mean().round(2)
            f.write(average_age_per_species.to_string() + '\n\n')
            f.write("="*75 + "\n\n")

            f.write("Average Health Status:\n")
            f.write(f"Overall: {df[df['Offspring'] == '']['Health Status'].mean().round(2)}\n\n")
            f.write("="*75 + "\n\n")

            f.write("Average Health Status per Species:\n")
            average_health_status_per_species = df[df['Offspring'] == ''].groupby('Species')['Health Status'].mean().round(2)
            f.write(average_health_status_per_species.to_string() + '\n\n')
            f.write("="*75 + "\n\n")

            f.write("Individual Animal Data:\n")
            f.write(f"{'Species':<20} {'Age':<5} {'Health Status':<15} {'Offspring':<10}\n")
            f.write("="*75 + "\n")
            for index, row in df.iterrows():
                f.write(f"{row['Species']:<20} {row['Age']:<5} {row['Health Status']:<15} {row['Offspring']:<10}\n")

        # Plot graphs

        # Define colors for the African savanna theme
        bar_colors = ['#87CEEB', '#ADD8E6', '#B0E0E6', '#AFEEEE', '#00BFFF']  
        pie_colors = ['#FFE4B5', '#FFDAB9', '#FFEFD5', '#F0E68C', '#FAFAD2']  

        # Population growth over time
        plt.figure()
        population_sizes = [int(entry.split()[-1]) for entry in log if entry.startswith("Population size after year")]
        plt.plot(range(1, len(population_sizes) + 1), population_sizes, marker='o')
        plt.title("Population Growth Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Population Size")
        plt.show()  
        
        # Population count per species
        plt.figure()
        species_counts.plot(kind='bar', color=bar_colors)
        plt.title("Population Count per Species")
        plt.xlabel("Species")
        plt.ylabel("Count")
        plt.show()  
        
        # Population proportion per species (Pie Chart)
        plt.figure()
        species_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=pie_colors)
        plt.title("Population Proportion per Species")
        plt.ylabel("")  
        plt.xlabel("")
        plt.show()  

    except Exception as e:
        print(f"Error saving simulation results: {e}")
