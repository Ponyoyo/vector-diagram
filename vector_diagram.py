import matplotlib.pyplot as plt
import numpy as np

# Define the vectors
u_magnitude = 12
u_angle = 30  # degrees, North 30° East
v_magnitude = 8.0
v_angle = 195  # degrees, West 15° South (180 + 15)

# Convert angles to radians for calculations
u_angle_rad = np.deg2rad(u_angle)
v_angle_rad = np.deg2rad(v_angle)

# Calculate the components of the vectors
u_x = u_magnitude * np.cos(u_angle_rad)
u_y = u_magnitude * np.sin(u_angle_rad)
v_x = v_magnitude * np.cos(v_angle_rad)
v_y = v_magnitude * np.sin(v_angle_rad)

# Resultant vector components
r_x = u_x + v_x
r_y = u_y + v_y

# Plot the vectors
plt.figure(figsize=(8, 8))
plt.quiver(0, 0, u_x, u_y, angles='xy', scale_units='xy', scale=1, color='b', label=r'$\vec{u} = 12 \, \mathrm{m/s} \, [\mathrm{N} \, 30^\circ \, \mathrm{E}]$')
plt.quiver(u_x, u_y, v_x, v_y, angles='xy', scale_units='xy', scale=1, color='g', label=r'$\vec{v} = 8.0 \, \mathrm{m/s} \, [\mathrm{W} \, 15^\circ \, \mathrm{S}]$')
plt.quiver(0, 0, r_x, r_y, angles='xy', scale_units='xy', scale=1, color='r', label=r'$\vec{r} = \vec{u} + \vec{v}$')

# Set the limits of the plot
plt.xlim(-15, 15)
plt.ylim(-15, 15)

# Add grid
plt.grid(True)

# Add labels and title
plt.xlabel('X-axis (m/s)')
plt.ylabel('Y-axis (m/s)')
plt.title('Vector Addition Diagram')

# Add legend
plt.legend()

# Draw the frame of reference
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Annotate the vectors
plt.text(u_x/2, u_y/2, 'u', fontsize=12, ha='right')
plt.text(u_x + v_x/2, u_y + v_y/2, 'v', fontsize=12, ha='left')
plt.text(r_x/2, r_y/2, 'r', fontsize=12, ha='left')

# Show the plot
plt.show()