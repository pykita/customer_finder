import click
from cli.controllers.customer import CustomerController
from cli.logger import log

@click.command()
@click.option('--input-file', help='File with customers')
@click.option('--output-file', help='File with customers')
@click.option('--radius', default=100, help='Radius in km.')
def exec_command(input_file, output_file, radius):
    '''
        Click interface of the cli command
    '''

    log.info(f'Input: {input_file}')
    log.info(f'Output: {output_file}')
    log.info(f'Radius: {radius}')
    controller = CustomerController()

    controller.get_close_customers(input_file, output_file, radius)
    

if __name__ == '__main__':
    exec_command()
    