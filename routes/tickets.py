from flask import Blueprint, request, jsonify
from models.ticket import db, Ticket
from services.classifier import classify_ticket

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([t.to_dict() for t in tickets])

@tickets_bp.route('/', methods=['POST'])
def create_ticket():
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({"error": "Description is required"}), 400
    
    description = data['description']
    
    # Call the AI service
    classification = classify_ticket(description)
    
    new_ticket = Ticket(
        description=description,
        category=classification.get('category'),
        priority=classification.get('priority'),
        team=classification.get('team')
    )
    
    db.session.add(new_ticket)
    db.session.commit()
    
    return jsonify(new_ticket.to_dict()), 201
