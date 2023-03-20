# python3

def parallel_processing(n, m, data):
    out = []
    times = [0 for _ in range(n)]
    for d in data:
        i = times.index(min(times))
        out.append((i, times[i]))
        times[i] += d
    return out


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
