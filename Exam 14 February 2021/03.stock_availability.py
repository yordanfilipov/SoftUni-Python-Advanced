def stock_availability(inventory_list, action, *args):
    if action == "delivery":
        for arg in args:
            inventory_list.append(arg)
    elif action == "sell":
        args_list = []
        if args:
            for arg in args:
                args_list.append(arg)
            if str(args_list[0]).isdigit():
                sold_boxes = int(args_list[0])
                for i in range(sold_boxes):
                    inventory_list.pop(0)
            else:
                for i in range(len(args_list)):
                    if args_list[i] in inventory_list:
                        inventory_list = [el for el in inventory_list if el != args[i]]
        else:
            inventory_list.pop(0)
    return inventory_list