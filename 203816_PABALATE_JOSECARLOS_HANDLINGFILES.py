products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def main():
    product_draftlist = []
    quantity_draftlist = []
    while True:
        try:
            product,quantity = input("Enter as {product code},{quantity}: ").split(",")
            product_draftlist.append(product)
            quantity_draftlist.append(quantity)
        except:
            break
    convert_quantity = [int(x) for x in quantity_draftlist]
    prodquantlist = [[a,b] for a,b in zip(product_draftlist,convert_quantity)]
    prodquant_dict = {}
    for k,v in prodquantlist:
        prodquant_dict[k] = prodquant_dict.get(k,0) + v
    final_sorted = sorted(map(list, prodquant_dict.items()))
    product_list,quantity_list = map(list, zip(*final_sorted))


    subtotal_list = []
    price_list = []
    name_list=[]
    total = 0
    def get_product(code):
        return products[code]
    for i in range(len(product_list)):
        product_dict = (get_product(product_list[i]))
        name = product_dict["name"]
        name_list.append(name)
    def get_property(code,property):
        return(products[code][property])
    for i in range(len(product_list)):
        product_price = get_property(product_list[i],"price")
        price_list.append(product_price)

    subtotal = [a*b for a,b in zip(price_list,quantity_list)]
    for m in subtotal:
        total += m

    receipt = "\n".join("{}\t{}\t{}\t\t{}".format(w,x,y,z) for w,x,y,z in zip(product_list,name_list, quantity_list, subtotal))
    final_receipt = "==" + "\n" + "CODE\t\tNAME\t\tQUANTITY\tSUBTOTAL" + "\n" + receipt + "\n" + "==" + "\n" + ("Total:\t\t\t\t\t\t" + "{}".format(total))

    with open("receipt.txt","w") as f:
        f.write(final_receipt)

main()
