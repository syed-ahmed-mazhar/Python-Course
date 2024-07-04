def main():
    rpn = Rpn()
    
    # Test cases for Rpn
    print(rpn([2, 2, '+']))  # Expected output: 4
    print(rpn([3, 4, 5, '*', '+']))  # Expected output: 23
    print(rpn([2, 'sqrt']))  # Expected output: 1.414...

    # Test cases for RpnStr
    rpn_str = RpnStr()
    print(rpn_str('2 2 +'))  # Expected output: 4
    print(rpn_str('3 4 5 * +'))  # Expected output: 23
    print(rpn_str('2 sqrt'))  # Expected output: 1.414...

    # Note: Actual test cases for RpnAstroFiles require FITS files.
    # Example test (requires actual FITS files):
    # rpn_astro = RpnAstroFiles()
    # rpn_astro(['files/flat_c.fits', 'files/bias_c.fits', '-', 'flat_image_c.fits'])

if __name__ == '__main__':
    main()
