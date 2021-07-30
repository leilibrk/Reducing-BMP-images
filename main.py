import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


def kCalculate(U, S, V, k):
    UPrime = U[:, 0:k]
    SPrime = S[0:k, 0:k]
    VPrime = V[0:k]
    new_Img = np.matmul(np.matmul(UPrime, SPrime), VPrime)
    return new_Img


img = mpimg.imread('2.bmp')
# plt.imshow(img)
# plt.show()

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

U1, S1, V1 = np.linalg.svd(r, full_matrices=False)
U2, S2, V2 = np.linalg.svd(g, full_matrices=False)
U3, S3, V3 = np.linalg.svd(b, full_matrices=False)

k = 250

new_r = kCalculate(U1, np.diag(S1), V1, k)
new_g = kCalculate(U2, np.diag(S2), V2, k)
new_b = kCalculate(U3, np.diag(S3), V3, k)

new_img = np.dstack((new_r, new_g, new_b)).astype(np.uint8)
plt.imshow(new_img)
plt.show()


