# Copyright (C) 2015 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# File: util.py
# Purpose:
#   Various common functions for use in build scripts.


import sys
import os

import defaults

def check_build_config():
    if not os.path.exists(defaults.BUILD_CONFIG):
        print("Build config file ({file}) does not exist".format(file=defaults.BUILD_CONFIG))
        print("If you are running this script by hand, you should better not. Run 'make iso' instead.")
        sys.exit(1)
