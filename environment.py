import random

def determine_environmental_condition(prev_condition):
    conditions = ["none", "drought", "flood", "disease"]
    weights = {
        "none": [0.6, 0.2, 0.1, 0.1],
        "drought": [0.5, 0.3, 0.1, 0.1],
        "flood": [0.5, 0.1, 0.3, 0.1],
        "disease": [0.5, 0.1, 0.1, 0.3]
    }
    return random.choices(conditions, weights=weights[prev_condition])[0]

def apply_environmental_effects(animal, condition):
    try:
        if condition == "drought":
            animal['health_status'] -= random.uniform(0.05, 0.1)
        elif condition == "flood":
            animal['health_status'] -= random.uniform(0.1, 0.15)
        elif condition == "disease":
            animal['health_status'] -= random.uniform(0.15, 0.2)
        animal['health_status'] = max(0.5, min(animal['health_status'], 1.0))
    except Exception as e:
        print(f"Error applying environmental effects: {e}")
    return animal

def adjust_rates_based_on_environment(condition, average_birth_rate, average_mortality_rate):
    try:
        if condition == "drought":
            birth_rate = average_birth_rate * 0.5
            mortality_rate = average_mortality_rate * 1.5
            print("Drought occurred! Birth rate decreased and mortality rate increased.")
        elif condition == "flood":
            birth_rate = average_birth_rate * 0.7
            mortality_rate = average_mortality_rate * 1.3
            print("Flood occurred! Birth rate decreased and mortality rate increased.")
        elif condition == "disease":
            birth_rate = average_birth_rate * 0.4
            mortality_rate = average_mortality_rate * 1.8
            print("Disease outbreak occurred! Birth rate decreased and mortality rate increased.")
        else:
            birth_rate = average_birth_rate
            mortality_rate = average_mortality_rate
    except Exception as e:
        print(f"Error adjusting rates based on environment: {e}")
        birth_rate = average_birth_rate
        mortality_rate = average_mortality_rate
    return birth_rate, mortality_rate