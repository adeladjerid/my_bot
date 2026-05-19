import os
import subprocess
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    subprocess.run(['sudo', 'stty', '-F', '/dev/ttyUSB0', 'raw', '115200'])  # ✅ with sudo

    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 115200,
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Boost'
            }]
        )
    ])