with open('Codingal.txt')as fp:
    detal = fp.read()

    with open('sample_doc.txt') as fp:
        data = fp.read()

        data+="\n"
        data+=data2

        print("merching two files")
        with open("mergedfile.txt",'w')as fp:
            fp.write (data)


