def get_int_list():
    return list(map(int, input().split()))

n, D, H = get_int_list()

# Base: Assume you do not need to climb - what is equation of line
m_base = H/D
line = lambda x, m, c: m*x + c

min_climb = 0.0

for i in range(n):
    d_i, h_i = get_int_list()

    # Do not climb if h_i is below y_base(hi)
    if h_i < line(d_i, m_base, 0):
        continue
    else:
        # We need to climb - minimum is line passing through obstacle
        m_new = (H - h_i) /(D - d_i)
        c_new = h_i - m_new*d_i

        climb = line(0, m_new, c_new)
        min_climb = climb if min_climb < climb else min_climb




print(min_climb)
