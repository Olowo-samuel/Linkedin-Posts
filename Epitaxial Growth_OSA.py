import numpy as np
import matplotlib.pyplot as plt

# Define the lattice mismatch (%) and corresponding strain values
lattice_mismatch = np.linspace(0, 2, 100)  # Lattice mismatch in percentage
strain = lattice_mismatch / (1 + lattice_mismatch)  # Simplified strain calculation

# Define a critical lattice mismatch where defects begin forming
critical_mismatch = 1.5  # Example value in %

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(lattice_mismatch, strain, label='Induced Strain', color='blue', linewidth=2)
plt.axvline(x=critical_mismatch, color='red', linestyle='--', label='Critical Mismatch')

# Adding annotations and labels
plt.title('Strain Induced by Lattice Mismatch in Epitaxial Growth', fontsize=16)
plt.xlabel('Lattice Mismatch (%)', fontsize=14)
plt.ylabel('Induced Strain', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.text(critical_mismatch + 0.1, max(strain)*0.5, 'Critical Mismatch\n(Defects Form)', 
         color='red', fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

# Display the graph
plt.show()
