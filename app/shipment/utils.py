from dashboard.models import Address


# create_address_obj receive address string and just create an Address objects
def create_address_obj(address: str) -> Address:
    """
    address : "Street 2, 20144 Hamburg, Germany"
    address_list : ['Street 1', '10115 Berlin', 'Germany']
    """
    address_list = [part.strip() for part in address.split(',')]
    address_obj = Address.objects.create(
        country=address_list[2],
        city=address_list[1].split(' ')[1],
        street=address_list[0],
        postal_code=address_list[1].split(' ')[0],
    )

    return address_obj
