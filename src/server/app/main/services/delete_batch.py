from app.main import db
from app.main.models.batch import Batch
from flask import jsonify


def delete_batch(data):
    batch = Batch.query.get(int(data["batch_id"]))
    print(batch)
    db.session.delete(batch)
    db.session.commit()
    response_object = jsonify({"response": "successfully delete Batch"})
    return response_object, 200