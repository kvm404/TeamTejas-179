from flask import render_template, jsonify, request

def register_error_handlers(app):
    """Register error handlers with the Flask application."""
    
    @app.errorhandler(400)
    def bad_request_error(error):
        """Handle 400 Bad Request errors."""
        if request.path.startswith('/api/'):
            return jsonify({
                'error': 'Bad Request',
                'message': str(error) or 'Invalid request'
            }), 400
        return render_template('errors/400.html', error=error), 400
    
    @app.errorhandler(404)
    def not_found_error(error):
        """Handle 404 Not Found errors."""
        if request.path.startswith('/api/'):
            return jsonify({
                'error': 'Not Found',
                'message': 'The requested resource was not found'
            }), 404
        return render_template('errors/404.html', error=error), 404
    
    @app.errorhandler(403)
    def forbidden_error(error):
        """Handle 403 Forbidden errors."""
        if request.path.startswith('/api/'):
            return jsonify({
                'error': 'Forbidden',
                'message': 'You do not have permission to access this resource'
            }), 403
        return render_template('errors/403.html', error=error), 403
    
    @app.errorhandler(500)
    def internal_server_error(error):
        """Handle 500 Internal Server errors."""
        app.logger.error(f'Server Error: {error}')
        if request.path.startswith('/api/'):
            return jsonify({
                'error': 'Internal Server Error',
                'message': 'An unexpected error occurred'
            }), 500
        return render_template('errors/500.html', error=error), 500
    
    @app.errorhandler(401)
    def unauthorized_error(error):
        """Handle 401 Unauthorized errors."""
        if request.path.startswith('/api/'):
            return jsonify({
                'error': 'Unauthorized',
                'message': 'Authentication is required'
            }), 401
        return render_template('errors/401.html', error=error), 401
    
    @app.errorhandler(405)
    def method_not_allowed_error(error):
        """Handle 405 Method Not Allowed errors."""
        if request.path.startswith('/api/'):
            return jsonify({
                'error': 'Method Not Allowed',
                'message': 'The method is not allowed for the requested URL'
            }), 405
        return render_template('errors/405.html', error=error), 405
    
    @app.errorhandler(429)
    def too_many_requests_error(error):
        """Handle 429 Too Many Requests errors."""
        if request.path.startswith('/api/'):
            return jsonify({
                'error': 'Too Many Requests',
                'message': 'Request rate limit exceeded'
            }), 429
        return render_template('errors/429.html', error=error), 429 