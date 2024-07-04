import sys
from rpn_sim import RpnAstroFiles

def main():
    if len(sys.argv) < 3:
        print("Usage: python run_rpn.py <input files and operations> <output file>")
        sys.exit(1)

    rpn = RpnAstroFiles()
    rpn(sys.argv[1:-1], sys.argv[-1])

if __name__ == '__main__':
    main()
