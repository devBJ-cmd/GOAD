import argparse
import os
def extract_user(input_file,output_file):
    start=0
    username_start=0
    with open(input_file,"r") as inputs , open(output_file,"w") as outputs:
        for line in inputs:
            if(line.find("-Username-") != -1):
                start=1
                username_start=line.find("-Username")
            if(start==1):
                n=0    
                n=line.find(' ',username_start)
                username=line[username_start:n]
                if(username != '-Username-' and username != '[*]'):
                    outputs.write(username+'\n')
def main():
    parser=argparse.ArgumentParser(description="extract users from netexec input_file and output file that just contains users")
    parser.add_argument("-input_file" ,help="input file that retrived users from netexec")
    parser.add_argument("-output_file" ,help="output file that only contains users to use with impacket tools")
    args=parser.parse_args()
    if(os.path.isfile(args.input_file)):
       extract_user(args.input_file,args.output_file)
       print(f'check {args.output_file}')
if __name__ == "__main__":
       main()