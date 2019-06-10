#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  ------------------------
#  ----- rcbuildtest  -----
#  ------------------------
#
#    Copyright (C) 2010 by RoboLab - University of Extremadura - Esteban Martinena
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#
#
#

import argparse
import subprocess
import sys


class BColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class MyParser(argparse.ArgumentParser):
	def error(self, message):
		sys.stderr.write((BColors.FAIL + 'error: %s\n' + BColors.ENDC) % message)
		self.print_help()
		sys.exit(2)

class RcBuildTest():
	def __init__(self):
		pass

	def check_docker_installation(self):



		cmd_output = subprocess.Popen(['dpkg-query', '-W', '--showformat=\'${Status}\n\'','docker-ce'],
									  stdout=subprocess.PIPE)
		cmd2_output = subprocess.Popen(['grep', '"install ok installed"'],
									   stdin = cmd_output.stdout,
									  stdout=subprocess.PIPE,
									  stderr=subprocess.STDOUT)
		cmd_output.stdout.close()
		stdout, stderr = cmd2_output.communicate()
		print(stdout)
		print(stderr)
		print("Checking for package docker-ce: %s"%stdout)
		if not stdout:
			print("No docker-ce. Setting up docker-ce.")
			cmd_output = subprocess.Popen(['sudo', 'apt install', 'apt-transport-https', 'ca-certificates', 'curl', 'software-properties-common'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			stdout, stderr = cmd_output.communicate()
			print(stdout)
			print(stderr)
			# cmd_output = os.popen('sudo apt install apt-transport-https ca-certificates curl software-properties-common').read()
			# cmd_output = os.popen('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -').read()
			# cmd_output = os.popen('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"').read()
			# cmd_output = os.popen('sudo apt-get update').read()
			# cmd_output = os.popen('sudo apt-get --yes install docker-ce').read()
		else:
			pass
			# md_output = os.popen(
			# 	'sudo apt install apt-transport-https ca-certificates curl software-properties-common').read()



# echo "Checking for package docker-ce: $PKG_OK"
# if [ -z "$PKG_OK" ]
# then
#   echo "No docker-ce. Setting up docker-ce."
#   sudo apt install apt-transport-https ca-certificates curl software-properties-common
#   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#   sudo apt-get update
#   sudo apt-get --yes install docker-ce
# fi
# sudo docker stop robocomp_test
# sudo docker kill robocomp_test
# sudo docker container rm robocomp_test
# if [ -z "$1" ] || [ "$1" != '18.04' ] && [ "$1" != '19.04' ] && [ "$1" != '16.04' ]
# then
#     if [ "$1" != '18.04' ] && [ "$1" != '19.04' ] && [ "$1" != '16.04' ]
#     then
#
#     fi
#     echo "Currently you only can use 16.04, 18.04 or 19.04 as Ubuntu versions"
#     UBUNTU_VERSION='18.04'
# else
#     UBUNTU_VERSION=$1
# fi
#
# if [ -z "$2" ] || [ "$2" != 'stable' ] && [ "$2" != 'development' ]
# then
#     echo "Currently you only can use stable or development as robocomp branches."
#     ROBOCOMP_BRANCH='stable'
# else
#     echo "WHY"
#     ROBOCOMP_BRANCH=$2
# fi
#
#
# sudo docker run --name robocomp_test -it -w /home/robolab/ --user robolab:robolab -v $(pwd)/../../install/robocomp_install.sh:/home/robolab/robocomp_install.sh robocomp/clean-testing:robocomp-ubuntu$UBUNTU_VERSION bash -l -x robocomp_install.sh $ROBOCOMP_BRANCH
# if [ $? == 0 ]; then
#   echo "built done"
# else
#   #sudo docker logs robocomp_test | mail -s "docker" elqueseaelmail@gmail.com
# fi
# sudo docker container rm robocomp_test

def main():

	parser = MyParser(description='Application to look for existing configured interfaces ports on components')
	# parser.add_argument("-v", "--verbose", help="increase output verbosity",
	# 					action="store_true")
	# parser.add_argument("-p", "--port", help="List only the selected port information",
	# 					type=int)
	# # parser.add_argument("-c", "--components", help="list the diffents ports associated to component",
	# #                     action="store_true")
	# parser.add_argument("-a", "--all",
	# 					help="show all ports configured for an interface instead of showing only those with more than one interface per port",
	# 					action="store_true")
	# parser.add_argument("-l", "--lower",
	# 					help="show all ports with numbers lower than 10000",
	# 					action="store_true")
	# parser.add_argument("-i", "--interface",
	# 					help="List only interfaces that contains this string",
	# 					type=str)
	# parser.add_argument('action', choices=('ports', 'interfaces'), help="Show the interfaces by name or by port")
	# parser.add_argument('path', nargs='?',
	# 					help="path to look for components config files recursively (default=\"~/robocomp/\")")
	args = parser.parse_args()



	rcbuildtest = RcBuildTest()
	rcbuildtest.check_docker_installation()



if __name__ == '__main__':
	main()