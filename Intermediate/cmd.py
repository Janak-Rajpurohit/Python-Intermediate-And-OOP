import argparse
import sys
def cal(arg):
	if arg.o == "add":
		return arg.x +arg.y
p=argparse.ArgumentParser()
p.add_argument("-x",type=float, default=1.0,help="write -x _number_ ")
p.add_argument("-y",type=float, default=1.0,help="write -y _number_ ")
p.add_argument("-o",type=str, default="add",help="write -o _operation_ ")

arg=p.parse_args()
sys.stdout.write(str(cal(arg)))