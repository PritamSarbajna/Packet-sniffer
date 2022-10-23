#!/usr/bin/env python3

print("""
______          _        _        _____       _  __  __          
| ___ \        | |      | |      /  ___|     (_)/ _|/ _|         
| |_/ /_ _  ___| | _____| |_     \ `--. _ __  _| |_| |_ ___ _ __ 
|  __/ _` |/ __| |/ / _ \ __|     `--. \ '_ \| |  _|  _/ _ \ '__|
| | | (_| | (__|   <  __/ |_     /\__/ / | | | | | | ||  __/ |   
\_|  \__,_|\___|_|\_\___|\__|    \____/|_| |_|_|_| |_| \___|_|   
                                                                 
                                                                 
""")
 
from scapy.all import *
from argparse import ArgumentParser
import argparse


class Sniffer:
	
	def __init__(self,args):
		self.args=args


	def __call__(self,packet):
		if self.args.verbose:
			packet.show()
		else:
			print(packet.summary())


	def run_forever(self):
		sniff(iface=self.args.interface, prn=self, store=0, filter="tcp")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-v','--verbose', default=False, action='store_true', help='You can talk to me more ')
	parser.add_argument('-i', '--interface', type=str, required=True, help='Please provide network interface name: ')

	args = parser.parse_args()
	sniffer = Sniffer(args)
	sniffer.run_forever()
