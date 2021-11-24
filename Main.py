from menu_item import MenuItem

menu_item1 = MenuItem('Roti Bakar', 5000)
menu_item2 = MenuItem('Kue Coklat', 10000)
menu_item3 = MenuItem('Kopi', 8000)
menu_item4 = MenuItem('Jus Apel', 10000)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('Masukkan nomor menu: '))
selected_menu = menu_items[order]
print('Item yang dipilih :' + selected_menu.name)

count = int(input('Jumlah pesanan (diskon 10% untuk 3 atau lebih): '))
result = selected_menu.get_total_price(count)

print('Total harga adalah Rp. ' + str(result))