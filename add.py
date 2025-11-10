def strip(a):
    return a.strip()

def setting():
    print("Choose an Option:")
    print("1. Edit Shop Name")
    print("2. Delete Products")
    print("3. Back")
    choice = input()
    if choice == "1":
        print("Enter Shop Name:")
        file = open("name1.txt", "w+")
        file.write(input())
        file.close()
        print("Shop Name Changed!\n")
    elif choice == "2":
        print("Enter Product Code to be deleted:")
        file = open("p_list", "r")
        x = file.readlines()
        file.close()
        file = open("p_list", "w+")
        new = []
        sk = input()
        for i in x:
            if sk.upper() != strip(i):
                new.append(i)
        file.writelines(new)
        file.close()
        print("Deleted Successfully!")
    elif choice == "3":
        return

def invoice():
    c = open("invoice#.txt", "a")
    c.close()
    f = open("p_list", "r")
    p_list = f.readlines()
    f.close()
    p1 = []
    for i in p_list:
        p1.append(strip(i))
    c = open("invoice#.txt", "r")
    x = c.read()
    c.close()
    c = open("invoice#.txt", "w")
    if len(x) == 0:
        c.write("1")
        counter = 1
    else:
        counter = int(x)
        counter += 1
        c.write(str(counter))
    c.close()
    from datetime import datetime
    time = datetime.now()
    tim = str(time)
    timee = strip(tim)
    file = open("name1.txt")
    name = file.read().upper()
    file.close()
    namep = ""
    for i in name:
        namep += i
    namep += " "
    ly = []
    ny = []
    a = 1
    print("Available Product Codes : ", end="")
    m = 0
    for i in p1:
        m += 1
        if m == len(p1):
            print(i)
        else:
            print(i, end=", ")
    while a == 1:
        print("Enter Product code:")
        p = input()
        if p.upper() not in p1:
            print("No Such Product Found! Please Try Again")
            continue
        ly.append(p.upper())
        print("Quantity:")
        while True:
            try:
                c = float(input())
                ny.append(c)
                break
            except:
                print("Quantity can only be Integer or Float! Please Add Again")
        print("Enter 1 to Stop adding product or press any other key to add more")
        if input() == "1":
            print("Enter Discount(in %)")
            dis = float(input())
            break

    p_list = []
    for i in range(len(ly)):
        p_list.append(ly[i])
    maxi = 0
    s_list = []
    a_list = []
    for i in p_list:
        x = ""
        for j in range(0, len(i)):
            x = x + i[j]
        file = open(x + ".txt")
        file.readline()
        s_list.append(len(file.readline()))
        a_list.append(x)
        file.close()
    x = open("invoice.txt", "w+")
    if max(s_list) < 12:
        maxi = 12
    else:
        maxi = max(s_list)
    l = " " + "S.no" + "  " + "Product Name" + " " * (maxi - 10) + "Price" + " " * 4 + "GST(%)" + "  " + "Quantity" + " " + "Total"
    f = len(l)
    z = int((f - len(namep)) / 2)
    v = int((f - len("INVOICE")) / 2)
    w = int((f - len(timee)) / 2)
    s = int((f - 9 - len(str(counter))) / 2)
    j = " " * z
    x.write(j + namep + "\n")
    x.write(" " * v + "INVOICE" + "\n\n")
    x.write(" " * w + timee + "\n")
    x.write(" " * s + "Invoice#" + " " + str(counter) + "\n\n\n")
    x.write(l + "\n\n")
    t = 0
    disc = 0
    for i in p_list:
        t += 1
        s_no = t
        code = i
        file = open(i + ".txt", "r")
        code = strip(file.readline())
        name = strip(file.readline())
        price = int(strip(file.readline()))
        gst = int(strip(file.read()))
        qt = (ny[t-1])
        total = round((price * float(qt) + price * gst * float(qt) / 100), 2)
        x.write(" " + str(s_no) + ")." + " " * (4 - len(str(s_no))) + name +
                " " * (maxi + 2 - len(name)) + str(price) + " " * (9 - len(str(price))) +
                str(gst) + " " * (8 - len(str(gst))) + str(qt) + " " * (10 - len(str(qt))) +
                str(total) + "\n")
        disc += total
        file.close()
    d = disc * dis * 0.01
    x.write("\n")
    x.write(" " * (len(l) - len("Discount:")) + " Discount: " + str(round(d, 2)) + "\n")
    x.write(" " * (len(l) - len("Net Payable:")) + " Net Payable: " + str(round(disc - d, 2)) + "\n\n\n\n")
    x.write("*. This is a Computer Generated Invoice and does not require Signature.\n")
    x.write("*. Return/Replacement is not allowed under any circumstances.\n")
    x.write("\nThanks for shopping with us")
    x.close()
    print("Invoice Saved Successfully in Invoice.txt at Desktop.")
    print("Net Payable : ", round((disc - d), 2))
    print("Press Any Key to continue!")
    input()

def add():
    name = input("Enter name of Product: ")
    while True:
        try:
            s = int(input("Enter Selling Price(Excluding GST): "))
            g = int(input("Enter GST (in %): "))
            n1 = input("Choose a Product code(Any alpha numeric character(Except spaces) to be used for Product Indentification): ")
            le = open("p_list", "r")
            if n1.upper() + "\n" in le.readlines():
                print("Product Already Exist!")
                le.close()
                return
            le.close()
            break
        except:
            print("Only Numerical Values are allowed in Selling Price and GST")
    f_name = n1.upper() + ".txt"
    file = open(f_name, "w+")
    w = n1.upper() + "\n" + name + "\n" + str(s) + "\n" + str(g) + "\n"
    file.write(w)
    file.close()
    file = open("p_list", "a+")
    file.write(n1.upper() + "\n")
    file.close()
    print("\nProduct added Successfully!\n")
    print("Press any key to Continue to Main Menu")
    if (len(input()) != 0):
        return

def view():
    maxi = 0
    file = open("p_list", "r")
    if len(file.read()) == 0:
        print("Product List Empty!")
        print("Press any key to continue!")
        input()
        file.close()
        return
    file.close()
    file = open("p_list", "r")
    p_list = file.readlines()
    file.close()
    s_list = []
    a_list = []
    for i in p_list:
        x = ""
        for j in range(0, len(i)-1):
            x = x + i[j]
        file2 = open(x + ".txt")
        file2.readline()
        s_list.append(len(file2.readline()))
        a_list.append(x)
        file2.close()
    if max(s_list) < 12:
        maxi = 12
    else:
        maxi = max(s_list)
    print(" " + "S.no" + "  " + "Product Name" + " " * (maxi - 10) + "Price"
          + " " * 4 + "GST(%)" + "  " + "Product Code")
    t = 0
    for i in a_list:
        t += 1
        code = i
        file = open(i + ".txt", "r")
        code = strip(file.readline())
        name = strip(file.readline())
        price = strip(file.readline())
        gst = strip(file.read())
        print(" " + str(t) + ")." + " " * (4 - len(str(t))) + name + " " * (maxi + 2 - len(name)) + price + " " * (9 - len(str(price))) + gst, end="")
        g = 8 - len(str(gst))
        print(" " * g + code)
        file.close()
    print("\nPress any key to Continue to Main Menu")
    if (len(input()) != 0):
        return

def main():
    while True:
        file = open("p_list", "a+")
        file.close()
        file = open("name1.txt", "a")
        file.close()
        file = open("name1.txt", "r")
        s = file.read()
        file.close()
        if len(s) == 0:
            s_name = str(input("Enter name of Shop :"))
            file = open("name1.txt", "w")
            file.write(s_name)
            file.close()
        file = open("name1.txt", "r")
        k = file.read()
        file.close()
        j = " "
        for i in k:
            j = j + i
        j = j + " "
        print("|" + j.upper() + "|")
        for i in range(3):
            print("")
        print("Select an Option:")
        print("1). Generate Invoice")
        print("2). Add Products")
        print("3). Veiw Products")
        print("4). Settings")
        print("5). Exit")
        print("")
        while True:
            try:
                choice = int(input("Your Choice : "))
                break
            except:
                print("Choose correct Option! ")
        if choice == 2:
            add()
        elif choice == 3:
            view()
        elif choice == 1:
            invoice()
        elif choice == 5:
            print("Program Closed!")
            break
        elif choice == 4:
            setting()
        else:
            print("Choose Correct Option!\n")

if __name__ == "__main__":
    main()

