CREATE TABLE "Users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "first_name" varchar,
    "last_name" varchar,
    "display_name" varchar,
    "email" varchar
);
CREATE TABLE "Posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "category_id" INTEGER,
    "title" varchar,
    "publication_date" date,
    "content" varchar,
    FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`category_id`) REFERENCES `Categories`(`id`)
);
CREATE TABLE "Comments" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "author_id" INTEGER,
    "content" varchar,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Tags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
CREATE TABLE "PostTags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "tag_id" INTEGER,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
INSERT INTO `Users`
VALUES(
        null,
        "Britt",
        "Pot",
        "Big Pimpin",
        "bp@email.com"
    );
INSERT INTO `Users`
VALUES(
        null,
        "Kylie",
        "Bee",
        "Lil Pimpin",
        "kb@email.com"
    );
INSERT INTO `Users`
VALUES(
        null,
        "Trent",
        "Sis",
        "Big Nappin",
        "ts@email.com"
    );
INSERT INTO `Users`
VALUES(
        null,
        "Nicole",
        "Tat",
        "Lil Devil",
        "nt@email.com"
    );

INSERT INTO `posts`
VALUES(
    null,
    1,
    1,
    "Cream of the Crop",
    "05/06/2020",
    "I'm the cream of the crop, I rise to the top
I never eat a pig 'cause a pig is a cop
Or better yet a Terminator, like Arnold Schwarzenegger
Try to play me out like as if my name was Sega
But I ain't going out like no punk bitch
Get used to one style and yo and I might switch
It up, up and around, then buck, buck you down
Put out your head and then you wake up in the Dawn of the Dead
I'm coming to get ya, I'm coming to get ya
Spitting out lyrics, homie, I'll wet ya
I came to get down, I came to get down
So get out your seat and jump around!"
);

INSERT INTO `posts`
VALUES(
    null,
    2,
    2,
    "Purple Rain",
    "05/05/2020",
    "
I never meant to cause you any sorrow
I never meant to cause you any pain
I only wanted to one time to see you laughing
I only wanted to see you
Laughing in the purple rain"
);

INSERT INTO `posts`
VALUES(
    null,
    3,
    3,
    "Whats going on?",
    "05/04/2020",
    "And so I cry sometimes when I'm lying in bed
Just to get it all out what's in my head
And I, I am feeling a little peculiar
And so I wake in the morning and I step outside
And I take a deep breath and I get real high
And I scream from the top of my lungs
Whats going on?"
);

INSERT INTO `posts`
VALUES(
    null,
    4,
    4,
    "I MISS YOU",
    "05/07/2020",
    "Hello, there
The angel from my nightmare
The shadow in the background of the morgue
The unsuspecting victim
Of darkness in the valley
We can live like Jack and Sally if we want
Where you can always find me
And we'll have Halloween on Christmas
And in the night, we'll wish this never ends
We'll wish this never ends.
Where are you?
And I'm so sorry
I cannot sleep, I cannot dream tonight
I need somebody and always
This sick, strange darkness
Comes creeping on, so haunting every time
And as I stare, I counted
The webs from all the spiders
Catching things and eating their insides
Like indecision to call you
And hear your voice of treason
Will you come home and stop this pain tonight?
Stop this pain tonight
"
);
SELECT * FROM Posts
DROP TABLE Posts