import csv

input1 = ["AT1020L-256V1R1","29-08-19","D0-5F-64-5F-29-4A"]
input2 = ["Atoll Solution","AT1020-256","DATE: 20-05-2019","VERSION:V1R1","MACID: D0-5F-64-50-00-8E"]
fileName = 'scanner.csv'
# #case 1
# macid1 = input1[len(input1)-17:]
# print(macid1)
# #case 2
# inp2 = input2.split()
# macid2 = inp2[3]
# print(macid2)

inp2 = input2.split()
for i in inp2:
    MACID = i.replace("-", "")
print(MACID)

if (len(MACID) == 12):
        data = "BV2"+MACID
        with open(fileName, 'a+', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([data])
            print("Record saved " + data)
