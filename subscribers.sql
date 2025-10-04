-- Create subscribers table
CREATE TABLE IF NOT EXISTS subscribers_subscriber (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    subscription_date DATE NOT NULL,
    status ENUM('active', 'inactive', 'cancelled') DEFAULT 'active'
);

-- Insert sample data
INSERT INTO subscribers_subscriber: (email, name, subscription_date, status) VALUES
('john.doe@example.com', 'John Doe', '2025-01-15', 'active'),
('jane.smith@example.com', 'Jane Smith', '2025-02-20', 'active'),
('alice.brown@example.com', 'Alice Brown', '2025-03-10', 'inactive'),
('bob.jones@example.com', 'Bob Jones', '2025-04-05', 'active'),
('emma.wilson@example.com', 'Emma Wilson', '2025-05-12', 'cancelled'),
('mike.davis@example.com', 'Mike Davis', '2025-06-18', 'active'),
('sarah.taylor@example.com', 'Sarah Taylor', '2025-07-22', 'active'),
('david.moore@example.com', 'David Moore', '2025-08-30', 'inactive'),
('laura.martin@example.com', 'Laura Martin', '2025-09-05', 'active'),
('chris.jackson@example.com', 'Chris Jackson', '2025-10-01', 'active');
