import numpy as np

#  sine functions
arr = np.array([1,2,3])
print('Sin Values: ',np.sin(arr))
            # Sin Values:  [0.84147098 0.90929743 0.14112001]

print('Cos values :',np.cos(arr))
            # Cos values : [ 0.54030231 -0.41614684 -0.9899925 ]

print('Tangent Values :',np.sin(arr)/np.cos(arr))
            # Tangent Values : [ 1.55740772 -2.18503986 -0.14254654]


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print('Sin Values: ',np.sin(arr))
            # Sin Values:  [[ 0.84147098  0.90929743  0.14112001]
            #  [-0.7568025  -0.95892427 -0.2794155 ]
            #  [ 0.6569866   0.98935825  0.41211849]]

print('Cos values :',np.cos(arr))
            # Cos values : [[ 0.54030231 -0.41614684 -0.9899925 ]
            #  [-0.65364362  0.28366219  0.96017029]
            #  [ 0.75390225 -0.14550003 -0.91113026]]

print('Tangent Values :',np.sin(arr)/np.cos(arr))

            # Tangent Values : [[ 1.55740772 -2.18503986 -0.14254654]
            #  [ 1.15782128 -3.38051501 -0.29100619]
            #  [ 0.87144798 -6.79971146 -0.45231566]]

angles = np.array(([0,np.pi,np.pi/2]))
print(np.sin(angles))
            # [0.0000000e+00 1.2246468e-16 1.0000000e+00]