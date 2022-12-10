# author: Benicio Alonzo
# CS 110 - dog that watches anime
# abstract: a launcher that calls dog_image.get_pic  and Quote.get_quote

import Quote # Proxy CLass
import Dog_image #Proxy Class

def main():
    #Proxy Class
    dog_API = Dog_image.Dog_image()
    dog_results = dog_API.get_pic()
    
    quote_API = Quote.Quote()
    quote_results = quote_API.get_quote()
    
    
main()
print("Project End")