def main():
    name = str(input("Type: "))
    first(name)



def first(s):
    if s == 'name':
        for c in s:
            print(s)
            break

    if s == 'firstName':
         for c in s:
            print("first_name")
            break

    if s == 'preferredFirstName':
         for c in s:
            print("preferred_first_name")
            break



main()