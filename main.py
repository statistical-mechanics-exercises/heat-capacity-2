import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

def potential(x) :
  energy = 0 
  forces = np.zeros([7,2])
  # Your code to calculate the potential goes here
  for i in range(1,7) :
      for j in range(i) :
          d = x[i,:]-x[j,:]
          r2 = sum(d*d)
          r6 = r2*r2*r2
          r12 = r6*r6
          energy = energy + 4/r12 - 4/r6
          pref = 4*( 6/(r6*r2) - 12/(r12*r2) )
          forces[i,:] =  forces[i,:] - pref*d
          forces[j,:] =  forces[j,:] + pref*d 
  return energy, forces
  
def kinetic(v) :
  ke = 0
  # Your code to calculate the kinetic energy from the velocities goes here
  for vel in v : ke = ke + 0.5*sum(vel*vel)
  return ke

def gen_traj( pos, vel, nsteps, timestep, stride, temperature, friction ) :
  # This calculates the initial values for the forces
  eng, forces = potential(pos)
  # This is the variable that you should use to keep track of the quantity of energy that is exchanged with 
  # the reservoir of the thermostat.
  therm = 0
  therm1 = np.exp( -friction*timestep / 2 )
  therm2 = np.sqrt( temperature*(1-therm1*therm1) )
  
  times = np.zeros(int(nsteps/stride))
  k_energy = np.zeros(int(nsteps/stride))
  p_energy = np.zeros(int(nsteps/stride))
  t_energy = np.zeros(int(nsteps/stride))
  conserved_quantity = np.zeros(int(nsteps/stride))
  for step in range(nsteps) :
    # Apply the thermostat for a half timestep 
    for i in range(7) :
      therm = therm + 0.5*vel[i][0]*vel[i][0] + 0.5*vel[i][1]*vel[i][1] 
      vel[i][0] = vel[i][0]*therm1 + therm2*np.random.normal()
      vel[i][1] = vel[i][1]*therm1 + therm2*np.random.normal()
      therm = therm - 0.5*vel[i][0]*vel[i][0] - 0.5*vel[i][1]*vel[i][1]
  
    # Update the velocities a half timestep
    # fill in the blanks in the code here
    for i in range(7) : 
      vel[i][0] = vel[i][0] + 0.5*timestep*forces[i][0]
      vel[i][1] = vel[i][1] + 0.5*timestep*forces[i][1]
    
    # Now update the positions using the new velocities
    # You need to add code here
    for i in range(7) :
      pos[i][0] = pos[i][0] + timestep*vel[i][0]
      pos[i][1] = pos[i][1] + timestep*vel[i][1] 
  
    # Recalculate the forces at the new position
    # You need to add code here
    eng, forces = potential(pos)
  
    # Update the velocities another half timestep
    # You need to add code here
    for i in range(7) :
      vel[i][0] = vel[i][0] + 0.5*timestep*forces[i][0]
      vel[i][1] = vel[i][1] + 0.5*timestep*forces[i][1]

    # And finish by applying the thermostat for the second half timestep 
    for i in range(7) :
      therm = therm + 0.5*vel[i][0]*vel[i][0] + 0.5*vel[i][1]*vel[i][1] 
      vel[i][0] = vel[i][0]*therm1 + therm2*np.random.normal()
      vel[i][1] = vel[i][1]*therm1 + therm2*np.random.normal()
      therm = therm - 0.5*vel[i][0]*vel[i][0] - 0.5*vel[i][1]*vel[i][1]

    # This is where we want to store the energies and times
    if step%stride==0 : 
      times[int(step/stride)] = step
      # Write code to ensure the proper values are saved here
      p_energy[int(step/stride)] = eng
      k_energy[int(step/stride)] = kinetic(vel)
      t_energy[int(step/stride)] = kinetic(vel) + eng
      conserved_quantity[int(step/stride)] = kinetic(vel) + eng + therm
      
  return times, p_energy, k_energy, t_energy, conserved_quantity
  
# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This command reads in the velocities that are contained in the file called velocities.txt
vel = np.loadtxt( "velocities.txt" )
  
# This command runs the molecular dynamics and generates a trajectory 
temperature = 1.0   # This variable must be defined to pass the tests
tt, potential_e, kinetic_e, total, conserved = gen_traj( pos, vel, 2400, 0.005, 1, temperature, 2.0 )

# This is the part to compute the block averages for the error estimation
i, bsize, averages, errors = 0, [200,400,600,800,1000,1200], np.zeros(6), np.zeros(6)
for blocksize in bsize :
  # Your code to calculate the block averages goes here
  nblocks = int( len(total) / blocksize )
  for j in range(nblocks) : 
    av = 0
    for k in range(j*blocksize,(j+1)*blocksize) : av = av + total[k]*total[k]
    av = av / blocksize
    averages[i] = averages[i] + av 
    errors[i] = errors[i] + av*av 
  averages[i] = averages[i] / nblocks 
  errors[i] = (nblocks / (nblocks-1))*( errors[i] / nblocks - averages[i]*averages[i] )
  errors[i] = np.sqrt( errors[i] / nblocks )*st.norm.ppf(1.90/2)
  i=i+1   
   
# This will plot the kinetic energy as a function of time
plt.errorbar( bsize, averages, yerr=errors, fmt='ko' )
plt.xlabel("Length of block")
plt.ylabel(r'$\langle E \rangle$' " / natural units")
plt.savefig( "average_energy2.png" )
