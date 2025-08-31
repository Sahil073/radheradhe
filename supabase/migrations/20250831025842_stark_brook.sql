-- Initialize database schema for smart microgrid system

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'household')),
    household_id VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Audit logs table
CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id VARCHAR(100),
    action TEXT NOT NULL,
    zone VARCHAR(50),
    extra_data JSONB,
    ip_address INET
);

-- Energy data cache table
CREATE TABLE IF NOT EXISTS energy_data (
    id SERIAL PRIMARY KEY,
    zone VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    battery_voltage FLOAT,
    input_power FLOAT,
    output_power FLOAT,
    solar_generation FLOAT,
    battery_percentage FLOAT,
    relay_state BOOLEAN
);

-- Optimization decisions table
CREATE TABLE IF NOT EXISTS optimization_decisions (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    decision_data JSONB NOT NULL,
    battery_level FLOAT,
    predicted_sustain_hours FLOAT,
    triggered_by VARCHAR(100)
);

-- Alerts table
CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    alert_type VARCHAR(100) NOT NULL,
    severity VARCHAR(20) NOT NULL CHECK (severity IN ('LOW', 'MEDIUM', 'HIGH', 'EMERGENCY')),
    message TEXT NOT NULL,
    recipient VARCHAR(255),
    status VARCHAR(20) DEFAULT 'sent' CHECK (status IN ('sent', 'failed', 'delivered')),
    zone VARCHAR(50)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_energy_data_zone_timestamp ON energy_data(zone, timestamp);
CREATE INDEX IF NOT EXISTS idx_audit_logs_timestamp ON audit_logs(timestamp);
CREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON alerts(timestamp);
CREATE INDEX IF NOT EXISTS idx_optimization_decisions_timestamp ON optimization_decisions(timestamp);

-- Insert default users
INSERT INTO users (email, password_hash, role) 
VALUES ('admin@urjalink.com', 'pbkdf2:sha256:260000$salt$hash', 'admin') 
ON CONFLICT (email) DO NOTHING;

INSERT INTO users (email, password_hash, role, household_id) 
VALUES ('house1@urjalink.com', 'pbkdf2:sha256:260000$salt$hash', 'household', 'H001') 
ON CONFLICT (email) DO NOTHING;