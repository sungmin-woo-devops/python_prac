class MyThread(threading.Thread):
    def run(self):
        print(f'{self.getName()} started!')
        time.sleep(2);
        print(f'{self.getName()} finished!')
    def main():
        for i in range(3):
            # Instantiate a thread and pass a identifier
            my_thread = MyThread(name=f'Thread-{i}')
            my_thread.run()
            # Sleep for half seconds before start another
            time.sleep(0.5) if __name__ == '__main__':
main()
