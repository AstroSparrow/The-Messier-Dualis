from ai import call_gpt
import time
import csv

Main = {}

print("Welcome to the Database Population Code!")
time.sleep(1)

def DataSaving(Desc_Dict):
    filename = "Database_Descriptions.csv"
    csvfile = open(filename, mode = 'w', newline = '')
    writer_lambda = csv.writer(csvfile)
    writer_lambda.writerow(Desc_Dict.keys())
    writer_lambda.writerow(Desc_Dict.values())

    print(f"The Dictionary has been Succesfully Saved as {filename}!")
    csvfile.close()

while(True):
    #print("1. Populate the Years of Discovery to the Database")
    #time.sleep(0.5)
    #print("2. Populate the Names of the Discoverers to the Database")
    #time.sleep(0.5)
    #print("2. Populate Fun Facts of the Objects to the Databse")
    #time.sleep(0.5)
    print("1. Populate the Descriptions of the Objects to the Database")
    time.sleep(0.5)
    print("2. Populate the Fun Facts of the Objects to the Database")
    time.sleep(0.5)
    print("3. Exit the Program")
    time.sleep(1)

    inp = int(input("Please enter what you wanna do?: "))
    if (inp == 1):
        time.sleep(0.6)
        print("Alright! Starting the Database Population Code for Messier Objects Descriptions!")
        time.sleep(0.5)
        for i in range (1, 111):
            response = call_gpt(f"Give me a Nice, Crisp 40 word Description for Messier {i} please (Maintain a Tone of Enthusiasim and make the Descriptions Engaging to read. Also put effort into sounding Human rather than AI. Also put great effort into ensuring that the Descriptions are factaully correct)")
            Main[f"Messier {i}"] = response
            print(f"Messier {i} has been added to the Dictionary!")
        time.sleep(1)
        print("All the Messier Object's Information has been added to the Dictionary!")
        time.sleep(1)
        print(Main)
        time.sleep(4)
        DataSaving(Main)
        
    elif (inp == 2):
        time.sleep(0.6)
        print("Alright! Starting the Database Population Code for Messier Objects Fun Facts!")
        time.sleep(0.5)
        for i in range (1, 111):
            response = call_gpt(f"Give me a Short Fun Fact for Messier {i} please (Maintain a Tone of Enthusiasim and make the Facts Engaging to read. Also put effort into sounding Human rather than AI)")
            Main[f"Messier {i}"] = response
            print(f"Messier {i} has been added to the Dictionary!")
        time.sleep(1)
        print("All the Messier Object's Information has been added to the Dictionaries!")
        time.sleep(0.4)
        print(Main)
        time.sleep(4)
    
    elif (inp == 3):
        print("Thanks a lot for using my Program!")
        time.sleep(1)
        print("Made with Love by Taha :D")
        time.sleep(1)
        print("Okiee Biee!")
        time.sleep(0.4)
        break
exit()