#Plotting:
import matplotlib.pyplot as plt
import numpy as np
plt.title('Asymmetry vs qt')
plt.xlim([0, 100])
#plt.yscale("log")

plt.xlabel(r"qt")
plt.ylabel(r"A")
num=np.loadtxt(f"/home/himanshu/gammagToccbarg/Icem/ICEMnlo.dat")
print(num)
plt.plot(num[:,0], num[:,1],  label=f'eptoJ/psi')

plt.legend()
#plt.savefig("epASYM_p1.pdf", format="pdf", dpi=300)
plt.show()