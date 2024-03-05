-- INSERT INTO categories(name)
-- VALUES
-- ("Interests"),
-- ("Contacts"),
-- ("Companies"),
-- ("Locations");


-- INSERT INTO tags(text, user_id, category_id)
-- VALUES
-- ("AI", 1, 1),
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


-- INSERT INTO links (text, url, description, category_id, user_id)
-- VALUES
-- ("TechCrunch Seance with Steve Jobs", "www.techcrunch.com/archives/coolseance", "TechCrunch panel summons the spirit of Steve Jobs to discuss the Vision Pro", null, 1),
-- ("Sleepless in Seattle", "www.theverge.com/places/seattle", null, null, 1),
-- ("Evan Stevens", "www.linkedin.com/my-network/userdiddledeedoo", "Cool dude, knows a lot about TypeScript", 2, 1),
-- ("Freduardo Uilliams", "www.linkedin.com/my-network/fredu", null, 2, 1),
-- ("Bonko Squilius-Timms", "www.linkedin.com/my-network/bsquilius", null, 2, 1),
-- ("Chorp Dunkaroo", "www.linkedin.com/my-network/chorpdunk", null, 2, 1),
-- ("Tillahassy Quinkton", "www.linkedin.com/my-network/tillyquinks", null, 2, 2),
-- ("Warrantless Spy Tech", "www.nsa.gov/icu-online-certificate", null, null, 2);


-- INSERT INTO links(text, url, description, category_id, user_id)
-- VALUES
-- ("What's this AI craze anyhow?", "www.oldmanreviews.net/tech", "Leroy Bojangles wants to know what all the hoopla is about", null, 1),
-- ("Is AI a sin? Probably", "www.catholictimes.vc/sin", "Catholic intellectual meditates on AI as a mortal sin", null, 1),
-- ("AI Erases My Identity", "www.huffpo.com/problematic", "Courageous Huffington Post think piece gets me worked up", null, 1);


-- INSERT INTO notes (text, user_id)
-- VALUES
-- ("What's all the buzz about?", 1),
-- ("I keep writing the word over and over again on social media, but so far it hasn't made me any money at all. Am I doing it wrong?", 1),
-- ("Will I be selling my soul?", 1),
-- ("Can I afford to move here?", 1),
-- ("I must enquire as to the monetary value of the aforementioned Acronyme known variously as 'A.I.', 'AI', 'Artificial Intelligence', &c., &c., and as to the veracity of the claim that, if I may quote, 'AI is cool, I guess', made by my nephew, Winstable Chumminguggins, last November.", 1);


-- INSERT INTO tags(text, user_id, category_id)
-- VALUES
-- ("Drones", 1, 1),
-- ("Dancing Robots", 1, 1),
-- ("Robotics", 1, 1),
-- ("CIA", 1, 3),
-- ("ACME", 1, 3),
-- ("Def Jam Recordings", 1, 3),
-- ("Moon Station", 1, 4),
-- ("Detroit", 1, 4),
-- ("Neverland Ranch", 1, 4);


-- INSERT INTO tags(text, user_id, category_id)
-- VALUES
-- ("Turn Tables", 2, 1),
-- ("Disco Tech", 2, 1),
-- ("Audio Recording", 2, 1),
-- ("Cheers", 2, 3),
-- ("S.P.E.C.T.R.E.", 2, 3),
-- ("City of New York Department of Sanitation", 2, 3),
-- ("Wonka Chocolate Factory", 2, 4),
-- ("Yonkers", 2, 4),
-- ("Atlantis", 2, 4);


-- INSERT INTO tags_join_tags(tag_id_1, tag_id_2)
-- VALUES
-- (1, 2),
-- (1, 3),
-- (1, 4),
-- (1, 15),
-- (1, 32);


-- INSERT INTO links_join_tags(link_id, tag_id)
-- VALUES
-- (3, 1),
-- (6, 1),
-- (7, 1),
-- (9, 1),
-- (10, 1),
-- (11, 1);


-- INSERT INTO tags_join_notes(tag_id, note_id)
-- VALUES
-- (1, 1),
-- (1, 2),
-- (1, 5),
-- (30, 3),
-- (37, 4);


