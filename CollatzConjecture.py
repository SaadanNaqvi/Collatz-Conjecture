import random

def collatz(num):
    sequence = [num]
    while(num!=1):
        if (num!=1):
            if(num%2==0):
                num=num/2
            else:
                num=3*num+1
        sequence.append(num)
    return sequence

def main():
    iterations = int(input("How many random Collatz Sequences do you want? "))
    for i in range(iterations-1):
        number = random.randint(1, 400)
        print("Collatz  Sequence for "+str(number)+" : ")
        print(collatz(number))


if __name__ == "__main__":
    main()