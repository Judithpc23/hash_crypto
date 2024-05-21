import multiprocessing
import config
from worker import hash_check

def main():
    line_count = 14344392  # Asegúrate de que este es el número correcto de líneas en tu archivo
    chunk_size = line_count // config.num_workers

    result_queue = multiprocessing.Queue()
    stop_event = multiprocessing.Event()
    processes = []

    for i in range(config.num_workers):
        start = i * chunk_size
        end = start + chunk_size if i < config.num_workers - 1 else line_count
        p = multiprocessing.Process(target=hash_check, args=(start, end, result_queue, stop_event))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not result_queue.empty():
        print(result_queue.get())

if __name__ == '__main__':
    main()