def GeneralEquation(x_1, y_1, x_2, y_2, x_3, y_3):
    # Ax+By+C=0
    global A, B, C


    A = y_2 - y_1
    B = x_1 - x_2
    C = x_2 * y_1 - x_1 * y_2
    k = -1 * A / B
    b = -1 * C / B
    print('{}x + {}y +{} = 0'.format(A, B, C))

    if (A * x_3 + C) / B == -y_3:
        print('correct')
        return True
    else:
        print('wrong')
        return False

