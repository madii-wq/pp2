with open('row.txt', 'r', encoding='utf-8') as f:
    with open('copied.txt', 'w', encoding='utf-8') as fs:
        fs.write(f.read())
