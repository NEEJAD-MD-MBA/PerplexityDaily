"""Flask web application for the multi-agent coordination system."""

from flask import Flask, render_template, request, jsonify, send_file
import json
import os
from datetime import datetime
from coordinator import AgentCoordinator
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Global coordinator instance
coordinator = AgentCoordinator()


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/build', methods=['POST'])
def build_application():
    """API endpoint to build and deploy a web application."""
    try:
        data = request.get_json()
        goal = data.get('goal', '')
        
        if not goal:
            return jsonify({
                'success': False,
                'error': 'No goal provided'
            }), 400
        
        # Process the request
        results = coordinator.build_and_deploy_web_app(goal)
        
        # Save results with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results_{timestamp}.json"
        coordinator.save_results_to_file(results, filename)
        
        return jsonify({
            'success': results['success'],
            'results': results,
            'filename': filename
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/history')
def get_history():
    """Get the task history."""
    try:
        history = coordinator.get_task_history()
        return jsonify({
            'success': True,
            'history': history
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/download/<filename>')
def download_results(filename):
    """Download a results file."""
    try:
        if os.path.exists(filename):
            return send_file(filename, as_attachment=True)
        else:
            return jsonify({
                'success': False,
                'error': 'File not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'agents': {
            'chatgpt': 'configured' if Config.OPENAI_API_KEY else 'not configured',
            'perplexity': 'configured' if Config.PERPLEXITY_API_KEY else 'not configured'
        }
    })


if __name__ == '__main__':
    # Validate configuration
    Config.validate()
    
    # Run the app
    print(f"\nStarting web server on {Config.HOST}:{Config.PORT}")
    print(f"Open http://localhost:{Config.PORT} in your browser\n")
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.FLASK_DEBUG
    )
