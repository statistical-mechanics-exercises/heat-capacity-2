import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_block_averages(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        i = 0
        total2=total*total
        for block in this_x :
            blocksize = int( block )
            # Your code to calculate the block averages goes here
            nblocks, average, error = int( len(total) / blocksize ), 0, 0
            for j in range(nblocks) : 
                av = sum( total2[j*blocksize:(j+1)*blocksize] ) / blocksize
                average = average + av 
                error = error + av*av 
            average = average / nblocks
            self.assertTrue( np.abs( average - averages[i] )<1E-4, "The block averages have been computed incorrectly" )
            error = (nblocks / (nblocks-1))*( error / nblocks - average*average )
            error = np.sqrt( error / nblocks )*st.norm.ppf((1+0.90)/2)
            self.assertTrue( np.abs( errors[i] - error )<1E-4, "The errors for the block averages have been computed incorrectly" )
            i=i+1
            
    def test_average_kinetic(self) : 
        average_ke = sum(kinetic_e) / len(total)
        self.assertTrue( np.abs( np.abs( average_ke - 7*temperature ) )<0.5, "the average kinetic energy is incorrect" )
        
    def test_conserved(self) :
        for i in range(1,len(conserved) ) :
            self.assertTrue( np.abs( conserved[i-1]-conserved[i] )<1E-2, "The conserved quantity is not conserved" )
            
    def test_kinetic(self) :
        for i in range(10) :
           vel = np.zeros([7,2])
           myeng = 0
           for j in range(7) : 
              vel[j,0], vel[j,1] = np.random.normal(), np.random.normal()
              myeng = myeng + vel[j,0]*vel[j,0] / 2 + vel[j,1]*vel[j,1] / 2
           self.assertTrue( np.abs( kinetic(vel) - myeng )<1E-6, "The kinetic energy is computed incorrectly" )
           
    def test_forces(self) : 
        pp = pos
        base_p, base_f = potential(pp)
        for i in range(7) :
            for j in range(2) :
                pp[i][j] = pp[i][j] + 1E-8
                new_p, crap = potential(pp)
                numder = (new_p-base_p)/1E-8
                self.assertTrue( np.abs(numder + base_f[i][j])<1e-4, "Forces and potential are not consistent" )
                pp[i][j] = pp[i][j] - 1E-8
