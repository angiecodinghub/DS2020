import argparse
import time

def pattern_match(text, pattern):
    # TODO
    # hint: Use dynamic programming to achieve O(T+P)
    #參考網頁: https://leetcode.com/problems/regular-expression-matching/discuss/5684/c-on-space-dp
    row = len(text) + 1
    column = len(pattern) + 1
    graph = [[False for j in range(column)] for j in range(row)]
    graph[0][0] = True
    count = 0
    
    for i in range(1, column):
        if pattern[i-1] != '*':
            count += 1
        else:
            count -= 1
        if i % 2 == 0 and pattern[i-1] == '*' and count == 0:
            graph[0][i] = True
			
   
    for i in range(1, row):
        for j in range(1, column):
            if text[i-1] == pattern[j-1] or pattern[j-1] == '.': # ok
                graph[i][j] = graph[i-1][j-1]
            elif pattern[j-1] == '*': 
                if (text[i-1] == pattern[j-2]) or (pattern[j-2] == '.'):
                    if graph[i][j-2] == True:
                        graph[i][j] = True
                    else:
                        graph[i][j] = graph[i-1][j]
                else:
                    graph[i][j] = graph[i][j-2] # ok
    return graph[row-1][column-1] 

def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip().split()
            text, pattern = line[0], line[1]
            if pattern_match(text, pattern):
                print('1', file=output)
            else:
                print('0', file=output)
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

    ts = time.time()
    main(args.input, args.output)
    te = time.time()
    print('Run Time: {:.5f}s'.format(te-ts))

