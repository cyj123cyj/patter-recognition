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
    """ �������ڻ����������һ�����б�ǰ5�����ǵײ��������Σ�һЩ���غ��� """
    p = []
    # �ײ�
    p.append([c[0] - wid, c[1] - wid, c[2] - wid])
    p.append([c[0] - wid, c[1] + wid, c[2] - wid])
    p.append([c[0] + wid, c[1] + wid, c[2] - wid])
    p.append([c[0] + wid, c[1] - wid, c[2] - wid])
    p.append([c[0] - wid, c[1] - wid, c[2] - wid])  # Ϊ�˻��Ʊպ�ͼ�񣬺͵�һ����ͬ

    # ����
    p.append([c[0] - wid, c[1] - wid, c[2] + wid])
    p.append([c[0] - wid, c[1] + wid, c[2] + wid])
    p.append([c[0] + wid, c[1] + wid, c[2] + wid])
    p.append([c[0] + wid, c[1] - wid, c[2] + wid])
    p.append([c[0] - wid, c[1] - wid, c[2] + wid])  # Ϊ�˻��Ʊպ�ͼ�񣬺͵�һ����ͬ

    # ��ֱ��
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
# ƥ�������������㵥Ӧ�Ծ���
matches = sift.match_twosided(d0,d1)
ndx = matches.nonzero()[0]
fp = homography.make_homog(l0[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
tp = homography.make_homog(l1[ndx2,:2].T)
model = homography.RansacModel()
H,ransac_data = homography.H_from_ransac(fp,tp,model)

# ����������궨����
K = my_calibration((747,1000))

# λ�ڱ߳�Ϊ 0.2��z=0 ƽ���ϵ���ά��
box = cube_points([0,0,0.1],0.1)

# ͶӰ��һ��ͼ���ϵײ���������
cam1 = camera.Camera( hstack((K,dot(K,array([[0],[0],[-1]])) )) )

# �ײ��������ϵĵ�
box_cam1 = cam1.project(homography.make_homog(box[:,:5]))

# ʹ�� H ����任���ڶ���ͼ����
box_trans = homography.normalize(dot(H,box_cam1))

# �� cam1 �� H �м���ڶ������������
cam2 = camera.Camera(dot(H,cam1.P))
A = dot(linalg.inv(K),cam2.P[:,:3])
A = array([A[:,0],A[:,1],cross(A[:,0],A[:,1])]).T
cam2.P[:,:3] = dot(K,A)


# ʹ�õڶ������������ͶӰ
box_cam2 = cam2.project(homography.make_homog(box))


# ���ԣ�����ͶӰ�� z=0 �ϣ�Ӧ���ܹ��õ���ͬ�ĵ�
point = array([1,1,0,1]).T
rcParams['font.sans-serif'] = ['SimHei']
im0 = array(Image.open('sys1.JPG'))
im1 = array(Image.open('sys2.JPG'))


# �ײ������εĶ�άͶӰ
figure()
imshow(im0)
plot(box_cam1[0,:],box_cam1[1,:],linewidth=3,color='g')
title('��άͶӰ')
axis('off')
# ʹ�� H �Զ�άͶӰ���б任
figure()
imshow(im1)
axis('off')
plot(box_trans[0,:],box_trans[1,:],linewidth=3,color='g')
title('��άͶӰ')

# ��ά������
figure()
imshow(im1)
plot(box_cam2[0,:],box_cam2[1,:],linewidth=3,color='g')
axis('off')
title('��ά������')

show()