def main():
        current  = 0
        content = [int(x) for x in "156794823"]
        highest = max(content)
        for i in range(highest+1, 1000001):
            content.append(i)
        original_length = len(content)
        lowest = min(content)
        highest = max(content)
        turn = 0
        while turn < 10000000:
            removed1 = content[current + 1 % 1000000]
            removed2 = content[current + 2 % 1000000]
            removed3 = content[current + 3 % 1000000]
            del(content[current + 1 % 1000000])
            del(content[current + 1 % 1000000])
            del(content[current + 1 % 1000000])
            destination = content[current] - 1
            if destination < lowest:
                destination = highest
            while destination == removed1 or destination == removed2 or destination == removed3:
                destination -= 1
                if destination < lowest:
                    destination = highest

            destindex = content.index(destination)
            destindex += 1
            content.insert(destindex, removed3)
            content.insert(destindex, removed2)
            content.insert(destindex, removed1)
            current = current + 1 % 1000000
            turn += 1


        content *= 2
        print(content[content.index(1) + 1] * content[content.index(1) + 2])

main()
