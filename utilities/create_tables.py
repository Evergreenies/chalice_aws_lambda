import boto3

from first_app.utilities import schema_def as sd

dynamodb = boto3.resource('dynamodb')


def create_table(table_name: str, key_schema: list, attributes: list,
                 provision: dict):
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attributes,
        ProvisionedThroughput=provision
    )
    table.meta.client.get_waiter('table_exists') \
        .wait(TableName=table_name)


def insert_data(table_name: str, data: list):
    table = dynamodb.Table(table_name)

    with table.batch_writer() as batch:
        for rw in data:
            batch.put_item(Item=rw)


if __name__ == '__main__':
    # Create tables
    create_table(**sd.student)
    create_table(**sd.teacher)

    dummy_teachers = [
        {'t_id': 1, 'username': 'Daniel Bader', 'first_name': 'Daniel', 'last_name': 'Bader'},
        {'t_id': 2, 'username': 'coreyschefer', 'first_name': 'Corey', 'last_name': 'Schefer'},
    ]
    dummy_students = [
        {'s_id': 1, 'username': 'suyogshimpi', 'first_name': 'Suyog', 'last_name': 'Shimpi'},
        {'s_id': 1, 'username': 'param', 'first_name': 'Param', 'last_name': 'Gudadhe'},
    ]

    # Insert dummy data
    insert_data('students', dummy_students)
    insert_data('teachers', dummy_teachers)
