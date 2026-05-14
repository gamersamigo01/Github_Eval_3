precios = [30,40,65,89,103,120,100]

for pro_pre in precios:
    if pro_pre < 50:
        print(f"Su producto no tiene descuento: ${pro_pre}")
    elif pro_pre >= 50:
        pro_pre *= 0.90
        print(f"Su producto tiene un descuento del 10%: ${pro_pre:.1f}")
    elif pro_pre >= 100:
        pro_pre *= 0.80
        print(f"Su producto tiene un descuento del 20%: ${pro_pre:.1f}")