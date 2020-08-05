import argparse

class Heap_Node():
    def __init__(self, key):
        self.value = key

    def __repr__(self):
        return 'Heap_Node({})'.format(str(self.value))

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value > other.value:
            return False
        else:
            return True

class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def __repr__(self):
        return str(self.heapList)

    def insert(self, node): # node : Heap_Node(key)
        #TODO
        self.heapList.append(node)
        self.currentSize += 1
        current = self.currentSize
        temp = 0
        while current > 1:
            if self.heapList[current].__lt__(self.heapList[current//2]): # current <= upper
                temp = self.heapList[current//2]
                self.heapList[current//2] = self.heapList[current]
                self.heapList[current] = temp
                current = current // 2
            else:
                break

    def delMin(self):
        #TODO
        pop = 0
        if self.currentSize > 0:
            pop = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.heapList.pop()   
            self.currentSize -= 1
        current = 1
        min_index = 1
        while 2*current <= self.currentSize: # not leaf
            if 2*current == self.currentSize: # only one node
                min_index = 2*current
            else:
                if self.heapList[2*current + 1].__gt__(self.heapList[2*current]): # [2*c+1] > [2*c]
                    min_index = 2*current
                else:
                    min_index = 2*current + 1
            if self.heapList[current].__gt__(self.heapList[min_index]): # current > upper
                temp = self.heapList[min_index]
                self.heapList[min_index] = self.heapList[current]
                self.heapList[current] = temp
                current = min_index
            else:
                break
        return pop

def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    minheap = MinHeap()
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.lower() == 'print':
                print(minheap, file=output)
            else:
                operation = line.split(' ')[0]
                if operation.lower() == 'insert':
                    key = int(line.split(' ')[1])
                    minheap.insert(Heap_Node(key))
                elif operation.lower() == 'delmin':
                    print(minheap.delMin(), file=output)
                else:
                    raise NotImplementedError
    output.close()

if __name__ == '__main__':
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input')
    parser.add_argument('--output', default='./output')
    args = parser.parse_args()

    main(args.input, args.output)


