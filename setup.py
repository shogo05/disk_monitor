# SPDX-FileCopyrightText: 2025 Shogo Uchida
# SPDX-License-Identifier: BSD-3-Clause

import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'disk_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shogo Uchida',
    maintainer_email='Sho808Sho07@gmail.com',
    description='TODO: Package description',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'monitor = disk_monitor.monitor:main',
            'warning = disk_monitor.warning:main',
        ],
    },
)
