-- ENT Clinical Calculator Database Schema
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) DEFAULT 'clinician',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE calculator_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    category VARCHAR(50) NOT NULL,
    version VARCHAR(20) DEFAULT '1.0.0'
);

CREATE TABLE calculation_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    calculator_type_id INT REFERENCES calculator_types(id),
    input_data JSONB NOT NULL,
    result_data JSONB NOT NULL,
    risk_score NUMERIC(5, 2),
    calculated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_logs_user ON calculation_logs(user_id);
CREATE INDEX idx_logs_date ON calculation_logs(calculated_at);

INSERT INTO calculator_types (name, category) VALUES 
('PTA', 'Audiology'),
('SNOT22', 'Rhinology'),
('STOPBANG', 'Sleep Medicine'),
('DHI', 'Vestibular');
