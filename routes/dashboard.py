from flask import Blueprint, jsonify
from models.ticket import Ticket

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/stats', methods=['GET'])
def get_stats():
    total_tickets = Ticket.query.count()
    return jsonify({
        "total_tickets": total_tickets,
        "status": "Operational"
    })
