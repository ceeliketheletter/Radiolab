import numpy as np
import ugradio


def takedata(observationlength, dt, filename):
    data = []
    times = []
    
    
    for i in range(observationlength):
        '''Client for reading from the HP 3478A Multimeter used to integrate
        baseband voltages in the UGRadio Interferometer.  Sends commands over
        the network to a microcontroller that translates commands to the GPIB
        bus on the back of the multimeter.'''
    
        hpm = ugradio.hp_multi.HP_Multimeter() 
    
        '''Initiate continuous reading from multimeter every dt seconds.'''
        hpm.start_recording(self, dt, tries=1100) 
    
        '''locally wait for 120 seconds (have to exceed the total processing time)'''
        #time.sleep(1200)  
    
    
        '''Terminate continuous reading from multimeter and return recording.
        May take up to dt seconds (as set in start_recording call) to complete
        final read.'''
        hpm.end_recording()
    
        datum, time = hpm.get_recording_data() 
    data.append(datum)
    times.append(time)
        
    #np.savez(filename+'_volts.npz', data)
    #np.savez(filename+'_time.npz', times)
    
    return(data, times)