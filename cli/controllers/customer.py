from cli.models.customer import Customer
from cli.models.location import Location
from cli.dao import get_customers, save_customers
from cli.logger import log
from cli.config import dublin_location

class CustomerController:
    def get_close_customers(self, input_file, output_file, radius):
        '''
            A method that loads customers from json file (jsonlines)
            and outputs those that are located within the given radius
            from the Dublin's office
        '''
        customers = get_customers(input_file)
        log.info(f'Amount of customers received: {len(customers)}')

        def filter_customers_by_distance(customer: Customer):
            distance = Location.get_distance(customer.location, dublin_location)
            log.info(distance)
            return distance <= radius

        close_customers = list(filter(filter_customers_by_distance, customers))
        log.info(f'Amount of customers that are close to Dublin: {len(close_customers)}')

        save_customers(close_customers, output_file)
        log.info(f'Customers are saved to {output_file}')