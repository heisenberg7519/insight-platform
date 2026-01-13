"""
AMEP Backend API Routes
Flask REST API connecting frontend to AI engines

Implements endpoints for BR1-BR9
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from datetime import datetime, timedelta
import uuid

# Import AI engines (from previous artifacts)
# from ai_engine.knowledge_tracing import HybridKnowledgeTracing
# from ai_engine.adaptive_practice import AdaptivePracticeEngine
# from ai_engine.engagement_detection import EngagementDetectionEngine

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize AI engines
# kt_engine = HybridKnowledgeTracing()
# adaptive_engine = AdaptivePracticeEngine()
# engagement_engine = EngagementDetectionEngine()

# ============================================================================
# MASTERY ROUTES (BR1, BR2, BR3)
# ============================================================================

@app.route('/api/mastery/calculate', methods=['POST'])
def calculate_mastery():
    """
    BR1: Calculate student mastery score for a concept
    
    Request body:
    {
        "student_id": "uuid",
        "concept_id": "uuid",
        "is_correct": bool,
        "response_time": float,
        "current_mastery": float,
        "response_history": [...],
        "related_concepts": [...]
    }
    """
    try:
        data = request.json
        
        # In production, call kt_engine.calculate_mastery()
        # For now, return mock response
        result = {
            'mastery_score': 78.5,
            'bkt_component': 75.2,
            'dkt_component': 82.1,
            'dkvmn_component': 78.3,
            'confidence': 0.85,
            'learning_velocity': 5.2,
            'needs_practice': True,
            'recommendation': 'LIGHT_REVIEW - 1-2 questions for maintenance',
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/mastery/student/<student_id>', methods=['GET'])
def get_student_mastery(student_id):
    """
    BR1: Get all concept mastery scores for a student
    """
    try:
        # Mock data - in production, query database
        mastery_data = {
            'student_id': student_id,
            'concepts': [
                {
                    'concept_id': 'c1',
                    'concept_name': 'Linear Equations',
                    'mastery_score': 78.5,
                    'last_assessed': '2025-01-13T10:30:00',
                    'times_assessed': 8,
                    'learning_velocity': 5.2
                },
                {
                    'concept_id': 'c2',
                    'concept_name': 'Quadratic Equations',
                    'mastery_score': 92.3,
                    'last_assessed': '2025-01-12T14:20:00',
                    'times_assessed': 12,
                    'learning_velocity': 3.1
                }
            ],
            'overall_mastery': 85.4
        }
        
        return jsonify(mastery_data), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/practice/generate', methods=['POST'])
def generate_practice_session():
    """
    BR2, BR3: Generate adaptive practice session
    
    Request body:
    {
        "student_id": "uuid",
        "session_duration": int (minutes),
        "subject_area": string
    }
    """
    try:
        data = request.json
        
        # In production, call adaptive_engine.generate_practice_session()
        session = {
            'session_id': str(uuid.uuid4()),
            'student_id': data['student_id'],
            'content_items': [
                {
                    'item_id': 'q1',
                    'concept_id': 'algebra_linear',
                    'difficulty': 0.6,
                    'estimated_time': 5
                },
                {
                    'item_id': 'q2',
                    'concept_id': 'algebra_linear',
                    'difficulty': 0.7,
                    'estimated_time': 6
                }
            ],
            'total_items': 2,
            'estimated_duration': 11,
            'cognitive_load': 0.65,
            'load_status': 'OPTIMAL - Student in ZPD',
            'zpd_alignment': 'Optimal'
        }
        
        return jsonify(session), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# ENGAGEMENT ROUTES (BR4, BR6)
# ============================================================================

@app.route('/api/engagement/analyze', methods=['POST'])
def analyze_engagement():
    """
    BR4: Analyze student engagement from implicit/explicit signals
    
    Request body:
    {
        "student_id": "uuid",
        "implicit_signals": {...},
        "explicit_signals": {...},
        "recent_responses": [...]
    }
    """
    try:
        data = request.json
        
        # In production, call engagement_engine methods
        result = {
            'engagement_score': 72.5,
            'implicit_component': 68.3,
            'explicit_component': 78.2,
            'engagement_level': 'PASSIVE',
            'behaviors_detected': 2,
            'recommendations': [
                'Monitor progress for next 3-5 days',
                'Add time-lock to questions (quick guessing detected)'
            ]
        }
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/engagement/class/<class_id>', methods=['GET'])
def get_class_engagement(class_id):
    """
    BR6: Get class-level engagement metrics for teacher dashboard
    """
    try:
        # Mock data - in production, aggregate from database
        class_data = {
            'class_id': class_id,
            'class_engagement_index': 87,
            'distribution': {
                'ENGAGED': 20,
                'PASSIVE': 6,
                'MONITOR': 1,
                'AT_RISK': 2,
                'CRITICAL': 0
            },
            'alert_count': 2,
            'students_needing_attention': [
                {
                    'student_id': 's1',
                    'name': 'Student A',
                    'engagement_score': 45,
                    'engagement_level': 'AT_RISK',
                    'recommendations': ['Schedule 1-on-1 within 48 hours']
                }
            ],
            'trend': 'improving',
            'engagement_rate': 89.7
        }
        
        return jsonify(class_data), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# LIVE POLLING ROUTES (BR4)
# ============================================================================

@app.route('/api/polls/create', methods=['POST'])
def create_poll():
    """
    BR4: Create anonymous live poll
    
    Request body:
    {
        "teacher_id": "uuid",
        "question": string,
        "options": [string],
        "poll_type": string
    }
    """
    try:
        data = request.json
        
        poll = {
            'poll_id': str(uuid.uuid4()),
            'teacher_id': data['teacher_id'],
            'question': data['question'],
            'options': data['options'],
            'poll_type': data.get('poll_type', 'multiple_choice'),
            'responses': [],
            'created_at': datetime.now().isoformat(),
            'is_active': True
        }
        
        # Broadcast poll to all students via WebSocket
        socketio.emit('new_poll', poll, broadcast=True)
        
        return jsonify(poll), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/polls/<poll_id>/respond', methods=['POST'])
def respond_to_poll(poll_id):
    """
    BR4: Submit anonymous poll response
    
    Request body:
    {
        "student_id": "uuid",
        "selected_option": string,
        "response_time": float
    }
    """
    try:
        data = request.json
        
        response = {
            'response_id': str(uuid.uuid4()),
            'poll_id': poll_id,
            'student_id': data['student_id'],
            'selected_option': data['selected_option'],
            'response_time': data.get('response_time'),
            'submitted_at': datetime.now().isoformat()
        }
        
        # Update poll results in real-time via WebSocket
        socketio.emit('poll_response', {
            'poll_id': poll_id,
            'total_responses': 15  # Would be calculated from DB
        }, broadcast=True)
        
        return jsonify(response), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/polls/<poll_id>', methods=['GET'])
def get_poll_results(poll_id):
    """
    BR6: Get aggregated poll results for teacher
    """
    try:
        # Mock data - in production, aggregate from database
        results = {
            'poll_id': poll_id,
            'question': 'Do you understand today\'s concept?',
            'responses': [
                {'option': 'Yes', 'count': 20, 'percentage': 71},
                {'option': 'Partially', 'count': 6, 'percentage': 21},
                {'option': 'No', 'count': 2, 'percentage': 7}
            ],
            'total_responses': 28,
            'class_size': 28,
            'participation_rate': 100
        }
        
        return jsonify(results), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# PBL ROUTES (BR5, BR9)
# ============================================================================

@app.route('/api/projects', methods=['GET'])
def list_projects():
    """
    BR9: Get all projects for a teacher or student
    """
    try:
        teacher_id = request.args.get('teacher_id')
        student_id = request.args.get('student_id')
        
        # Mock data
        projects = [
            {
                'project_id': 'p1',
                'title': 'Sustainable Energy Solutions',
                'current_stage': 'research',
                'start_date': '2025-01-06',
                'end_date': '2025-02-14',
                'team_count': 3,
                'status': 'on_track'
            }
        ]
        
        return jsonify(projects), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/projects/<project_id>', methods=['GET'])
def get_project_details(project_id):
    """
    BR9: Get detailed project information
    """
    try:
        # Mock data
        project = {
            'project_id': project_id,
            'title': 'Sustainable Energy Solutions',
            'description': 'Design renewable energy solutions',
            'current_stage': 'research',
            'stages': [
                {'id': 'questioning', 'name': 'Questioning', 'status': 'completed'},
                {'id': 'define', 'name': 'Define', 'status': 'completed'},
                {'id': 'research', 'name': 'Research', 'status': 'in_progress'},
                {'id': 'create', 'name': 'Create', 'status': 'pending'},
                {'id': 'present', 'name': 'Present', 'status': 'pending'}
            ],
            'milestones': [
                {
                    'milestone_id': 'm1',
                    'title': 'Research Report',
                    'due_date': '2025-01-20',
                    'status': 'in_progress'
                }
            ],
            'teams': []
        }
        
        return jsonify(project), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/soft-skills/assess', methods=['POST'])
def submit_soft_skill_assessment():
    """
    BR5: Submit peer review or self-assessment
    
    Request body:
    {
        "team_id": "uuid",
        "assessed_student_id": "uuid",
        "assessor_student_id": "uuid",
        "assessment_type": "peer_review",
        "ratings": {
            "td_communication": 4.0,
            "td_mutual_support": 4.5,
            ...
        }
    }
    """
    try:
        data = request.json
        
        # Calculate dimension averages
        ratings = data['ratings']
        td_avg = sum([
            ratings.get('td_communication', 0),
            ratings.get('td_mutual_support', 0),
            ratings.get('td_trust', 0),
            ratings.get('td_active_listening', 0)
        ]) / 4.0
        
        ts_avg = sum([
            ratings.get('ts_clear_roles', 0),
            ratings.get('ts_task_scheduling', 0),
            ratings.get('ts_decision_making', 0),
            ratings.get('ts_conflict_resolution', 0)
        ]) / 4.0
        
        tm_avg = sum([
            ratings.get('tm_clear_purpose', 0),
            ratings.get('tm_smart_goals', 0),
            ratings.get('tm_passion', 0),
            ratings.get('tm_synergy', 0)
        ]) / 4.0
        
        te_avg = sum([
            ratings.get('te_growth_mindset', 0),
            ratings.get('te_quality_work', 0),
            ratings.get('te_self_monitoring', 0),
            ratings.get('te_reflective_practice', 0)
        ]) / 4.0
        
        assessment = {
            'assessment_id': str(uuid.uuid4()),
            'team_id': data['team_id'],
            'assessed_student_id': data['assessed_student_id'],
            'overall_td_score': round(td_avg, 2),
            'overall_ts_score': round(ts_avg, 2),
            'overall_tm_score': round(tm_avg, 2),
            'overall_te_score': round(te_avg, 2),
            'overall_score': round((td_avg + ts_avg + tm_avg + te_avg) / 4, 2),
            'assessed_at': datetime.now().isoformat()
        }
        
        return jsonify(assessment), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/soft-skills/team/<team_id>', methods=['GET'])
def get_team_soft_skills(team_id):
    """
    BR5: Get aggregated soft skill scores for a team
    """
    try:
        # Mock data
        team_scores = {
            'team_id': team_id,
            'team_name': 'Team Alpha',
            'current_scores': {
                'td': 4.2,
                'ts': 3.8,
                'tm': 4.5,
                'te': 4.0
            },
            'trend_data': [
                {'week': 'Week 1', 'td': 3.2, 'ts': 3.0, 'tm': 3.5, 'te': 3.3},
                {'week': 'Week 2', 'td': 3.8, 'ts': 3.2, 'tm': 4.0, 'te': 3.6},
                {'week': 'Week 3', 'td': 4.0, 'ts': 3.5, 'tm': 4.2, 'te': 3.8},
                {'week': 'Week 4', 'td': 4.2, 'ts': 3.8, 'tm': 4.5, 'te': 4.0}
            ],
            'assessment_count': 12
        }
        
        return jsonify(team_scores), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# TEACHER PRODUCTIVITY ROUTES (BR7, BR8)
# ============================================================================

@app.route('/api/templates', methods=['GET'])
def list_templates():
    """
    BR7: Get curriculum-aligned templates
    """
    try:
        subject_area = request.args.get('subject_area')
        grade_level = request.args.get('grade_level')
        
        # Mock data
        templates = [
            {
                'template_id': 't1',
                'title': 'Ecosystem Investigation Project',
                'subject_area': 'Science',
                'grade_level': 7,
                'template_type': 'project_brief',
                'learning_objectives': ['Understand ecosystem dynamics'],
                'estimated_duration': 180,
                'times_used': 45,
                'avg_rating': 4.6
            }
        ]
        
        return jsonify(templates), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analytics/unified', methods=['GET'])
def get_unified_analytics():
    """
    BR8: Get unified institutional metrics
    """
    try:
        date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
        
        # Mock data
        metrics = {
            'metric_date': date,
            'mastery_rate': 78.5,
            'teacher_adoption_rate': 92.3,
            'admin_confidence_score': 94.1,
            'total_students': 450,
            'active_students': 432,
            'total_teachers': 28,
            'active_teachers': 26,
            'avg_engagement_score': 87.2,
            'avg_planning_time_minutes': 45.0,  # Down from 180
            'data_entry_events': 3  # Down from 6
        }
        
        return jsonify(metrics), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/interventions/track', methods=['POST'])
def track_intervention():
    """
    BR6: Track teacher intervention and measure impact
    
    Request body:
    {
        "teacher_id": "uuid",
        "concept_id": "uuid",
        "intervention_type": string,
        "target_students": [uuid],
        "mastery_before": float
    }
    """
    try:
        data = request.json
        
        intervention = {
            'intervention_id': str(uuid.uuid4()),
            'teacher_id': data['teacher_id'],
            'concept_id': data['concept_id'],
            'intervention_type': data['intervention_type'],
            'target_students': data['target_students'],
            'mastery_before': data['mastery_before'],
            'performed_at': datetime.now().isoformat()
        }
        
        return jsonify(intervention), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============================================================================
# WEBSOCKET EVENTS FOR REAL-TIME UPDATES
# ============================================================================

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    print('Client connected')
    emit('connected', {'message': 'Connected to AMEP server'})

@socketio.on('join_class')
def handle_join_class(data):
    """Student/teacher joins a class room"""
    class_id = data.get('class_id')
    print(f'User joined class: {class_id}')

@socketio.on('poll_response_submitted')
def handle_poll_response(data):
    """Broadcast poll response update to all clients"""
    emit('poll_updated', data, broadcast=True)

# ============================================================================
# HEALTH CHECK
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """API health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat()
    }), 200

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)