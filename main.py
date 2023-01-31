import csv 
import docx

ticker=0
with open('donor_list.csv', newline= '') as f:
    reader = csv.reader(f)

    doc = docx.Document("Donation Receipt.docx")

    for row in reader:
        donors = list(row)
        #name the charecteristic of the words from the list
        last_name= donors[0]
        first_name= donors[1]
        address= donors[2]
        donation= donors[3]
        #split the address into two parts
        address =address.split(",", 1)
        addressp1=address[0]
        print("")
        addressp2=address[1]
        #for testing
        print(address[1])
        print("")
        print(addressp1)
        print(addressp2)

        #this is where every thing is in the section of the word document, run is used to specify the text in a paragraph
        doc.paragraphs[5].text= first_name, last_name #first name
        doc.paragraphs[6].text= addressp1#address
        doc.paragraphs[7].text=addressp2 #address part2
        doc.paragraphs[10].runs[0].text= "Dear", first_name,"," #first
        doc.paragraphs[12].runs[1].text= "$",donation #donations

        #this saves the document with the name of the person
        doc.save(f"{first_name}{last_name}.docx")
        print(first_name, last_name, address, donation)
        
        ticker=ticker+1 #to make sure the number of people is correct


print("number of people are:", ticker)#this is used to make sure the number of people is correct




