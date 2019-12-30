from flask import Blueprint, request
from app.main.services.add_batch import add_new_batch
from app.main.services.add_section import add_new_section
from app.main.services.add_test_type import add_new_test_type
from app.main.services.delete_batch import delete_batch
from app.main.services.delete_section import delete_section
from app.main.services.delete_test_type import delete_test_type
from app.main.services.get_all_batches import get_all_batches
from app.main.services.get_all_test_type import get_all_test_types
from app.main.services.get_all_sections import get_all_sections

admin = Blueprint("admin", __name__)

# Add New Batch
@admin.route("/add_batch", methods=['POST'])
def addBatch():
    data = request.json
    return add_new_batch(data)


# Add New Section
@admin.route("/add_section", methods=['POST'])
def addSection():
    data = request.json
    return add_new_section(data)


# Add New Test Type
@admin.route("/add_test_type", methods=["POST"])
def addTestType():
    data = request.json
    return add_new_test_type(data)


# Delete a Batch
@admin.route("/delete_batch", methods=['DELETE'])
def deleteBatch():
    data = request.json
    return delete_batch(data)


# Delete a Section
@admin.route("/delete_section", methods=['DELETE'])
def deleteSection():
    data = request.json
    return delete_section(data)

# Delete a Test_type
@admin.route("/delete_section", methods=['DELETE'])
def deleteTestType():
    data = request.json
    return delete_test_type(data)

# Get all Batches
@admin.route("/all_batches", methods=['GET'])
def allBatches():
    return get_all_batches()

# Get all Sections
@admin.route("/all_sections", methods=['GET'])
def allSections():
    return get_all_sections()


# Get all Test_types
@admin.route("/all_test_types", methods=['GET'])
def allTestTypes():
    return get_all_test_types()