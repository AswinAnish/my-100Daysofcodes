def mulatble(string, position, character):
    l = list(string)
    l[position] = character;
    string = ''.join(l);
    return string

string = input()
position, character = input().split()
new = mulatble(string, int(position), character)
print(new)