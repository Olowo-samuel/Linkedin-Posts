import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Draw transistor schematic
# Base rectangle representing the substrate
substrate = patches.Rectangle((0, 0), 10, 2, edgecolor='black', facecolor='lightgray', label='Substrate')
ax.add_patch(substrate)

# Channel region
channel = patches.Rectangle((3, 2), 4, 1, edgecolor='black', facecolor='skyblue', label='Channel')
ax.add_patch(channel)

# Stress liner (tensile and compressive regions)
tensile_region = patches.Rectangle((0, 3), 3, 1, edgecolor='black', facecolor='lightcoral', label='Tensile Stress')
compressive_region = patches.Rectangle((7, 3), 3, 1, edgecolor='black', facecolor='lightgreen', label='Compressive Stress')
ax.add_patch(tensile_region)
ax.add_patch(compressive_region)

# Add annotations
ax.text(1.5, 4, 'Tensile Stress Liner', fontsize=12, color='darkred', ha='center')
ax.text(8.5, 4, 'Compressive Stress Liner', fontsize=12, color='darkgreen', ha='center')
ax.text(5, 3.5, 'Channel Region', fontsize=12, color='blue', ha='center')

# Add arrows to indicate strain direction
ax.arrow(1.5, 3, 0, -0.5, head_width=0.2, head_length=0.2, fc='darkred', ec='darkred')
ax.arrow(8.5, 3, 0, -0.5, head_width=0.2, head_length=0.2, fc='darkgreen', ec='darkgreen')

# Graph settings
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 5)
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')

# Add legend
ax.legend(loc='upper left', fontsize=12)

# Title
plt.title('Stress Liners and Strain Impact on Transistor Channel', fontsize=16, pad=20)

# Add LinkedIn handle with professional styling
# Create a light gray box for the handle
handle_box = patches.Rectangle((8, -0.8), 3, 0.4, 
                             facecolor='lightgray', 
                             alpha=0.3, 
                             edgecolor='none',
                             transform=ax.transData)
ax.add_patch(handle_box)

# To add my LinkedIn handle text
ax.text(9.5, -0.6, 'Samuel Olowosile',
        fontsize=10,
        color='navy',
        ha='center',
        va='center',
        style='italic',
        transform=ax.transData)

# Adjust layout to make room for the handle
plt.subplots_adjust(bottom=0.15)

# Show the plot
plt.show()
