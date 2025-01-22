from flask import Blueprint, request, jsonify
from app.services.pdb_service import parse_pdb

pdb_bp = Blueprint('pdb', __name__)

@pdb_bp.route('/upload', methods=['POST'])
def upload_pdb():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = f"/tmp/{file.filename}"
    file.save(file_path)

    data = parse_pdb(file_path)
    return jsonify(data)
