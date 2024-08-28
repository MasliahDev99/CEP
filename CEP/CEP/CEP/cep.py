import argparse
import os
import sys
from arguments import get_arguments,handle_command


if __name__ == '__main__':
    args = get_arguments()
    handle_command(args)
    
    
