import requests
import urllib.request
from bs4 import BeautifulSoup as bs


def get_info(uri):
    r = urllib.request.Request(uri)
    html = urllib.request.urlopen(r).read()
    soup = bs(html, 'html.parser')
    soup = str(soup)
    soup = soup[2:]
    soup = soup[:-2]
    
    # print(soup.split(',"'))
    # return str(soup)
    return soup.split(',"')

def get_auctions_from_player(api, uuid):
    return get_info(f"https://api.hypixel.net/skyblock/auction?key={api}&player={uuid}")

api = "2c10d5fc-f22f-4730-af44-9a24e2852b40"
player_uuid = "70ab84a8daaf40e095c4123746630df9"

# pprint(get_auctions_from_player(api, player_uuid))

def getUserid(username):
    req = requests.get("https://api.mojang.com/users/profiles/minecraft/%s" %username)
    data = req.text
    idc = data.find('"id":')
    data = data[(idc+5):]
    data = data.replace('"',' ').replace('}'," ")
    userid = data[1:]

    return userid

def count_str_in_list(list, str):
    count = 0

    for i in list:
        if str in i:
            count += 1

    return count

def find_dic(dic, str, key, num):
    dic[key] = dic[key][(dic[key].find(str))+num:-2]
    return dic

def return_item_info(item):
    # del item[0]
    item = str(item).split("', '")

    if count_str_in_list(item, 'timestamp') >= 1:
        dic = {
            "_id" : item[0],
            "uuid" : item[1],
            "auctioneer" : item[2],
            "profile_id" : item[3],
            "coop" : item[4],
            "start" : item[5], 
            "end" : item[6], 
            "item_name" : item[7],
            "item_lore" : item[8],
            "extra" : item[9],
            "category" : item[10],
            "tier" : item[11],
            "starting_bid" : item[12],
            # "data" : item[14],
            "claimed" : item[15],
            "claimed_bidders" : item[16],
            "hightest_bid_amount" : item[18],
            "bidder" : item[20],
            "amount" : item[22],
            "timestamp" : item[23]}
        
        
        dic['_id'] = dic['_id'][(dic['_id'].find('_id":'))+6:-1]
        dic['uuid'] = dic['uuid'][(dic['uuid'].find('uuid":'))+7:-1]
        dic['auctioneer'] = dic['auctioneer'][(dic['auctioneer'].find('auctioneer":'))+13:-1]
        dic['profile_id'] = dic['profile_id'][(dic['profile_id'].find('profile_id":'))+13:-1]
        dic = find_dic(dic, 'coop":', 'coop', 8)
        dic['start'] = dic['start'][(dic['start'].find('start":'))+7:]
        dic['end'] = dic['end'][(dic['end'].find('end":'))+5:]
        dic['item_name'] = dic['item_name'][(dic['item_name'].find('item_name":'))+12:-1]
        dic['item_lore'] = dic['item_lore'][(dic['item_lore'].find('item_lore":'))+12:-1]
        dic['extra'] = dic['extra'][(dic['extra'].find('extra":'))+8:-1]
        dic['category'] = dic['category'][(dic['category'].find('category":'))+11:-1]
        dic['tier'] = dic['tier'][(dic['tier'].find('tier":'))+7:-1]
        dic['starting_bid'] = dic['starting_bid'][(dic['starting_bid'].find('starting_bid":'))+14:]
        # dic = find_dic(dic, 'data":', 'data', 7)
        dic['claimed'] = dic['claimed'][(dic['claimed'].find('claimed":'))+9:]
        dic = find_dic(dic, 'claimed_bidders":', 'claimed_bidders', 19)
        dic['hightest_bid_amount'] = dic['hightest_bid_amount'][20:]
        dic['bidder'] = dic["bidder"][9:-1]
        dic['amount'] = dic['amount'][8:]
        dic["timestamp"] = dic["timestamp"][11:-5]

        return dic

    else:
        dic = {
            "_id" : item[0],
            "uuid" : item[1],
            "auctioneer" : item[2],
            "profile_id" : item[3],
            "coop" : item[4],
            "start" : item[5], 
            "end" : item[6], 
            "item_name" : item[7],
            "item_lore" : item[8],
            "extra" : item[9],
            "category" : item[10],
            "tier" : item[11],
            "starting_bid" : item[12],
            # "data" : item[14],
            "claimed" : item[15],
            "claimed_bidders" : item[16],
            "hightest_bid_amount" : item[18]}
        
        dic['_id'] = dic['_id'][(dic['_id'].find('_id":'))+6:-1]
        dic['uuid'] = dic['uuid'][(dic['uuid'].find('uuid":'))+7:-1]
        dic['auctioneer'] = dic['auctioneer'][(dic['auctioneer'].find('auctioneer":'))+13:-1]
        dic['profile_id'] = dic['profile_id'][(dic['profile_id'].find('profile_id":'))+13:-1]
        dic = find_dic(dic, 'coop":', 'coop', 8)
        dic['start'] = dic['start'][(dic['start'].find('start":'))+7:]
        dic['end'] = dic['end'][(dic['end'].find('end":'))+5:]
        dic['item_name'] = dic['item_name'][(dic['item_name'].find('item_name":'))+12:-1]
        dic['item_lore'] = dic['item_lore'][(dic['item_lore'].find('item_lore":'))+12:-1]
        dic['extra'] = dic['extra'][(dic['extra'].find('extra":'))+8:-1]
        dic['category'] = dic['category'][(dic['category'].find('category":'))+11:-1]
        dic['tier'] = dic['tier'][(dic['tier'].find('tier":'))+7:-1]
        dic['starting_bid'] = dic['starting_bid'][(dic['starting_bid'].find('starting_bid":'))+14:]
        dic['claimed'] = dic['claimed'][(dic['claimed'].find('claimed":'))+9:]
        dic = find_dic(dic, 'claimed_bidders":', 'claimed_bidders', 19)
        dic['hightest_bid_amount'] = dic['hightest_bid_amount'][20:]
        

        return dic



