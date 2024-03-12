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


-- INSERT INTO notes (text, link_text, link_url, user_id)
-- VALUES
-- ('“If I could go back, I probably wouldn’t have finished a master\’s degree,” he says. “You can easily teach yourself the skills and programs you need to work in AI online, and mastering those is what helps you stand out.”
-- “It\’s not yet a highly professionalized field with role bands, career ladders and title progressions.” Kashef, a self-identified optimist, anticipates a future in which AI doesn\’t replace jobs, 
-- but is woven into the fabric of existing jobs across a wide range of industries, rather than siloed into a separate category.
-- "', "As AI creates more 6-figure, remote work opportunities, ‘the upside is high, but so are the risks,’ experts say", 
-- "https://www.cnbc.com/2024/02/12/ai-is-creating-more-6-figure-remote-jobs-but-its-not-all-upside-experts-say.html", 1),
-- ("We have developed a system that can infer and model human actions on computer applications, perform the actions reliably and quickly, and is well-suited for deployment in various AI assistants and operating systems. 
-- Our system is called the Large Action Model (LAM). Enabled by recent advances in neuro-symbolic programming, the LAM allows for the direct modeling of the structure of various applications and user actions performed on them 
-- without a transitory representation, such as text. The LAM system achieves results competitive with state-of-the-art approaches in terms of accuracy, interpretability, and speed. Engineering the LAM architecture involves 
-- overcoming both research challenges and engineering complexities, from real-time communication to virtual network computing technologies. We hope that our efforts could help shape the next generation of 
-- natural-language-driven consumer experiences.", "rabbit r1’s Large Action Model", "https://www.rabbit.tech/research", 1),
-- ("Machine Learning Engineer would be the best fit title for you (and is the most interesting and highest-paying compared to other roles like Data Engineer", "", "", 1);


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


-- INSERT INTO tags_join_notes(tag_id, note_id)
-- VALUES
-- (1, 1),
-- (1, 2),
-- (1, 3);

-- INSERT INTO notes(text, user_id, link_text, link_url, category_id)
-- VALUES
-- ("Super nice guy from that developer meetup at the Holiday Inn", 1, "Heffalump Hill-Dale", "www.linkedin.com/contacts/Heffalum-Hill_Dale", 2),
-- ("", 1, "Stumpula Quicks", "www.linkedin.com/contacts/stumpula-quicks", 2),
-- ("Terrible date, great for talking about mixture of experts", 1, "Wanita Sportingoods", "www.linkedin.com/contacts/w_sportingoods", 2),
-- ("", 2, "Tumper Effluvium", "www.linkedin.com/contacts/t_effluvium_12", 2);

-- INSERT INTO tags_join_notes(tag_id, note_id)
-- VALUES
-- (1, 4),
-- (1, 5),
-- (1, 6);
