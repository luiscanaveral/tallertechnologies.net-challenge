-- Insert sample projects
INSERT INTO project (name, description)
VALUES
  ('Website Redesign', 'Improve UX/UI and add new landing pages'),
  ('Mobile App Launch', 'Develop and release version 1.0 of the app'),
  ('Marketing Campaign', 'Plan and execute Q4 advertising strategy');

-- Insert sample tasks
INSERT INTO task (project_id, title, priority, completed, due_date)
VALUES
  (1, 'Create wireframes', 3, FALSE, '2025-11-15'),
  (1, 'Implement responsive layout', 2, FALSE, '2025-12-01'),
  (2, 'Setup API endpoints', 4, TRUE, '2025-10-20'),
  (2, 'Integrate Firebase auth', 3, FALSE, '2025-11-10'),
  (3, 'Design campaign assets', 5, FALSE, '2025-11-05'),
  (3, 'Schedule social media posts', 2, FALSE, '2025-11-12');