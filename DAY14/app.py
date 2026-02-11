from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)  


class BaseModel:
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Bus(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    

    def __repr__(self):
        return f'<Bus {self.id} - {self.name}>'


with app.app_context():
    db.create_all()



@app.route('/bus', methods=['GET'])
def get_all_buses():
    buses = db.session.execute(db.select(Bus)).scalars().all()
    return jsonify([bus.to_dict() for bus in buses])

@app.route('/bus/<int:bus_id>', methods=['GET'])
def get_bus(bus_id):
    bus = db.session.get(Bus, bus_id)
    if bus:
        return jsonify(bus.to_dict())
    return jsonify({"message": "Bus not found"}), 404

@app.route('/bus', methods=['POST'])
def create_bus(): 
    new_bus_data = request.json
    if not new_bus_data:
        return jsonify({"message": "Invalid JSON"}), 400
    
    if 'name' not in new_bus_data:
        return jsonify({"message": "Missing 'name' field"}), 400

    new_bus = Bus(name=new_bus_data['name'])

    
    db.session.add(new_bus)
    db.session.commit() 
    
    return jsonify(new_bus.to_dict()), 201

@app.route('/bus/<int:bus_id>', methods=['PUT'])
def update_bus(bus_id):
    bus = db.session.get(Bus, bus_id)
    if not bus:
        return jsonify({"message": "Bus not found"}), 404
    
    updated_data = request.json
    if not updated_data:
        return jsonify({"message": "Invalid JSON"}), 400
    
    if 'name' in updated_data:
        bus.name = updated_data['name']
    
    db.session.commit()
    return jsonify(bus.to_dict())

@app.route('/bus/<int:bus_id>', methods=['DELETE'])
def delete_bus(bus_id):
    bus = db.session.get(Bus, bus_id)
    if bus:
        db.session.delete(bus)
        db.session.commit()
        return jsonify({"message": "Bus deleted successfully"}), 200
    return jsonify({"message": "Bus not found"}), 404



@app.route('/')
def home():
    return "Welcome to the BUS API."

if __name__ == '__main__':
    app.run(debug=True) 