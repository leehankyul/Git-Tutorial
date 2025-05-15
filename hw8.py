def add_item(cart):
    while True:
        item = input("[구입] 상품명? ")
        if item == "":
            break
        qty = int(input("수량은? "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"장바구니에 {item} {qty}개가 담겼습니다.")

def print_cart(cart):
    print(">>> 장바구니 보기:", cart)

def find_item(cart):
    while True:
        name = input("[검색] 장바구니에서 확인하고자 하는 상품은? ")
        if name == "":
            break
        if name in cart:
            print(f"{name}(는) {cart[name]}개 담겨 있습니다.")
        else:
            print(f"장바구니에 {name}은(는) 없습니다.")

shopping_cart = {}
add_item(shopping_cart)
print_cart(shopping_cart)
find_item(shopping_cart)
