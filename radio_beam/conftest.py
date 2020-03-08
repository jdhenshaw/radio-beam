# this contains imports plugins that configure py.test for astropy tests.
# by importing them here in conftest.py they are discoverable by py.test
# no matter how it is invoked within the source tree.
from __future__ import print_function, absolute_import, division

import os
from distutils.version import LooseVersion

# Import casatools and casatasks here if available as they can otherwise
# cause a segfault if imported later on during tests.
try:
    import casatools
    import casatasks
except ImportError:
    pass

import pytest
import numpy as np
from astropy.io import fits
from astropy import wcs
from astropy.version import version as astropy_version

from astropy.version import version as astropy_version

if astropy_version < '3.0':
    from astropy.tests.pytest_plugins import *
    del pytest_report_header
else:
    from pytest_astropy_header.display import PYTEST_HEADER_MODULES, TESTED_VERSIONS
