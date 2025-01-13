# MOSFET Characteristics Animation

This project visualizes the electrical characteristics of NMOS and PMOS transistors through animated plots. The animation dynamically shows how the drain current (Ids) varies with the drain-source voltage (Vds) and gate-source voltage (Vgs) in both triode and saturation regions.

## Features
- Animated plots for:
  - **NMOS Ids vs Vds**
  - **NMOS Ids vs Vgs**
  - **PMOS Ids vs Vds**
  - **PMOS Ids vs Vgs**
- Smooth transitions between curves for multiple Vgs and Vds values.
- Highlights saturation points on the curves.
- Customizable parameters for MOSFET behavior.

## Requirements
- Python 3.7+
- Required libraries:
  - `numpy`
  - `matplotlib`

Install the required libraries using pip:
```bash
pip install numpy matplotlib
```

## How It Works
### Constants:
- `K_N`, `K_P`: Process transconductance parameters for NMOS and PMOS.
- `VT_N`, `VT_P`: Threshold voltages for NMOS and PMOS.

### Functions:
1. `ids_nmos(vgs, vds)`: Computes NMOS drain current based on Vgs and Vds.
2. `ids_pmos(vgs, vds)`: Computes PMOS drain current based on Vgs and Vds.

### Animation:
- Uses `matplotlib.animation.FuncAnimation` to update plots dynamically.
- Displays curves for different Vgs and Vds values, marking saturation points.
- Saves the final animation as an MP4 file.

## Output
- The animation is saved as `samuel_mosfet.mp4`.

## Usage
1. Clone the repository or copy the code.
2. Run the Python script:
```bash
Samuel_MOSFET_Animated_Plot.py
```

## Output
- The animation is saved as `samuel_mosfet.mp4`.

## Customization
- Modify the constants (`K_N`, `K_P`, `VT_N`, `VT_P`) to simulate different MOSFETs.
- Adjust `vds_range_nmos`, `vgs_range_nmos`, `vds_range_pmos`, and `vgs_range_pmos` for different voltage ranges.
- Change animation settings (`frames`, `interval`, `fps`) for a smoother or faster animation.

## Author
Samuel Olowosile

