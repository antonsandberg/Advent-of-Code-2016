import time

def process_data(FILENAME):
    with open(FILENAME) as f:
        data = f.read().split()
    return data 


def main():
    return





if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()


    print(f'Time taken {t2-t1:.6f}s')