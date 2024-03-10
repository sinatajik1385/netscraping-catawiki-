from bs4 import BeautifulSoup
import requests
import json

html_text = requests.get("https://www.catawiki.com/en/c/599-gemstones/932-material/62159-tanzanite/").text
soup = BeautifulSoup (html_text , "lxml")
tanzanites = soup.find_all ("article" , class_ = "c-lot-card__container")
for tanzanite in tanzanites :
    if tanzanite :
        tanzanite_title = tanzanite.find ("a" , class_= "c-lot-card").text.strip()
        tanzanite_url = tanzanite.find ("a", class_= "c-lot-card")
        tanzanite_url1 = (tanzanite_url["href"])
        html_text1 = requests.get (tanzanite_url["href"]).text
        soup1 = BeautifulSoup(html_text1 , "lxml")
        seller_description = soup1.find("div" , class_= "lot-info-description__description").text.strip()
        tanzanite_img = soup1.find ("div", class_="be-lot-details__col-main")
        tanzanite_img_src = tanzanite_img.find("img")
        tanzanite_img_src1 = tanzanite_img_src.get("src")
        tracking_number =  soup1.find("p" , class_="be-lot-details-main-section__reference u-typography-label-s u-typography-uppercase u-color-dark-gray u-m-b-xxs").text
        last_bid_ammount = requests.get (tanzanite_url["href"]).text
        response = last_bid_ammount.split(",")
        list1 = list(response)
        list2 = list()
        for i in range(len(list1)):
            if "EUR"  in list1[i]:
                list2.append(list1[i])
        list3 = list2[-1]
        list3 = list3.replace("{" , " ")

        with open(f"tanzanite_number{tracking_number}.txt", "w") as f :
            f.write(f"tracking no : {tracking_number} \n tanzanite Title: \n {tanzanite_title} \n tanzanite URL: \n {tanzanite_url1} \n tanzanite description: \n {seller_description} \n example image : \n {tanzanite_img_src1} \n last bid ammount : \n {list3} \n -------------------------------------------------------")
        print (f'tanzanite number : {tracking_number}')



    else :
        print("no emerald for sale")