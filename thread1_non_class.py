import threading
import timedef run(name):
    print(f'Thread-{name} started!')
    time.sleep(2)
    print(f'Thread-{name} finished!')def main():
    print(f'Main: Before starting thread')
    for i in range(3):
        # Instantiate a thread and pass a identifier
        my_thread = threading.Thread(target=run, args=[i], daemon=False)
        my_thread.start()
    #my_thread.join()
    print(f'Main: After finishing thread')if __name__ == '__main__':
    main()
