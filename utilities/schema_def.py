common_schema = [
    {
        'AttributeName': 'username',
        'KeyType': 'RANGE'
    },
]

common_def = [
    {
        'AttributeName': 'username',
        'AttributeType': 'S'
    },
]

provision = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

student_schema = [
    {
        'AttributeName': 's_id',
        'KeyType': 'HASH'
    },
    *common_schema
]

student_def = [
    {
        'AttributeName': 's_id',
        'AttributeType': 'N'
    },
    *common_def
]

teacher_schema = [
    {
        'AttributeName': 't_id',
        'KeyType': 'HASH'
    },
    *common_schema
]

teacher_def = [
    {
        'AttributeName': 't_id',
        'AttributeType': 'N'
    },
    *common_def
]

student = {
    'table_name': 'students',
    'key_schema': student_schema,
    'attributes': student_def,
    'provision': provision
}

teacher = {
    'table_name': 'teachers',
    'key_schema': teacher_schema,
    'attributes': teacher_def,
    'provision': provision
}
