import threading

def find_even_numbers():
    even_numbers = [num for num in range(30, 51) if num % 2 == 0]
    print("Even numbers:", even_numbers)

def find_odd_numbers():
    odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
    print("Odd numbers:", odd_numbers)

if __name__ == "__main__":
    even_thread = threading.Thread(target=find_even_numbers)
    odd_thread = threading.Thread(target=find_odd_numbers)
    
 
    even_thread.start()
    odd_thread.start()
    
  
    even_thread.join()
    odd_thread.join()

    print("Main thread exiting.")
