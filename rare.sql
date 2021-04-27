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


INSERT INTO `Tags` VALUES (null, "soft");
INSERT INTO `Tags` VALUES (null, "limber");
INSERT INTO `Tags` VALUES (null, "flexible");
INSERT INTO `Tags` VALUES (null, "pretzel");

INSERT INTO `PostTags` VALUES (null, 1, 1);
INSERT INTO `PostTags` VALUES (null, 2, 2);
INSERT INTO `PostTags` VALUES (null, 3, 3);
INSERT INTO `PostTags` VALUES (null, 4, 4);


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

    INSERT INTO `Comments`
VALUES(null, 1, 2, "This changed my world.");

INSERT INTO `Comments`
VALUES(null, 1, 1, "lol u suk");

INSERT INTO `Comments`
VALUES(null, 2, 3, "FIRST COMMENT");

INSERT INTO `Comments`
VALUES(null, 2, 4, "MIND=BLOWN");
