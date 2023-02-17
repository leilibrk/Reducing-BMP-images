# BMP compression

We tried to compress bmp images using SVD formula:

![](https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/svd.png)

Since sigma matrix is decreasing so when we get downer their values get near to zero and we can not condiser them in our calculation:


![](https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/svd-k.png)

For example if our Input image is : 

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/bmp%20compression/images/2.bmp" title="" alt="" width="266">

with k = 10 :

<img src="https://github.com/leilibrk/Reducing-BMP-images/blob/main/k%3D10.png" title="" alt="" width="266">

with k = 50 :

<img src="https://github.com/leilibrk/Reducing-BMP-images/blob/main/k%3D50.png" title="" alt="" width="272">


with k = 250 :

<img src="https://github.com/leilibrk/Reducing-BMP-images/blob/main/k%3D250.png" title="" alt="" width="280">

