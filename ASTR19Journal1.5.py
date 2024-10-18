import numpy as np

def generate_sin_table(start: float, end: float, thous_entries: int):
    # Create array of values from start to end with thous_entries
    x_values = np.linspace(start, end, thous_entries)
    
    # sinvalues for every x value
    sin_values = np.sin(x_values)
    
    print(f"{'x':>10} {'sin(x)':>10}")
    print('-' * 22)
    
    # Print the x and sin(x) values
    for x, sin_x in zip(x_values, sin_values):
        print(f"{x:10.4f} {sin_x:10.4f}")
        
def main():
    # call function to generate the sin table
    generate_sin_table(0, 2, 1000)
if __name__ == "__main__":
    main()
