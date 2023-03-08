import sys

def main():
    word_counter = {"gold": 0, "silver": 0, "bronze": 0}
    for line in sys.stdin:
        for word in line.split():
            if word == "gold":
                word_counter["gold"] +=1
            if word == "silver":
                word_counter["silver"] +=1
            if word == "bronze":
                word_counter["bronze"] +=1    

    print(word_counter)

if __name__ == "__main__":
    main()