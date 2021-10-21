def d_to_b(n, sgn_len=1, exp_len=8, mant_len=23):
    n = struct.unpack('I', struct.pack('f', n))[0]
    return '{:032b}'.format(n)

def b_to_d(n, sgn_len=1, exp_len=8, mant_len=23):
    if len(n) !=32:
        return "error"

    sign = int(n[0],2)
    exponent_raw = int(n[1:9],2)
    mantissa = int(n[9:32],2)

    sign_mult = 1
    if sign == 1:
        sign_mult = -1

    if exponent_raw == 2 ** exp_len - 1:  # Could be Inf or NaN
        if mantissa == 2 ** mant_len - 1:
            return float('nan')  # NaN

        return sign_mult * float('inf')  # Inf

    exponent = exponent_raw - (2 ** (exp_len - 1) - 1)

    if exponent_raw == 0:
        mant_mult = 0  # Gradual Underflow
    else:
        mant_mult = 1

    for b in range(mant_len - 1, -1, -1):
        if mantissa & (2 ** b):
            mant_mult += 1 / (2 ** (mant_len - b))
    
    
    return sign_mult * (2 ** exponent) * mant_mult



if __name__ == '__main__':
    ## 有些數字轉二進位會出現誤差
    ## 因為超過16777215(2**24-1)就溢位了，frac的部分無法存超過23bit
    ## 16777215 = (24bit) 去掉第0個bit = 23bit
    import struct
    m = 1234
    b = d_to_b(m)
    d = b_to_d(b)
    print(m, b, d)
    
    
