def markdown_to_blocks(markdown):
    strings = markdown.split("\n\n")
    
    headed_strings = []
    for i in range(len(strings)):
        split_strings = strings[i].split("#")
        for j in range(1, len(split_strings)-1):
            split_strings[j] = "#" + split_strings[j]
        headed_strings.append(split_strings)
    
    listed_strings = []
    for i in range(len(strings)):
        split_strings = strings[i].split("-")
        for j in range(1, len(split_strings)-1):
            split_strings[j] = "-" + split_strings[j]
        listed_strings.append(split_strings)
    
    rejoined_strings = []
    for i in range(len(strings)):
        split_strings = strings[i].split("\n")
        for j in range(len(split_strings)-1):
            rejoined_strings.append(split_strings[j] + "\n")
        rejoined_strings.append(split_strings[-1])
    
    return rejoined_strings