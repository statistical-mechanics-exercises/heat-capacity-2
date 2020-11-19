import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

def potential(x) :
  energy = 0 
  forces = np.zeros([7,2])
  # Your code to calculate the potential goes here
  
  return energy, forces
  
def kinetic(v) :
  ke = 0
  # Your code to calculate the kinetic energy from the velocities goes here
  
  return ke

def gen_traj( pos, vel, nsteps, timestep, stride, temperature, friction ) :
  # This calculates the initial values for the forces
  eng, forces = potential(pos)
  # This is the variable that you should use to keep track of the quantity of energy that is exchanged with 
  # the reservoir of the thermostat.
  therm = 0
  
  times = np.zeros(int(nsteps/stride))
  k_energy = np.zeros(int(nsteps/stride))
  p_energy = np.zeros(int(nsteps/stride))
  t_energy = np.zeros(int(nsteps/stride))
  conserved_quantity = np.zeros(int(nsteps/stride))
  for step in range(nsteps) :
    # Apply the thermostat for a half timestep 
    for i in range(7) : 
      vel[i][0] = 
      vel[i][1] = 
  
    # Update the velocities a half timestep
    # fill in the blanks in the code here
    for i in range(7) : 
      vel[i][0] = 
      vel[i][1] = 
    
    # Now update the positions using the new velocities
    # You need to add code here
  
  
    # Recalculate the forces at the new position
    # You need to add code here
    eng, forces = 
  
    # Update the velocities another half timestep
    # You need to add code here


    # And finish by applying the thermostat for the second half timestep 
    for i in range(7) : 
      vel[i][0] = 
      vel[i][1] = 

    # This is where we want to store the energies and times
    if step%stride==0 : 
      times[int(step/stride)] = step
      # Write code to ensure the proper values are saved here
      p_energy[int(step/stride)] = 
      k_energy[int(step/stride)] = 
      t_energy[int(step/stride)] =
      conserved_quantity[int(step/stride)] =
      
  return times, p_energy, k_energy, t_energy, conserved_quantity
  
# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This command reads in the velocities that are contained in the file called velocities.txt
vel = np.loadtxt( "velocities.txt" )
  
# This command runs the molecular dynamics and generates a trajectory 
temperature = 1.0   # This variable must be defined to pass the tests
tt, potential_e, kinetic_e, total, conserved = gen_traj( pos, vel, 2400, 0.005, 1, temperature, 2.0 )

# This is the part to compute the block averages for the error estimation
bsize, averages, errors = [200,400,600,800,1000,1200], np.zeros(6), np.zeros(6)
for blocksie in bsize :
  # Your code to calculate the block averages goes here
   
   
# This will plot the kinetic energy as a function of time
plt.errorbar( bsize, averages, yerr=errors, fmt='ko' )
plt.xlabel("Length of block")
plt.ylabel(r'$\langle E \rangle$' " / natural units")
plt.savefig( "average_energy2.png" )
