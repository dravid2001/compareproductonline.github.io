from django.shortcuts import render
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from .models import Contact
# Searching keywords on which it is working :- iphone 12, hp laptop

# Create your views here.
from django.http import HttpResponse


def index(request):
    try:
        if request.method == "POST":
            searchValue = request.POST.get('main-search-field', ' ')
            print(searchValue)

            product_name = request.POST.get('mainSearchField', '')
            

            # For Amazon

            def get_url(search_item):
                temp = "https://www.amazon.com/s?k={}&currency=INR&ref=nb_sb_noss_2"
                search_item = search_item.replace(" ", "+")
                return temp.format(search_item)

            driver = webdriver.Chrome(
            #     # executable_path="D:\mini projects\chromedriver_win32\chromedriver")
                executable_path="D:\college work\major_project\chromedriver")
            url = get_url(searchValue)
            driver.get(url)
            
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        
            result = soup.find_all(
                'div', {"data-component-type": "s-search-result"})
            for item in result:
                
                try:
                    pre_final_heading = item.h2.a.span.text
                    heading = pre_final_heading.strip()
                    pre_price = item.find("span", {"class": "a-offscreen"})
                    price = pre_price.string
                    hyperlink = url
                    amazon_image_url = item.find('img')['src']
                    break
                except:
                    print("There is an error")

            # For Flipcart

            def get_flipcart_url(search_item):
                temp = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
                search_item = search_item.replace(" ", "+")
                return temp.format(search_item)

            flipcart_url = get_flipcart_url(searchValue)
            flip_driver = webdriver.Chrome(
                executable_path="D:\college work\major_project\chromedriver")
            flip_driver.get(flipcart_url)

            flip_soup = BeautifulSoup(flip_driver.page_source, "html.parser")
            flip_result = flip_soup.find_all(
                "a", {"class": "_1fQZEK", "rel": "noopener noreferrer"})
            for flip_item in flip_result:
               
                try:
                    flip_pre_heading = flip_item.find("div", {"class": "_4rR01T"})
                    flip_heading = flip_pre_heading.string
                    flip_price = flip_item.find(
                        "div", {"class": "_30jeq3 _1_WHN1"}).string
                    flip_link = flipcart_url
                    flip_image_url = flip_item.find('img')['src']
                    break
                except:
                    print("There is an error in flipkart scraping code.")

            # For RelianceDigital

            def get_RelianceDigital_url(search_item):
                temp = "https://www.reliancedigital.in/search?q={}:relevance"
                search_item = search_item.replace(" ", "+")
                return temp.format(search_item)

            relianceDigital_url = get_RelianceDigital_url(searchValue)
            reliance_driver = webdriver.Chrome(
                executable_path="D:\college work\major_project\chromedriver")
            reliance_driver.get(relianceDigital_url)

            
            reliance_soup = BeautifulSoup(
                reliance_driver.page_source, "html.parser")

            reliance_result = reliance_soup.find_all(
                "div", {"class": "sp__product"})

            for reliance_item in reliance_result:
                try:
                    reliance_pre_heading = reliance_item.find(
                        "p", {"class": "sp__name"})
                    reliance_heading = reliance_pre_heading.string
                    reliance_pre_price = reliance_item.find(
                        "span", {"class": "sc-bxivhb"}).find_all("span")[1]
                    reliance_price = reliance_pre_price.string
                    reliance_image_url = reliance_item.find('img')['src']

                    # Reliance stores its image in a static file not in a url form so we can use same image as we use in amazon.
                    break

                except:
                    print(
                        "There is an error. Please remove error first and try again later.")

            param = {
                'heading': heading, 'price': price, 'link': hyperlink, 'flip_heading': flip_heading, 'flip_price': flip_price, 'flip_link': flip_link,
                'amazon_image_url': amazon_image_url, 'flip_image_url': flip_image_url, 'reliance_heading': reliance_heading,
                'reliance_price': reliance_price, 'relianceDigital_url': relianceDigital_url
            }
            return render(request, "compare/productView.html", param)
        return render(request, "compare/index.html")

    except:
        return render(request,"compare/error_page.html")  


def chatbot(request):

    return render(request, "compare/chatbot.html")


def contact(request):
    # return HttpResponse("This is the Contact Us page of compare app.")
    print("Yahan tak to puhan raha hai.***************")
    if request.method == "GET":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        query = request.POST.get('query', '')

       
        contact = Contact(name=name, email=email, phone=phone,
                          address=address, city=city, state=state, zip=zip, query=query)
        print(contact)
        contact.save()

    return render(request, "compare/contact.html")


def about(request):
    return render(request, "compare/about.html")
