The following scenes corresponds to the original images with name xx_background.png
scene 1: 00-06, test
scene 2: 07-17, train
scene 3: 18-29, train
scene 4: 30-32, train

To read the file use cv2.imread() with flags=0, e.g.

im = cv2.imread('data/scene1_mask.png'), 0)

label values corresponds to:
0: unlabeled
1: pavement
2: road
3: structure
4: terrain
5: tree
