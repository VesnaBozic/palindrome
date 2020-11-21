from stack import Stack
from queue import Queue
def main():
    stack1 = Stack()
    queue = Queue()

    sentence = input("Enter a sentence to check for palidrom: ")

    sentence2 = sentence.replace(" ","").lower()
    
    index = 0
    while index < len(sentence2):
        letter = sentence2[index]
        stack1.push(letter)
        index +=1

    print(stack1)

    indexs = 0
    while indexs < len(sentence2):
        letter = sentence2 [indexs]
        queue.enqueue(letter)
        indexs +=1

    print(queue)
    i=0
    condition = True
    while i < len(stack1):
        if stack1.pop() == queue.dequeue():
            condition = True
        else: 
            condition = False
            if condition == False:
                print("Sentence is not palindrome!")
                break
    if condition == True:
        print("Sentence is palindrome.")

    



main()