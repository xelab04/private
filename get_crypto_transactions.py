import httplib2
from bs4 import BeautifulSoup, SoupStrainer

def i_to_j(string):
    accepted = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return_array = []
    for i in range(len(string)):
        if string[i:i+7] == "Balance":
            print(string[i:i+100])
            new_string = string[i:i+100]

            for j in range(100):
                if new_string[j:j+4] == "</b>":

                    for k in range(j+4,100):
                        if new_string[k] in accepted:
                            print(new_string[j+4:k])
                            return new_string[j+4:k]

#<span class="hash-tag text-truncate" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="0x908127a767e76788dc1f582d8928675eff244434">0x908127a767e76788dc1f582d8928675eff244434</span>

http = httplib2.Http()
status,response = http.request("https://etherscan.io/address/0x908127A767E76788Dc1F582D8928675efF244434")


balance = i_to_j(str(response).strip(" "))
print("")
usual_file = "/home/alex/Desktop/usual.txt"
with open(usual_file,"r") as file:
    lines = file.readlines()
    old_balance = lines[0].strip("\n")

    print(old_balance,balance)
    if balance == old_balance:
        print("SAME")

if old_balance != balance:
    with open(usual_file,"w") as file:
        file.writelines([balance])
