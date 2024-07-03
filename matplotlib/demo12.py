import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.random.rand(10, 10)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""
plt.imshow(a, interpolation='nearest', cmap='bone')
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()