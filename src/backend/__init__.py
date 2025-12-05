import os
import sys

# Agregar carpeta 'apps' al path de Python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "..", "apps"))
