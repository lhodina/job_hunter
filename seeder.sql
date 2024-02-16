-- INSERT INTO categories(name)
-- VALUES
-- ("Interests"),
-- ("Contacts"),
-- ("Companies"),
-- ("Locations");


-- INSERT INTO tags(text, user_id, category_id)
-- VALUES
-- ("AI (Artificial Intelligence)", 1, 1),
-- ("ML (Machine Learning)", 1, 1),
-- ("LLM (Large Language Models)", 1, 1),
-- ("Python", 1, 1),
-- ("JavaScript", 1, 1),
-- ("Java", 1, 1),
-- ("C++", 1, 1),
-- ("TypeScript", 1, 1),
-- ("React", 1, 1),
-- ("React Native", 1, 1),
-- ("Mobile", 1, 1),
-- ("Mobile Development", 1, 1),
-- ("iOS", 1, 1),
-- ("Android", 1, 1),
-- ("Fintech", 1, 1),
-- ("Crypto", 1, 1),
-- ("Blockchain", 1, 1),
-- ("Biotech", 1, 1),
-- ("Healthcare", 1, 1),
-- ("Transportation", 1, 1),
-- ("Energy", 1, 1),
-- ("Clean/Renewable Energy", 1, 1),
-- ("Aerospace", 1, 1),
-- ("Transportation", 1, 1),
-- ("Auto", 1, 1),
-- ("IoT (Internet of Things)", 1, 1);


-- INSERT INTO tags(text, user_id, category_id)
-- VALUES
-- ("Apple", 1, 3),
-- ("Microsoft", 1, 3),
-- ("Facebook (Meta)", 1, 3),
-- ("Amazon", 1, 3),
-- ("Uber", 1, 3),
-- ("NVIDIA", 1, 3),
-- ("Google", 1, 3),
-- ("Oracle", 1, 3);

-- INSERT INTO tags(text, user_id, category_id)
-- VALUES
-- ("San Francisco Bay Area", 1, 4),
-- ("Seattle", 1, 4),
-- ("New York City", 1, 4),
-- ("Chicago", 1, 4),
-- ("London", 1, 4),
-- ("Paris", 1, 4),
-- ("Berlin", 1, 4),
-- ("Amsterdam", 1, 4),
-- ("Austin", 1, 4),
-- ("Los Angeles", 1, 4),
-- ("Raleigh-Durham", 1, 4),
-- ("Portland OR", 1, 4);

-- INSERT INTO links (text, url, category_id, user_id)
-- VALUES
-- ("TechCrunch Seance with Steve Jobs", "www.techcrunch.com/archives/coolseance", 3, 2),
-- ("Sleepless in Seattle", "www.theverge.com/places/seattle", 4, 2),
-- ("Evan Stevens", "www.linkedin.com/my-network/userdiddledeedoo", 2, 2),
-- ("Warrantless Spy Tech", "www.nsa.gov/icu-online-certificate", 1, 2);

-- INSERT INTO notes (text, user_id)
-- VALUES
-- ("What's all the buzz about?", 2),
-- ("What's the point?", 2),
-- ("Will I be selling my soul?", 2),
-- ("Can I afford to move here?", 2);

-- INSERT INTO tags_join_notes(tag_id, note_id)
-- VALUES
-- (1, 1),
-- (28, 3),
-- (37, 4);

-- UPDATE links
-- SET note_id = 2
-- WHERE id = 3;

