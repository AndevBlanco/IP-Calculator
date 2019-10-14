# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os, time
import subprocess


# Iterable con las rutas de los scripts
scripts_paths = ("loadlogo.py", "loadinterface.py")

# Creamos cada proceso
procesos = [subprocess.Popen(["python", script]) for script in scripts_paths]

# Esperamos a que todos los subprocesos terminen.
for proceso in procesos:
    proceso.wait()
