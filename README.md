## Implementation

The project includes a reconstructed software demonstration based on the proposed AI and IoT hydroponic agriculture concept.

### Data Flow

IoT Sensors → Sensor Data → Data Processing → AI/ML Model → Plant Condition Prediction → Monitoring Dashboard

### Components

**IoT Sensor Simulator**
- Generates sample temperature readings
- Generates humidity readings
- Generates pH readings
- Generates nutrient-level readings

**AI/ML Module**
- Processes the sensor dataset
- Classifies growing conditions
- Uses a Random Forest classifier
- Produces a plant-condition prediction

**Monitoring Dashboard**
- Displays sensor parameters
- Provides a basic condition assessment
- Visualizes sensor readings using graphs

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
