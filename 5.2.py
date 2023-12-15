import Bio.SeqIO

for_search_file, where_to_search_file = input().split(' ')

for_search_file = open(for_search_file)
where_to_search_file = open(where_to_search_file)
for_search =  str(next(Bio.SeqIO.parse(for_search_file, "fasta")).seq)
where_to_search = str(next(Bio.SeqIO.parse(where_to_search_file, "fasta")).seq)


def PrefixFunction(string):
    Prefixes = [0 for _ in range(len(string))]
    j = 0
    i = 1
    while i < len(string):
        if string[i] == string[j]:
            Prefixes[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                Prefixes[i] = 0
                i += 1
            else:
                j = Prefixes[j-1]
    return(Prefixes)


all_hail = for_search + '$' + where_to_search

counter = 0
prefixes = PrefixFunction(all_hail)
for _ in range(len(prefixes)):
    if prefixes[_] == len(for_search):
        print(_ - 2 * len(for_search) + 1)
        counter += 1
if counter == 0:
    print('-1')
