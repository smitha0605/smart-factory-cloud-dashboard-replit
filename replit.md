# CloudFactory Pro - Smart Manufacturing Dashboard

## Overview
A static website showcasing a smart manufacturing dashboard powered by cloud computing. The site demonstrates real-time IoT monitoring, predictive maintenance, and production analytics capabilities.

## Project Structure
- `index.html` - Main landing page with dashboard demo
- `style.css` - All styling and responsive design
- `server.py` - Python HTTP server for serving static files
- `netlify.toml` - Original Netlify configuration (reference only)

## Technology Stack
- **Frontend**: HTML5, CSS3
- **Backend**: Flask (Python)
- **Server**: Python 3 with Flask web framework
- **Hosting**: Replit (originally Netlify)

## Features
- Real-time production dashboard with metrics
- Machine health monitoring
- IoT sensor displays
- AI-powered predictive maintenance
- Contact form (originally using Netlify Forms)
- Fully responsive design

## Recent Changes
- 2025-11-06: Imported from GitHub and configured for Replit environment
  - Added Flask web server with cache control headers
  - Configured to run on port 5000 with 0.0.0.0 host
  - Implemented contact form handler with POST support
  - Form submissions saved to form_submissions.json file
  - Created thank you page for successful submissions
  - Added /submissions endpoint to view all form submissions
  - Added .gitignore for Python and form data
  - Configured deployment for autoscale
  - Created project documentation

## Development
The site runs on a Flask web server at port 5000. The server includes:
- Cache control headers to ensure updates are visible immediately during development
- POST endpoint `/submit-form` for handling contact form submissions
- GET endpoint `/submissions` to view all form submissions (JSON format)
- Automatic form data storage in `form_submissions.json`

## Form Submissions
Contact form submissions are stored locally in `form_submissions.json` with timestamps. To view all submissions, navigate to `/submissions` or check the JSON file directly.
