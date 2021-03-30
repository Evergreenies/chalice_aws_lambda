import boto3
import chalice

app = chalice.Chalice(app_name='students_service')


def get_db():
    """Get DB object"""
    import queries
    dynamodb = boto3.resource('dynamodb')
    return queries.DatabaseOperations(dynamodb.Table('students'))


@app.route('/')
def index():
    """Root view"""
    return {'details': 'This are API endpoints for students.'}


@app.route('/all-students', methods=['GET'])
def all_students():
    """Get all students data at a time."""
    return {'students': get_db().get_all_items()}


@app.route('/student', methods=['GET', 'POST', 'PUT', 'DELETE'])
def student():
    """Perform operations on individual student
    Base Schema:
    {
        "s_id": number,
        "username": "string"
    }
    """
    try:
        request = app.current_request
        request_data = app.current_request.json_body

        if request.method == 'GET':
            # Get student data
            data = get_db().get_item(**request_data)
            return {'students': data.get('Item')}
        elif request.method == 'POST':
            # Insert student record
            return {'status': get_db().put_item(**request_data)}
        elif request.method == 'DELETE':
            # Delete specific item from table
            return {'status': get_db().delete_item(request_data)}
        elif request.method == 'PUT':
            # Update existing student -
            # If item not exist then it will insert new record
            return {'status': get_db().update_item(request_data)}
    except Exception as e:
        raise chalice.BadRequestError(e)
