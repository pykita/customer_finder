from cli.models.customer import Customer
from json import loads, dumps
from cli.logger import log

def get_customers(file_name):
    '''
        Returns customers loaded from the given file
        and converted to the Customer object.
        Here input can be validated but for now we consider
        it to be always valid.
    '''
    customers = []

    with open(file_name, 'r') as file_reader:
        line = file_reader.readline()
        while line:
            customer_dict = loads(line)
            customer_dict['latitude'] = float(customer_dict['latitude'])
            customer_dict['longitude'] = float(customer_dict['longitude'])
            customer = Customer(**customer_dict)
            customers.append(customer)
            line = file_reader.readline()

    return customers

def save_customers(customers, file_name):
    '''
        Saves customers to the given file. 
    '''

    def customer_mapper(c):
        return dumps({
            'user_id': c.user_id,
            'name': c.name
        })

    customers = sorted(customers, key=lambda c: c.user_id, reverse=False)

    with open(file_name, 'w') as file_writer:
        newline_customers = '\n'.join([customer_mapper(c) for c in customers])
        file_writer.write(newline_customers)
