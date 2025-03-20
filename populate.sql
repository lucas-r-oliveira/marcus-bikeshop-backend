DELETE from products;
DELETE from product_parts;
DELETE from part_options;
DELETE from part_configurations;
DELETE from part_configuration_options;
-- Populate the products table with 5 bicycle products
INSERT INTO products (id, name, description, base_price, image_url, category)
VALUES 
    ('11111111-1111-1111-1111-111111111111', 'Mountain Explorer', 'A rugged mountain bike for challenging terrains', 1299.99, 'https://example.com/mountain-explorer.jpg', 'Mountain'),
    ('22222222-2222-2222-2222-222222222222', 'City Cruiser', 'Comfortable urban bike for daily commutes', 899.99, 'https://example.com/city-cruiser.jpg', 'City'),
    ('33333333-3333-3333-3333-333333333333', 'Road Racer', 'Lightweight and aerodynamic for speed enthusiasts', 1599.99, 'https://example.com/road-racer.jpg', 'Road'),
    ('44444444-4444-4444-4444-444444444444', 'Fat Tire Beast', 'All-terrain bike with extra-wide tires for stability', 1499.99, 'https://example.com/fat-tire-beast.jpg', 'Fat Bike'),
    ('55555555-5555-5555-5555-555555555555', 'Hybrid Pathfinder', 'Versatile bike combining road and mountain features', 1099.99, 'https://example.com/hybrid-pathfinder.jpg', 'Hybrid');

-- Populate the product_parts table with frame types, finishes, wheels, rim colors, and chains
INSERT INTO product_parts (id, name, description, product_id)
VALUES
    -- Frame types
    ('a1111111-1111-1111-1111-111111111111', 'Frame Type', 'Type of bicycle frame', '11111111-1111-1111-1111-111111111111'),
    ('a2222222-2222-2222-2222-222222222222', 'Frame Type', 'Type of bicycle frame', '22222222-2222-2222-2222-222222222222'),
    ('a3333333-3333-3333-3333-333333333333', 'Frame Type', 'Type of bicycle frame', '33333333-3333-3333-3333-333333333333'),
    ('a4444444-4444-4444-4444-444444444444', 'Frame Type', 'Type of bicycle frame', '44444444-4444-4444-4444-444444444444'),
    ('a5555555-5555-5555-5555-555555555555', 'Frame Type', 'Type of bicycle frame', '55555555-5555-5555-5555-555555555555'),
    
    -- Frame finishes
    ('b1111111-1111-1111-1111-111111111111', 'Frame Finish', 'Finish of the bicycle frame', '11111111-1111-1111-1111-111111111111'),
    ('b2222222-2222-2222-2222-222222222222', 'Frame Finish', 'Finish of the bicycle frame', '22222222-2222-2222-2222-222222222222'),
    ('b3333333-3333-3333-3333-333333333333', 'Frame Finish', 'Finish of the bicycle frame', '33333333-3333-3333-3333-333333333333'),
    ('b4444444-4444-4444-4444-444444444444', 'Frame Finish', 'Finish of the bicycle frame', '44444444-4444-4444-4444-444444444444'),
    ('b5555555-5555-5555-5555-555555555555', 'Frame Finish', 'Finish of the bicycle frame', '55555555-5555-5555-5555-555555555555'),
    
    -- Wheels
    ('c1111111-1111-1111-1111-111111111111', 'Wheels', 'Type of wheels for the bicycle', '11111111-1111-1111-1111-111111111111'),
    ('c2222222-2222-2222-2222-222222222222', 'Wheels', 'Type of wheels for the bicycle', '22222222-2222-2222-2222-222222222222'),
    ('c3333333-3333-3333-3333-333333333333', 'Wheels', 'Type of wheels for the bicycle', '33333333-3333-3333-3333-333333333333'),
    ('c4444444-4444-4444-4444-444444444444', 'Wheels', 'Type of wheels for the bicycle', '44444444-4444-4444-4444-444444444444'),
    ('c5555555-5555-5555-5555-555555555555', 'Wheels', 'Type of wheels for the bicycle', '55555555-5555-5555-5555-555555555555'),
    
    -- Rim colors
    ('d1111111-1111-1111-1111-111111111111', 'Rim Color', 'Color of the wheel rims', '11111111-1111-1111-1111-111111111111'),
    ('d2222222-2222-2222-2222-222222222222', 'Rim Color', 'Color of the wheel rims', '22222222-2222-2222-2222-222222222222'),
    ('d3333333-3333-3333-3333-333333333333', 'Rim Color', 'Color of the wheel rims', '33333333-3333-3333-3333-333333333333'),
    ('d4444444-4444-4444-4444-444444444444', 'Rim Color', 'Color of the wheel rims', '44444444-4444-4444-4444-444444444444'),
    ('d5555555-5555-5555-5555-555555555555', 'Rim Color', 'Color of the wheel rims', '55555555-5555-5555-5555-555555555555'),
    
    -- Chains
    ('e1111111-1111-1111-1111-111111111111', 'Chain', 'Type of bicycle chain', '11111111-1111-1111-1111-111111111111'),
    ('e2222222-2222-2222-2222-222222222222', 'Chain', 'Type of bicycle chain', '22222222-2222-2222-2222-222222222222'),
    ('e3333333-3333-3333-3333-333333333333', 'Chain', 'Type of bicycle chain', '33333333-3333-3333-3333-333333333333'),
    ('e4444444-4444-4444-4444-444444444444', 'Chain', 'Type of bicycle chain', '44444444-4444-4444-4444-444444444444'),
    ('e5555555-5555-5555-5555-555555555555', 'Chain', 'Type of bicycle chain', '55555555-5555-5555-5555-555555555555');

-- Populate the part_options table with options for each part
INSERT INTO part_options (id, name, in_stock, product_part_id)
VALUES
    -- Frame type options
    ('aa111111-1111-1111-1111-111111111111', 'Full-suspension', TRUE, 'a1111111-1111-1111-1111-111111111111'),
    ('aa222222-2222-2222-2222-222222222222', 'Diamond', TRUE, 'a1111111-1111-1111-1111-111111111111'),
    ('aa333333-3333-3333-3333-333333333333', 'Step-through', TRUE, 'a1111111-1111-1111-1111-111111111111'),
    
    ('ab111111-1111-1111-1111-111111111111', 'Diamond', TRUE, 'a2222222-2222-2222-2222-222222222222'),
    ('ab222222-2222-2222-2222-222222222222', 'Step-through', TRUE, 'a2222222-2222-2222-2222-222222222222'),
    
    ('ac111111-1111-1111-1111-111111111111', 'Diamond', TRUE, 'a3333333-3333-3333-3333-333333333333'),
    
    ('ad111111-1111-1111-1111-111111111111', 'Full-suspension', TRUE, 'a4444444-4444-4444-4444-444444444444'),
    ('ad222222-2222-2222-2222-222222222222', 'Diamond', TRUE, 'a4444444-4444-4444-4444-444444444444'),
    
    ('ae111111-1111-1111-1111-111111111111', 'Diamond', TRUE, 'a5555555-5555-5555-5555-555555555555'),
    ('ae222222-2222-2222-2222-222222222222', 'Step-through', TRUE, 'a5555555-5555-5555-5555-555555555555'),
    
    -- Frame finish options
    ('ba111111-1111-1111-1111-111111111111', 'Matte', TRUE, 'b1111111-1111-1111-1111-111111111111'),
    ('ba222222-2222-2222-2222-222222222222', 'Shiny', TRUE, 'b1111111-1111-1111-1111-111111111111'),
    
    ('bb111111-1111-1111-1111-111111111111', 'Matte', TRUE, 'b2222222-2222-2222-2222-222222222222'),
    ('bb222222-2222-2222-2222-222222222222', 'Shiny', TRUE, 'b2222222-2222-2222-2222-222222222222'),
    
    ('bc111111-1111-1111-1111-111111111111', 'Shiny', TRUE, 'b3333333-3333-3333-3333-333333333333'),
    
    ('bd111111-1111-1111-1111-111111111111', 'Matte', TRUE, 'b4444444-4444-4444-4444-444444444444'),
    
    ('be111111-1111-1111-1111-111111111111', 'Matte', TRUE, 'b5555555-5555-5555-5555-555555555555'),
    ('be222222-2222-2222-2222-222222222222', 'Shiny', TRUE, 'b5555555-5555-5555-5555-555555555555'),
    
    -- Wheel options
    ('ca111111-1111-1111-1111-111111111111', 'Mountain wheels', TRUE, 'c1111111-1111-1111-1111-111111111111'),
    
    ('cb111111-1111-1111-1111-111111111111', 'Road wheels', TRUE, 'c2222222-2222-2222-2222-222222222222'),
    
    ('cc111111-1111-1111-1111-111111111111', 'Road wheels', TRUE, 'c3333333-3333-3333-3333-333333333333'),
    
    ('cd111111-1111-1111-1111-111111111111', 'Fat bike wheels', TRUE, 'c4444444-4444-4444-4444-444444444444'),
    
    ('ce111111-1111-1111-1111-111111111111', 'Road wheels', TRUE, 'c5555555-5555-5555-5555-555555555555'),
    ('ce222222-2222-2222-2222-222222222222', 'Mountain wheels', TRUE, 'c5555555-5555-5555-5555-555555555555'),
    
    -- Rim color options
    ('da111111-1111-1111-1111-111111111111', 'Black', TRUE, 'd1111111-1111-1111-1111-111111111111'),
    ('da222222-2222-2222-2222-222222222222', 'Blue', TRUE, 'd1111111-1111-1111-1111-111111111111'),
    
    ('db111111-1111-1111-1111-111111111111', 'Black', TRUE, 'd2222222-2222-2222-2222-222222222222'),
    
    ('dc111111-1111-1111-1111-111111111111', 'Red', TRUE, 'd3333333-3333-3333-3333-333333333333'),
    ('dc222222-2222-2222-2222-222222222222', 'Black', TRUE, 'd3333333-3333-3333-3333-333333333333'),
    
    ('dd111111-1111-1111-1111-111111111111', 'Black', TRUE, 'd4444444-4444-4444-4444-444444444444'),
    ('dd222222-2222-2222-2222-222222222222', 'Blue', TRUE, 'd4444444-4444-4444-4444-444444444444'),
    
    ('de111111-1111-1111-1111-111111111111', 'Red', TRUE, 'd5555555-5555-5555-5555-555555555555'),
    ('de222222-2222-2222-2222-222222222222', 'Black', TRUE, 'd5555555-5555-5555-5555-555555555555'),
    ('de333333-3333-3333-3333-333333333333', 'Blue', TRUE, 'd5555555-5555-5555-5555-555555555555'),
    
    -- Chain options
    ('ea111111-1111-1111-1111-111111111111', '8-speed chain', TRUE, 'e1111111-1111-1111-1111-111111111111'),
    
    ('eb111111-1111-1111-1111-111111111111', 'Single-speed chain', TRUE, 'e2222222-2222-2222-2222-222222222222'),
    ('eb222222-2222-2222-2222-222222222222', '8-speed chain', TRUE, 'e2222222-2222-2222-2222-222222222222'),
    
    ('ec111111-1111-1111-1111-111111111111', '8-speed chain', TRUE, 'e3333333-3333-3333-3333-333333333333'),
    
    ('ed111111-1111-1111-1111-111111111111', '8-speed chain', TRUE, 'e4444444-4444-4444-4444-444444444444'),
    
    ('ee111111-1111-1111-1111-111111111111', 'Single-speed chain', TRUE, 'e5555555-5555-5555-5555-555555555555'),
    ('ee222222-2222-2222-2222-222222222222', '8-speed chain', TRUE, 'e5555555-5555-5555-5555-555555555555');

-- Populate the part_configurations table
INSERT INTO part_configurations (id, product_id, part_id)
VALUES
    -- Mountain Explorer configurations
    ('ca111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', 'a1111111-1111-1111-1111-111111111111'),
    ('cb111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', 'b1111111-1111-1111-1111-111111111111'),
    ('cc111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111'),
    ('cd111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', 'd1111111-1111-1111-1111-111111111111'),
    ('ce111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111', 'e1111111-1111-1111-1111-111111111111'),
    
    --cCity Cruiser configurations
    ('ca222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222', 'a2222222-2222-2222-2222-222222222222'),
    ('cb222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222', 'b2222222-2222-2222-2222-222222222222'),
    ('cc222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222', 'c2222222-2222-2222-2222-222222222222'),
    ('cd222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222', 'd2222222-2222-2222-2222-222222222222'),
    ('ce222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222', 'e2222222-2222-2222-2222-222222222222'),
    
    --cRoad Racer configurations
    ('ca333333-3333-3333-3333-333333333333', '33333333-3333-3333-3333-333333333333', 'a3333333-3333-3333-3333-333333333333'),
    ('cb333333-3333-3333-3333-333333333333', '33333333-3333-3333-3333-333333333333', 'b3333333-3333-3333-3333-333333333333'),
    ('cc333333-3333-3333-3333-333333333333', '33333333-3333-3333-3333-333333333333', 'c3333333-3333-3333-3333-333333333333'),
    ('cd333333-3333-3333-3333-333333333333', '33333333-3333-3333-3333-333333333333', 'd3333333-3333-3333-3333-333333333333'),
    ('ce333333-3333-3333-3333-333333333333', '33333333-3333-3333-3333-333333333333', 'e3333333-3333-3333-3333-333333333333'),
    
    --cFat Tire Beast configurations
    ('ca444444-4444-4444-4444-444444444444', '44444444-4444-4444-4444-444444444444', 'a4444444-4444-4444-4444-444444444444'),
    ('cb444444-4444-4444-4444-444444444444', '44444444-4444-4444-4444-444444444444', 'b4444444-4444-4444-4444-444444444444'),
    ('cc444444-4444-4444-4444-444444444444', '44444444-4444-4444-4444-444444444444', 'c4444444-4444-4444-4444-444444444444'),
    ('cd444444-4444-4444-4444-444444444444', '44444444-4444-4444-4444-444444444444', 'd4444444-4444-4444-4444-444444444444'),
    ('ce444444-4444-4444-4444-444444444444', '44444444-4444-4444-4444-444444444444', 'e4444444-4444-4444-4444-444444444444'),
    
    --cHybrid Pathfinder configurations
    ('ca555555-5555-5555-5555-555555555555', '55555555-5555-5555-5555-555555555555', 'a5555555-5555-5555-5555-555555555555'),
    ('cb555555-5555-5555-5555-555555555555', '55555555-5555-5555-5555-555555555555', 'b5555555-5555-5555-5555-555555555555'),
    ('cc555555-5555-5555-5555-555555555555', '55555555-5555-5555-5555-555555555555', 'c5555555-5555-5555-5555-555555555555'),
    ('cd555555-5555-5555-5555-555555555555', '55555555-5555-5555-5555-555555555555', 'd5555555-5555-5555-5555-555555555555'),
    ('ce555555-5555-5555-5555-555555555555', '55555555-5555-5555-5555-555555555555', 'e5555555-5555-5555-5555-555555555555');

-- Populate the part_configuration_options table (linking configurations to specific options)
INSERT INTO part_configuration_options (id, configuration_id, option_id)
VALUES
    -- Mountain Explorer configuration options
    -- Frame type options
    ('daa11111-1111-1111-1111-111111111111', 'pa111111-1111-1111-1111-111111111111', 'aa111111-1111-1111-1111-111111111111'),
    ('daa11112-1111-1111-1111-111111111111', 'pa111111-1111-1111-1111-111111111111', 'aa222222-2222-2222-2222-222222222222'),
    --dFaame finish options
    ('dba11111-1111-1111-1111-111111111111', 'pb111111-1111-1111-1111-111111111111', 'ba111111-1111-1111-1111-111111111111'),
    ('dba11112-1111-1111-1111-111111111111', 'pb111111-1111-1111-1111-111111111111', 'ba222222-2222-2222-2222-222222222222'),
    --dWaeel options
    ('dca11111-1111-1111-1111-111111111111', 'pc111111-1111-1111-1111-111111111111', 'ca111111-1111-1111-1111-111111111111'),
    --dRam color options
    ('dda11111-1111-1111-1111-111111111111', 'pd111111-1111-1111-1111-111111111111', 'da111111-1111-1111-1111-111111111111'),
    ('dda11112-1111-1111-1111-111111111111', 'pd111111-1111-1111-1111-111111111111', 'da222222-2222-2222-2222-222222222222'),
    --dCaain options
    ('dea11111-1111-1111-1111-111111111111', 'pe111111-1111-1111-1111-111111111111', 'ea111111-1111-1111-1111-111111111111'),
    
    --dCaty Cruiser configuration options
    --dFaame type options
    ('daa22221-2222-2222-2222-222222222222', 'pa222222-2222-2222-2222-222222222222', 'ab111111-1111-1111-1111-111111111111'),
    ('daa22222-2222-2222-2222-222222222222', 'pa222222-2222-2222-2222-222222222222', 'ab222222-2222-2222-2222-222222222222'),
    --dFaame finish options
    ('dba22221-2222-2222-2222-222222222222', 'pb222222-2222-2222-2222-222222222222', 'bb111111-1111-1111-1111-111111111111'),
    --dWaeel options
    ('dca22221-2222-2222-2222-222222222222', 'pc222222-2222-2222-2222-222222222222', 'cb111111-1111-1111-1111-111111111111'),
    --dRam color options
    ('dda22221-2222-2222-2222-222222222222', 'pd222222-2222-2222-2222-222222222222', 'db111111-1111-1111-1111-111111111111'),
    --dCaain options
    ('dea22221-2222-2222-2222-222222222222', 'pe222222-2222-2222-2222-222222222222', 'eb111111-1111-1111-1111-111111111111'),
    
    --dRaad Racer configuration options
    --dFaame type options
    ('daa33331-3333-3333-3333-333333333333', 'pa333333-3333-3333-3333-333333333333', 'ac111111-1111-1111-1111-111111111111'),
    --dFaame finish options
    ('dba33331-3333-3333-3333-333333333333', 'pb333333-3333-3333-3333-333333333333', 'bc111111-1111-1111-1111-111111111111'),
    --dWaeel options
    ('dca33331-3333-3333-3333-333333333333', 'pc333333-3333-3333-3333-333333333333', 'cc111111-1111-1111-1111-111111111111'),
    --dRam color options
    ('dda33331-3333-3333-3333-333333333333', 'pd333333-3333-3333-3333-333333333333', 'dc111111-1111-1111-1111-111111111111'),
    ('dda33332-3333-3333-3333-333333333333', 'pd333333-3333-3333-3333-333333333333', 'dc222222-2222-2222-2222-222222222222'),
    --dCaain options
    ('dea33331-3333-3333-3333-333333333333', 'pe333333-3333-3333-3333-333333333333', 'ec111111-1111-1111-1111-111111111111'),
    
    --dFat Tire Beast configuration options
    --dFaame type options
    ('daa44441-4444-4444-4444-444444444444', 'pa444444-4444-4444-4444-444444444444', 'ad111111-1111-1111-1111-111111111111'),
    ('daa44442-4444-4444-4444-444444444444', 'pa444444-4444-4444-4444-444444444444', 'ad222222-2222-2222-2222-222222222222'),
    --dFaame finish options
    ('dba44441-4444-4444-4444-444444444444', 'pb444444-4444-4444-4444-444444444444', 'bd111111-1111-1111-1111-111111111111'),
    --dWaeel options
    ('dca44441-4444-4444-4444-444444444444', 'pc444444-4444-4444-4444-444444444444', 'cd111111-1111-1111-1111-111111111111'),
    --dRam color options
    ('dda44441-4444-4444-4444-444444444444', 'pd444444-4444-4444-4444-444444444444', 'dd111111-1111-1111-1111-111111111111'),
    ('dda44442-4444-4444-4444-444444444444', 'pd444444-4444-4444-4444-444444444444', 'dd222222-2222-2222-2222-222222222222'),
    --dCaain options
    ('dea44441-4444-4444-4444-444444444444', 'pe444444-4444-4444-4444-444444444444', 'ed111111-1111-1111-1111-111111111111'),
    
    --dHabrid Pathfinder configuration options
    --dFaame type options
    ('daa55551-5555-5555-5555-555555555555', 'pa555555-5555-5555-5555-555555555555', 'ae111111-1111-1111-1111-111111111111'),
    ('daa55552-5555-5555-5555-555555555555', 'pa555555-5555-5555-5555-555555555555', 'ae222222-2222-2222-2222-222222222222'),
    --dFaame finish options
    ('dba55551-5555-5555-5555-555555555555', 'pb555555-5555-5555-5555-555555555555', 'be111111-1111-1111-1111-111111111111'),
    ('dba55552-5555-5555-5555-555555555555', 'pb555555-5555-5555-5555-555555555555', 'be222222-2222-2222-2222-222222222222'),
    --Whael options
    ('dca55551-5555-5555-5555-555555555555', 'pc555555-5555-5555-5555-555555555555', 'ce111111-1111-1111-1111-111111111111'),
    ('dca55552-5555-5555-5555-555555555555', 'pc555555-5555-5555-5555-555555555555', 'ce222222-2222-2222-2222-222222222222'),
    --Ria color options
    ('dda55551-5555-5555-5555-555555555555', 'pd555555-5555-5555-5555-555555555555', 'de111111-1111-1111-1111-111111111111'),
    ('dda55552-5555-5555-5555-555555555555', 'pd555555-5555-5555-5555-555555555555', 'de222222-2222-2222-2222-222222222222'),
    ('dda55553-5555-5555-5555-555555555555', 'pd555555-5555-5555-5555-555555555555', 'de333333-3333-3333-3333-333333333333'),
    --Chain options
    ('dea55551-5555-5555-5555-555555555555', 'pe555555-5555-5555-5555-555555555555', 'ee111111-1111-1111-1111-111111111111'),
    ('dea55552-5555-5555-5555-555555555555', 'pe555555-5555-5555-5555-555555555555', 'ee222222-2222-2222-2222-222222222222');
