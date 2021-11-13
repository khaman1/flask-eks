/*
 Navicat Premium Data Transfer

 Source Server         : Local Postgres
 Source Server Type    : PostgreSQL
 Source Server Version : 90525
 Source Host           : localhost:5432
 Source Catalog        : postgres
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90525
 File Encoding         : 65001

 Date: 13/11/2021 10:48:04
*/


-- ----------------------------
-- Table structure for accounts
-- ----------------------------
DROP TABLE IF EXISTS "public"."accounts";
CREATE TABLE "public"."accounts" (
  "id" int4 NOT NULL,
  "account_id" text
)
;

-- ----------------------------
-- Records of accounts
-- ----------------------------
INSERT INTO "public"."accounts" VALUES (1, 1);
INSERT INTO "public"."accounts" VALUES (2, 2);

-- ----------------------------
-- Primary Key structure for table accounts
-- ----------------------------
ALTER TABLE "public"."accounts" ADD CONSTRAINT "accounts_pkey" PRIMARY KEY ("id");
