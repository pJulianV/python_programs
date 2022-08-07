def ordenamiento_burbuja (N, codigo_producto, nombre_producto, cantidad_comprada, valor_unitario, valor_iva, valor_producto, valor_final_producto):
    for i in range (0, N-1):
        for j in range (i+1, N):
            if nombre_producto[i] > nombre_producto[j]:
                temp=codigo_producto[i]
                codigo_producto[i]=codigo_producto[j]
                codigo_producto[j]=temp
                
                temp=nombre_producto[i]
                nombre_producto[i]=nombre_producto[j]
                nombre_producto[j]=temp
                
                temp=cantidad_comprada[i]
                cantidad_comprada[i]=cantidad_comprada[j]
                cantidad_comprada[j]=temp
                
                temp=valor_unitario[i]
                valor_unitario[i]=valor_unitario[j]
                valor_unitario[j]=temp
                
                temp=valor_iva[i]
                valor_iva[i]=valor_iva[j]
                valor_iva[j]=temp
                
                temp=valor_producto[i]
                valor_producto[i]=valor_producto[j]
                valor_producto[j]=temp
                
                temp=valor_final_producto[i]
                valor_final_producto[i]=valor_final_producto[j]
                valor_final_producto[j]=temp
                
    return codigo_producto, nombre_producto, cantidad_comprada, valor_unitario, valor_iva, valor_producto, valor_final_producto

N=int(input())
valor_total_compra=0
valor_total_iva=0

codigo_producto=[]
nombre_producto=[]
cantidad_comprada=[]
valor_unitario=[]
tipo_iva=[]
 
valor_producto=[]
valor_iva=[]
valor_final_producto=[]

for i in range(N):
    codigo_producto.append(int(input()))
    nombre_producto.append(input())
    cantidad_comprada.append(float(input()))
    valor_unitario.append(float(input()))
    tipo_iva.append(int(input()))

    valor_producto.append(cantidad_comprada[i] * valor_unitario[i])
    
    if tipo_iva[i]==1:
        valor_iva.append(0)
    elif tipo_iva[i]==2:
        valor_iva.append(valor_producto[i] * 0.05)
    else:
        valor_iva.append(valor_producto[i] * 0.19)
        
    valor_final_producto.append(valor_producto[i] + valor_iva[i])
    valor_total_compra= valor_total_compra + valor_final_producto[i]
    valor_total_iva= valor_total_iva + valor_iva[i]
    
codigo_producto, nombre_producto, cantidad_comprada, valor_unitario, valor_iva, valor_producto, valor_final_producto = ordenamiento_burbuja (N, codigo_producto, nombre_producto, cantidad_comprada, valor_unitario, valor_iva, valor_producto, valor_final_producto)

#IMPRIMIR ORDENADO
for i in range(N):
    print(codigo_producto[i])
    print(valor_iva[i])
    print(valor_producto[i])
    print(valor_final_producto[i])

print(valor_total_compra)
print(valor_total_iva)