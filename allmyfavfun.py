
from matplotlib import cm

# Create a series of color handles from colormap
def createmap(nn,cmap):
  mapvec = []
  for j in range(0,nn):
    idd = np.rint(j*256/(nn-1))
    idd = idd.astype(int)
    mapvec.append(cmap(idd))
  return mapvec

# Break down a temporal series into a smaller set of (windowed) time averages
def seqaveraging(field,n,axis=0):
  avearr = []
  m = field.shape[0]//n
  for i in range(n):
    avearr.append(np.mean(field[i*m:(i+1)*m],axis=0))
  avearr = np.stack(avearr,axis=0)
  return avearr

# Filter for ICs in DEDALUS
def filterfield(field,frac=0.5):
  field.require_coeff_space()
  dom=field.domain
  local_slice = dom.dist.coeff_layout.slices(scales=dom.dealias)
  coeff = []
  for n in dom.global_coeff_shape:
    coeff.append(np.linspace(0,1,n,endpoint=False))
  cc = np.meshgrid(*coeff,indexing='ij')
  field_filter = np.zeros(dom.local_coeff_shape,dtype='bool')
  for i in range(dom.dim):
    field_filter = field_filter | (cc[i][local_slice] > frac)
  field['c'][field_filter] = 0j

# Find zeroes of a function within bounds
def Cfun(x):
  return -7.0785e-3+1.8217e-7*x+4.2679e-12*x**2
p_star = optimize.brentq(Cfun, xmin, xmax) 

# Make a function take arguments from command line using docopt
python3 test.py files/* --option1=value1 ...
"""
Usage:
    test.py <files> [options] 

Options:
    --option1=<option1>		option1 [default: value]
"""
from docopt import docopt
args = docopt(__doc__)
