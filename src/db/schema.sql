-- =========================================================================
-- S.A.P.P.M Database Schema (Supabase PostgreSQL)
-- Core tables for staff auth profiles, student input metrics, model benchmarks,
-- and prediction audit logs.
-- =========================================================================

-- 1. Staff Profiles Table
-- Stores extended staff details linked to Supabase auth accounts.
CREATE TABLE IF NOT EXISTS public.staff_profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    staff_id TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT DEFAULT 'Academic Advisor',
    department TEXT DEFAULT 'Academic Affairs',
    created_at TIMESTAMPTZ DEFAULT TIMEZONE('utc', NOW())
);

-- 2. Model Info Table
-- Registry tracking trained ML models (XGBoost, Random Forest, Logistic Regression)
-- and evaluation benchmark scores.
CREATE TABLE IF NOT EXISTS public.model_info (
    model_id SERIAL PRIMARY KEY,
    model_name TEXT NOT NULL,
    accuracy FLOAT NOT NULL,
    precision FLOAT NOT NULL,
    recall FLOAT NOT NULL,
    f1_score FLOAT NOT NULL,
    model_file TEXT NOT NULL,
    training_date TIMESTAMPTZ DEFAULT TIMEZONE('utc', NOW())
);

-- Seed initial model benchmarks for the analytics dashboard
INSERT INTO public.model_info (model_name, accuracy, precision, recall, f1_score, model_file)
VALUES 
('XGBoost Classifier (Champion)', 99.81, 99.80, 99.81, 99.80, 'models/best_model.pkl'),
('Random Forest Classifier', 99.78, 99.75, 99.78, 99.76, 'models/random_forest_model.pkl'),
('Logistic Regression (Baseline)', 93.84, 93.50, 93.84, 93.60, 'models/logistic_model.pkl')
ON CONFLICT DO NOTHING;

-- 3. Student Data Table
-- Stores academic and behavioral metrics entered for prediction.
CREATE TABLE IF NOT EXISTS public.student_data (
    student_id BIGSERIAL PRIMARY KEY,
    student_name TEXT,
    matric_number TEXT,
    weekly_self_study_hours FLOAT NOT NULL,
    attendance_percentage FLOAT NOT NULL,
    class_participation FLOAT NOT NULL,
    total_score FLOAT NOT NULL,
    created_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ DEFAULT TIMEZONE('utc', NOW())
);

-- 4. Prediction Output Table
-- Records prediction results, risk levels, confidence scores, and SHAP factors.
CREATE TABLE IF NOT EXISTS public.prediction_output (
    prediction_id BIGSERIAL PRIMARY KEY,
    student_id BIGINT REFERENCES public.student_data(student_id) ON DELETE CASCADE,
    model_id INT REFERENCES public.model_info(model_id) ON DELETE SET NULL,
    predicted_grade VARCHAR(5) NOT NULL,
    risk_level VARCHAR(20) NOT NULL,
    confidence_score FLOAT NOT NULL,
    shap_summary JSONB,
    predicted_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    prediction_date TIMESTAMPTZ DEFAULT TIMEZONE('utc', NOW())
);

-- Enable Row Level Security (RLS)
ALTER TABLE public.staff_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.student_data ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.prediction_output ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.model_info ENABLE ROW LEVEL SECURITY;

-- Access Policies for authenticated staff
CREATE POLICY "Allow authenticated read/write on staff_profiles" 
ON public.staff_profiles FOR ALL TO authenticated USING (true) WITH CHECK (true);

CREATE POLICY "Allow authenticated read/write on student_data" 
ON public.student_data FOR ALL TO authenticated USING (true) WITH CHECK (true);

CREATE POLICY "Allow authenticated read/write on prediction_output" 
ON public.prediction_output FOR ALL TO authenticated USING (true) WITH CHECK (true);

CREATE POLICY "Allow authenticated read on model_info" 
ON public.model_info FOR SELECT TO authenticated USING (true);
