# imported the requests library
import urllib.request
import re

#create dictionary for patterns
thisdict = {
    "Caribbean_folk_art_with_ackee_and_palm_leaf_on_navy_background" : "Ackee Fruit with Island Leaves Navy",
    "Caribbean_folk_art_with_coconut_hibiscus_flower_mango_fish_and_watermelon_on_navy_background" : "Fish with Watermelon Navy",
    "Caribbean_folk_art_with_coconut_flowers_turtles_and_starfish_on_orange_background" : "Coconut with Flowers and Turtles Orange",
    "Caribbean_folk_art_for_Jamaica_Independence_day" : "Jamaica Independence day",
    "Caribbean_folk_art_with_fish_fruits_house_and_drums_on_green_background" : "Fish Fruit and Drums Green",
    "Childrens_novelty_geometric_windowpane_shape_pattern_on_yellow_background" : "Stripe Pattern Yellow",
    "Nautical_beach_seamless_pattern_theme_with_beach_chair_and_great_egret_bird_on_white_background" : "Beach Chair and Great Egret Bird",
    "Childrens_novelty_pattern_with_small_polka_dots_and_herringbone_pattern_on_turquoise_background" : "Small Polka Dots and Herringbone Turquoise", 
    "Colorful_blossoming_budding_flowers_seamless_pattern_white_print" : "Blossoming Budding Flowers White",
    "Childrens_novelty_penguins_in_checker_pattern_on_green_background" : "Penguin Green",
    "Childrens_novelty_shapes_with_baby_tiger_and_polka_dots_pattern_on_yellow_background" : "Cat Polka Dot Yellow",
    "Childrens_novelty_geometric_animal_faces_pattern_on_soft_lavender_background" : "Penguin With Cat Purple",
    "Childrens_novelty_shapes_with_penguin_and_herringbone_pattern_on_white_background" : "Penguin With Stripes Yellow",
    "Childrens_novelty_shapes_with_duck_pattern_on_white_background" : "Duck With Diamond White",
    "Nautical_theme_seamless_pattern_with_crab_variety_on_tan_background" : "Crab Feast Tan",
    "Nautical_theme_seamless_pattern_with_storks_and_seashells_on_nude_background" : "Storks and Shells Nude Srock",
    "Nautical_theme_seamless_pattern_with_sailboat_fishes_and_stork_on_sea_blue_background" : "Sailboat Fish Rope and Stork Sea Blue",
    "Nautical_theme_seamless_pattern_with_buckets_shells_and_crabs_on_white_background" : "Bucket Shell and Crabs White",
    "Nautical_beach_seamless_pattern_theme_with_multi_seashells_on_sky_blue_background" : "Multitude of Shells Sky Blue",
    "Nautical_beach_seamless_pattern_theme_with_seashells_beach_chairs_buckets_and_crabs_on_taupe_background" : "Beach Chair Bucket and Shell Taupe",
    "Nautical_beach_seamless_pattern_theme_with_beach_chair_and_great_egret_bird_on_tan_background" : "Beach Chair with Stork Tan",
    "Blossoming_tropical_color_flowers_seamless_pattern_on_hot_pink_print" : "Hot Pink Flower",
    "Colorful_blossoming_budding_flowers_seamless_pattern_white_print" : "White Original",
    "Blossoming_multi_layer_flowers_seamless_pattern_on_white_background" : "Blossoming White Buds with Shrubs",
    "Holiday_2020_pearls_ribbons_and_pine_cones_on_yellow_orange_background" : "Pearls Ribbons Pine Cones Yellow Orange",
    "Holiday_2020_pine_cones_and_shrub_berries_on_deep_green_background" : "Pine Cones and Shrub Berries Deep Green",
    "Holiday_2020_pearls_ribbons_and_gift_box_on_dark_green_background" : "Pearls Ribbons and Gift Box Dark Green",
    "Holiday_2020_pearls_shrubs_with_berries_and_leaves_on_green_background" : "Pearls Shrub Berry Leaves Green",
    "Blossoming_multi_layer_flowers_seamless_pattern_on_pink_background" : "Pink Buds with Shrubs",
    "Holiday_2020_ribbons_and_bows_and_gift_box_lime_green_stock" : "Ribbons and Bows and Gift Box Lime Green",
    "Holiday_pines_with_pearls_seamless_pattern_on_tan_background" : "Pearls and Flat Pine Tan",
    "Blossoming_multi_layer_flowers_seamless_pattern_on_deep_sea_green_print" : "Deep Sea Green",
    "Blossoming_flowers_with_petals_seamless_pattern_on_dark_blue_print" : "Dark Blue",
    "Blossoming_subtle_flowers_seamless_repeat_pattern_on_blue_print" : "Blue Cotton",
    "Vibrant_floral_on_vines_seamless_pattern_on_red_print" : "Flowers on Vines Red",
    "Colorful_blossoming_flowers_seamless_pattern_white_print" : "", #(missing)
    "Colorful_blossoming_flowers_seamless_pattern_beige_print" : "Beige Stock",
    "Colorful_blossoming_flowers_seamless_pattern_sky_blue_print" : "", #(missing)
    "Classic_abstract_geometric_diamond_check_on_peach_background" : "Diamond Checkers Peach",
    "Classic_abstract_geometric_multi_stripe_diamond_on_white_background" : "Multi Diamond Stripe White",
    "Classic_abstract_geometric_rectangle_bracket_on_beige_background" : "Multi Square Bracket Beige",
    "Abstract_geometric_pattern_with_polka_dots__on_mint_background" : "Polkadots Mintgreen",
    "Abstract_geometric_pattern_with_stars_on_green_background" : "Multi Diamond Stripe White",
    "Classic_shape_seamless_plaid_pattern_blue_background_print" : "Plaid Sky Blue",
    "Classic_shape_seamless_diamond_pattern_hot_pink_background_print" : "Mini Diamond Check Hot Pink",
    "Classic_navy_polka_dots_seamless_pattern_print" : "Dots Navy Blue with White",
    "Classic_blue_polka_dots_seamless_pattern_print" : "Dots Blue With Pink",
    "Classic_white_chevron_shape_seamless_pattern_print" : "Wide Chevron White",
    "Classic_terracotta_chevron_shape_seamless_pattern_print" : "Chevron Terracotta",
    "Classic_shape_seamless_boxy_diamond_pattern_pink_background" : "Boxy Diamond Pink",
    "Classic_plum_slanted_rectangle_seamless_print" : "Rectangle Plum with Pink",
    "Classic_shape_seamless_pattern_caramel_background_print" : "Boxy Diamond Caramel",
    "Classic_black_slanted_rectangle_seamless_pattern_print" : "Slanted Rectangle Black with Blue",
    "yellow_lemon_types_seamless_pattern" : "Yellow Lemon Variety",
    "white_lemon_blueberries_herbs_and_cutting_boards_seamless_pattern" : "White Lemon and Berries",
    "white_cutting_boards_with_herbs_seamless_pattern" : "White Cutting Boards",
    "Violet_leaves_seamless_pattern" : "Violet Leaves",
    "Light_green_lemon_blueberry_and_cutting_board_seamless_pattern" : "Turquoise Lemon and Berries",
    "Purple_lemon_blueberries_with_flowers_seamless_pattern" : "Purple Bluberry Lemon",
    "Pink_blueberry_variety_seamless_pattern" : "Pink Bluberries",
    "Pink_overlapping_wildflowers_seamless_pattern" : "Mauve Pink Flowers",
    "Light_green_lemon_outline_seamless_pattern" : "Light Green Lemon",
    "Hunter_green_wild_flowers_seamless_pattern" : "Hunter Green Leaves Flowers",
}

imagesdict = {}

# request the input of the url to parse
print('Enter the URL:')
x = input()
print('Extracting Source code from: ' + x) 

# pull the source code from the page
opener = urllib.request.FancyURLopener({})
url = x
webpage = opener.open(url)
content = webpage.read()

# test print of code that was extracted
#print(content)

####### create and fill the files #######
# create a html file to save the code
html_file = open("source.html", "w")
html_file.write(str(content) + "\n")
html_file.close()

# create a txt file to save links for available products
links_file = open("links.txt", "w")
link_list = re.findall('<a data-testid="available-product" href="(.+?)" element="a" class="styles__link--3QJ5N">', str(content))
# test print of list of links
#print(*link_list)
links = '\n'.join(map(str,link_list))
links_file.write(links)
links_file.close()

# create a txt file to save product names for available products
names_file = open("names.txt", "w")
names_list = re.findall('<span class="styles__box--2Ufmy styles__text--23E5U styles__display6--3wsBG styles__nowrap--33UtL styles__display-block--3kWC4" data-testid="ds-box">(.+?)</span>', str(content))
collection_name = re.findall('<title data-react-helmet="true">(.+?) by RoseTextileArt | Redbubble</title>', str(content))
# test print of list of names
#print(*names_list)
#print(d[0])
names = '\n'.join(map(str,names_list))
names_file.write(names)
names_file.close()

# create a txt file to save product prices for available products
prices_file = open("prices.txt", "w")
prices_list = re.findall('<span class="styles__box--2Ufmy styles__text--23E5U styles__display5--2KoKo styles__display-block--3kWC4" data-testid="ds-box"><span>(.+?)</span>', str(content))
# test print of list of names
#print(*prices_list)
prices = '\n'.join(map(str,prices_list))
prices_file.write(prices)
prices_file.close()

# create a txt file to save product prices for available products
images_file = open("images.txt", "w")
images_list = re.findall('{"previewTypeId":"default","url":"(.+?)","__typename":"inventory_Preview"},', str(content))
# test print of list of names
#print(*images_list)
images = '\n'.join(map(str,images_list))
images_file.write(images)
images_file.close()



####### replace the unnecessary substrings #######
repl1 = [sub.replace('.', '') for sub in collection_name]
repl2 = [sub.replace(',', '') for sub in repl1]
repl6 = [sub.replace(' ', '_') for sub in repl2]
repl7 = [sub.replace("'", '') for sub in repl6]
collection_fix = [sub.replace('&#x27;', "") for sub in repl7]

images_fix = [sub.replace('{{%2F}}', '/') for sub in images_list]

repl3 = [sub.replace('\\xc2\\xbe ', '') for sub in names_list]
repl4 = [sub.replace('(', '') for sub in repl3]
repl5 = [sub.replace(')', '') for sub in repl4]
names_fix = [sub.replace(' ', '_') for sub in repl5]

for j in range(len(images_fix)):
    if( 'ur,mouse_pad_small_flatlay_prop' in str(images_fix[j]) ):
        imagesdict.update({'Mouse Pad' : str(images_fix[j])})
    if( 'ur,pet_bowl_product_front_small' in str(images_fix[j]) ):
        imagesdict.update({'Pet Bowl' : str(images_fix[j])})
    if( 'ssrco,bucket_hat' in str(images_fix[j]) ):
        imagesdict.update({'Bucket Hat' : str(images_fix[j])})
    if( 'ssrco,dad_hat' in str(images_fix[j]) ):
        imagesdict.update({'Dad Hat' : str(images_fix[j])})
    if( 'ur,pet_bandana_small_flatlay_srp' in str(images_fix[j]) ):
        imagesdict.update({'Pet Bandana' : str(images_fix[j])})
    if( 'ssrco,baseball_cap' in str(images_fix[j]) ):
        imagesdict.update({'Baseball Cap' : str(images_fix[j])})
    if( 'ssrco,active_tshirt' in str(images_fix[j]) ):
        imagesdict.update({'Active T-Shirt' : str(images_fix[j])})
    if( 'ra,raglan' in str(images_fix[j]) ):
        imagesdict.update({'Baseball Sleeve T-Shirt' : str(images_fix[j])})
    if( 'ssrco,classic_tee' in str(images_fix[j]) ):
        imagesdict.update({'Classic T-Shirt' : str(images_fix[j])})
    if( 'ssrco,lightweight_hoodie' in str(images_fix[j]) ):
        imagesdict.update({'Lightweight Hoodie' : str(images_fix[j])})
    if( 'ssrco,lightweight_sweatshirt' in str(images_fix[j]) ):
        imagesdict.update({'Lightweight Sweatshirt' : str(images_fix[j])})
    if( 'ra,longsleeve' in str(images_fix[j]) ):
        imagesdict.update({'Long Sleeve T-Shirt' : str(images_fix[j])})
    if( 'ssrco,long_t_shirt' in str(images_fix[j]) ):
        imagesdict.update({'Long T-Shirt' : str(images_fix[j])})
    if( 'ssrco,mens_premium_t_shirt' in str(images_fix[j]) ):
        imagesdict.update({'Premium T-Shirt' : str(images_fix[j])})
    if( 'ssrco,mhoodie' in str(images_fix[j]) ):
        imagesdict.update({'Pullover Hoodie' : str(images_fix[j])})
    if( 'ra,sweatshirt' in str(images_fix[j]) ):
        imagesdict.update({'Pullover Sweatshirt' : str(images_fix[j])})
    if( 'ssrco,racerback' in str(images_fix[j]) ):
        imagesdict.update({'Racerback Tank Top' : str(images_fix[j])})
    if( '/ctkr,' in str(images_fix[j]) ):
        imagesdict.update({'Sleeveless Top' : str(images_fix[j])})
    if( 'ssrco,slim_fit_t_shirt' in str(images_fix[j]) ):
        imagesdict.update({'Essential T-Shirt' : str(images_fix[j])})
    if( 'ra,tank' in str(images_fix[j]) ):
        imagesdict.update({'Tank Top' : str(images_fix[j])})
    if( 'ssrco,triblend_tee' in str(images_fix[j]) ):
        imagesdict.update({'Tri-blend T-Shirt' : str(images_fix[j])})
    if( 'ra,vneck' in str(images_fix[j]) ):
        imagesdict.update({'V-Neck T-Shirt' : str(images_fix[j])})
    if( 'ssrco,mhoodiez' in str(images_fix[j]) ):
        imagesdict.update({'Zipped Hoodie' : str(images_fix[j])})
    if( 'ra,relaxed_fit' in str(images_fix[j]) ):
        imagesdict.update({'Fitted Scoop T-Shirt' : str(images_fix[j])})
    if( 'ra,womens_tshirt' in str(images_fix[j]) ):
        imagesdict.update({'Fitted T-Shirt' : str(images_fix[j])})
    if( 'ra,fitted_v_neck' in str(images_fix[j]) ):
        imagesdict.update({'Fitted V-Neck T-Shirt' : str(images_fix[j])})
    if( 'ur,leggings_womens_front' in str(images_fix[j]) ):
        imagesdict.update({'Leggings' : str(images_fix[j])})
    if( 'pencil_skirt' in str(images_fix[j]) ):
        imagesdict.update({'Mini Skirt' : str(images_fix[j])})
    if( 'rco,womens_premium_t_shirt,womens' in str(images_fix[j]) ):
        imagesdict.update({'Premium Scoop T-Shirt' : str(images_fix[j])})
    if( 'ra,fitted_scoop' in str(images_fix[j]) ):
        imagesdict.update({'Relaxed Fit T-Shirt' : str(images_fix[j])})
    if( '/st,small' in str(images_fix[j]) ):
        if 'Sticker' not in  imagesdict.keys():
            imagesdict.update({'Sticker' : str(images_fix[j])})
        if 'Glossy Sticker' not in imagesdict.keys():
            imagesdict.update({'Glossy Sticker' : str(images_fix[j])})
    if( 'pd,x750,macbook_air_13-pad' in str(images_fix[j]) ):
        imagesdict.update({'Laptop Skin' : str(images_fix[j])})
    if( '/ls,' in str(images_fix[j]) ):
        imagesdict.update({'Laptop Sleeve' : str(images_fix[j])})
    if( 'tst,small,' in str(images_fix[j]) ):
        imagesdict.update({'Transparent Sticker' : str(images_fix[j])})
    if( 'mwo,x1000,ipad_2_skin-pad' in str(images_fix[j]) ):
        imagesdict.update({'iPad Skin' : str(images_fix[j])})
    if( 'mwo,x1000,ipad_2_snap-pad' in str(images_fix[j]) ):
        imagesdict.update({'iPad Snap Case' : str(images_fix[j])})
    if( 'mwo,x1000,iphone_6_skin-pad' in str(images_fix[j]) ):
        imagesdict.update({'iPhone Skin' : str(images_fix[j])})
    if( 'icr,iphone_14_snap' in str(images_fix[j]) ):
        imagesdict.update({'iPhone Snap Case' : str(images_fix[j])})
    if( 'icr,iphone_14_soft' in str(images_fix[j]) ):
        imagesdict.update({'iPhone Soft Case' : str(images_fix[j])})
    if( 'icr,iphone_14_tough,' in str(images_fix[j]) ):
        imagesdict.update({'iPhone Tough Case' : str(images_fix[j])})
    if( 'wallet,1000x,iphone_6s_wallet-pad' in str(images_fix[j]) ):
        imagesdict.update({'iPhone Wallet' : str(images_fix[j])})
    if( 'mwo,1000x,samsung_galaxy_s5_skin-pad' in str(images_fix[j]) ):
        imagesdict.update({'Samsung Galaxy Skin' : str(images_fix[j])})
    if( 'icr,samsung_galaxy_s21_snap' in str(images_fix[j]) ):
        imagesdict.update({'Samsung Galaxy Snap Case' : str(images_fix[j])})
    if( 'icr,samsung_galaxy_s21_soft' in str(images_fix[j]) ):
        imagesdict.update({'Samsung Galaxy Soft Case' : str(images_fix[j])})
    if( 'icr,samsung_galaxy_s21_tough' in str(images_fix[j]) ):
        imagesdict.update({'Samsung Galaxy Tough Case' : str(images_fix[j])})
    if( '/gbra,' in str(images_fix[j]) ):
        imagesdict.update({'Art Board Print' : str(images_fix[j])})
    if( '/aps,' in str(images_fix[j]) ):
        imagesdict.update({'Art Print' : str(images_fix[j])})
    if( '/mp,' in str(images_fix[j]) ):
        if 'Canvas Print' not in  imagesdict.keys():
            imagesdict.update({'Canvas Print' : str(images_fix[j])})
        if 'Metal Print' not in  imagesdict.keys():
            imagesdict.update({'Metal Print' : str(images_fix[j])})
    if( '/fp,' in str(images_fix[j]) ):
        imagesdict.update({'Framed Art Print' : str(images_fix[j])})
    if( '/pp,' in str(images_fix[j]) ):
        imagesdict.update({'Photographic Print' : str(images_fix[j])})
    if( '/paperpc,' in str(images_fix[j]) ):
        imagesdict.update({'Postcard' : str(images_fix[j])})
    if( '/poster,' in str(images_fix[j]) ):
        imagesdict.update({'Poster' : str(images_fix[j])})
    if( '/abf,' in str(images_fix[j]) ):
        imagesdict.update({'Acrylic Block' : str(images_fix[j])})
    if( '/clkf,' in str(images_fix[j]) ):
        imagesdict.update({'Clock' : str(images_fix[j])})
    if( 'ur,coaster_pack_4_flatlay' in str(images_fix[j]) ):
        imagesdict.update({'Coasters Set of 4' : str(images_fix[j])})
    if( 'ur,comforter_top_king' in str(images_fix[j]) ):
        imagesdict.update({'Comforter' : str(images_fix[j])})
    if( '/dc,' in str(images_fix[j]) ):
        imagesdict.update({'Duvet Cover' : str(images_fix[j])})
    if( 'ur,shower_curtain_closed' in str(images_fix[j]) ):
        imagesdict.update({'Shower Curtain' : str(images_fix[j])})
    if( '/throwpillow,small' in str(images_fix[j]) ):
        imagesdict.update({'Throw Pillow' : str(images_fix[j])})
    if( '/drawstring_bag,' in str(images_fix[j]) ):
        imagesdict.update({'Drawstring Bag' : str(images_fix[j])})
    if( '/tb,' in str(images_fix[j]) ):
        imagesdict.update({'All Over Print Tote Bag' : str(images_fix[j])})
    if( '/mug,standard,' in str(images_fix[j]) ):
        imagesdict.update({'Classic Mug' : str(images_fix[j])})
    if( 'ssrco,tote,cotton' in str(images_fix[j]) ):
        imagesdict.update({'Cotton Tote Bag' : str(images_fix[j])})
    if( 'ur,fitted_mask_flatlay_fitted_regular' in str(images_fix[j]) ):
        imagesdict.update({'Fitted 3-Layer' : str(images_fix[j])})
    if( 'ur,pin_large_front' in str(images_fix[j]) ):
        imagesdict.update({'Pin' : str(images_fix[j])})
    if( '/scarf,' in str(images_fix[j]) ):
        imagesdict.update({'Scarf' : str(images_fix[j])})
    if( '/mug,tall,' in str(images_fix[j]) ):
        imagesdict.update({'Tall Mug' : str(images_fix[j])})
    if( '/mug,travel,' in str(images_fix[j]) ):
        imagesdict.update({'Travel Coffee Mug' : str(images_fix[j])})
    if( 'ur,water_bottle_metal_lid_on' in str(images_fix[j]) ):
        imagesdict.update({'Water Bottle' : str(images_fix[j])})
    if( '/pr,' in str(images_fix[j]) ):
        imagesdict.update({'Zipper Pouch' : str(images_fix[j])})
    if( '/papergc,' in str(images_fix[j]) ):
        imagesdict.update({'Greeting Card' : str(images_fix[j])})
    if( '/hj,' in str(images_fix[j]) ):
        imagesdict.update({'Hardcover Journal' : str(images_fix[j])})
    if( '/sn,x1000-pad,' in str(images_fix[j]) ):
        imagesdict.update({'Spiral Notebook' : str(images_fix[j])})
    if( '/mo,small,flatlay' in str(images_fix[j]) ):
        imagesdict.update({'Magnet' : str(images_fix[j])})
    if( 'ssrco,chiffon_top' in str(images_fix[j]) ):
        imagesdict.update({'Chiffon Top' : str(images_fix[j])})
    if( '/ur,mask_flatlay_front' in str(images_fix[j]) ):
        imagesdict.update({'Flat Mask' : str(images_fix[j])})
    if( '/ur,kids_mask' in str(images_fix[j]) ):
        imagesdict.update({'Kids Mask' : str(images_fix[j])})
    if( '/ur,apron_realistic_flatlay' in str(images_fix[j]) ):
        imagesdict.update({'Apron' : str(images_fix[j])})
    if( '/ur,dog_mat_flatlay_srp' in str(images_fix[j]) ):
        imagesdict.update({'Dog Mat' : str(images_fix[j])})
    if( '/ur,cat_mat_flatlay_srp' in str(images_fix[j]) ):
        imagesdict.update({'Cat Mat' : str(images_fix[j])})
    if( '/ur,bathmat_flatlay_small' in str(images_fix[j]) ):
        imagesdict.update({'Bath Mat' : str(images_fix[j])})
    if( '/aldr,' in str(images_fix[j]) ):
        imagesdict.update({'A-Line Dress' : str(images_fix[j])})
    if( '/gtdr,' in str(images_fix[j]) ):
        imagesdict.update({'Graphic T-Shirt Dress' : str(images_fix[j])})
    if( '/ur,mounted_print_wood_portrait_small_front' in str(images_fix[j]) ):
        imagesdict.update({'Wood Mounted Print' : str(images_fix[j])})
    if( '/ur,mounted_print_canvas_portrait_small_front' in str(images_fix[j]) ):
        imagesdict.update({'Canvas Mounted Print' : str(images_fix[j])})
    if( '/tapestry,' in str(images_fix[j]) ):
        imagesdict.update({'Tapestry' : str(images_fix[j])})
    if( '/ur,blanket_medium_bed' in str(images_fix[j]) ):
        imagesdict.update({'Throw Blanket' : str(images_fix[j])})
    if( '/ur,backpack_front' in str(images_fix[j]) ):
        imagesdict.update({'Backpack' : str(images_fix[j])})
    if( '/ur,desk_mat_flatlay_prop' in str(images_fix[j]) ):
        imagesdict.update({'Desk Mat' : str(images_fix[j])}) 
    if( '/ur,socks_flatlay_medium' in str(images_fix[j]) ):
        imagesdict.update({'Socks' : str(images_fix[j])})
    if( '/gptr,' in str(images_fix[j]) ):
        imagesdict.update({'Graphic T-Shirt' : str(images_fix[j])})
    if( '/ur,duffle_bag_large_front' in str(images_fix[j]) ):
        imagesdict.update({'Duffle Bag' : str(images_fix[j])})

# create a html file to automate coding
final_html = open("final.html", "w")

#Create lists for clothing Categories
Masks = ["Flat_Mask", "Kids_Mask", "Fitted_3-Layer"]
Hats = ["Bucket_Hat", "Dad_Hat", "Baseball_Cap"]
T_Shirts = ["Active_T-Shirt", "Baseball_Sleeve_T-Shirt", "Classic_T-Shirt", "Long_Sleeve_T-Shirt", "Long_T-Shirt", "Premium_T-Shirt", "Sleeveless_Top", "Essential_T-Shirt", "Tri-blend_T-Shirt", "V-Neck_T-Shirt", "Fitted_Scoop_T-Shirt", "Fitted_T-Shirt", "Fitted_V-Neck_T-Shirt", "Premium_Scoop_T-Shirt", "Relaxed_Fit_T-Shirt", "Chiffon_Top", "Graphic_T-Shirt"]
Tank_Tops = ["Racerback_Tank_Top", "Tank_Top"]
Clothing_Oneoffs = ["Apron", "Leggings", "Mini_Skirt", "Socks"]
Hoodies = ["Lightweight_Hoodie", "Pullover_Hoodie", "Zipped_Hoodie"]
Sweatshirts = ["Lightweight_Sweatshirt", "Pullover_Sweatshirt"]
Dresses = ["A-Line_Dress", "Graphic_T-Shirt_Dress"]

#Create lists for Computer and Phone Accessories Categories
Computer = ["Mouse_Pad", "Laptop_Skin", "Laptop_Sleeve"]
iPad = ["iPad_Skin", "iPad_Snap_Case"]
iPhone = ["iPhone_Skin", "iPhone_Snap_Case", "iPhone_Soft_Case", "iPhone_Tough_Case", "iPhone_Wallet"]
Samsung = ["Samsung_Galaxy_Skin", "Samsung_Galaxy_Snap_Case", "Samsung_Galaxy_Soft_Case", "Samsung_Galaxy_Tough_Case"]

#Create lists for Pet Accessories Categories
Pet = ["Pet_Bandana", "Pet_Bowl", "Dog_Mat", "Cat_Mat"]

#Create lists for Stickers Categories
Stickers = ["Sticker", "Glossy_Sticker", "Transparent_Sticker"]

#Create lists for Wall Art Categories
Wall_Art = ["Art_Board_Print", "Art_Print", "Canvas_Print", "Framed_Art_Print", "Metal_Print", "Photographic_Print", "Poster", "Wood_Mounted_Print", "Canvas_Mounted_Print", "Tapestry"]

#Create lists for Stationery & Office Categories
Stationery = ["Postcard", "Greeting_Card", "Hardcover_Journal", "Spiral_Notebook", "Desk_Mat"]

#Create lists for Home & Living Categories
Home_OneOffs = ["Water_Bottle", "Throw_Pillow", "Coasters_Set_of_4", "Clock", "Acrylic_Block"]
Bedding = ["Comforter", "Duvet_Cover", "Throw_Blanket"]
Mugs = ["Classic_Mug", "Tall_Mug", "Travel_Coffee_Mug"]
Bathroom = ["Bath_Mat", "Shower_Curtain"]

#Create lists for Accessories Categories
Bags = ["Drawstring_Bag" , "All_Over_Print_Tote_Bag", "Cotton_Tote_Bag", "Backpack", "Duffle_Bag"]
Accessories_Oneoffs = ["Pin", "Scarf", "Zipper_Pouch", "Magnet"]

for i in range(len(link_list)):
  if( names_fix[i] in Masks ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Clothing Masks ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Hats ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Clothing Hats ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in T_Shirts ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Clothing Shirts T-Shirts ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Tank_Tops ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Clothing Shirts Tank_Tops ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Clothing_Oneoffs ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Clothing ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Hoodies ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Clothing Hoodies ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Sweatshirts ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Clothing Sweatshirts ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Computer ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Computer_and_Phone_Accessories Computer_Accessories ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in iPad ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Computer_and_Phone_Accessories iPad_Accessories ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in iPhone ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Computer_and_Phone_Accessories iPhone_Accessories ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Samsung ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Computer_and_Phone_Accessories Samsung_Accessories ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Pet ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Pet_Supplies ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Stickers ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Stickers ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Wall_Art ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Wall_Art ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Stationery ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Stationery_and_office ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Home_OneOffs ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Home_and_Living ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Bedding ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Home_and_Living Bedding ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Mugs ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Home_and_Living Mugs ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Bathroom ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Home_and_Living Bathroom_Accessories ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Bags ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Accessories Bags ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  elif( names_fix[i] in Accessories_Oneoffs ):
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' Accessories ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  else:
    final_html.write('\t\t\t<div class="col-sm-6 col-md-3 col-lg-3 ' + collection_fix[0] + ' ' + names_fix[i] + '">\n\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t<div class="hover-bg">')
  final_html.write('<a href="' + link_list[i] + '" data-lightbox-gallery="gallery1">\n\t\t\t\t\t\t<div class="hover-text">\n\t\t\t\t\t\t\t')
  final_html.write('<h4>' + thisdict[collection_fix[0]] + ' ' + repl5[i] + '</h4>\n\t\t\t\t\t\t\t')
  final_html.write('<small>Redbubble<br><b>' + prices_list[i] + '</b></small>\n\t\t\t\t\t\t</div>\t\t\n\t\t\t\t\t')
  final_html.write('<img src=' + imagesdict[str(repl5[i])] + ' class="img-responsive"></a>')
  final_html.write('</div>\n\t\t\t\t</div>\n\t\t\t</div>\n')

final_html.close()

k = input("press close to exit")