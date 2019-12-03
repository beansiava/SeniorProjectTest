import numpy as np
thresholds = np.loadtxt('TimTutorial/thresholds.txt', dtype=float)
thresholds[0] = -.35
thresholds[1] = 0
thresholds[2] = .35
np.savetxt('TimTutorial/thresholds.txt', thresholds)
