import numpy as np
import quaternion
from loguru import logger

inst = np.quaternion(1, 0, 0, 0)
logger.info(inst)
rotate = np.quaternion(0, -0.75, 0, 0.75)
matrix_ = quaternion.as_rotation_matrix(rotate)
logger.info(matrix_)
euler_ = quaternion.as_euler_angles(rotate)
logger.info(euler_)
abs_ = np.absolute(rotate)
new_inst = inst * rotate
logger.info(f"{new_inst}, {type(new_inst)}")
