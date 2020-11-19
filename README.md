# The average square energy

This next exercise is like the previous one in that you are going to compute an ensemble average.  This time, however,  you should calculate the ensemble average for the square of the total energy.  In other words, I want you to square each of the total energies that you obtain from your trajectory and to calculate the average of these squared quantities.  As in the previous exercise, you must perform block averaging to get suitable error bars because the final value that you obtain is an estimate for the average squared energy. Thus the uncertainty in this estimate must be quantified.

As in the last exercise, I have written an outline for a constant temperature MD code in the cell on the right.  This outline is the same as the outline in the previous exercise so you must:  

1. Write a function called `potential` that computes the potential energy and the forces for each of the configurations you generate.
2. Write a function called `kinetic` that calculates the instantaneous kinetic energy.
3. Use your potential function to write code that uses the velocity Verlet algorithm and the thermostat to integrate the equations of motion.
4. Every stride MD steps store the instantaneous values of the potential, kinetic, total and conserved quantity in the lists called `p_energy`, `k_energy`, `t_energy` and `conserved_quantity`.

Furthermore, as in the previous exercise, a function called `gen_traj` has been written.  This function generates the molecular dynamics trajectory and takes seven input arguments:  

1. `pos` - the initial positions of the atoms
2. `vel` - the initial velocities of the atoms
3. `nsteps` - the number of steps in the trajectory that will be generated
4. `timestep` - the simulation timestep
5. `stride` - the frequency with which to store the energies - energies are stored every stride MD steps.
6. `temperature` - the temperature at which to run the simulation
7. `friction` - the friction parameter for the thermostat

It then returns five lists:  

1. `times` - the times at which data has been collected
2. `p_energy` - the potential energy as a function of time.
3. `k_energy` - the kinetic energy as a function of time
4. `t_energy` - the total energy of the system as a function of time
5. `conserved_quantity` - the value of the conserved quantity as a function of time.

As in the last exercise, you are going to need to fill in the blanks in the code within it using what you have learned about constant temperature molecular dynamics to get this function working correctly.  

You will notice that there is a call to `gen_traj` after the definition of this function and that arrays called `tt`, `potential_e`, `kinetic_e`, `total` and `conserved` are used to hold the values that the energy took during the trajectory that was generated.  You need to use the data in these arrays to compute block averages and errors with blocks of trajectory that are 200 steps, 400 steps, 600 steps, 800 steps, 1000 steps and 1200 steps long.  

Remember that you are computing block averages for the __square of the total energy__ so you must square the energy __before__ you add it to the variable that accumulates the mean.  The value of the average of the block averages should be stored in the list called `averages`, and the error bar for a 90 % confidence limit should be stored in the list called `errors`.  

The final result should be a graph showing how the size of the error bar changes as the size of the blocks from which it is computed changes.
