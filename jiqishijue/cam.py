# -*- coding: cp936 -*-
from pylab import *
from PIL import Image

# If you have PCV installed, these imports should work
from PCV.geometry import homography, camera
from PCV.localdescriptors import sift

"""
This is the augmented reality and pose estimation cube example from Section 4.3.
"""


def cube_points(c, wid):
    """ 创建用于绘制立方体的一个点列表（前5个点是底部的正方形，一些边重合了 """
    p = []
    # 底部
    p.append([c[0] - wid, c[1] - wid, c[2] - wid])
    p.append([c[0] - wid, c[1] + wid, c[2] - wid])
    p.append([c[0] + wid, c[1] + wid, c[2] - wid])
    p.append([c[0] + wid, c[1] - wid, c[2] - wid])
    p.append([c[0] - wid, c[1] - wid, c[2] - wid])  # 为了绘制闭合图像，和第一个相同

    # 顶部
    p.append([c[0] - wid, c[1] - wid, c[2] + wid])
    p.append([c[0] - wid, c[1] + wid, c[2] + wid])
    p.append([c[0] + wid, c[1] + wid, c[2] + wid])
    p.append([c[0] + wid, c[1] - wid, c[2] + wid])
    p.append([c[0] - wid, c[1] - wid, c[2] + wid])  # 为了绘制闭合图像，和第一个相同

    # 竖直边
    p.append([c[0] - wid, c[1] - wid, c[2] + wid])
    p.append([c[0] - wid, c[1] + wid, c[2] + wid])
    p.append([c[0] - wid, c[1] + wid, c[2] - wid])
    p.append([c[0] + wid, c[1] + wid, c[2] - wid])
    p.append([c[0] + wid, c[1] + wid, c[2] + wid])
    p.append([c[0] + wid, c[1] - wid, c[2] + wid])
    p.append([c[0] + wid, c[1] - wid, c[2] - wid])

    return array(p).T


def my_calibration(sz):

    row, col = sz
    fx = 2555 * col / 2592
    fy = 2586 * row / 1936
    K = diag([fx, fy, 1])
    K[0, 2] = 0.5 * col
    K[1, 2] = 0.5 * row
    return K
sift.process_image('sys1.JPG','im0.sift')
l0,d0 = sift.read_features_from_file('im0.sift')
sift.process_image('sys2.JPG','im1.sift')
l1,d1 = sift.read_features_from_file('im1.sift')
# 匹配特征，并计算单应性矩阵
matches = sift.match_twosided(d0,d1)
ndx = matches.nonzero()[0]
fp = homography.make_homog(l0[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
tp = homography.make_homog(l1[ndx2,:2].T)
model = homography.RansacModel()
H,ransac_data = homography.H_from_ransac(fp,tp,model)

# 计算照相机标定矩阵
K = my_calibration((747,1000))

# 位于边长为 0.2，z=0 平面上的三维点
box = cube_points([0,0,0.1],0.1)

# 投影第一幅图像上底部的正方形
cam1 = camera.Camera( hstack((K,dot(K,array([[0],[0],[-1]])) )) )

# 底部正方形上的点
box_cam1 = cam1.project(homography.make_homog(box[:,:5]))

# 使用 H 将点变换到第二幅图像中
box_trans = homography.normalize(dot(H,box_cam1))

# 从 cam1 和 H 中计算第二个照相机矩阵
cam2 = camera.Camera(dot(H,cam1.P))
A = dot(linalg.inv(K),cam2.P[:,:3])
A = array([A[:,0],A[:,1],cross(A[:,0],A[:,1])]).T
cam2.P[:,:3] = dot(K,A)


# 使用第二个照相机矩阵投影
box_cam2 = cam2.project(homography.make_homog(box))


# 测试：将点投影在 z=0 上，应该能够得到相同的点
point = array([1,1,0,1]).T
rcParams['font.sans-serif'] = ['SimHei']
im0 = array(Image.open('sys1.JPG'))
im1 = array(Image.open('sys2.JPG'))


# 底部正方形的二维投影
figure()
imshow(im0)
plot(box_cam1[0,:],box_cam1[1,:],linewidth=3,color='g')
title('二维投影')
axis('off')
# 使用 H 对二维投影进行变换
figure()
imshow(im1)
axis('off')
plot(box_trans[0,:],box_trans[1,:],linewidth=3,color='g')
title('二维投影')

# 三维立方体
figure()
imshow(im1)
plot(box_cam2[0,:],box_cam2[1,:],linewidth=3,color='g')
axis('off')
title('三维立方体')

show()