from ProductUpdProc import ProductUpdProc
from ClientUpdProc import ClientUpdProc
from OrderUpdProc import OrderUpdProc

if __name__ == "__main__":
    product_proc = ProductUpdProc()
    product_proc.update_entity()

    client_proc = ClientUpdProc()
    client_proc.update_entity()

    order_proc = OrderUpdProc()
    order_proc.update_entity()