from flask_app.extensions.database import database as db


class CRUD(db.Model):
    # Mark this class as abstract, so it won't create a database table.
    __abstract__ = True

    def save(self):
        """
        Adds the current instance to the database session and commits the transaction.
        Use this method to persist the current object in the database.
        """
        db.session.add(self)  # Add the object to the session
        db.session.commit()  # Commit the transaction to save changes

    def delete(self):
        """
        Removes the current instance from the database and commits the transaction.
        Use this method to delete the current object from the database.
        """
        db.session.delete(self)  # Mark the object for deletion
        db.session.commit()  # Commit the transaction to apply the deletion

    @classmethod
    def get(cls, identifier):
        """
        Fetches an object of the current class type by its primary key.

        Args:
            identifier: The primary key of the object to retrieve.

        Returns:
            An instance of the current class type if found, otherwise None.
        """
        return db.session.get(cls, identifier)  # Retrieve the object using the session
