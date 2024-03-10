from bs4 import BeautifulSoup
import requests
import json
#import googletrans
#from googletrans import Translator
#translator = Translator()

html_text = requests.get("https://www.catawiki.com/en/c/599-gemstones/932-material/62144-opal/").text
soup = BeautifulSoup (html_text , "lxml")
opals = soup.find_all ("article" , class_ = "c-lot-card__container")
for opal in opals :
    if opal :
        opal_title = opal.find ("a" , class_= "c-lot-card").text.strip()
        opal_url = opal.find ("a", class_= "c-lot-card")
        opal_url1 = (opal_url["href"])
        html_text1 = requests.get (opal_url["href"]).text
        soup1 = BeautifulSoup(html_text1 , "lxml")
        seller_description = soup1.find("div" , class_= "lot-info-description__description").text.strip()
        opal_img = soup1.find ("div", class_="be-lot-details__col-main")
        opal_img_src = opal_img.find("img")
        opal_img_src1 = opal_img_src.get("src") 
        tracking_number =  soup1.find("p" , class_="be-lot-details-main-section__reference u-typography-label-s u-typography-uppercase u-color-dark-gray u-m-b-xxs").text
        last_bid_ammount = requests.get (opal_url["href"]).text
        response = last_bid_ammount.split(",")
        list1 = list(response)
        list2 = list()
        for i in range(len(list1)):
            if "EUR"  in list1[i]:
                list2.append(list1[i])
        list3 = list2[-1]
        list3 = list3.replace("{" , " ")

        with open(f"oapl_number{tracking_number}.txt", "w") as f :
            f.write(f"tracking no : {tracking_number} \n opal Title: \n {opal_title} \n spal URL: \n {opal_url1} \n opal description: \n {seller_description} \n example image : \n {opal_img_src1} \n last bid ammount : \n {list3} \n -------------------------------------------------------")
        print (f'opal number : {tracking_number}')



    else :
        print("no emerald for sale")