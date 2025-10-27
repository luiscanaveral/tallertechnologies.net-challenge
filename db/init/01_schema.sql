-- ========================
-- Table: Project
-- ========================
CREATE TABLE project (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ========================
-- Table: Task
-- ========================
CREATE TABLE task (
    id BIGSERIAL PRIMARY KEY,
    project_id BIGINT NOT NULL REFERENCES project(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    priority INTEGER DEFAULT 0,
    completed BOOLEAN DEFAULT FALSE,
    due_date DATE
);

-- Optional indexes for performance
CREATE INDEX idx_task_project_id ON task(project_id);
CREATE INDEX idx_task_priority ON task(priority);
CREATE INDEX idx_task_completed ON task(completed);