#!/usr/local/bin/python
import sdf
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import h5py 
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from optparse import OptionParser
import os

######## Constant defined here ########
pi        =     3.1415926535897932384626
q0        =     1.602176565e-19 # C
m0        =     9.10938291e-31  # kg
v0        =     2.99792458e8    # m/s^2
kb        =     1.3806488e-23   # J/K
mu0       =     4.0e-7*pi       # N/A^2
epsilon0  =     8.8541878176203899e-12 # F/m
h_planck  =     6.62606957e-34  # J s
wavelength=     1.0e-6
frequency =     v0*2*pi/wavelength

exunit    =     m0*v0*frequency/q0
bxunit    =     m0*frequency/q0
denunit    =     frequency**2*epsilon0*m0/q0**2
print('electric field unit: '+str(exunit))
print('magnetic field unit: '+str(bxunit))
print('density unit nc: '+str(denunit))

font = {'family' : 'monospace',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 20,  
        }  
font_size = 20
font_size2= 15
######### Script code drawing figure ################
if __name__ == "__main__":
    from_path ='./'
    to_path   ='./'
    start   =  1  # start time
    stop    =  10  # end time
    step    =  1  # the interval or step
    
    dt      = 1.0/160.0*0.9
    grid_x  = np.linspace(0,50,8001)
    if True==False:
      f = h5py.File('Fields0.h5', 'r')
      for i in f['data'].keys():
        time = 1.0*int(i)*dt
        for j in f['data'][i].keys():
            print(f['data'][i][j])
            name = j
            field = f['data'][i][j].value
            plt.plot(grid_x,field,'-r',linewidth=2)
            #### manifesting colorbar, changing label and axis properties ####
            plt.xlabel('$x [\mu m]$',fontdict=font)
            plt.ylabel('Normalized '+name,fontdict=font)
            plt.xticks(fontsize=font_size); 
            plt.yticks(fontsize=font_size);
            plt.title(name+' at '+str(round(time,6))+' $T_0$',fontdict=font)
            fig = plt.gcf()
            fig.set_size_inches(12, 7)
            fig.savefig(to_path+'fig_'+name+str(i).zfill(10)+'.png',format='png',dpi=80)
            print(to_path+'fig_'+name+str(i).zfill(10)+'.png')
            plt.close("all")

    if True==True:
      f = h5py.File('ParticleBinning0.h5', 'r')
      for i in f.keys():
          time = 1.0*int(i[-8:])*dt 
          name = 'proton'
          value_x = np.linspace(0,50,500) 
          value_y = f[i].value
          plt.plot(value_x*0.51,value_y,'-r',linewidth=2)
          #### manifesting colorbar, changing label and axis properties ####
          plt.xlabel(r'$\varepsilon\ [MeV]$',fontdict=font)
          plt.ylabel('dN_dE '+name,fontdict=font)
          plt.xticks(fontsize=font_size); 
          plt.yticks(fontsize=font_size);
          plt.yscale('log');
          plt.title('dN_dE'+name+' at '+str(round(time,6))+' $T_0$',fontdict=font)
          fig = plt.gcf()
          fig.set_size_inches(12, 7)
          fig.savefig(to_path+'fig_'+'dN_dE'+name+str(i).zfill(10)+'.png',format='png',dpi=80)
          print(to_path+'fig_'+'dN_dE'+name+str(i).zfill(10)+'.png')
          plt.close("all")

    if True==True:
      f = h5py.File('ParticleBinning1.h5', 'r')
      for i in f.keys():
          time = 1.0*int(i[-8:])*dt 
          name = 'electron'
          value_x = np.linspace(0,50,500) 
          value_y = f[i].value
          plt.plot(value_x*0.51,value_y,'-r',linewidth=2)
          #### manifesting colorbar, changing label and axis properties ####
          plt.xlabel(r'$\varepsilon\ [MeV]$',fontdict=font)
          plt.ylabel('dN_dE '+name,fontdict=font)
          plt.xticks(fontsize=font_size); 
          plt.yticks(fontsize=font_size);
          plt.yscale('log');
          plt.title('dN_dE'+name+' at '+str(round(time,6))+' $T_0$',fontdict=font)
          fig = plt.gcf()
          fig.set_size_inches(12, 7)
          fig.savefig(to_path+'fig_'+'dN_dE'+name+str(i).zfill(10)+'.png',format='png',dpi=80)
          print(to_path+'fig_'+'dN_dE'+name+str(i).zfill(10)+'.png')
          plt.close("all")

    if True==False:
      f=h5py.File('Probes0.h5', 'r')
      n_time = 31
      time = np.zeros(31)
      field_list = ['Ex','Ey','Bz']
      number = f['number'].value
      p0     = f['p0'].value
      positions = f['positions'].value
      probe_data = np.zeros([np.size(field_list),n_time])
      j = 0
      for i in f.keys():
          if i.isdigit() == False:
              continue
          time[j] = 1.0*int(i)*dt
          for k in range(np.size(field_list)):
              probe_data[k,j]= f[i].value[k]
          j=j+1
      print("time:",time)
      for i in range(np.size(field_list)):
          name = field_list[i]
          plt.plot(time,probe_data[i,:],'-b',linewidth=2)
          #### manifesting colorbar, changing label and axis properties ####
          plt.xlabel('t [fs]',fontdict=font)
          plt.ylabel('Normalized '+name,fontdict=font)
          plt.xticks(fontsize=font_size); 
          plt.yticks(fontsize=font_size);
          plt.title(name+' at '+str(positions),fontdict=font)
          fig = plt.gcf()
          fig.set_size_inches(12, 7)
          fig.savefig(to_path+'fig_prob'+name+'.png',format='png',dpi=80)
          print(to_path+'fig_prob'+name+'.png')
          plt.close("all")
