from bisect import bisect_left


def main():
    L, Q = map(int, input().split())

    d = [0, L]

    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            idx = bisect_left(d, x)
            d.insert(idx, x)
        else:
            idx = bisect_left(d, x)
            print(d[idx] - d[idx-1])

if __name__ == "__main__":
    main()