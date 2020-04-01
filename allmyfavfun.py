
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
