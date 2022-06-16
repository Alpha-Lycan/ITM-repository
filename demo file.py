def compute_compound_interest(P, r, n, t):
    return P*(1+(r/n))**(n*t)
compute_compound_interest (10000, 0.07, 2, 5)