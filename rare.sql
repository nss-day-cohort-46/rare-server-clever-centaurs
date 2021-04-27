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

