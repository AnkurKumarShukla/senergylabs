Liu Bolin is known for his camouflage art where he blends into the background. Image processing techniques like **semantic segmentation** could potentially be used to detect him, but it would be challenging since his camouflage is very effective.<br>
Other way can be **cyclic gan** in which we would use 2 GAN network . first one is ordinary gan network and second we pass generated image from first to reconstruct the orignal image . <br>
The loss between original image and 2nd genarated is used as heurestic to find the minima . 
<br>

Here is work of my senior which brought me to this conclusion : https://ieeexplore.ieee.org/document/10207960


I closely studied his work . 


![Image](image.png)

<br>
<br>
<br>
Q2 solution <br>

High   ![High](../filtered_high_noise.jpg)

low  ![low](../filtered_low_noise.jpg)

Med  ![med](../filtered_med_noise.jpg)
