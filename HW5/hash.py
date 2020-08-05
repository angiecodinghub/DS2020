import argparse

class singly_node():
    def __init__(self, item = None):
        self.value = item
        self.right = None
        
class hash_table():
    # TODO
    def __init__(self):
        self.table = [None] * 1001
    def insert(self, item):
        number = self.carry(item)
        spot = number % 1001
        inserting = singly_node(item)
        if self.table[spot] is not None:
            inserting.right = self.table[spot]
        self.table[spot] = inserting
    def look(self, k):
        if int(k) >= 1001:
            return 'Null'
        if self.table[int(k)] is not None:
            string = ''
            pointer = self.table[int(k)]
            while pointer != None:
                string += pointer.value
                string += ' '
                pointer = pointer.right
            return string
        else:
            return 'Null'
    def delete(self, n):
        number = self.carry(n)
        spot = number % 1001
        if self.table[spot] is None:
            return 'Error'
        else:
            if self.table[spot].value == n:
                self.table[spot] = self.table[spot].right
            else:
                now = self.table[spot].right
                previous = self.table[spot]
                while now != None:
                    if now.value == n:
                        previous.right = now.right
                        return
                    else:
                        now = now.right
                        previous = previous.right
                return 'Error'
    def search(self, n):
        number = self.carry(n)
        spot = number % 1001
        if self.table[spot] is None:
            return 'No'
        else:
            pointer = self.table[spot]
            while pointer != None:
                if pointer.value == n:
                    return 'Yes'
                else:
                    pointer = pointer.right
            return 'No'
    def carry(self, item):
        length = len(item)
        integer = 0
        for i in range(length):
            integer += 27**(length-1-i)*(ord(item[i].lower())-96)
        return integer       
        		
def main(input_path, output_path):
    table = hash_table()
    output = open(output_path, 'w')
    # TODO
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            #while line.lower() != 'end':
            operation = line.split(' ')[0]
            if operation.lower() == 'insert':
                item = line.split(' ')[1]
                table.insert(item)
            elif operation.lower() == 'look':
                k = line.split(' ')[1]
                writing = table.look(k)     
                print(writing, file = output)
            elif operation.lower() == 'delete':
                n = line.split(' ')[1]
                writing = table.delete(n)
                if writing:
                    print(writing, file = output)
            elif operation.lower() == 'search':
                n = line.split(' ')[1]
                writing = table.search(n)
                print(writing, file = output)
            elif operation.lower() == 'end':
                output.close()
                break
            else:
                raise NotImplementedError    

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