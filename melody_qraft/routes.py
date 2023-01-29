from flask import Blueprint, render_template, request


# Blueprint Configuration

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/')
def index():
    return render_template('index.html')

