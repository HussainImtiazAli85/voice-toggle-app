from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Store toggle states for each box (0-11)
toggle_states = {f'box_{i}': False for i in range(12)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/toggle', methods=['POST'])
def toggle_box():
    data = request.json
    box_id = data.get('box_id')
    
    if box_id in toggle_states:
        toggle_states[box_id] = not toggle_states[box_id]
        return jsonify({'success': True, 'state': toggle_states[box_id], 'box_id': box_id})
    
    return jsonify({'success': False}), 400

@app.route('/api/states', methods=['GET'])
def get_states():
    return jsonify(toggle_states)

@app.route('/api/reset', methods=['POST'])
def reset_all():
    global toggle_states
    toggle_states = {f'box_{i}': False for i in range(12)}
    return jsonify({'success': True, 'states': toggle_states})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
