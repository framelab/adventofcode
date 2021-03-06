#!/usr/bin/python
# http://adventofcode.com/2017/day/9

def main():
    input_file = open("dec09a_input.txt")
    stream = input_file.read()

    depth = 0
    garbage_count = 0
    in_garbage = False
    ignore_next = False

    for char in stream:
        if ignore_next:
            ignore_next = False
            continue
        
        if char == "!":
            ignore_next = True

        if in_garbage:
            if char == ">":
                in_garbage = False
            elif not ignore_next:
                garbage_count += 1    
        else:
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            elif char == "<":
                in_garbage = True

    print(garbage_count)

main()
