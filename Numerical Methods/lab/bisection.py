def bisection(
        f, 
        xl: float,
        xu: float,
        es: float = 0.005,
        max_iter: int = 10000
    ) -> float:

    # 1. Check if the initial interval brackets a root
    if f(xl) * f(xu) > 0:
        print("No sign change detected. A root might not exist in this interval.")
        return None

    # 2. Check if one or two endpoint is already the exact root
    elif f(xl) * f(xu) == 0:

        if f(xl) == 0 and f(xu) == 0:
            print(f"Roots are {xl} and {xu}")
            return xl, xu

        elif f(xl) == 0:
            print(f"Root is {xl}")
            return xl

        else:
            print(f"Root is {xu}")
            return xu

    else:

        xm_old = None
        ea = float('inf')

        for i in range(max_iter):
            xm_new = (xl + xu) / 2.0

            if xm_old is not None and xm_new != 0:
                ea = abs((xm_new - xm_old) / xm_new) * 100.0
        
            # Stop if error is small enough or if you hit the exact root
            if ea < es or f(xm_new) == 0:
                print("tolerance achieved or exact root found...")
                return xm_new

            if f(xl) * f(xm_new) < 0:
                xu = xm_new
            else:
                xl = xm_new

            xm_old = xm_new

        print("iterations completed...")
        return xm_new


def f(x):
    return x + 1

ans = bisection(f, -1000, 1000)
print(ans)

