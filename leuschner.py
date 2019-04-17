#ssh -XY radiolab@leuschner.berkeley.edu -p 31
# password = Cud4b4ck
import ugradio
import numpy np
import astropy
import calibrate
import pyfits
from ugradio import nch
from astropy.io import fits
import agilent
from ugradio import leo
from ugradio import leusch
import leuschner

print('Importing done')

''' Telescope controls'''
tele = ugradio.leusch.LeuschTelescope() # '''Interface for controlling the Leuschner Telescope.'
#tele.get_pointing()  # returns the current (alt,az) of the dish in degrees
#tele.point(alt,az) #moves the telescope to a specified alt, az in degrees.
#tele.main() #moves the telescope to maintenance position.

''' Noise'''
LeuschNoise = ugradio.leusch.LeuschNoise() #nstantiates an interface to the noise diode
LeuschNoise.on()
LeuschNoise.off()


''' Set LO '''
lo = ugradio.agilent.SynthDirect() #instantiates an interface to the LO
#lo.get_frequency()
#lo.get_amplitude()
# lo.set_frequency(633, 'MHz')
#lo.set_frequency(635,'MHz')
#lo.set_amplitude(10, 'dBm')

#synth=ugradio.agilent.SynthClient(host='127.0.0.1')

''' Coordinates '''

#leo.lat = 37.9183
#leo.lon = -122.1067

''' Galactic Coordinates '''
from astropy.coordinates import ICRS
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.coordinates import Galactic

l = 120
b = 0
gal = Galactic(l*u.degree,b*u.degree)
eq = gal.transform_to(ICRS)


_jd = ugradio.timing.julian_date()
alt,az = ugradio.coord.get_altaz(6.45083114, 62.72572675 ,_jd,leo.lat,leo.lon,leo.alt,equinox='J2019')

''' Read spectrometer '''

spec = leuschner.Spectrometer('10.0.1.2') #instantiates an interface to the spectrometer at the specified IP address.
#spec.int_time #tells you how long each spectrum is integrated for

'''Take data '''
'''Will read N spectra and store the output in a FITS file, writing the ra/dec coordinates into the header of the file. Note that this does not point the telescope; it just documents where it is pointed in the file. '''
#spec.read_spec('_test_.fits', N, (ra, dec), 'eq')
#e.g. spec.read_spec('compas.fits',10,(50,60),'eq')


#spec.check_connected() #allows you to check that you are ready to take data

''' Open your Data'''

#f = pyfits.open('test.fits')
#f[0].header
# f[1].data['auto0_real'] #returns the first spectrum for the first polarization
# f[1].data['auto1_real'] #returns the first spectrum for the second polarization
#f[N].data[’auto0 real’] returns the N th spectrum for the first polarization.


#plt.plot(f[10].data['auto0_real'])
#Spectrometer.read_spec('noise_off.fits',100,(80.01,180.01),'eq')

calibrate.calibrate()
#Spectrometer.read_spec('noise_on.fits',100,(80.01,180.01),'eq')


#Spectrometer.read_spec('cassiopea1.fits',100,(6.45,62.73),'eq')

f = pyfits.open('Calibrate633.fits')
power = f[1].data['auto0_real']
freq = np.fft.fftfreq(len(power))
plt.plot(power)

hdu = fits.open('noise_off.fits')
hdr = hdu[1].header
data = hdu[1].data[0]
plt.plot(data)
