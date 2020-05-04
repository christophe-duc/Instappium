# flake8: noqa

# __variables__ with double-quoted values will be available in setup.py
__version__ = "0.0.2"

from .instappium import InstAppium
from .engine.fsm import FSMSession
from .common import Settings
