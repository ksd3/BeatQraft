from flask import Blueprint, render_template, jsonify
from melody_qraft.get_beat import get_beat_strings
from melody_qraft.beatgenerator import create_midi_file


# Blueprint Configuration

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/api/a', methods=['GET'])
def get_a():
    hihat_beat, snare_beat, bass_beat = get_beat_strings()
    create_midi_file(bass_beat, snare_beat, hihat_beat)
    return jsonify({'status': 'success', 'result': 123})



