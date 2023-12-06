#! /usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# {{ cookiecutter.python_node_name | snakecase }}.py
#
# TODO: Add some description of the module
#
# Created: 12/06/23
#   - {{ cookiecutter.author }}
#   - {{ cookiecutter.author_email }}
#
# Modified:
#   * 
#
# TODO:
#   * 
###############################################################################

import rclpy
from rclpy.node import Node


class NewNode(Node):
    def __init__(self):
        super().__init__('{{ cookiecutter.python_node_name }}')
        self.logger_info('Hello ROS 2')

    def logger_info(self, text: str):
        self.get_logger().info(text)


def main(*args):
    rclpy.init(args=args)
    node = NewNode()

    try:
        rclpy.spin(node)  # will hold/keep alive node

    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()