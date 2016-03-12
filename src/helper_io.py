def read_input(file):
    '''
    Return input from the file f in a tuple:
    (W, H , [(w_1, h_1, v_1), ..., (w_n, h_n, v_n)])
    '''
    lines = file.split('\n')

    if len(lines) < 1:
        raise ValueError('Need at least one line')

    # Line 0
    dimensions = lines[0].split()
    if len(dimensions) != 2:
        raise ValueError('Bad input format on line 1')
    W = int(dimensions[0])
    H = int(dimensions[1])

    # Rectangles information
    rectangles = []
    for i, line in enumerate(lines[1:]):
        r = line.split()
        if len(r) != 3:
            raise ValueError('Bad input format on line {}'.format(i+1))
        rectangle = (int(r[0]), int(r[1]), float(r[2]))
        rectangles.append(rectangle)

    return (W, H, rectangles)
