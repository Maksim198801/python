# {sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}}
import re


filename = "input.txt"
sphere = dict()
with open(filename, 'r') as file:
    data = file.readlines()

data = re.split(',{}: ', data[0])

if __name__ == '__main__':
    print(data)
    print(len(data))
