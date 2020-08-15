expected_links_list = ["/lighting", "/tools", "/atm-kiosk", "/patriot-items", "/refurbished-casino-parts", "/seating",
                       "patriotgaming.com", "/aboutus", "/contact", "/resources", "/checkout/cart", "/inv", "/gaming,"
                           "/shop-by-game", "/repair-services", "/refurbished-casino-parts", "/bill-validators",
                           "/touch-screens-monitors", "/printers", "/gaming", "/cleaning-maintenance", "/electronic-components",
                           "/electrical-tripp-lite", "/table-game-products", "/player-tracking", "/oem-product-showcase",
                           "/personal-protection-equipment", "patriotgaming.com", "/aboutus", "/contact", "/resources",
                           "/contact", "/terms-and-conditions", "/sitemap"]

list_numbers = ["patriotgaming.com", "/aboutus", "/contact", "/resources", "/checkout/cart", "/inv", "/gaming,"
                           "/shop-by-game", "/repair-services", "/refurbished-casino-parts", "/bill-validators",
                           "/touch-screens-monitors", "/printers1", "/aboutus", "/aboutus", "/aboutus"]

for link in list_numbers:

    if link in expected_links_list:
         print(expected_links_list.index(link), link)
         expected_links_list.remove(link)

    else:
        print(f"{link} not found")

print(expected_links_list)