import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.gridspec import GridSpec

# Constants for MOSFET parameters
K_N = 0.5  # Process transconductance for NMOS
K_P = 0.25  # Process transconductance for PMOS
VT_N = 1.0  # Threshold voltage for NMOS
VT_P = -1.0  # Threshold voltage for PMOS

def ids_nmos(vgs, vds):
    if vgs <= VT_N:
        return 0
    if vds <= (vgs - VT_N):  # Linear region
        return K_N * ((vgs - VT_N) * vds - vds**2/2)
    else:  # Saturation region
        return K_N * (vgs - VT_N)**2/2

def ids_pmos(vgs, vds):
    if vgs >= VT_P:
        return 0
    if vds >= (vgs - VT_P):  # Linear region
        return -K_P * ((vgs - VT_P) * vds - vds**2/2)
    else:  # Saturation region
        return -K_P * (vgs - VT_P)**2/2

# Create figure and subplots
fig = plt.figure(figsize=(15, 10))
gs = GridSpec(2, 2, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

# Setup plots
vds_range_nmos = np.linspace(0, 5, 100)
vds_range_pmos = np.linspace(-5, 0, 100)  # Negative range for PMOS
vgs_range_nmos = np.linspace(0, 5, 100)
vgs_range_pmos = np.linspace(-5, 0, 100)  # Negative range for PMOS

def init():
    ax1.set_title('NMOS: Ids vs Vds')
    ax1.set_xlabel('Vds (V)')
    ax1.set_ylabel('Ids (mA)')
    ax1.grid(True)
    
    ax2.set_title('NMOS: Ids vs Vgs')
    ax2.set_xlabel('Vgs (V)')
    ax2.set_ylabel('Ids (mA)')
    ax2.grid(True)
    
    ax3.set_title('PMOS: Ids vs Vds')
    ax3.set_xlabel('Vds (V)')
    ax3.set_ylabel('Ids (mA)')
    ax3.grid(True)
    
    ax4.set_title('PMOS: Ids vs Vgs')
    ax4.set_xlabel('Vgs (V)')
    ax4.set_ylabel('Ids (mA)')
    ax4.grid(True)
    
    return []

def animate(frame):
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    init()
    
    # Create smooth transitions by varying the number of curves
    num_curves = 3 + int(2 * np.sin(frame * 2 * np.pi / 150))  # Varies between 1 and 5 curves
    
    # NMOS Ids vs Vds curves
    vgs_values = np.linspace(1, 5, num_curves)
    for vgs in vgs_values:
        ids_values = [ids_nmos(vgs, vds) for vds in vds_range_nmos]
        ax1.plot(vds_range_nmos, ids_values, label=f'Vgs={vgs:.1f}V')
        # Mark saturation point
        vds_sat = vgs - VT_N
        if vds_sat > 0:
            ax1.plot(vds_sat, ids_nmos(vgs, vds_sat), 'ro')
    
    # NMOS Ids vs Vgs curves
    vds_values = np.linspace(1, 5, num_curves)
    for vds in vds_values:
        ids_values = [ids_nmos(vgs, vds) for vgs in vgs_range_nmos]
        ax2.plot(vgs_range_nmos, ids_values, label=f'Vds={vds:.1f}V')
    
    # PMOS Ids vs Vds curves (negative voltages and currents)
    vgs_values = np.linspace(-5, -1, num_curves)  # Negative Vgs values
    for vgs in vgs_values:
        ids_values = [ids_pmos(vgs, vds) for vds in vds_range_pmos]
        ax3.plot(vds_range_pmos, ids_values, label=f'Vgs={vgs:.1f}V')
        # Mark saturation point
        vds_sat = vgs - VT_P
        if vds_sat < 0:
            ax3.plot(vds_sat, ids_pmos(vgs, vds_sat), 'ro')
    
    # PMOS Ids vs Vgs curves (negative voltages and currents)
    vds_values = np.linspace(-5, -1, num_curves)
    for vds in vds_values:
        ids_values = [ids_pmos(vgs, vds) for vgs in vgs_range_pmos]
        ax4.plot(vgs_range_pmos, ids_values, label=f'Vds={vds:.1f}V')
    
    # Set appropriate axis limits
    ax1.set_xlim(0, 5)
    ax1.set_ylim(0, 5)
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 5)
    ax3.set_xlim(-5, 0)  # Negative x-axis for PMOS
    ax3.set_ylim(-5, 0)  # Negative y-axis for PMOS
    ax4.set_xlim(-5, 0)  # Negative x-axis for PMOS
    ax4.set_ylim(-5, 0)  # Negative y-axis for PMOS
    
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    
    plt.tight_layout()
    return []

# Create animation with more frames and slower transitions
anim = FuncAnimation(fig, animate, init_func=init, 
                    frames=300,  # 300 frames for ~10 seconds
                    interval=33,  # ~30 fps
                    blit=True)

# Save the animation as MP4
writer = FFMpegWriter(fps=30, bitrate=2000)
anim.save('samuel_mosfet.mp4', writer=writer)

plt.show()