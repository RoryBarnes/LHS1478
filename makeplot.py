import pathlib
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import vplot

import vplanet

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))
#from get_args import get_args

# Run vplanet
cpl = vplanet.run(path / "CPL" / "vpl.in", units=False)
ctl = vplanet.run(path / "CTL" / "vpl.in", units=False)
e0=0.5

fig = plt.figure(figsize=(6.5, 4))


plt.plot(cpl.b.Time, (cpl.b.Eccentricity - e0)*1e6, color="k", linestyle="dashed",label='CPL')
plt.plot(ctl.b.Time, (ctl.b.Eccentricity - e0)*1e6, color="k", linestyle="solid",label='CTL')
#plt.xscale("log")
plt.xlabel("Time (Days)",fontsize=16)
plt.ylabel(r"$\Delta$ Eccentricity ($\times 10^{6}$)",fontsize=16)
plt.legend()
plt.ylim([-1,0])


# Save the figure
#ext = get_args().ext
fig.savefig(path / f"lhs1478.ecc.png",dpi=300)
