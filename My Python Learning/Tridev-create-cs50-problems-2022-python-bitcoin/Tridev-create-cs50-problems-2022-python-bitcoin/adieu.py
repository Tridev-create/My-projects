Count = 0
Name_list = {
    'first' : 'Adieu, adieu, to Liesl',
    'second' :'Adieu, adieu, to Liesl and Friedrich',
    'third' : 'Adieu, adieu, to Liesl, Friedrich, and Louisa',
    'forth' : 'Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt',
    'fifth' : 'Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta',
    'sixth' : 'Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta',
    'seventh' : 'Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl'

}

while True:
    try:
        name = input()
        Count += 1

        #if Count == 1:
            #print(f"{Name_list[0]['Adieu']}")


    except EOFError:
        match Count:
            case 1:
                print(Name_list['first'])
            case 2:
                print(Name_list['second'])
            case 3:
                print(Name_list['third'])
            case 4:
                print(Name_list['forth'])
            case 5:
                print(Name_list['fifth'])
            case 6:
                print(Name_list['sixth'])
            case 7:
                print(Name_list['seventh'])
        break

    else:
        match Count:
            case 1:
                print(Name_list['first'])
            case 2:
                print(Name_list['second'])
            case 3:
                print(Name_list['third'])
            case 4:
                print(Name_list['forth'])
            case 5:
                print(Name_list['fifth'])
            case 6:
                print(Name_list['sixth'])
            case 7:
                print(Name_list['seventh'])
