import numpy as np
import quaternion
from loguru import logger


def main():
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
    euler_a = [0, 0, 1.57]
    logger.info(f'\n{quaternion.from_euler_angles(euler_a)}')

def quat_action(to_proc):
    logger.info(f'{to_proc=}')
    for i in range(10000000):
        inst = np.quaternion(*to_proc)
        rotate = np.quaternion(0.0, -0.75, 0.0, 0.75)
        new_inst = inst * rotate
    to_ret = quaternion.as_float_array(new_inst).tolist()
    logger.info(f'{to_ret=}')
    return to_ret


if __name__ == '__main__':
    to_proc = [1, 0, 0, 0]
    ret = quat_action(to_proc)
    print(ret, type(ret))