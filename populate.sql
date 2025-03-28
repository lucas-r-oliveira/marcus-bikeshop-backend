DELETE from products;
DELETE from product_parts;
DELETE from part_options;
DELETE from part_configurations;
DELETE from part_configuration_options;
-- DELETE FROM characteristics_options;
DROP TABLE IF EXISTS characteristic_options;
-- Populate the products table with 5 bicycle products
DROP TABLE IF EXISTS product_characteristic_options;

-- idk why this isnt working in flask
CREATE TABLE IF NOT EXISTS characteristic_options (
    id TEXT PRIMARY KEY,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    in_stock BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS product_characteristic_options (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT NOT NULL,
    option_id TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (option_id) REFERENCES characteristic_options (id)
);


INSERT INTO products (id, name, description, base_price, image_url, category)
VALUES 
    ('11111111-1111-1111-1111-111111111111', 'Mountain Explorer', 'A rugged mountain bike for challenging terrains', 1299.99, 'https://images.unsplash.com/photo-1576435728678-68d0fbf94e91?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&h=600&q=80', 'Mountain'),
    ('22222222-2222-2222-2222-222222222222', 'City Cruiser', 'Comfortable urban bike for daily commutes', 899.99, 'https://images.unsplash.com/photo-1485965120184-e220f721d03e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&h=600&q=80', 'City'),
    ('33333333-3333-3333-3333-333333333333', 'Road Racer', 'Lightweight and aerodynamic for speed enthusiasts', 1599.99, 'https://images.unsplash.com/photo-1571068316344-75bc76f77890?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&h=600&q=80', 'Road'),
    ('44444444-4444-4444-4444-444444444444', 'Fat Tire Beast', 'All-terrain bike with extra-wide tires for stability', 1499.99, 'https://images.unsplash.com/photo-1532298229144-0ec0c57515c7?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&h=600&q=80', 'Fat Bike'),
    ('55555555-5555-5555-5555-555555555555', 'Hybrid Pathfinder', 'Versatile bike combining road and mountain features', 1099.99, 'https://images.unsplash.com/photo-1507035895480-2b3156c31fc8?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&h=600&q=80', 'Hybrid');


-- Insert characteristics options
INSERT INTO characteristic_options (id, type, name, in_stock)
VALUES 
    -- Frame Type
    ('FT001', 'Frame Type', 'Full-suspension', true),
    ('FT002', 'Frame Type', 'Diamond', true),
    ('FT003', 'Frame Type', 'Step-through', true),
    
    -- Frame Finish
    ('FF001', 'Frame Finish', 'Matte Black', true),
    ('FF002', 'Frame Finish', 'Matte Silver', true),
    ('FF003', 'Frame Finish', 'Shiny Red', true),
    ('FF004', 'Frame Finish', 'Shiny Blue', false),
    
    -- Wheels
    ('WH001', 'Wheels', 'Road Wheels', true),
    ('WH002', 'Wheels', 'Mountain Wheels', true),
    ('WH003', 'Wheels', 'Fat Bike Wheels', true),
    
    -- Rim Color
    ('RC001', 'Rim Color', 'Red', true),
    ('RC002', 'Rim Color', 'Black', true),
    ('RC003', 'Rim Color', 'Blue', true),
    ('RC004', 'Rim Color', 'Silver', false),
    
    -- Chain
    ('CH001', 'Chain', 'Single-speed Chain', true),
    ('CH002', 'Chain', '8-speed Chain', true),
    ('CH003', 'Chain', '11-speed Chain', true),
    
        -- Additional Characteristics
    ('SZ001', 'Size', 'Small', true),
    ('SZ002', 'Size', 'Medium', true),
    ('SZ003', 'Size', 'Large', true),
    
    -- Brake Type
    ('BR001', 'Brake Type', 'Disc Brakes', true),
    ('BR002', 'Brake Type', 'Rim Brakes', true),
    
    -- Suspension
    ('SP001', 'Suspension', 'Front Suspension', false),
    ('SP002', 'Suspension', 'Full Suspension', true),
    ('SP003', 'Suspension', 'Rigid', true);

-- Mountain Explorer - Rugged Bike
INSERT INTO product_characteristic_options (product_id, option_id)
VALUES 
    -- Frame Types
    ('11111111-1111-1111-1111-111111111111', 'FT001'),  -- Full-suspension frame
    ('11111111-1111-1111-1111-111111111111', 'FT002'),  -- Diamond frame (additional option)
    
    -- Frame Finishes
    ('11111111-1111-1111-1111-111111111111', 'FF001'),  -- Matte Black finish
    ('11111111-1111-1111-1111-111111111111', 'FF002'),  -- Matte Silver finish (additional option)
    
    -- Wheels
    ('11111111-1111-1111-1111-111111111111', 'WH002'),  -- Mountain Wheels
    ('11111111-1111-1111-1111-111111111111', 'WH001'),  -- Road Wheels (additional option)
    
    -- Rim Colors
    ('11111111-1111-1111-1111-111111111111', 'RC002'),  -- Black rims
    ('11111111-1111-1111-1111-111111111111', 'RC001'),  -- Red rims (additional option)
    
    -- Chains
    ('11111111-1111-1111-1111-111111111111', 'CH002'),  -- 8-speed Chain
    ('11111111-1111-1111-1111-111111111111', 'CH003'),  -- 11-speed Chain (additional option)
    
    -- Sizes
    ('11111111-1111-1111-1111-111111111111', 'SZ002'), -- Medium Size
    ('11111111-1111-1111-1111-111111111111', 'SZ003'), -- Large Size (additional option)
    
    -- Brake Types
    ('11111111-1111-1111-1111-111111111111', 'BR001'), -- Disc Brakes
    ('11111111-1111-1111-1111-111111111111', 'BR002'), -- Rim Brakes (additional option)
    
    -- Suspension
    ('11111111-1111-1111-1111-111111111111', 'SP002'); -- Full Suspension

-- City Cruiser - Urban Bike
INSERT INTO product_characteristic_options (product_id, option_id)
VALUES 
    -- Frame Types
    ('22222222-2222-2222-2222-222222222222', 'FT002'),  -- Diamond frame
    ('22222222-2222-2222-2222-222222222222', 'FT003'),  -- Step-through frame (additional option)
    
    -- Frame Finishes
    ('22222222-2222-2222-2222-222222222222', 'FF002'),  -- Matte Silver finish
    ('22222222-2222-2222-2222-222222222222', 'FF001'),  -- Matte Black finish (additional option)
    
    -- Wheels
    ('22222222-2222-2222-2222-222222222222', 'WH001'),  -- Road Wheels
    ('22222222-2222-2222-2222-222222222222', 'WH002'),  -- Mountain Wheels (additional option)
    
    -- Rim Colors
    ('22222222-2222-2222-2222-222222222222', 'RC002'),  -- Black rims
    ('22222222-2222-2222-2222-222222222222', 'RC001'),  -- Red rims (additional option)
    
    -- Chains
    ('22222222-2222-2222-2222-222222222222', 'CH001'),  -- Single-speed Chain
    ('22222222-2222-2222-2222-222222222222', 'CH002'),  -- 8-speed Chain (additional option)
    
    -- Sizes
    ('22222222-2222-2222-2222-222222222222', 'SZ002'), -- Medium Size
    ('22222222-2222-2222-2222-222222222222', 'SZ001'), -- Small Size (additional option)
    
    -- Brake Types
    ('22222222-2222-2222-2222-222222222222', 'BR002'), -- Rim Brakes
    ('22222222-2222-2222-2222-222222222222', 'BR001'), -- Disc Brakes (additional option)
    
    -- Suspension
    ('22222222-2222-2222-2222-222222222222', 'SP003'); -- Rigid

-- Road Racer - Speed Bike
INSERT INTO product_characteristic_options (product_id, option_id)
VALUES 
    -- Frame Types
    ('33333333-3333-3333-3333-333333333333', 'FT002'),  -- Diamond frame
    ('33333333-3333-3333-3333-333333333333', 'FT003'),  -- Step-through frame (additional option)
    
    -- Frame Finishes
    ('33333333-3333-3333-3333-333333333333', 'FF003'),  -- Shiny Red finish
    ('33333333-3333-3333-3333-333333333333', 'FF001'),  -- Matte Black finish (additional option)
    
    -- Wheels
    ('33333333-3333-3333-3333-333333333333', 'WH001'),  -- Road Wheels
    ('33333333-3333-3333-3333-333333333333', 'WH002'),  -- Mountain Wheels (additional option)
    
    -- Rim Colors
    ('33333333-3333-3333-3333-333333333333', 'RC004'),  -- Silver rims
    ('33333333-3333-3333-3333-333333333333', 'RC002'),  -- Black rims (additional option)
    
    -- Chains
    ('33333333-3333-3333-3333-333333333333', 'CH003'),  -- 11-speed Chain
    ('33333333-3333-3333-3333-333333333333', 'CH002'),  -- 8-speed Chain (additional option)
    
    -- Sizes
    ('33333333-3333-3333-3333-333333333333', 'SZ002'), -- Medium Size
    ('33333333-3333-3333-3333-333333333333', 'SZ003'), -- Large Size (additional option)
    
    -- Brake Types
    ('33333333-3333-3333-3333-333333333333', 'BR001'), -- Disc Brakes
    ('33333333-3333-3333-3333-333333333333', 'BR002'), -- Rim Brakes (additional option)
    
    -- Suspension
    ('33333333-3333-3333-3333-333333333333', 'SP003'); -- Rigid

-- Fat Tire Beast - All-Terrain Bike
INSERT INTO product_characteristic_options (product_id, option_id)
VALUES 
    -- Frame Types
    ('44444444-4444-4444-4444-444444444444', 'FT001'),  -- Full-suspension frame
    ('44444444-4444-4444-4444-444444444444', 'FT002'),  -- Diamond frame (additional option)
    
    -- Frame Finishes
    ('44444444-4444-4444-4444-444444444444', 'FF004'),  -- Shiny Blue finish
    ('44444444-4444-4444-4444-444444444444', 'FF001'),  -- Matte Black finish (additional option)
    
    -- Wheels
    ('44444444-4444-4444-4444-444444444444', 'WH003'),  -- Fat Bike Wheels
    ('44444444-4444-4444-4444-444444444444', 'WH002'),  -- Mountain Wheels (additional option)
    
    -- Rim Colors
    ('44444444-4444-4444-4444-444444444444', 'RC003'),  -- Blue rims
    ('44444444-4444-4444-4444-444444444444', 'RC002'),  -- Black rims (additional option)
    
    -- Chains
    ('44444444-4444-4444-4444-444444444444', 'CH002'),  -- 8-speed Chain
    ('44444444-4444-4444-4444-444444444444', 'CH003'),  -- 11-speed Chain (additional option)
    
    -- Sizes
    ('44444444-4444-4444-4444-444444444444', 'SZ003'), -- Large Size
    ('44444444-4444-4444-4444-444444444444', 'SZ002'), -- Medium Size (additional option)
    
    -- Brake Types
    ('44444444-4444-4444-4444-444444444444', 'BR001'), -- Disc Brakes
    ('44444444-4444-4444-4444-444444444444', 'BR002'), -- Rim Brakes (additional option)
    
    -- Suspension
    ('44444444-4444-4444-4444-444444444444', 'SP002'); -- Full Suspension

-- Hybrid Pathfinder - Versatile Bike
INSERT INTO product_characteristic_options (product_id, option_id)
VALUES 
    -- Frame Types
    ('55555555-5555-5555-5555-555555555555', 'FT003'),  -- Step-through frame
    ('55555555-5555-5555-5555-555555555555', 'FT002'),  -- Diamond frame (additional option)
    
    -- Frame Finishes
    ('55555555-5555-5555-5555-555555555555', 'FF001'),  -- Matte Black finish
    ('55555555-5555-5555-5555-555555555555', 'FF002'),  -- Matte Silver finish (additional option)
    
    -- Wheels
    ('55555555-5555-5555-5555-555555555555', 'WH002'),  -- Mountain Wheels
    ('55555555-5555-5555-5555-555555555555', 'WH001'),  -- Road Wheels (additional option)
    
    -- Rim Colors
    ('55555555-5555-5555-5555-555555555555', 'RC002'),  -- Black rims
    ('55555555-5555-5555-5555-555555555555', 'RC001'),  -- Red rims (additional option)
    
    -- Chains
    ('55555555-5555-5555-5555-555555555555', 'CH002'),  -- 8-speed Chain
    ('55555555-5555-5555-5555-555555555555', 'CH003'),  -- 11-speed Chain (additional option)
    
    -- Sizes
    ('55555555-5555-5555-5555-555555555555', 'SZ001'), -- Small Size
    ('55555555-5555-5555-5555-555555555555', 'SZ002'), -- Medium Size (additional option)
    
    -- Brake Types
    ('55555555-5555-5555-5555-555555555555', 'BR001'), -- Disc Brakes
    ('55555555-5555-5555-5555-555555555555', 'BR002'), -- Rim Brakes (additional option)
    
    -- Suspension
    ('55555555-5555-5555-5555-555555555555', 'SP001'); -- Front Suspension
