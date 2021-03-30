class DatabaseOperations(object):
    """Database interface for all DynamoDB tables."""

    def __init__(self, table_resource):
        self._table = table_resource

    def get_all_items(self):
        """Get all data exist in table"""
        return self._table.scan().get('Items')

    def get_item(self, **kwargs):
        """Get single item by passing values as key-value pair to query record"""
        return self._table.get_item(Key=kwargs)

    def put_item(self, **kwargs):
        """Update a record where value matches"""
        return self._table.put_item(Item=kwargs)

    def update_item(self, data, **kwargs):
        """Update a record where value matches"""
        return self._table.update_item(Key=data, **kwargs)

    def delete_item(self, data, **kwargs):
        """Remove specific record from table"""
        return self._table.delete_item(Key=data, **kwargs)
