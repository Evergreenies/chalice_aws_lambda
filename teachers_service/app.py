import boto3
import chalice

app = chalice.Chalice(app_name='teachers_service')


def get_db():
    """Get DB object"""
    import queries
    dynamodb = boto3.resource('dynamodb')
    return queries.DatabaseOperations(dynamodb.Table('teachers'))


@app.route('/')
def index():
    """Root view"""
    return {'details': 'This are API endpoints for teachers.'}


@app.route('/all-teachers', methods=['GET'])
def all_teachers():
    """Get all teachers data at a time."""
    return {'teachers': get_db().get_all_items()}


@app.route('/teacher', methods=['GET', 'POST', 'PUT', 'DELETE'])
def teacher():
    """Perform operations on individual teacher
    Base Schema:
    {
        "t_id": number,
        "username": "string"
    }
    """
    try:
        request = app.current_request
        request_data = app.current_request.json_body

        if request.method == 'GET':
            # Get teacher data
            data = get_db().get_item(**request_data)
            return {'teachers': data.get('Item')}
        elif request.method == 'POST':
            # Insert teacher record
            return {'status': get_db().put_item(**request_data)}
        elif request.method == 'DELETE':
            # Delete specific item from table
            return {'status': get_db().delete_item(request_data)}
        elif request.method == 'PUT':
            # Update existing teacher -
            # If item not exist then it will insert new record
            return {'status': get_db().update_item(request_data)}
    except Exception as e:
        raise chalice.BadRequestError(e)
