
def sun_alt():
    '''#locate the current position of sun in alt and az'''
    jd = ugradio.timing.julian_date()
    ra,dec = ugradio.coord.sunpos(jd)
    alt,az = ugradio.coord.get_altaz(ra,dec,jd,nch.lat,nch.lon,nch.alt)
    return (alt,az)


def point_interferometers(observing_object):
    ifm = ugradio.interf.Interferometer() 
    
    if observing_object == 'sun':
        '''#locate the current position of sun in alt and az'''
        alt,az = sun_alt() 

    '''Point both antennas to the specified alt/az.'''
    ifm.point(alt,az) 

    '''Return the current telescope pointing'''
    pointing = ifm.get_pointing()
    w_alt,w_az = pointing["ant_w"] 
    e_alt,e_az = pointing["ant_e"] 

    print("target:"+ str(alt)+","+str(az)) 
    print("west pointed :"+ str(w_alt)+","+str(w_az)) 
    print("east pointed :"+ str(e_alt)+","+str(e_az))
    
    
    if (diff(alt,e_alt)>tol or
        diff(az,e_az)>tol or
        diff(alt,w_alt)>tol or
        diff(az,w_az)>tol ):
            
        raise Exception ("pointing error")
    
    except Exception as e:
        print(e)
    

def stow_interferometers():
    '''Point both antennas to the stow position'''
    ifm.stow()
    print('Telescope stowed')

