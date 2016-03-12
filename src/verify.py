import sys
import subprocess


def validate_output(output):
    lines = output.split('\n')

    if len(lines) < 2:
        print 'Need at least two lines'
        return False

    try:
        total = float(lines[0])
    except:
        print 'Badly fomatted line:', lines[0]
        return False

    try:
        w, h = [float(x) for x in lines[1].split()]
    except:
        print 'Badly fomatted line:', lines[1]
        return False

    for line in lines[2:]:
        nums = line.split()

        try:
            x1, y1, x2, y2, v = [float(x) for x in nums]
        except:
            print 'Badly formatted line:', line
            return False

        if x1 >= x2 or y1 >= y2:
            print 'Invalid rectangle coordinates:', x1, y1, x2, y2
            return False

    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python verify.py your_progam.py'
        sys.exit()
        
    with open('rand0.in') as f:
        output = subprocess.check_output([sys.executable, sys.argv[1]], stdin=f).strip()

    if validate_output(output):
        print 'Output had correct format :)'
        print 'But maybe it will fail our real tests...'
    else:
        print 'Output had wrong format :('
